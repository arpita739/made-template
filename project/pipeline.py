import sqlite3
import pandas as pd
import io
import requests
import kaggle
import shutil
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile
import os

def extract_and_move(old_name: str, new_name: str, extract_path: str):
    shutil.move(old_name, new_name)
    with zipfile.ZipFile(new_name, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

# Set paths using os.path.join for platform independence
data= '../data'
dataset_folder = os.path.join(data, 'dataset-folder')
clean_salary_db_path = os.path.join(data, 'clean_salary.sqlite')
global_salary_db_path = os.path.join(data, 'global_salary.sqlite')

api = KaggleApi()
api.authenticate()

# Example:
api.dataset_download_file('thedevastator/jobs-dataset-from-glassdoor','file.zip')

extract_and_move('file.zip', dataset_folder, data_folder)

# Read CSV file
file_path = os.path.join(dataset_folder, 'salary_data_cleaned.csv')
cleancsv_df = pd.read_csv(file_path)

# Cleaning
cleancsv_df = cleancsv_df[(cleancsv_df['Sector'] != 'unknown') & (cleancsv_df['Sector'] != '-1')]

# Save to SQLite database
with sqlite3.connect(clean_salary_db_path) as conn:
    cleancsv_df.to_sql('clean_salary', conn, index=False, if_exists='replace')

print("American Salary Data loaded successfully!")

# URL of the Excel file
excel_url = 'https://query.data.world/s/7swlcctjkj7vxuhxta7oxjtcy36ptk?dws=00000'

# Use requests to get the content from the URL
response = requests.get(excel_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Read the Excel content from the response
    excel_content = response.content

    # Use io.BytesIO to create a buffer and read_excel to read from the buffer
    df = pd.read_excel(io.BytesIO(excel_content))

    # Convert the DataFrame to CSV
    csv_content = df.to_csv(index=False)

    # Save the CSV content to a file
    global_salary_csv_path = os.path.join(data, 'global_salary.csv')
    with open(global_salary_csv_path, 'w', encoding='utf-8') as csv_file:
        csv_file.write(csv_content)

    print("Conversion to CSV successful. CSV file saved as 'global_salary.csv'")

    # Cleaning
    with sqlite3.connect(global_salary_db_path) as conn:
        df.to_sql('global_salary', conn, index=False, if_exists='replace')

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

print("Global Salary Data loaded successfully!")
