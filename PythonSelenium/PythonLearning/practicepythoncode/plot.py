import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
import csv

sal=pd.read_csv("C:\\madhan\\appsql\\Salaries.csv") # read the csv file
"""print(sal)

df= sal.groupby('Year')[['BasePay','OvertimePay','TotalPayBenefits']].mean().sort_values(by='BasePay',ascending=False)
print(df)

print(df.plot())"""
print(sal.select_dtypes(include='number')) # returns the DF which has column of type numbers

print(sal.select_dtypes(include='object'))
