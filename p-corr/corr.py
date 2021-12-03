import numpy as np
import plotly.express as px
import csv

def readCsv(dataPath):
    with open(dataPath) as f :
        data = csv.DictReader(f)
        fig = px.scatter(data,x="Marks In Percentage",y="Days Present")
        fig.show()

def getData(dataPath):
    icecreamSales = []
    temp = []
    with open(dataPath) as f:
        data1 = csv.DictReader(f)
        for i in data1 :
            icecreamSales.append(float(i["Marks In Percentage"]))
            temp.append(float(i["Days Present"]))
    return {"x":temp, "y":icecreamSales}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("The correlation is : \n --->",correlation[0,1])

def setup():
    dataPath = "data.csv"
    dataSource = getData(dataPath)
    findCorrelation(dataSource)
    readCsv(dataPath)

setup()