import csv 
import pandas as pd
import plotly_express as px

with open('class1.csv',newline='')as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
totalEntries = len(file_data)
sum = 0
for item in file_data:
    sum = sum+float(item[1])

mean = sum/totalEntries
#print(mean)

df = pd.read_csv('class1.csv')
fig = px.scatter(df,x='Student Number',y='Marks')
fig.update_layout(shapes=[
    dict(
        type = 'line',
        y0 = mean,
        y1 = mean,
        x0 = 0,
        x1 = totalEntries
    )
])
fig.show()