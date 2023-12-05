#!/usr/bin/env python
# coding: utf-8

# 1\. **Pandas DataFrame**
# 
# This exercise consists in analyzing a dataset containg timing information from a series of Time-to-Digital-Converters (TDC) implemented in a pair of FPGAs. Each measurement (i.e. each row of the input file) consists of a flag that specifies the type of message ('HEAD', which in this case is always 1), two addresses of the TDC providing the signal ('FPGA' and 'TDC_CHANNEL'), and the timing information ('ORBIT_CNT', 'BX_COUNTER', and 'TDC_MEAS'). Each TDC count corresponds to 25/30 ns, whereas a unit of BX_COUNTER corresponds to 25 ns, and the ORBIT_CNT is increased every `x` BX_COUNTER. This allows to store the time in a similar way to hours, minutes and seconds.

# In[1]:


# If haven't downloaded it yet, please get the data file with wget
#!wget https://www.dropbox.com/s/xvjzaxzz3ysphme/data_000637.txt -P ./data/


# 1\. Create a Pandas DataFrame reading N rows of the `data/data_000637.txt` dataset. Choose N to be smaller than or equal to the maximum number of rows and larger that 10k (check the documentation).

# In[2]:
print("************************************1.*************************************************************************")

import pandas as pd
file_path = './data/data_000637.txt'
N = 15000 
column_names = ['HEAD', 'FPGA', 'TDC_CHANNEL', 'ORBIT_CNT', 'BX_COUNTER', 'TDC_MEAS']
df = pd.read_csv(file_path,  nrows=N)
print(df)


# 2\. Estimate the number of BX in a ORBIT (the value `x`).
# 
# *Hint*: check when the BX counter reaches the maximum value before being reset to 0.

# In[3]:
print("************************************2.*************************************************************************")

max_bx = df['BX_COUNTER'].max()

reset_indices = df[df['BX_COUNTER'] == 0].index

if len(reset_indices) >= 2:    
    bx_per_orbit = reset_indices[1] - reset_indices[0]
    print(f"Maximum BX_COUNTER value: {max_bx}")
    print(f"Estimated number of BX in an ORBIT (x): {bx_per_orbit}")
else:
    print("No BX_COUNTER reset to 0 found in the dataset.")


# 3\. Create a new column with the absolute time in ns (as a combination of the other three columns with timing information) since the beginning of the data acquisition, and convert the new column to a Time Series.
# 
# *Hint:* introduce an offset to the absolute time such that the start of the data acquisition (i.e. the first entry) is zero.

# In[4]:

print("************************************3.*************************************************************************")
df['Absolute_Time_ns'] = (((df['ORBIT_CNT'] * max_bx + df['BX_COUNTER']) * 25 / 30 + df['TDC_MEAS']) * 1e9)

start_time_offset = df['Absolute_Time_ns'].min()
df['Absolute_Time_ns'] -= start_time_offset
df['Time_Series'] = pd.to_datetime(df['Absolute_Time_ns'], unit='ns')

print(df[['ORBIT_CNT', 'BX_COUNTER', 'TDC_MEAS', 'Absolute_Time_ns', 'Time_Series']])




# 4\. Find out the duration of the data taking in hours, minutes and seconds, by using the features of the Time Series. Perform this check reading the whole dataset.

# In[5]:
print("************************************4.*************************************************************************")

df['ABSOULTE_TIME'] = pd.to_timedelta(df['Absolute_Time_ns'], unit='ns')
df.head(4)


# 5\. Use the `.groupby()` method to find out the noisy channels, i.e. the TDC channels with most counts (print to screen the top 3 and the corresponding counts)

# In[6]:
print("************************************5.*************************************************************************")

channel_counts = df.groupby('TDC_CHANNEL').size()

top_3channels = channel_counts.sort_values(ascending=False).head(3)

print("Top 3 Noisy Channels:")
print(top_3channels)


# 6\. Count the number of non-empty orbits (i.e. the number of orbits with at least one hit).

# In[7]:
print("************************************6.*************************************************************************")

non_empty_orbits_count = df['ORBIT_CNT'].nunique()

print("Number of Non-Empty Orbits:", non_empty_orbits_count)


# In[8]:


df.groupby("ORBIT_CNT").count().shape[0]


# 7\. Count the number of unique orbits with at least one measurement from TDC_CHANNEL=139.

# In[9]:
print("************************************7.*************************************************************************")

df_channel_139 = df[df['TDC_CHANNEL'] == 139]

unique_orbits_count_channel_139 = df_channel_139['ORBIT_CNT'].nunique()

print("Number of Unique Orbits with TDC_CHANNEL=139:", unique_orbits_count_channel_139)


# 8\. Create two Series (one for each FPGA) that have the TDC channel as index, and the number of counts for the corresponding TDC channel as values.

# In[10]:

print("************************************8.*************************************************************************")
fpga_counts = df.groupby(['FPGA', 'TDC_CHANNEL']).size()

fpga_0_series = fpga_counts.loc[0] if 0 in fpga_counts.index.levels[0] else pd.Series()

fpga_1_series = fpga_counts.loc[1] if 1 in fpga_counts.index.levels[0] else pd.Series()


print("FPGA 0 Series:")
print(fpga_0_series)

print("\nFPGA 1 Series:")
print(fpga_1_series)


# 9\. **Optional:** Create two histograms (one for each FPGA) that show the number of counts for each TDC channel.

# In[11]:

print("************************************9.*************************************************************************")
import matplotlib.pyplot as plt


plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(fpga_0_series, bins=50, color='blue', alpha=0.7)
plt.title('Histogram for FPGA 0')
plt.xlabel('Number of Counts')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(fpga_1_series, bins=50, color='green', alpha=0.7)
plt.title('Histogram for FPGA 1')
plt.xlabel('Number of Counts')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()


# In[ ]:




