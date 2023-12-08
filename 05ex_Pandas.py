#Solution number 1

import pandas as pd
import numpy as np

# Define the file path
file_path = r'C:\Users\dell\Desktop\data\data_000637.txt'
rows=10100# specify a given number of rows

# Read the data into a Pandas DataFrame
df = pd.read_csv(file_path, nrows=rows)
print(df)

//////////////////////////END OF SOLUTION 1//////

#SOLUTION NUMBER 2

import pandas as pd
import numpy as np

file_path = r'C:\Users\dell\Desktop\data\data_000637.txt'
rows=10100# specify a given number of rows

# Read the data into a Pandas DataFrame
data = pd.read_csv(file_path, nrows=rows)

# Group by ORBIT_CNT and find the maximum BX_COUNTER value within each ORBIT_CNT
max_Obt = data.groupby('ORBIT_CNT')['BX_COUNTER'].max()
print(max_Obt)
print()

# Find the maximum value before BX_COUNTER resets to 0
V_max = max_Obt.max()

print("Maximum BX_COUNTER value before reset:", V_max)
print()

///END OF SOLUTION 2///////////////

#SOLUTION NUMBER 3
import pandas as pd
import numpy as p

# the dataframe

file_path = r'C:\Users\dell\Desktop\data\data_000637.txt'
rows=10100# specify a given number of rows
df = pd.read_csv(file_path, nrows=rows)
#print(df)

# Constants for time conversion
TDC_MEAS= 25/30  #  nanoseconds
BX_COUNTER =25 # nanoseconds
df['ORBIT_CNT'] = df['ORBIT_CNT'] * BX_COUNTER # to nano seconds

# adding a new column on ['HEAD'  'FPGA'  'TDC_CHANNEL'   'ORBIT_CNT'  'BX_COUNTER'  'TDC_MEAS']
df['Abs_time'] = df.loc[:,['ORBIT_CNT','BX_COUNTER', 'TDC_MEAS']].sum(axis=1)
print("The DataFrame after adding a new Column:\n", df)
print()


print("offset to make the start of data acquisition as zero")
S_time = df['Abs_time'].min()
df['A_T_ns_F_START'] = df['Abs_time'] - S_time
print()


df['Abs_time'] = pd.to_timedelta(df['A_T_ns_F_START'], unit='ns')
print(df)

//////////END OF SOLUTION 3/////
#SOLUTION NUMBER 4
import pandas as pd
import numpy as np
# Load the whole dataset
file_path = r'C:\Users\dell\Desktop\data\data_000637.txt'
rows=10100# specify a given number of rows
df = pd.read_csv(file_path, nrows=rows)


# Constants for time conversion
TDC_MEAS= 25/30  #  nanoseconds
BX_COUNTER =25 # nanoseconds
df['ORBIT_CNT'] = df['ORBIT_CNT'] * BX_COUNTER # to nano seconds

# adding a new column on ['HEAD'  'FPGA'  'TDC_CHANNEL'   'ORBIT_CNT'  'BX_COUNTER'  'TDC_MEAS']
df['Abs_time'] = df.loc[:,['ORBIT_CNT','BX_COUNTER', 'TDC_MEAS']].sum(axis=1)
print("The DataFrame after adding a new Column, results in nanoseconds:\n", df)
print()

print("offset to make the start of data acquisition as zero")
S_time = df['Abs_time'].min()
df['A_T_ns_F_START'] = df['Abs_time'] - S_time
print()

df['Abs_time'] = pd.to_timedelta(df['A_T_ns_F_START'], unit='ns')
print(df)
S_time = df['Abs_time'].min()
E_time = df['Abs_time'].max()

# Calculate the duration of data taking
D = E_time - S_time

# duration in hours, minutes, and seconds
HOURS = D.components.hours
MINUTES = D.components.minutes
SECONDS = D.components.seconds

print(f"Duration IS: {HOURS} hours, {MINUTES} minutes, {SECONDS} seconds")
print()
///////////////END OF SOLUTION 4

#SOLUTION NUMBER 5

#number 5
import pandas as pd
import numpy as np

# Load the whole dataset
file_path = r'C:\Users\dell\Desktop\data\data_000637.txt'
rows=10100# specify a given number of rows
df = pd.read_csv(file_path, nrows=rows)

# Group by TDC_CHANNEL and count occurrences
C_count = df.groupby('TDC_CHANNEL').size().reset_index(name='COUNT')

# Sort the channels by count in descending order
Order = C_count.sort_values(by='COUNT', ascending=False)

# Get the top 3 noisy channels and their counts
N_Channels = Order.head(3)

# Print the top 3 noisy channels and their counts
print("The top three noisy channels are:")
print(N_Channels[['TDC_CHANNEL', 'COUNT']])
print()
////////////////END OF SOLUTION 5
#SOLUTION 6
import pandas as pd
import numpy as np

# Load the whole dataset
file_path = r'C:\Users\dell\Desktop\data\data_000637.txt'
rows=10100# specify a given number of rows
df = pd.read_csv(file_path, nrows=rows)

# Group by ORBIT_CNT and count unique orbits
Nempty_Obt = df.groupby('ORBIT_CNT')['TDC_CHANNEL'].nunique()
Num_Nempty_Obt = Nempty_Obt.count()

print("the Number of non-empty orbits is:", Num_Nempty_Obt)
print()
//////////////END OF SOLUTION 6
#SOLUTION NUMER 7

import pandas as pd

# Load the whole dataset
file_path = r'C:\Users\dell\Desktop\data\data_000637.txt'
rows=10100# specify a given number of rows
df = pd.read_csv(file_path, nrows=rows)

#Filter the DataFrame for TDC_CHANNEL=139
Nunq_Obt = df[df['TDC_CHANNEL'] == 139]

#Count the number of unique orbits with at least one measurement from TDC_CHANNEL=139
Nunq_Obt_139 = Nunq_Obt['ORBIT_CNT'].nunique()

print("Number of unique orbits with at least one measurement from TDC_CHANNEL=139:\n",Nunq_Obt_139)

/////////////////END OF SOLUTION 7////////

#SLUTION NUMBER 8

import pandas as pd

file_path = r'C:\Users\dell\Desktop\data\data_000637.txt'
rows=10100# specify a given number of rows
df = pd.read_csv(file_path, nrows=rows)

fpga_0 = pd.Series(df[df['FPGA']==0]['TDC_CHANNEL'].value_counts())
fpga_1 = pd.Series(df[df['FPGA']==1]['TDC_CHANNEL'].value_counts())
print("The FPGA identified with 0:\n", fpga_0)

///////////////END OF SOLUTION 8////////////