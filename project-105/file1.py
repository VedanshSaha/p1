import csv
from numpy import memmap
import pandas as pd
import plotly.express as px

with open('class2.csv',newline="") as f:
    r = csv.reader(f)
    ls = list(r)

ls.pop(0)

total_marks = 0
total_entries = len(ls)

for marks in ls:
    total_marks += float(marks[1])

mean = total_marks/total_entries

print("mean = "+str(mean))

file = pd.read_csv("class2.csv")

fig = px.scatter(file,x="Student Number",y="Marks")

fig.update_layout(shapes = [dict(
    type = "line",
    y0 = mean,
    y1 = mean,
    x0 = 0,
    x1 = total_entries
)])

fig.update_yaxes(rangemode = "tozero")

fig.show()