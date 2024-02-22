from turtle import title
import pandas as pd 
import matplotlib.pyplot as plt

print("data was printed")

#reads the file
wd_file = pd.read_csv("weather_data.txt")

#collects the specific data from the file
data = wd_file.loc[:,["date", "actual_max_temp", "actual_min_temp"]]

#plots the data in a graph with legends added
data.plot(x = "date", title = "Weather Data")
plt.legend()
plt.show()

#prints histogram
print("histogram was printed")
wd_file["actual_precipitation"].plot(kind = 'hist')
plt.show()