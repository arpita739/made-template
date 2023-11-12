import pandas as pd
import sqlite3

# Read the CSV file into a pandas DataFrame
csv_file_path = 'rhein-kreis-neuss-flughafen-weltweit.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(csv_file_path)

# Connect to the SQLite database (it will be created if it doesn't exist)
db_connection = sqlite3.connect('airports.sqlite')

# Define the SQLite data types for each column
# Replace 'your_column_name' with the actual column names from your CSV file
column_data_types = {
    'column_1': 'INTEGER',
    'column_2': 'TEXT',
    'column_3': 'TEXT',
    'column_4': 'TEXT',
    'column_5': 'TEXT',
    'column_6': 'TEXT',
    'column_7': 'BIGINT',
    'column_8': 'BIGINT',
    'column_9': 'INTEGER',
    'column_10': 'REAL',
    'column_11': 'TEXT',
    'column_12': 'TEXT',
    'column_13': 'BIGINT'
    # Add more columns as needed
}

# Generate the CREATE TABLE SQL statement
create_table_sql = f"CREATE TABLE airports ({', '.join([f'{col} {data_type}' for col, data_type in column_data_types.items()])});"

# Execute the CREATE TABLE SQL statement
db_connection.execute(create_table_sql)

# Write the DataFrame to the SQLite database
df.to_sql('airports', db_connection, index=False, if_exists='replace')

# Commit the changes and close the database connection
db_connection.commit()
db_connection.close()
