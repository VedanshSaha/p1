import plotly.figure_factory as ff
import statistics
import random
import pandas as pd 
import csv
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
population_mean = statistics.mean(data)
population_stdev = statistics.stdev(data)
fig = ff.create_distplot([data],["reading_time"],show_hist=False)
fig.show()

print("Population Mean: ",population_mean)
print("Population Standard Deviation: ",population_stdev)

# dataset = []
# for i in range(0,100):
#     random_index = random.randint(0,len(data))
#     value = data[random_index]
#     dataset.append(value)
# mean =  statistics.mean(dataset)
# stdev = statistics.stdev(dataset)

# print("mean : ",mean)
# print("stdev: ",stdev)

def randommeans():
    dataset = []
    l = len(data)-1
    for i in range(0,100):
        random_index = random.randint(0,l)
        value = data[random_index]
        dataset.append(value)
    mean =  statistics.mean(dataset)
    return mean

def showfig(mean_list):
    mean = statistics.mean(mean_list)
    fig = ff.create_distplot([mean_list],["reading_time"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode = "lines",name="mean"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set = randommeans()
        mean_list.append(set)
    showfig(mean_list)
    mean = statistics.mean(mean_list)
    print("mean for sampling distribution : ",mean)
setup()

def stdev():
    mean_list = []
    for i in range(0,1000):
        set = randommeans()
        mean_list.append(set)
    stdev = statistics.stdev(mean_list)
    print("standard deviation of sampling data: ",stdev)
stdev()
# standard deviation of sampling mean distribution(sampling error) = standard deviation of population / sqrt(no. of data in each sample)