import matplotlib.pyplot as plt
import numpy as np

with open("C:/Users/Rita/Desktop/temperature.txt" ,'r') as data:
    read_data=data.readlines()
    
year=[]
maxtemp=[]
mintemp=[]
avtemp=[]

for i in read_data:
    year.append(float(i[0:4]))
    maxtemp.append(float(i[5:9]))
    mintemp.append(float(i[10:14]))
    #check for trends with average values
    avtemp.append((float(i[5:9]) + float(i[10:14])) / 2.0)

plt.title("Temperature since 1905")
plt.xlabel("Years")
plt.ylabel("Degrees (Farenheit)")
plt.plot(year, avtemp)
plt.xticks(np.arange(1905, max(year), 10.0))
#Regression line / line of best fit
plt.plot(year, np.poly1d(np.polyfit(year, avtemp, 1))(year))
plt.show()