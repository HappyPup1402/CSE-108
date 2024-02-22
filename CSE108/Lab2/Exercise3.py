import pandas as pd
import numpy as np

print("Part A:")
print("days of the highest actual precipitation")
#prints out the actual highest precipitation from highest to least
wd_file = pd.read_csv("weather_data.txt")
print(wd_file.sort_values(["actual_precipitation"],ascending=False))
print("\n")

print("Part B:")
print("The average actual max temp for July 2014:")
#gets the average of the actual max temp data suring the month of july, year 2014
print(np.round(wd_file.loc[0:30, "actual_max_temp"].mean(),2))
print('\n')

print("Part C:")
print("the actual max temp was the record max temp")
#prints out which days the max temp was the record max temp
print(wd_file[wd_file['actual_max_temp'] == wd_file['record_max_temp']]['date'])
print('\n')

print("Part D:")
print("Amount of Rain in October 2014:")
#prints the sum of actual preceipitation data in the month of october
print(wd_file.loc[92:122, "actual_precipitation"].sum())
print('\n')

print("Part E:")
print("all days where the min temp is under 60 and the max temp is over 90")
#the condition that is needed to be checked when looking at the data
condition = (wd_file.actual_min_temp < 60) & (wd_file.actual_max_temp > 90) 
print(wd_file.loc[condition, "date"])