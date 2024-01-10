import unittest
import os
import opendatasets as od
import sqlite3
import pandas as pd
import io
import requests
import kaggle
import shutil
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile

# Testing automated pipeline
class TestDownloadAndSaveDataset(unittest.TestCase):

    def setUp(self):
        # Set up necessary variables for testing
        self.dataset_url = 'https://www.kaggle.com/datasets/thedevastator/jobs-dataset-from-glassdoor/download?datasetVersionNumber=2'
        self.file_path = '..data/dataset-folder/salary_data_cleaned.csv'
        self.db_path = '../data/clean_salary.sqlite'

        self.excel_url = "https://query.data.world/s/7swlcctjkj7vxuhxta7oxjtcy36ptk?dws=00000"
        self.csv_path = "../data/global_salary.csv"
        self.b_path = "../data/global_salary.sqlite"

    def download_dataset(self):
        def extract_and_move(old_name: str, new_name: str):
            shutil.move(old_name, new_name)
            with zipfile.ZipFile(new_name, 'r') as zip_ref:
                zip_ref.extractall('../data')

        api = KaggleApi()
        api.authenticate()

        # Add your Kaggle dataset download and preprocessing logic here

        # Example:
        api.dataset_download_file('thedevastator/jobs-dataset-from-glassdoor', 'file.zip')

        extract_and_move('file.zip', '../data/dataset-folder')

    def read_csv_and_save_to_sql(self, file_path, db_path, table_name):
        cleancsv_df = pd.read_csv(file_path)
        # Cleaning
        cleancsv_df = cleancsv_df[(cleancsv_df['Sector'] != 'unknown') & (cleancsv_df['Sector'] != '-1')]
        # Check if DataFrame is not empty
        self.assertFalse(cleancsv_df.empty)

        # Connect to SQLite database and save the DataFrame
        conn = sqlite3.connect(db_path)
        cleancsv_df.to_sql(table_name, conn, index=False, if_exists='replace')

        # Check if the table exists in the database
        cursor = conn.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
        result = cursor.fetchone()
        self.assertIsNotNone(result)

        # Close the database connection
        conn.close()

    def download_excel_convert_to_csv_save_to_sql(self, excel_url, csv_path, db_path, table_name):
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
            with open('../data/global_salary.csv', 'w', encoding='utf-8') as csv_file:
                csv_file.write(csv_content)

            print("Conversion to CSV successful. CSV file saved as 'global_salary.csv'")

            # Cleaning
            conn = sqlite3.connect(db_path)
            df.to_sql(table_name, conn, index=False, if_exists='replace')
            conn.close()

        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")

    def test_download_and_save_dataset(self):
        # Download dataset
        self.download_dataset(self.dataset_url)

        # Check if the downloaded file exists
        self.assertTrue(os.path.exists(self.file_path))


        # Read CSV and save to SQLite
        self.read_csv_and_save_to_sql(self.file_path, self.db_path, 'clean_salary')

        #self.assertTrue(os.path.exists(self.csv_path))
        # Download Excel, convert to CSV, and save to SQLite
        self.download_excel_convert_to_csv_save_to_sql(self.excel_url, self.csv_path, self.b_path, 'global_salary')

    def tearDown(self):
        # Clean up after the test
        '''
        for file_path in [self.file_path, self.db_path, self.csv_path, self.b_path]:
            if os.path.exists(file_path):
                os.remove(file_path)
                '''


if __name__ == '__main__':
    unittest.main()
