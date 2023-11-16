## Exercise 1
import pandas as pd

# Specify the number of rows to read
N = 15000

# Create a DataFrame from the dataset, reading N rows
data = pd.read_csv('data/data_000637.txt', sep=',', nrows=N)


## Exercise 2

# The maximum BX_COUNTER value, which is equal to x, is the number before that BX_COUNTER is resetted and ORBIT_CNT is increased by one
x = data['BX_COUNTER'].max()


## Exercise 3

# Calculate the absolute time in nanoseconds
data['ABSOLUTE_TIME'] = (data['ORBIT_CNT'] * x) * 25 + data['BX_COUNTER'] * 25 + data['TDC_MEAS'] * (25/30)

# Calculate the offset to make the start of data acquisition zero
offset = data['ABSOLUTE_TIME'].min()
data['ABSOLUTE_TIME'] -= offset

# Convert the new column to a Time Series
data['ABSOLUTE_TIME'] = pd.to_datetime(data['ABSOLUTE_TIME'], unit='ns').dt.strftime('%H:%M:%S.%f')


## Exercise 4


## Exercise 5



## Exercise 6



## Exercise 7

