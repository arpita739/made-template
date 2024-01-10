import unittest
import os
import sqlite3
import pandas as pd



class TestSalaryDataProcessing(unittest.TestCase):

    def setUp(self):
        # Set up paths

        self.data='../data'
        self.clean_salary_db_path = '../data/clean_salary.sqlite'
        self.ds_salary_db_path = '../data/ds_salaries.sqlite'
        self.cleancsv_path = '../dataset-folder/salary_data_cleaned.csv'
        self.ds_salary_path = '../dataset-folder/ds_salaries.csv'

        # Call your functions to set up the environment
        # ...


    def test_clean_salary_data_processing(self):
        # Test the clean salary data processing steps
        cleancsv_df = pd.read_csv(self.cleancsv_path)

        # Test if the dataset is cleaned
        self.assertNotEqual(len(cleancsv_df), 0)

        # Test if the SQLite database is created
        with sqlite3.connect(self.clean_salary_db_path) as conn:
            result = pd.read_sql_query("SELECT * FROM clean_salary", conn)
        self.assertNotEqual(len(result), 0)

    def test_ds_salary_data_processing(self):
        # Test the data science salary data processing steps
        dsSalary_df = pd.read_csv(self.ds_salary_path)



        # Test if the SQLite database is created
        with sqlite3.connect(self.ds_salary_db_path) as conn:
            result = pd.read_sql_query("SELECT * FROM ds_salaries", conn)
        self.assertNotEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
