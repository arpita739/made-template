import os
import sqlite3
import pandas as pd
import pytest

@pytest.fixture
def base_path():
    return '/path/to/your/project/'  # Replace with the actual path to your project

def test_cleaned_data_import_and_sql(base_path):
    file_path = os.path.join(base_path, 'jobs-dataset-from-glassdoor/salary_data_cleaned.csv')
    db_path = os.path.join(base_path, 'data/clean_salary.sqlite')

    assert os.path.exists(file_path), f"File not found: {file_path}"

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clean_salary")
    result = cursor.fetchall()
    conn.close()

    assert len(result) > 0, f"No data found in clean_salary table: {result}"

def test_glassdoor_data_import_and_sql(base_path):
    file_path = os.path.join(base_path, 'jobs-dataset-from-glassdoor/glassdoor_jobs.csv')
    db_path = os.path.join(base_path, 'data/glassdoor.sqlite')

    assert os.path.exists(file_path), f"File not found: {file_path}"

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM glassdoor")
    result = cursor.fetchall()
    conn.close()

    assert len(result) > 0, f"No data found in glassdoor table: {result}"

def test_eda_data_import_and_sql(base_path):
    file_path = os.path.join(base_path, 'jobs-dataset-from-glassdoor/eda_data.csv')
    db_path = os.path.join(base_path, 'data/eda.sqlite')

    assert os.path.exists(file_path), f"File not found: {file_path}"

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM eda")
    result = cursor.fetchall()
    conn.close()

    assert len(result) > 0, f"No data found in eda table: {result}"
