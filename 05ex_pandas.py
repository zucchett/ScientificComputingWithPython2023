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


get_ipython().system('jt -t monokai -T')


# In[3]:


import pandas as pd


file_path = 'data/data_000637.txt'

# read file
df = pd.read_csv(file_path)

# rows number
rows = len(df)

N = 15000  # initialize N 

# edit N 
if N > 10000 and N <= rows:
    #N = rows
    df = df.head(N)
    print(df)
else:
    print(f"Change N")


# 2\. Estimate the number of BX in a ORBIT (the value `x`).
# 
# *Hint*: check when the BX counter reaches the maximum value before being reset to 0.

# In[4]:


orbit = df.loc[0, 'ORBIT_CNT']
df_filtered = df[df['ORBIT_CNT'] == orbit]
# the 1st element of the tuple given by shape is the number of rows of the filtered dataframe
rows_numb = df_filtered.shape[0]
print(f'Number of BX in a ORBIT: {rows_numb}')


# 3\. Create a new column with the absolute time in ns (as a combination of the other three columns with timing information) since the beginning of the data acquisition, and convert the new column to a Time Series.
# 
# *Hint:* introduce an offset to the absolute time such that the start of the data acquisition (i.e. the first entry) is zero.

# In[5]:


offset = df.loc[0, 'BX_COUNTER']
offset = -offset

df['Absolute time'] = (df['BX_COUNTER'] + offset) * 25
df['Absolute time'] = pd.to_datetime(df['Absolute time'], unit='ns')

print(df)


# 4\. Find out the duration of the data taking in hours, minutes and seconds, by using the features of the Time Series. Perform this check reading the whole dataset.

# In[6]:


duration = df['Absolute time'].max() - df['Absolute time'].min()
print(duration)


# 5\. Use the `.groupby()` method to find out the noisy channels, i.e. the TDC channels with most counts (print to screen the top 3 and the corresponding counts)

# In[7]:


channel_counts = df.groupby('TDC_CHANNEL')['TDC_MEAS'].count()
top_channels = channel_counts.nlargest(3)
print(top_channels)


# 6\. Count the number of non-empty orbits (i.e. the number of orbits with at least one hit).

# In[8]:


# Conta il numero di orbite non vuote
non_empty_orbits_numb = df['ORBIT_CNT'].nunique()

print(f"Number of non-empty orbits: {non_empty_orbits_numb}")


# 7\. Count the number of unique orbits with at least one measurement from TDC_CHANNEL=139.

# In[9]:


df_subset = df[df['TDC_CHANNEL'] == 139]

unique_orbits_TDC = df_subset['ORBIT_CNT'].nunique()

print(f"TDC_CHANNEL 139: {unique_orbits_TDC}")


# 8\. Create two Series (one for each FPGA) that have the TDC channel as index, and the number of counts for the corresponding TDC channel as values.

# In[10]:


# filtered dataframes based on FPGA
df_FPGA1 = df[df['FPGA'] == 0]
df_FPGA2 = df[df['FPGA'] == 1]

serie_fpga1 = df_FPGA1.set_index('TDC_CHANNEL')['TDC_MEAS']
serie_fpga2 = df_FPGA1.set_index('TDC_CHANNEL')['TDC_MEAS']
print(serie_fpga1)
print(serie_fpga2)


# 9\. **Optional:** Create two histograms (one for each FPGA) that show the number of counts for each TDC channel.

# In[12]:


import matplotlib.pyplot as plt

serie_fpga1.plot(kind='bar')

plt.xlabel('TDC_CHANNEL')
plt.ylabel('TDC_MEAS')
plt.title('Histogram FPGA0')

plt.show()

serie_fpga2.plot(kind='bar')

plt.xlabel('TDC_CHANNEL')
plt.ylabel('TDC_MEAS')
plt.title('Histogram FPGA1')

plt.show()

