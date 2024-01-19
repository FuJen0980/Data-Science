import pandas as pd 

totals = pd.read_csv('totals.csv').set_index(keys=['name'])
counts = pd.read_csv('counts.csv').set_index(keys=['name'])

# Q1: Which city has the lowerst total precipitation over the year?
totals_city_sum = totals.sum(axis=1)
min_index = totals_city_sum.idxmin()
print("City with lowest total precipitation:")
print(min_index)

# Q2: Determine the average precipitation in these locations for each month.
totals_month_sum = totals.sum(axis=0)
counts_month_sum = counts.sum(axis=0)
averages_month = totals_month_sum / counts_month_sum
print("Average precipitation in each month:")
print(averages_month)

# Q3 Average precipitation for each city
totals_city_sum = totals.sum(axis=1)
counts_city_sum = counts.sum(axis=1)
averages_city = totals_city_sum / counts_city_sum
print("Average precipitation in each city:")
print(averages_city)