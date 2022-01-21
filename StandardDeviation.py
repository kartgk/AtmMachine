import csv 
import pandas as pd
import plotly_express as px
import math

with open('data.csv',newline='')as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data = file_data[0]

def Mean(file_data):
    totalEntries = len(file_data)
    sum = 0
    for item in file_data:
        sum = sum+int(item)

    mean = sum/totalEntries   
    return(mean)

Mean(file_data)

difList = []
for item in file_data:
    difference = Mean(file_data)-int(item)
    difference = difference**2
    difList.append(difference)

SumOfDif = 0
for item in difList:
    SumOfDif = SumOfDif + item

Entries = len(file_data)-1
Value = SumOfDif/Entries

StandardDeviation = math.sqrt(Value)
print(StandardDeviation)