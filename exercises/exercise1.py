import pandas as pd
from sqlalchemy import create_engine, inspect

# Step 1: Download the CSV file
url = 'https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv'
df = pd.read_csv(url,sep=';')

# Step 2: Analyze DataFrame and map pandas data types to SQLite types
sqlite_type_mapping = {
    'object': 'TEXT',
    'int64': 'INTEGER',
    'float64': 'REAL',
}

column_data_types = {col: sqlite_type_mapping[str(df[col].dtype)] for col in df.columns}

# Step 3: Define the SQLite database connection and create an SQLAlchemy engine
db_connection_str = 'sqlite:///airports.sqlite'
engine = create_engine(db_connection_str)

# Step 4: Write the DataFrame to the SQLite database with assigned types
df.to_sql('airports', con=engine, index=False, if_exists='replace', dtype=column_data_types)

# Optional: Print the defined column data types
inspector = inspect(engine)
table_columns = inspector.get_columns('airports')
for column in table_columns:
    print(f"Column: {column['name']}, Type: {column['type']}")

# Step 5: Close the engine
engine.dispose()
