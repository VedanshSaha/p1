import csv
import pandas as pd
import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("z.csv")
data = df["Math_score"].tolist()

# fig = ff.create_distplot([data],["Math Score"],show_hist=False)
# fig.show()

mean = statistics.mean(data)
stdev = statistics.stdev(data)

# print("Mean = ",mean)
# print("Stdev = ",stdev)

def randomsetofmean(counter):
    dataset = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataset.append(value)
    data_mean = statistics.mean(dataset)
    return data_mean

mean_list = []
for i in range(0,1000):
    setofmeans = randomsetofmean(100)
    mean_list.append(setofmeans)

meanofmlist = statistics.mean(mean_list)
stdevofmlist = statistics.stdev(mean_list)
print("Mean of Sampling Distribution : ",meanofmlist)
print("Stdev of Sampling Distribution",stdevofmlist)

# fig = ff.create_distplot([mean_list],["Student Marks"],show_hist=False)
# fig.add_trace(go.Scatter(x=[meanofmlist,meanofmlist],y=[0,0.2],mode="lines",name = "Mean"))
# fig.show()

first_stdev_start,first_stdev_end = mean-stdev,mean+stdev
second_stdev_start,second_stdev_end = mean-(2*stdev),mean+(2*stdev)
third_stdev_start,third_stdev_end = mean-(3*stdev),mean+(3*stdev)

# print("std1",first_stdev_start,first_stdev_end)
# print("std2",second_stdev_start,second_stdev_end)
# print("std3",third_stdev_start,third_stdev_end)

# fig = ff.create_distplot([mean_list],["Student Marks"],show_hist=False)
# fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode="lines",name = "Mean"))
# fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.2],mode="lines",name = "first_stdev_start"))
# fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.2],mode="lines",name = "first_stdev_end"))
# fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.2],mode="lines",name = "second_stdev_start"))
# fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.2],mode="lines",name = "second_stdev_end"))
# fig.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.2],mode="lines",name = "third_stdev_start"))
# fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.2],mode="lines",name = "third_stdev_end"))
# fig.show()

# data1, Hello Vedansh?
df1 = pd.read_csv("sample1.csv")
data1 = df1["Math_score"].tolist()
mean1 = statistics.mean(data1)
print("Mean of sample 1= ",mean1)
fig = ff.create_distplot([mean_list],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name = "Mean"))
fig.add_trace(go.Scatter(x=[mean1,mean1],y=[0,0.17],mode="lines",name = "mean1"))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.17],mode="lines",name = "first_stdev_end"))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.17],mode="lines",name = "second_stdev_end"))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.17],mode="lines",name = "third_stdev_end"))
fig.show()

# data2
df2 = pd.read_csv("sample2.csv")
data2 = df2["Math_score"].tolist()
mean2 = statistics.mean(data2)
print("Mean of sample 2= ",mean2)
fig = ff.create_distplot([mean_list],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name = "Mean"))
fig.add_trace(go.Scatter(x=[mean2,mean2],y=[0,0.17],mode="lines",name = "mean2"))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.17],mode="lines",name = "first_stdev_end"))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.17],mode="lines",name = "second_stdev_end"))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.17],mode="lines",name = "third_stdev_end"))
fig.show()

df3 = pd.read_csv("sample3.csv")
data3 = df3["Math_score"].tolist()
mean3 = statistics.mean(data3)
print("Mean of sample 3= ",mean3)
fig = ff.create_distplot([mean_list],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name = "Mean"))
fig.add_trace(go.Scatter(x=[mean3,mean3],y=[0,0.17],mode="lines",name = "mean3"))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.17],mode="lines",name = "first_stdev_end"))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.17],mode="lines",name = "second_stdev_end"))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.17],mode="lines",name = "third_stdev_end"))
fig.show()

#Z-score = (New Sample Mean - Sampling Distribution mean)/Standard Deviation.
zscore1 = (mean1-mean)/stdev
print("Z score for SD1",zscore1)

zscore2 = (mean2-mean)/stdev
print("Z score for SD2",zscore2)

zscore3 = (mean3-mean)/stdev
print("Z score for SD3",zscore3)