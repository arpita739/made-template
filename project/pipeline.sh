#!/bin/bash

# Install necessary Python packages
pip install kaggle
pip install opendatasets
pip install pandas
cp project/kaggle.json /home/runner/.kaggle
# Execute the Python script
python3 pipeline.py
