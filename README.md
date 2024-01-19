[![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/downloads/release/python-3110/)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

# Data Science Job Salary Analysis
![Data Science](Data-Science-Studium.jpeg)

## Introduction

In the era of big data and technological advancement, the role of data science has become integral to driving innovation, efficiency, and strategic decision-making across diverse industries. As organizations increasingly rely on data-driven insights, the demand for skilled data scientists has surged, leading to a competitive job market where salary structures play a crucial role. This report undertakes a comprehensive exploration into the factors influencing data science salaries, aiming to uncover patterns, trends, and geographical variations that define compensation packages in this dynamic field.

## Motivation

The motivation behind this in-depth analysis lies in addressing the growing curiosity and necessity surrounding data science salaries. For aspiring data scientists, understanding the key determinants of compensation is essential in shaping career trajectories and making informed choices regarding skill development. Simultaneously, employers and industry stakeholders seek insights into the factors that attract and retain top-tier data science talent in order to remain competitive and innovative.

The field of data science is not static; it evolves with technological advancements, industry demands, and methodological innovations. Consequently, the motivation for this report is to offer a nuanced perspective on the salary landscape, moving beyond a superficial examination to delve into the specific factors that contribute to earning differentials within the profession. *Additionally, a particular emphasis will be placed on exploring which states and cities within the United States, as well as countries globally, offer the highest-paying data science roles*. By doing so, this report aims to provide a comprehensive understanding of the regional dynamics shaping data science salaries, offering valuable insights for both professionals and employers navigating the dynamic landscape of data science compensation.

In my preliminary attempt to predict salaries according to job descriptions, this report takes a step further by examining how various factors influence compensation within the dynamic realm of data science. This initial exploration sets the stage for a more comprehensive understanding of salary determinants and aims to contribute valuable insights for both professionals and employers navigating the intricate landscape of data science compensation.

## Data Sources

### Data Source 1: Glassdoor Jobs Dataset 2017

- **Data URL:** [Glassdoor Jobs Dataset](https://www.kaggle.com/datasets/thedevastator/jobs-dataset-from-glassdoor/)
- **Data Type:** CSV format
- **Total Datasize:** 741
- **Dataset Year:** 2017

#### Key Attributes:
- Job Title
- Salary Estimate
- Job Description
- Rating
- Company Name
- Location
- Headquarters
- Size
- Founded
- Type of Ownership
- Industry
- Sector
- Revenue
- Competitors
- Hourly
- Employer Provided
- Min Salary, Max Salary, Avg Salary
- Company Text
- Job State
- Same State
- Age
- Python, R, Spark, AWS, Excel (Skills Indicators)

### Data Source 2: Data Science Salaries (2020-2023)

- **Data URL:** [Data Science Salaries](https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023)
- **Data Type:** CSV format
- **Total Datasize:** 3755
- **Dataset Year:** 2020-2023

#### Variables:
1. Work Year
2. Experience Level
3. Employment Type
4. Job Title
5. Salary
6. Salary Currency
7. Salary in USD
8. Employee Residence
9. Remote Ratio
10. Company Location
11. Company Size

This comprehensive dataset offers a wealth of information for analysis and exploration, providing valuable insights into trends and patterns in the job market within specified timeframes and regions.

## Project Link

- [Data Science Job Salary Analysis Project](https://github.com/arpita739/made-template/blob/main/project/report.ipynb)

## Interactive session

- [Interactive Session](https://arpita739.github.io/made-template/project/report.html)

## Usage

To use this project, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/arpita739/made-template.git
   cd made-template
   ```

2. **Run the Pipeline Script:**
   - Before running the pipeline script, ensure you have the required dependencies installed.
   ```bash
   pip install -r requirements.txt
   ```

   - Execute the following command to run the pipeline script and download the datasets from Kaggle.
   ```bash
   bash pipeline.sh
   ```

   The script will handle the download and extraction of datasets.

3. **Explore the Jupyter Notebooks:**
   - After downloading the datasets, explore the analysis by running the provided Jupyter Notebooks.
   ```bash
   jupyter notebook
   ```

4. **Modify and Contribute:**
   - Feel free to modify the analysis or extend it according to your needs.
   - If you make improvements, consider contributing back by submitting a pull request.

Please note that you need to have a Kaggle account and API key configured on your system for the pipeline script to work correctly. Refer to the Kaggle API documentation for more information on setting up your credentials: [Kaggle API Documentation](https://www.kaggle.com/docs/api).


