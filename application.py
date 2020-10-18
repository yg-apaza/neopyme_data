import logging.handlers
import requests
import psycopg2

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
LOG_FILE = '/tmp/crawler-ruc.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

connection = psycopg2.connect(
    database="ebdb",
    user="master",
    password="motita$123",
    host="aa7ymq7ssa88pk.cacq4m9m1pye.us-east-1.rds.amazonaws.com",
    port='5432'
)

welcome = """
<!DOCTYPE>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Welcome</title>
  </head>
  <body>
    <h1>Congratulations</h1>
    <p>Your first AWS Elastic Beanstalk Python Application is now running on your own dedicated environment in the AWS Cloud</p>
    <p>This environment is launched with Elastic Beanstalk Python Platform</p>
  </body>
</html>
"""


def crawl_ruc(ruc):
  if len(ruc) == 11:
    r = requests.get('https://api.sunat.cloud/ruc/' + ruc)
    if r.status_code == 200 and len(r.text) > 0:
        cursor = connection.cursor()
        postgres_select_query = """select * from info_sources_entityinformation where ruc = %s and source = %s"""
        cursor.execute(postgres_select_query, (ruc, "1"))
        records = cursor.fetchone()
        if len(records) > 0:
          id = records[0]
          postgres_update_query = """update info_sources_entityinformation set data = %s where id = %s"""
          cursor.execute(postgres_update_query, (r.text, id))
          connection.commit()
          logger.info('[SUNAT] Se actualiza un registro para el RUC {}'.format(ruc))
        else:
          postgres_insert_query = """ INSERT INTO info_sources_entityinformation (ruc, data, link, source) VALUES (%s,%s,%s,%s)"""
          record_to_insert = (ruc, r.text, "","1")
          cursor.execute(postgres_insert_query, record_to_insert)
          connection.commit()
          logger.info('[SUNAT] Se crea un nuevo registro para el RUC {}'.format(ruc))
    else:
      logger.error('[SUNAT] No hay informacion para el RUC {}'.format(ruc))
  else:
    logger.error('[SUNAT] RUC {} no tiene 11 digitos'.format(ruc))

def application(environ, start_response):
  path = environ['PATH_INFO']
  method = environ['REQUEST_METHOD']
  if method == 'POST':
    try:
      if path == '/':
        request_body_size = int(environ['CONTENT_LENGTH'])
        request_body = environ['wsgi.input'].read(request_body_size)
        logger.info("Received message: %s" % request_body)
        crawl_ruc(request_body.decode("utf-8"))
    except (TypeError, ValueError):
      logger.warning('Error retrieving request body for async work.')
    response = ''
  else:
      response = welcome
  start_response("200 OK", [
    ("Content-Type", "text/html"),
    ("Content-Length", str(len(response)))
  ])
  return [bytes(response, 'utf-8')]
