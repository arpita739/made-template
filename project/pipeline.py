import sqlite3
import pandas as pd
import io
import requests
#import kaggle
import shutil
import pycountry
#from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile
import os

def extract_and_move(old_name: str, new_name: str, extract_path: str):
    shutil.move(old_name, new_name)
    with zipfile.ZipFile(new_name, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

# Set paths using os.path.join for platform independence
data= '../data'
#data_folder = '../project'
#dataset_folder = os.path.join(data_folder, 'dataset-folder')
clean_salary_db_path = os.path.join(data, 'clean_salary.sqlite')
ds_salary_db_path = os.path.join(data, 'ds_salaries.sqlite')
cleancsv_path = './dataset-folder/salary_data_cleaned.csv'
ds_salary_path = './dataset_folder/ds_salaries.csv'


#api = KaggleApi()
#api.authenticate()

# Example:
#api.dataset_download_file('thedevastator/jobs-dataset-from-glassdoor','file.zip')

#extract_and_move('file.zip', dataset_folder, data_folder)

# Read CSV file
file_path = './dataset-folder/salary_data_cleaned.csv'
cleancsv_df = pd.read_csv(file_path)
# Define a function to extract the company name before '\n'
def extract_company_name(row):
    return row['Company Name'].split('\n')[0]

# Apply the function to create a new column 'company'
cleancsv_df['company'] = cleancsv_df.apply(lambda row: extract_company_name(row), axis=1)
# Drop the original 'Company Name' column
cleancsv_df = cleancsv_df.drop(columns=['Company Name'])

# Cleaning
cleancsv_df = cleancsv_df[(cleancsv_df['Sector'] != 'unknown') & (cleancsv_df['Sector'] != '-1')]

# Save to SQLite database
with sqlite3.connect(clean_salary_db_path) as conn:
    cleancsv_df.to_sql('clean_salary', conn, index=False, if_exists='replace')

print("American Salary Data loaded successfully!")

path2 = './dataset_folder/ds_salaries.csv'
dsSalary_df = pd.read_csv(path2)
# Transformation of the codes of the categorical variables

dsSalary_df['experience_level'] = dsSalary_df['experience_level'].replace(
    {'SE': 'Expert', 'MI': 'Intermediate', 'EN': 'Junior', 'EX': 'Director'})

dsSalary_df['employment_type'] = dsSalary_df['employment_type'].replace(
    {'FT': 'Full-time', 'CT': 'Contract', 'FL': 'Freelance', 'PT': 'Part-time'})


def country_name(country_code):
    try:
        return pycountry.countries.get(alpha_2=country_code).name
    except:
        return 'other'


dsSalary_df['company_location'] = dsSalary_df['company_location'].apply(country_name)
dsSalary_df['employee_residence'] = dsSalary_df['employee_residence'].apply(country_name)

# Save to SQLite database
with sqlite3.connect(ds_salary_db_path) as conn:
    dsSalary_df.to_sql('ds_salaries', conn, index=False, if_exists='replace')

print("Global Data Science Salary Data loaded successfully!")

