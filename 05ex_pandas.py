import pandas as pd
from IPython.display import display

# 1. Create a Pandas DataFrame reading N rows of the data/data_000637.txt dataset.
N = 1000000
df = pd.read_csv('data/data_000637.txt', nrows=N)
print(df)


# 2. Estimate the number of BX in a ORBIT (the value x).
max_bx = df['BX_counter'].max() + 1
print("Estimation: ", max_bx)



# 3. Create a new column with the absolute time in ns (as a combination of the other three columns with timing information) since the beginning of the data acquisition, and convert the new column to a Time Series.
max_bx = df['BX_COUNTER'].max() + 1

max_tdc = max(df["TDC_MEAS"]) + 1

bx_with_max_orbit = df.loc[df['ORBIT_CNT'] == max(df["ORBIT_CNT"])]
bx_with_min_orbit = df.loc[df['ORBIT_CNT'] == min(df["ORBIT_CNT"])]

tdc_with_min_bx = bx_with_min_orbit.loc[bx_with_min_orbit['BX_COUNTER'] == min(bx_with_min_orbit["BX_COUNTER"])]

initial_ns = (min(df["ORBIT_CNT"])*max_bx + min(bx_with_min_orbit["BX_COUNTER"])) * 25 + min(tdc_with_min_bx["TDC_MEAS"]) * 25/30
df['NS_PASSED'] = ((df['ORBIT_CNT']*max_bx + df['BX_COUNTER']) * 25 + df['TDC_MEAS']*25/30) - initial_ns
df



# 4\. Find out the duration of the data taking in hours, minutes and seconds, by using the features of the Time Series. Perform this check reading the whole dataset.

max_bx = df['BX_COUNTER'].max() + 1

max_tdc = max(df["TDC_MEAS"]) + 1

dif_orbit = max(df["ORBIT_CNT"]) - min(df["ORBIT_CNT"])

bx_with_max_orbit = df.loc[df['ORBIT_CNT'] == max(df["ORBIT_CNT"])]
bx_with_min_orbit = df.loc[df['ORBIT_CNT'] == min(df["ORBIT_CNT"])]

dif_bx = max(bx_with_max_orbit["BX_COUNTER"]) - min(bx_with_min_orbit["BX_COUNTER"])

tdc_with_max_bx = bx_with_max_orbit.loc[bx_with_max_orbit['BX_COUNTER'] == max(bx_with_max_orbit["BX_COUNTER"])]
tdc_with_min_bx = bx_with_min_orbit.loc[bx_with_min_orbit['BX_COUNTER'] == min(bx_with_min_orbit["BX_COUNTER"])]

dif_tdc = max(tdc_with_max_bx["TDC_MEAS"]) - min(tdc_with_min_bx["TDC_MEAS"])

if dif_tdc < 0:
    dif_bx = dif_bx - 1
    dif_tdc = dif_tdc + max_tdc

print(dif_orbit, " orbit ")
print(dif_bx, " bx")
print(dif_tdc, " tdc")

print(((dif_orbit*max_bx)+dif_bx)*25*1e-9 + dif_tdc * 25/30*1e-9, " seconds")


# 5. Use the .groupby() method to find out the noisy channels, i.e. the TDC channels with most counts (print to screen the top 3 and the corresponding counts)
max_bx = df['BX_COUNTER'].max() + 1
noisy_channels = df.groupby(by=["TDC_CHANNEL"]).size().sort_values(ascending = False).head(3)



#6. Count the number of non-empty orbits (i.e.the number of orbits with at least one hit).
non_empty_orbits = df.groupby('ORBIT_CNT')
print("Number of non-empty orbits: ", len(non_empty_orbits))


# 7. Count the number of unique orbits with at least one measurement from TDC_CHANNEL=139.
tdc_channel_139 = df[df['TDC_CHANNEL'] == 139].groupby('ORBIT_CNT')
print("Number of unique orbits where TDC_CHANNEL is equal to 139: ", len(tdc_channel_139))



# 8. Create two Series (one for each FPGA) that have the TDC channel as index, and the number of counts for the corresponding TDC channel as values.