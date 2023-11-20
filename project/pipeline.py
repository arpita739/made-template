import opendatasets as od
import sqlite3
import pandas as pd


dataset ='https://www.kaggle.com/datasets/thedevastator/jobs-dataset-from-glassdoor/download?datasetVersionNumber=2'

od.download(dataset)

file_path = 'jobs-dataset-from-glassdoor/salary_data_cleaned.csv'
cleancsv_df = pd.read_csv(file_path)
db_path = '../data/clean_salary.sqlite'
conn = sqlite3.connect(db_path)
cleancsv_df.to_sql('clean_salary', conn, index=False, if_exists='replace')

file_path = 'jobs-dataset-from-glassdoor/glassdoor_jobs.csv'
glassdoor_df = pd.read_csv(file_path)
db_path = '../data/glassdoor.sqlite'
conn = sqlite3.connect(db_path)
glassdoor_df.to_sql('glassdoor', conn, index=False, if_exists='replace')

file_path = 'jobs-dataset-from-glassdoor/eda_data.csv'
eda_df = pd.read_csv(file_path)
db_path = '../data/eda.sqlite'
conn = sqlite3.connect(db_path)
eda_df.to_sql('eda', conn, index=False, if_exists='replace')

conn.close()