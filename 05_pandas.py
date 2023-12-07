################################ 05_pandas ###################################################
import pandas as pd
import numpy as np
print("============== 1. Create a Pandas DataFrame ==============")

file = "data_000637.txt"
N = 100000   # Since we have 1310k rows in our dataframe I chose to get 100k
df = pd.read_csv(file, nrows=N)   # Getting our dataframe
print(df) # Printing the dataframe
print("============== 2. Estimate the number of BX in a ORBIT ==============")
BX_max = df[df['BX_COUNTER'] == df['BX_COUNTER'].max()] # Bx_max is a small dataframe containing the rows of the original dataframe where BX_COUNTER is at its maximum
print(BX_max)
# Calculate the difference in ORBIT_CNT between consecutive maximum BX_COUNTER values
orbit_diff = BX_max['ORBIT_CNT'].diff()
print(orbit_diff)
est_bx_orbit = orbit_diff.mode()
print("Estimated number of BX in one complete ORBIT:", est_bx_orbit)

print("============== 3. Create a new column with the absolute time in ns ==============")
# df['absolute_time'] = df['ORBIT_CNT'] * 1e9 * 3600 * 24 + df['BX_COUNTER'] * 1e9 + df['TDC_MEAS']
# df['absolute_time'] = pd.to_datetime(df['absolute_time'], unit='ns', errors='coerce')
# start_time = df['absolute_time'].min()
# df['absolute_time'] = (df['absolute_time'] - start_time).dt.total_seconds() * 1e9
# df['absolute_time'] = pd.to_datetime(df['absolute_time'], unit='ns')
df['Absolute_Time_ns'] = ((df['ORBIT_CNT'] * df['BX_COUNTER'] + df['TDC_MEAS']) * 25 / 30 * 1e9)
offset = df['Absolute_Time_ns'].iloc[0]
df['Absolute_Time_ns']= df['Absolute_Time_ns']- offset
df['Absolute_Time'] = pd.to_datetime(df['Absolute_Time_ns'], unit='ns', errors='coerce')
print(df)

print("============== 4. Find out the duration of the data ==============")
# Finding the start and end time of the new column
start_time = df['Absolute_Time'].min().timestamp()
end_time = df['Absolute_Time'].max().timestamp()
duration = end_time - start_time # Calculating the duration
# print(int(duration))
hours, remainder = divmod(int(duration), 3600)
minutes, seconds = divmod(remainder, 60)
print(f"Duration: {hours} hours, {minutes} minutes, {seconds} seconds")

print("============== 5. Use the .groupby() method to find out the noisy channels ==============")
tdc_nb = df.groupby('TDC_CHANNEL').size().reset_index(name='Count') # group.by() TDC channels and count their occurrences
sort_tdc_nb = tdc_nb.sort_values(by='Count', ascending=False)
top_noisy_channels = sort_tdc_nb.head(3)
print("The top 3 Noisy Channels:", top_noisy_channels[['TDC_CHANNEL', 'Count']])

print("============== 6. Count the number of non-empty orbits ==============")
non_empty_orbits_count = df['ORBIT_CNT'].nunique()
print('Non empty orbits are : ', non_empty_orbits_count)

print("============== 7. Count the number of unique orbits ==============")
tdc_new = df[df['TDC_CHANNEL'] == 139]
unique_orbits_count = tdc_new['ORBIT_CNT'].nunique()
print("The number of unique orbits where at least one measurement from TDC_CHANNEL=139= ", unique_orbits_count)

print("============== 8. Create two Series that have the TDC channel as index and the number of counts for the corresponding TDC channel as values ==============")
fpga0 = df[df['FPGA'] == 0]
fpga1 = df[df['FPGA'] == 1]

fpga_0_series = fpga0['TDC_CHANNEL'].value_counts().sort_index()
fpga_1_series = fpga1['TDC_CHANNEL'].value_counts().sort_index()
print("FPGA 0 TDC Counts:", fpga_0_series)
print("FPGA 1 TDC Counts:", fpga_1_series)






