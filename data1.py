from unicodedata import name
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import csv
import statistics
import random

df = pd.read_csv("data.csv")

data = df["Math_score"].to_list()

#fig = ff.create_distplot([data],["Math_score"],show_hist = False)
#fig.show()

mean = statistics.mean(data )
std = statistics.stdev(data )

print("Mean of the data :",mean)
print("std of the data :",std)

#find the mean of 100 data points 1000 times

def random_mean(counter) :
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

mean_list = [] 
for i in range(0,1000):
    set_of_means = random_mean(100)
    mean_list.append(set_of_means)   
 
mean = statistics.mean(mean_list )
std = statistics.stdev(mean_list )

print("Mean of the data :",mean)
print("std of the data :",std) 

#fig = ff.create_distplot([mean_list],["Math_score"],show_hist = False)
#fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.2],mode = "lines",name = "MEAN LINE"))
#fig.show()

std_first_start,std_first_end = mean-std,mean+std
std_second_start,std_second_end = mean-(2*std),mean+(2*std)
std_third_start,std_third_end = mean-(3*std),mean+(3*std)

print("std1",std_first_start,std_first_end)
print("std2",std_second_start,std_second_end)
print("std3",std_third_start,std_third_end)

#fig = ff.create_distplot([mean_list],["Math_score"],show_hist = False)
#fig.add_trace(go.Scatter(x = [std_first_start,std_first_start], y = [0,0.17],mode = "lines",name = "std1 line"))
#fig.add_trace(go.Scatter(x = [std_first_end,std_first_end], y = [0,0.17],mode = "lines",name = "std 1 end"))

#fig.add_trace(go.Scatter(x = [std_second_start,std_second_start], y = [0,0.17],mode = "lines",name = "std2 start"))
#fig.add_trace(go.Scatter(x = [std_second_end,std_second_end], y = [0,0.17],mode = "lines",name = "std 2 end"))

#fig.add_trace(go.Scatter(x = [std_third_start,std_third_start], y = [0,0.17],mode = "lines",name = "std3 start"))
#fig.add_trace(go.Scatter(x = [std_third_end,std_third_end], y = [0,0.17],mode = "lines",name = "std 3 end"))
#fig.show()


 #finding the mean of data1.csv

df = pd.read_csv("data1.csv")

data = df["Math_score"].to_list()

mean1 = statistics.mean(data )
std1 = statistics.stdev(data )

print("Mean of the data :",mean1)
print("std of the data :",std1)

df = pd.read_csv("data2.csv")

data = df["Math_score"].to_list()

mean2 = statistics.mean(data )
std2 = statistics.stdev(data )

print("Mean of the data :",mean2)
print("std of the data :",std2)

df = pd.read_csv("data3.csv")

data = df["Math_score"].to_list()

mean3 = statistics.mean(data )
std3 = statistics.stdev(data )

print("Mean of the data :",mean3)
print("std of the data :",std3)


fig = ff.create_distplot([mean_list],["Math_score"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17],mode = "lines",name = "MEAN LINE"))
fig.add_trace(go.Scatter(x = [mean1,mean1], y = [0,0.17],mode = "lines",name = "mean of sample 1"))
fig.add_trace(go.Scatter(x = [mean2,mean2], y = [0,0.17],mode = "lines",name = "mean of sample 2"))
fig.add_trace(go.Scatter(x = [mean3,mean3], y = [0,0.17],mode = "lines",name = "mean of sample 3"))

fig.add_trace(go.Scatter(x = [std_first_end,std_first_end], y = [0,0.17],mode = "lines",name = "std 1 end"))
fig.add_trace(go.Scatter(x = [std_second_end,std_second_end], y = [0,0.17],mode = "lines",name = "std 2 end"))
fig.add_trace(go.Scatter(x = [std_third_end,std_third_end], y = [0,0.17],mode = "lines",name = "std 3 end"))

fig.show()



