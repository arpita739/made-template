import pandas as pd
from sqlalchemy import create_engine


csv_file_path = '../data/rhein-kreis-neuss-flughafen-weltweit.csv'
df = pd.read_csv(csv_file_path,sep=';')


db_connection_str = 'sqlite:///airports.sqlite'

engine = create_engine(db_connection_str)


df.to_sql('airports', con =engine, index=False, if_exists='replace')

engine.dispose()
