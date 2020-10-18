# Manejo de datos en NEOPYME

- application.py: Consumidor de la cola SQS en AWS que a partir de un RUC crea o actualiza un registro en la base de datos con los nueva informacion disponible desde una API publica con datos de la SUNAT
- cleanerdata_.py: Se encarga del pre-procesamiento (limpieza y normalización) de datos obtenidos de fuentes internas bancarizada.
- Archivos *.csv: Resultados de archivos obtenidos por cada paso en la etapa de pre-procesamiento
- PGMult.py: Se enarga de encontrar la función que relaciona todos los datos de entrada, lo cual seria complicado de hacer con la clasica regresión matemática
- Evaluate.py: Se encarga la información de manera tradicional

# Transformación de datos en NEOPYME
- 1. dbUniversoRankingSunatAfilDigitalRccSunarp : Archivo que une todos los archvos
- 2. dbUniversoRankingSunatAfilDigitalRccSunarp_clean irrelevant : Se eliminan columnas despreciables:
- 3. dbUniversoRankingSunatAfilDigitalRccSunarp_clean repetitive : Se elimina la información que es repetitiva en toda la información
- 4. dbUniversoRankingSunatAfilDigitalRccSunarp_average: Comprime los datos periodicos, mediante el average
- 5. dbUniversoRankingSunatAfilDigitalRccSunarp_compress: Transformar de fechas largas dd-mm-yy a formato yyyy
- 6. dbUniversoRankingSunatAfilDigitalRccSunarp: Transforma la información cualitativa a cuantitativa