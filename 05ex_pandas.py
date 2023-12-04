# -*- coding: utf-8 -*-
"""05ex_pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qlQWt4rfXEDcW0hfUpwmPG78rTpdBmda

1\. **Pandas DataFrame**

This exercise consists in analyzing a dataset containg timing information from a series of Time-to-Digital-Converters (TDC) implemented in a pair of FPGAs. Each measurement (i.e. each row of the input file) consists of a flag that specifies the type of message ('HEAD', which in this case is always 1), two addresses of the TDC providing the signal ('FPGA' and 'TDC_CHANNEL'), and the timing information ('ORBIT_CNT', 'BX_COUNTER', and 'TDC_MEAS'). Each TDC count corresponds to 25/30 ns, whereas a unit of BX_COUNTER corresponds to 25 ns, and the ORBIT_CNT is increased every `x` BX_COUNTER. This allows to store the time in a similar way to hours, minutes and seconds.
"""

# If haven't downloaded it yet, please get the data file with wget
!wget https://www.dropbox.com/s/xvjzaxzz3ysphme/data_000637.txt -P ./data/

"""1\. Create a Pandas DataFrame reading N rows of the `data/data_000637.txt` dataset. Choose N to be smaller than or equal to the maximum number of rows and larger that 10k (check the documentation)."""

import pandas as pd
import numpy as np
df = pd.read_csv('/content/data/data_000637.txt',nrows=10000)
df.head(10)

df.describe()

"""2\. Estimate the number of BX in a ORBIT (the value `x`).

*Hint*: check when the BX counter reaches the maximum value before being reset to 0.
"""

df['BX_num'] = df.groupby('ORBIT_CNT')['BX_COUNTER'].transform(np.max)
mean_BX = df['BX_num'].mean()
print("mean BX counter in each orbit :",mean_BX, '\n')
df

"""3\. Create a new column with the absolute time in ns (as a combination of the other three columns with timing information) since the beginning of the data acquisition, and convert the new column to a Time Series.

*Hint:* introduce an offset to the absolute time such that the start of the data acquisition (i.e. the first entry) is zero.
"""

dfa = df.copy()

dfa['ABS_TIME'] = dfa['TDC_CHANNEL'] * 25/30 + dfa['BX_COUNTER'] * 25
dfa

"""4\. Find out the duration of the data taking in hours, minutes and seconds, by using the features of the Time Series. Perform this check reading the whole dataset."""

dfa["ABS_TIME_SECOND"]=pd.to_datetime(dfa["ABS_TIME"],unit='ns')
duration = dfa["ABS_TIME_SECOND"].max()-dfa["ABS_TIME_SECOND"].min()
print(duration)

durations = dfa.groupby('ORBIT_CNT').max()-dfa.groupby('ORBIT_CNT').min()
duration_for_all_orbits = durations['ABS_TIME_SECOND'].sum()
print('all data taking time: ',duration_for_all_orbits)

"""5\. Use the `.groupby()` method to find out the noisy channels, i.e. the TDC channels with most counts (print to screen the top 3 and the corresponding counts)"""

# dfa_noise = dfa.groupby('TDC_CHANNEL').transform(np.count_nonzero)
dfa['NOISE'] = dfa.groupby('TDC_CHANNEL')['ORBIT_CNT'].transform(np.count_nonzero).apply(np.max)
dfa.sort_values('NOISE',ascending=False).head(3)

"""6\. Count the number of non-empty orbits (i.e. the number of orbits with at least one hit)."""

count_of_orbits =np.count_nonzero( dfa['ORBIT_CNT'].unique())
print(count_of_orbits)

"""7\. Count the number of unique orbits with at least one measurement from TDC_CHANNEL=139."""

dfa_non_empty=dfa.loc[dfa['TDC_CHANNEL'] == 139]
count_of_orbits =np.count_nonzero( dfa_non_empty['ORBIT_CNT'].unique())
print(count_of_orbits)

"""8\. Create two Series (one for each FPGA) that have the TDC channel as index, and the number of counts for the corresponding TDC channel as values."""

df_fpga_0 = dfa.loc[dfa['FPGA'] == 0]
df_fpga_1 = dfa.loc[dfa['FPGA'] == 1]
series_fpga_0 = df_fpga_0['TDC_CHANNEL'].value_counts().sort_index()
series_fpga_1 = df_fpga_1['TDC_CHANNEL'].value_counts().sort_index()

print(series_fpga_0)
print(series_fpga_1)

"""9\. **Optional:** Create two histograms (one for each FPGA) that show the number of counts for each TDC channel."""

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(df_fpga_0['TDC_CHANNEL'], bins=range(df_fpga_0['TDC_CHANNEL'].min(), df_fpga_0['TDC_CHANNEL'].max() + 1), edgecolor='black')
plt.title('FPGA 0 - TDC Channel Counts')
plt.xlabel('TDC Channel')
plt.ylabel('Count')

plt.subplot(1, 2, 2)
plt.hist(df_fpga_1['TDC_CHANNEL'], bins=range(df_fpga_1['TDC_CHANNEL'].min(), df_fpga_1['TDC_CHANNEL'].max() + 1), edgecolor='black')
plt.title('FPGA 1 - TDC Channel Counts')
plt.xlabel('TDC Channel')
plt.ylabel('Count')

plt.tight_layout()
plt.show()