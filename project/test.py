import unittest
import os
import sqlite3
import pandas as pd
from .pipeline import extract_company_name


class TestSalaryDataProcessing(unittest.TestCase):

    def setUp(self):
        # Set up paths
        self.data_folder = '../data'
        self.dataset_folder = os.path.join(self.data_folder, 'dataset-folder')
        self.clean_salary_db_path = os.path.join(self.data_folder, 'clean_salary.sqlite')
        self.ds_salary_db_path = os.path.join(self.data_folder, 'ds_salaries.sqlite')
        self.cleancsv_path = os.path.join(self.dataset_folder, 'salary_data_cleaned.csv')
        self.ds_salary_path = os.path.join('../data', 'ds_salaries.csv')

        # Call your functions to set up the environment
        # ...


    def test_clean_salary_data_processing(self):
        # Test the clean salary data processing steps
        cleancsv_df = pd.read_csv(self.cleancsv_path)

        # Test if the 'company' column is created
        self.assertTrue('company' in cleancsv_df.columns)

        # Test if the 'Company Name' column is dropped
        self.assertFalse('Company Name' in cleancsv_df.columns)

        # Test if the dataset is cleaned
        self.assertNotEqual(len(cleancsv_df), 0)

        # Test if the SQLite database is created
        with sqlite3.connect(self.clean_salary_db_path) as conn:
            result = pd.read_sql_query("SELECT * FROM clean_salary", conn)
        self.assertNotEqual(len(result), 0)

    def test_ds_salary_data_processing(self):
        # Test the data science salary data processing steps
        dsSalary_df = pd.read_csv(self.ds_salary_path)

        # Test if the 'experience_level' column is transformed
        self.assertNotEqual(dsSalary_df['experience_level'].nunique(), 4)

        # Test if the 'employment_type' column is transformed
        self.assertNotEqual(dsSalary_df['employment_type'].nunique(), 4)

        # Test if the 'company_location' and 'employee_residence' columns are transformed
        self.assertNotEqual(dsSalary_df['company_location'].nunique(), 0)
        self.assertNotEqual(dsSalary_df['employee_residence'].nunique(), 0)

        # Test if the SQLite database is created
        with sqlite3.connect(self.ds_salary_db_path) as conn:
            result = pd.read_sql_query("SELECT * FROM ds_salaries", conn)
        self.assertNotEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
