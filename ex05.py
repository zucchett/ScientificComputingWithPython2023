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

# Total duration is the maximum absolute time in the set
total_duration = data['ABSOLUTE_TIME'].max()

## Exercise 5

# Group the DataFrame by the "TDC_CHANNEL" column and count the occurrences
grouped = data.groupby('TDC_CHANNEL').size()

# Get the top three most frequent TDC channels
top_three_channels = grouped.nlargest(3)

print(top_three_channels)


## Exercise 6

# Get the number of unique entries in ORBIT CNT
non_empty_orbits = data['ORBIT_CNT'].nunique()


## Exercise 7

# Filter the DataFrame based on the condition TDC_CHANNEL == 139
filtered_data = data[data['TDC_CHANNEL'] == 139]

# Get the unique orbits from the "TEAM" column in the filtered DataFrame
unique_orbits = filtered_data['ORBIT_CNT'].nunique()


## Exercise 8

# Creating the two series
fpga0 = data[data['FPGA'] == 0]['TDC_CHANNEL'].value_counts().sort_index()
fpga1 = data[data['FPGA'] == 1]['TDC_CHANNEL'].value_counts().sort_index()
print("FPGA 0:\n", fpga0)
print("FPGA 1:\n", fpga1)

