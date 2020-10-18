# Manejo de datos en NEOPYME

- application.py: Consumidor de la cola SQS en AWS que a partir de un RUC crea o actualiza un registro en la base de datos con los nueva informacion disponible desde una API publica con datos de la SUNAT
- cleanerdata_.py: Se encarga del pre-procesamiento (limpieza y normalización) de datos obtenidos de fuentes internas bancarizada.
- Archivos *.csv: Resultados de archivos obtenidos por cada paso en la etapa de pre-procesamiento