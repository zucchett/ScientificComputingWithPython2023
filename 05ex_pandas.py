import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'data/data_000637.txt'
column_names = ['HEAD', 'FPGA', 'TDC_CHANNEL', 'ORBIT_CNT', 'BX_COUNTER', 'TDC_MEAS']
N = 15000
data = pd.read_csv(file_path, delimiter=',', names=column_names, nrows=N)
data = data.iloc[1:]
data.reset_index(drop=True, inplace=True)

print(data.head())
columns_to_convert = ['ORBIT_CNT', 'BX_COUNTER', 'TDC_MEAS']
data[columns_to_convert] = data[columns_to_convert].apply(pd.to_numeric)

max_bx_counter = data['BX_COUNTER'].max()

print(f"The maximum value of BX_COUNTER before reset is: {max_bx_counter}")

##############################END OF 2.#######################################
condition = data['BX_COUNTER'] != 0
data['Absolute_Time'] = np.where(condition,
                                 data['ORBIT_CNT'] * data['BX_COUNTER'] * 25 + data['TDC_MEAS'] * (30 / 25),
                                 data['ORBIT_CNT'] + data['TDC_MEAS'] * (30 / 25))

start_time = data['Absolute_Time'].min()

print(data.head())
##############################END OF 3.#######################################

max_time = data['Absolute_Time'].max()
min_time = data['Absolute_Time'].min()

duration_ns = max_time - min_time

duration_seconds = duration_ns / 1e9 
hours = duration_seconds // 3600
minutes = (duration_seconds % 3600) // 60
seconds = duration_seconds % 60

print(f"Duration of data taking: {int(hours)} hours, {int(minutes)} minutes, {seconds:.2f} seconds")

##############################END OF 4.#######################################

top_channels = data['TDC_CHANNEL'].value_counts().sort_values(ascending=False)

print("Top 3 Noisy Channels:")
for channel, count in top_channels.head(3).items():
    print("Channel", channel, ": Count", count)
    
##############################END OF 5.#######################################

non_empty_orbits = len(data[data['TDC_MEAS'] > 0])
print("Number of non-empty orbits:", non_empty_orbits)

##############################END OF 6.#######################################

tdc_channel_139 = data[data['TDC_CHANNEL'] == '139']
unique_orbits = tdc_channel_139['ORBIT_CNT'].nunique()
print("Number of unique orbits with TDC_CHANNEL=139:", unique_orbits)

##############################END OF 7.#######################################

fpga_0_data = data[data['FPGA'] == '0']
fpga_1_data = data[data['FPGA'] == '1']

fpga_0_counts = fpga_0_data['TDC_CHANNEL'].value_counts()
fpga_1_counts = fpga_1_data['TDC_CHANNEL'].value_counts()

fpga_0_series = pd.Series(fpga_0_counts.values, index=fpga_0_counts.index, name='FPGA_0_Counts')
fpga_1_series = pd.Series(fpga_1_counts.values, index=fpga_1_counts.index, name='FPGA_1_Counts')

print("Series for FPGA 0:")
print(fpga_0_series.tail())

print("\nSeries for FPGA 1:")
print(fpga_1_series.head())

##############################END OF 7.#######################################

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(fpga_0_data['TDC_CHANNEL'],bins=100)
plt.title('Histogram for FPGA 0')
plt.xlabel('TDC Channel')
plt.ylabel('Counts')

plt.subplot(1, 2, 2)
plt.hist(fpga_1_data['TDC_CHANNEL'],bins=100)
plt.title('Histogram for FPGA 1')
plt.xlabel('TDC Channel')
plt.ylabel('Counts')

plt.tight_layout()
plt.show()