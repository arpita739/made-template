import unittest
import pandas as pd
import sqlite3
import os

class TestDatasetProcessing(unittest.TestCase):
    def setUp(self):
        # You can modify this path based on your project structure
        self.base_path = '/Users/arpitahalder/Lecture/SAKI/made-template'

    def test_cleaned_data_import_and_sql(self):
        file_path = os.path.join(self.base_path, 'project/jobs-dataset-from-glassdoor/salary_data_cleaned.csv')
        db_path = os.path.join(self.base_path, 'data/clean_salary.sqlite')

        # Ensure the file exists
        self.assertTrue(os.path.exists(file_path))

        # Ensure the SQLite database is created and the table is populated
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clean_salary")
        result = cursor.fetchall()
        conn.close()

        self.assertGreater(len(result), 0)

    def test_glassdoor_data_import_and_sql(self):
        file_path = os.path.join(self.base_path, 'project/jobs-dataset-from-glassdoor/glassdoor_jobs.csv')
        db_path = os.path.join(self.base_path, 'data/glassdoor.sqlite')

        # Ensure the file exists
        self.assertTrue(os.path.exists(file_path))

        # Ensure the SQLite database is created and the table is populated
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM glassdoor")
        result = cursor.fetchall()
        conn.close()

        self.assertGreater(len(result), 0)

    def test_eda_data_import_and_sql(self):
        file_path = os.path.join(self.base_path, 'project/jobs-dataset-from-glassdoor/eda_data.csv')
        db_path = os.path.join(self.base_path, 'data/eda.sqlite')

        # Ensure the file exists
        self.assertTrue(os.path.exists(file_path))

        # Ensure the SQLite database is created and the table is populated
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM eda")
        result = cursor.fetchall()
        conn.close()

        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()
