# get Boston City data from S3 https://pollysnips.s3.amazonaws.com/bostonEmployeeSalaries.json
import pandas as pd
import json
import pandas as pd


def get_data():
    # url = "https://pollysnips.s3.amazonaws.com/bostonEmployeeSalaries.json"
    # get json data from local file bostonEmployeeSalaries.json
    data = json.load(open('bostonEmployeeSalaries.json'))
    return data


data = get_data()
salaries = pd.DataFrame(data["data"])
print(salaries.head())
