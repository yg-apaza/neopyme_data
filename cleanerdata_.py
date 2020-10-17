import csv
import pandas as pd

dbUniverso=pd.read_csv('dbUniverso.csv',sep="|", header=0, index_col='taxpayer_id', parse_dates=None, error_bad_lines=False)
dbUniverso = dbUniverso[~dbUniverso.index.duplicated(keep='first')]
dbUniverso.to_csv('out/dbUniverso_dedup.csv') 

dbRanking=pd.read_csv('dbRanking.csv',sep="|", header=0, index_col='taxpayer_id', parse_dates=None, error_bad_lines=False)
dbRanking = dbRanking[~dbRanking.index.duplicated(keep='first')]
dbRanking.to_csv('out/dbRanking_dedup.csv') 

dbSunat=pd.read_csv('dbSunat.csv',sep="|", header=0, index_col='taxpayer_id', parse_dates=None, error_bad_lines=False)
dbSunat = dbSunat[~dbSunat.index.duplicated(keep='first')]
dbSunat.to_csv('out/dbSunat_dedup.csv') 

dbAfilDigital=pd.read_csv('dbAfilDigital.csv',sep="|", header=0, index_col='customer_id', parse_dates=None, error_bad_lines=False)
dbAfilDigital = dbAfilDigital[~dbAfilDigital.index.duplicated(keep='first')]
dbAfilDigital.to_csv('out/dbAfilDigital_dedup.csv') 

dbRcc=pd.read_csv('dbRcc.csv',sep="|", header=0, index_col='sbs_customer_id', parse_dates=None, error_bad_lines=False)
dbRcc = dbRcc[~dbRcc.index.duplicated(keep='first')]
dbRcc.to_csv('out/dbRcc.csv') 

dbSunarp=pd.read_csv('dbSunarp.csv',sep="|", header=0, index_col='personal_id', parse_dates=None, error_bad_lines=False)
dbSunarp = dbSunarp[~dbSunarp.index.duplicated(keep='first')]
dbSunarp.to_csv('out/dbSunarp.csv') 

dbSunarp=pd.read_csv('dbSunarp.csv',sep="|", header=0, index_col='personal_id', parse_dates=None, error_bad_lines=False)
dbSunarp = dbSunarp[~dbSunarp.index.duplicated(keep='first')]
dbSunarp.to_csv('out/dbSunarp.csv') 


dbUniversoRanking = pd.merge(dbUniverso, dbRanking, on=['taxpayer_id'])
dbUniversoRanking.to_csv('out/dbUniversoRanking.csv') 

dbUniversoRankingSunat = pd.merge(dbUniversoRanking, dbSunat, on=['taxpayer_id'])
dbUniversoRankingSunat.to_csv('out/dbUniversoRankingSunat.csv') 

dbUniversoRankingSunat = pd.merge(dbUniversoRankingSunat, dbSunat, on=['taxpayer_id'])
dbUniversoRankingSunat.to_csv('out/dbUniversoRankingSunat.csv') 

dbUniversoRankingSunat.set_index("customer_id")
dbUniversoRankingSunatAfilDigital = pd.merge(dbUniversoRankingSunat, dbAfilDigital, on=['customer_id'], how='left')
dbUniversoRankingSunatAfilDigital.to_csv('out/dbUniversoRankingSunatAfilDigital.csv') 

dbUniversoRankingSunatAfilDigital.set_index("sbs_customer_id")
dbUniversoRankingSunatAfilDigitalRcc = pd.merge(dbUniversoRankingSunatAfilDigital, dbRcc, on=['sbs_customer_id'], how='left')
dbUniversoRankingSunatAfilDigitalRcc.to_csv('out/dbUniversoRankingSunatAfilDigitalRcc.csv') 

dbUniversoRankingSunatAfilDigitalRccSunarp = pd.merge(dbUniversoRankingSunatAfilDigitalRcc, dbSunarp, on=['personal_id'], how='left')
dbUniversoRankingSunatAfilDigitalRccSunarp.to_csv('out/dbUniversoRankingSunatAfilDigitalRccSunarp.csv') 
