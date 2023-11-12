import pandas as pd
import sqlite3


csv_file_path = '../data/rhein-kreis-neuss-flughafen-weltweit.csv'
df = pd.read_csv(csv_file_path,sep=';')


db_connection = sqlite3.connect('airports.sqlite')


df.to_sql('airports', db_connection, index=False, if_exists='replace')


db_connection.commit()
db_connection.close()
