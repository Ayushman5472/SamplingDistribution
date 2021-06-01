import plotly.figure_factory as ff
import pandas as pd
import statistics
import random 

data = pd.read_csv('weatherData.csv')
data = data["temp"].tolist()
#print(data)

PopulationMean = statistics.mean(data)
print(PopulationMean)

PopulationStandardDeviation = statistics.stdev(data)
print(PopulationStandardDeviation)

#graph = ff.create_distplot([data], ["temperature"], show_hist = False)
#graph.show()

def Samples():
    sample = []
    for i in range(0,10000):
        randomTemp = random.randint(0,len(data)-1)
        value = data[randomTemp]
        sample.append(float(value))

    SampleMean = statistics.mean(sample)
    #print(SampleMean)

    SampleStandardDeviation = statistics.stdev(sample)
    #print(SampleStandardDeviation)
    return(SampleMean)

SampleMeans = []

for i in range(0,500):
    Means = Samples()
    SampleMeans.append(float(Means))

plot = ff.create_distplot([SampleMeans], ["Means of the Samples"], show_hist = False)
plot.show()

SampleM = statistics.mean(SampleMeans)
print(SampleM)

SampleSD = statistics.stdev(SampleMeans)
print(SampleSD)