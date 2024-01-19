import numpy as np  

data = np.load('monthdata.npz')
totals = data['totals']
counts = data['counts']

# Q1: Which city has the lowerst total precipitation over the year?
totals_city_sum = np.sum(totals, axis=1)
min_index = np.argmin(totals_city_sum)
print("Row with lowest total precipitation: ")
print(min_index)

# Q2: Determine the average precipitation in these locations for each month. 
totals_month_sum = np.sum(totals, axis=0)
counts_month_sum = np.sum(counts, axis=0)
averages_month = totals_month_sum / counts_month_sum
print("Average precipitation in each month: ")
print(averages_month)

# Q3 Average precipitation for each city
totals_city_sum = np.sum(totals, axis=1)
counts_city_sum = np.sum(counts, axis=1)
averages_city = totals_city_sum / counts_city_sum
print("Average precipitation in each city: ")
print(averages_city)

# Q4: Total precipitation for each quarter in each city
reshaped_totals = np.reshape(totals, (-1,3))
quarter_totals = np.sum(reshaped_totals, axis=1)
quarter_totals = np.reshape(quarter_totals, (-1,4))
print("Quarterly precipitation totals: ")
print(quarter_totals)