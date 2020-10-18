import json
import requests
from io import BytesIO
import zipfile
import pandas as pd
import boto3
from botocore.exceptions import ClientError
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
LOG_FILE = '/tmp/schedule.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

sqs = boto3.client('sqs', region_name='us-east-1')

def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename

def send_message(message):
    queue_url = 'https://sqs.us-east-1.amazonaws.com/949132823843/neopyme-ruc'
    resp = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=(
            message
        )
    )
    print(resp)

def process(filename):
    chunksize = 10 ** 6
    padrondf = pd.read_csv(filename, chunksize=chunksize, sep="|", encoding='latin-1');
    for chunk in padrondf:
        for index, row in chunk.iterrows():
            send_message(str(row['RUC']))

def main():
    local_filename = download_file("http://www2.sunat.gob.pe/padron_reducido_ruc.zip")
    zip_ref =  zipfile.ZipFile(local_filename, 'r')
    with zipfile.ZipFile(local_filename, 'r') as zip_ref:
        zip_ref.extractall(local_filename[:-4])
    print(local_filename[:-4] + "/padron_reducido_ruc.txt")
    #process("padron_reducido_ruc/padron_reducido_ruc.txt")
    process(local_filename[:-4] + "/padron_reducido_ruc.txt")

if __name__ == '__main__':
    main()