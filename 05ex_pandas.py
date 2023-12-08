import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#1
print("1. Create a Pandas DataFrame reading N rows of the data/data_000637.txt dataset.")
file_name = "data_000637.txt"
data = pd.read_csv(file_name)
print(data)

dt=pd.read_csv(file_name, nrows = 30000)
print(dt)

#2
print("2. Estimate the number of BX in a ORBIT (the value x).")
max_orbit = dt.groupby('ORBIT_CNT')['BX_COUNTER'].max()

diff = max_orbit.diff().dropna()

x = int(diff.values[0])
print("Value x (amount of BX_COUNTER in one ORBIT_CNT):", x)


#3
print("3. Create a new column with the absolute time in ns")
dt['Absolute_Time_in_ns'] = dt['ORBIT_CNT'] * (dt['BX_COUNTER'] * 25 + dt['TDC_MEAS'] * (25/30))

dt['Absolute_Time_in_ns'] = pd.to_datetime(dt['Absolute_Time_in_ns'], unit='ns')

print(dt)

#4
print("4. Find out the duration of the data taking in hours, minutes and seconds")
duration = dt['Absolute_Time_in_ns'].max() - dt['Absolute_Time_in_ns'].min()

hours = duration.components.hours
minutes = duration.components.minutes
seconds = duration.components.seconds

print("Duration of the data taking is", hours, "hours", minutes, "minutes", seconds, "seconds")

#5
print("5. Use the .groupby() method to find out the noisy channels")
noisy_channels = dt.groupby('TDC_CHANNEL').count()["FPGA"].nlargest(3)

for channel, count in noisy_channels.items():
    print("Channel", channel, ":", count, "events" )
	
#6
print("6. Count the number of non-empty orbits (i.e. the number of orbits with at least one hit).")
nonempty_orbits = dt['ORBIT_CNT'].nunique()
print('Number of non-empty orbits', nonempty_orbits)

#7
print("7. Count the number of unique orbits with at least one measurement from TDC_CHANNEL=139.")
data_channel = dt[dt['TDC_CHANNEL'] == 139]
unique_orbits_amount = data_channel['ORBIT_CNT'].nunique()
print('Number of unique orbits in 139 channel :', unique_orbits_amount)

#8
print("8. Create two Series (one for each FPGA) that have the TDC channel as index")
fpga1 = dt[dt['FPGA']==1].value_counts('TDC_CHANNEL')
fpga0 = dt[dt['FPGA']==0].value_counts('TDC_CHANNEL')
print("FPGA 1 Series:\n", fpga1)
print("FPGA 1 Series:\n", fpga0)



#9
print("Create two histograms (one for each FPGA) that show the number of counts for each TDC channel.")

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(fpga0, bins=50, color='red', alpha=0.7)
plt.title('FPGA 0 - TDC Channel Counts')
plt.xlabel('TDC Channel')
plt.ylabel('Count')

plt.subplot(1, 2, 2)
plt.hist(fpga1, bins=50, color='green', alpha=0.7)
plt.title('FPGA 1 - TDC Channel Counts')
plt.xlabel('TDC Channel')
plt.ylabel('Count')

plt.tight_layout()
plt.show()