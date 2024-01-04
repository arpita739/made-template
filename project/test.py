import unittest
import os
import opendatasets as od
import sqlite3
import pandas as pd

class TestDownloadAndSaveDataset(unittest.TestCase):

    def setUp(self):
        # Set up necessary variables for testing
        self.dataset_url = 'https://www.kaggle.com/datasets/thedevastator/jobs-dataset-from-glassdoor/download?datasetVersionNumber=2'
        self.file_path = 'jobs-dataset-from-glassdoor/salary_data_cleaned.csv'
        self.db_path = '../data/clean_salary.sqlite'

    def test_download_and_save_dataset(self):
        # Download dataset
        od.download(self.dataset_url)

        # Check if the downloaded file exists
        self.assertTrue(os.path.exists(self.file_path))

        # Read the CSV file into a DataFrame
        cleancsv_df = pd.read_csv(self.file_path)

        # Check if DataFrame is not empty
        self.assertFalse(cleancsv_df.empty)

        # Connect to SQLite database and save the DataFrame
        conn = sqlite3.connect(self.db_path)
        cleancsv_df.to_sql('clean_salary', conn, index=False, if_exists='replace')

        # Check if the table exists in the database
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='clean_salary';")
        result = cursor.fetchone()
        self.assertIsNotNone(result)

        # Close the database connection
        conn.close()

    def tearDown(self):
        # Clean up after the test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

if __name__ == '__main__':
    unittest.main()
