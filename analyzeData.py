# get Boston City data from S3 https://pollysnips.s3.amazonaws.com/bostonEmployeeSalaries.json
import pandas as pd
import json


def get_data():
    # url = "https://pollysnips.s3.amazonaws.com/bostonEmployeeSalaries.json"
    # get json data from local file bostonEmployeeSalaries.json
    data = json.load(open('bostonEmployeeSalaries.json'))
    return data


data = get_data()
df = pd.DataFrame(data["data"])
print(df.head())
print(df.shape)
# get salries from column 18
salaries = df[18]
print(salaries.head())
test = salaries.head()
# plot histogram of salaries for all employees column 18
test.plot.hist()
# print(salaries.describe())
# print(salaries.info())
# print(salaries.columns)
print("END")
# plot histogram of salaries for all employees column 18
