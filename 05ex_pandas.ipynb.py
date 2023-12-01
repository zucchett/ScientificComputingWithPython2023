#---------------------------------------------------------------------------------------------------------------
# exercise 5.PART ONE


import pandas as pd

# Set the file path where data is located
file_path = 'C:/Users/nahal/PycharmProjects/exercise5/project 1/.data/data_000637.txt'

# Define the column names for data
columns = ['HEAD', 'FPGA', 'TDC_CHANNEL', 'ORBIT_CNT', 'BX_COUNTER', 'TDC_MEAS']

# Read the data into a Pandas DataFrame
Pandas_DataFrame = pd.read_csv(file_path, names=columns, skiprows=1, nrows=5)

# Display the first few rows of the DataFrame
print(Pandas_DataFrame.head())

#---------------------------------------------------------------------------------------------------------------
# exercise 5.PART TWO


import pandas as pd

# Set the file path where your data is located.
file_path = 'C:/Users/nahal/PycharmProjects/exercise5/project2/.data/data_000637.txt'

# Define the column names for your data.
columns = ['HEAD', 'FPGA', 'TDC_CHANNEL', 'ORBIT_CNT', 'BX', 'TDC_MEAS']

# Read the data from the file into a pandas DataFrame.
pandas_DataFrame = pd.read_csv(file_path, names=columns, skiprows=1, nrows=5)

# Find the unique values in the 'BX' column.
BX_values = pandas_DataFrame['BX'].unique()

# Find the maximum value in the 'BX' column.
maximum_value = pandas_DataFrame['BX'].max()

# Find a point where the 'BX' is reset to 0.
point = BX_values[0]

# Calculate the estimated number of BX in an ORBIT.
estimated_bx_in_orbit = maximum_value + point

# Display the result.
print(f"\nEstimated number of BX in an ORBIT: {estimated_bx_in_orbit}")

#---------------------------------------------------------------------------------------------------------------
# exercise 5.PART THREE


import pandas as pd

# Set the file path where data is located
file_path = 'C:/Users/nahal/PycharmProjects/exercise5/project 3/.data/data_000637.txt'

# Define the column names for data
columns = ['HEAD', 'FPGA', 'TDC_CHANNEL', 'ORBIT_CNT', 'BX', 'TDC_MEAS']

# Read the data into a Pandas DataFrame
pandas_DataFrame = pd.read_csv(file_path, names=columns, nrows=5)

# Convert the entire DataFrame to numeric, replacing non-numeric values with NaN
pandas_DataFrame = pandas_DataFrame.apply(pd.to_numeric, errors='coerce')

# Calculate values for the 'absolute_time' column
orbit_time = pandas_DataFrame['ORBIT_CNT'] * 25 * 30
bx_time = pandas_DataFrame['BX'] * 25
tdc_time = pandas_DataFrame['TDC_MEAS'] * 25/30  # Contribution from 'TDC_MEAS'

# Create the 'absolute_time' column by adding the values
pandas_DataFrame['absolute_time'] = orbit_time + bx_time + tdc_time

# Introduce an offset to make the start of data
offset = pandas_DataFrame['absolute_time'].min()
pandas_DataFrame['absolute_time'] = pandas_DataFrame['absolute_time'].sub(offset)

# Convert the 'absolute_time' column to a Time Series
pandas_DataFrame['absolute_time'] = pd.to_datetime(pandas_DataFrame['absolute_time'], unit='ns')

# Display the DataFrame with the new 'absolute_time' column
print(pandas_DataFrame)

#---------------------------------------------------------------------------------------------------------------
# exercise 5.PART FOUR


import pandas as pd

# Set the file path where data is located
file_path = 'C:/Users/nahal/PycharmProjects/exercise5/project 4/.data/data_000637.txt'

# Define the column names for data
columns = ['HEAD', 'FPGA', 'TDC_CHANNEL', 'ORBIT_CNT', 'BX', 'TDC_MEAS']

# Indicate the dtype of any problematic columns.
dtype_dict = {'ORBIT_CNT': 'float64', 'BX': 'float64', 'TDC_MEAS': 'float64'}

# Read the data into a Pandas DataFrame, skipping the first row (header)
Pandas_DataFrame = pd.read_csv(file_path, names=columns, skiprows=1, dtype=dtype_dict)

columns_to_check = ['ORBIT_CNT', 'BX', 'TDC_MEAS']

for column in columns_to_check:
    values = Pandas_DataFrame[column]
    unique_values = values.unique()
    print(f"\nUnique values in {column}: {unique_values}")

# Calculate values for the 'absolute_time' column
orbit_time = Pandas_DataFrame['ORBIT_CNT'] * 25 * 30
bx_time = Pandas_DataFrame['BX'] * 25

# Perform the division
tdc_time = Pandas_DataFrame['TDC_MEAS'] * 25 / 30

# Create the 'absolute_time' column by adding the values
Pandas_DataFrame['absolute_time'] = orbit_time + bx_time + tdc_time

# Introduce an offset to make the start of data
offset = Pandas_DataFrame['absolute_time'].min()
Pandas_DataFrame['absolute_time'] = Pandas_DataFrame['absolute_time'].sub(offset)

# Convert the 'absolute_time' column to a Time Series
Pandas_DataFrame['absolute_time'] = pd.to_datetime(Pandas_DataFrame['absolute_time'], unit='ns')

# Calculate the duration
start_time = Pandas_DataFrame['absolute_time'].min()
end_time = Pandas_DataFrame['absolute_time'].max()
duration = end_time - start_time

# Print the duration in days, hours, minutes, and seconds
days = duration.days
hours = duration.seconds // 3600
minutes = (duration.seconds // 60) % 60
seconds = duration.seconds % 60

print(f"\nDuration: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

#---------------------------------------------------------------------------------------------------------------
# exercise 5.PART FIVE


import pandas as pd

# Set the file path where data is saved
file_path = 'C:/Users/nahal/PycharmProjects/exercise5/project 5/.data/data_000637.txt'

# Define the names of the columns in the data
columns = ['HEAD', 'FPGA', 'TDC_CHANNEL', 'ORBIT_CNT', 'BX', 'TDC_MEAS']

dtypes = {'ORBIT_CNT': int, 'BX': int, 'TDC_MEAS': int}

# Read the data from the file into a table (DataFrame)
Pandas_DataFrame = pd.read_csv(file_path, names=columns, dtype=dtypes, skiprows=1)

# Group the data by TDC_CHANNEL and count how many times each channel appears
channel_counts = Pandas_DataFrame.groupby('TDC_CHANNEL').size()

# Sort the channels in descending order of appearance frequency.
sorted_channels = channel_counts.sort_values(ascending=False)

# Print the three most often appearing channels along with their frequency of occurrence.
top_3_noisy_channels = sorted_channels.head(3)

print("Top 3 Noisy Channels:")
print(top_3_noisy_channels)

#---------------------------------------------------------------------------------------------------------------
# exercise 5.PART SIX


import pandas as pd

# Set the file path where the data is saved
file_path = 'C:/Users/nahal/PycharmProjects/exercise5/project 6/.data/data_000637.txt'

# Define the names of the columns in the data
columns = ['HEAD', 'FPGA', 'TDC_CHANNEL', 'ORBIT_CNT', 'BX', 'TDC_MEAS']

# Specify the data types for certain columns
dtypes = {'ORBIT_CNT': int, 'BX': int, 'TDC_MEAS': int}

# Read the data from the file into a table (DataFrame)
Pandas_DataFrame = pd.read_csv(file_path, names=columns, dtype=dtypes, skiprows=1)

# Identify non-empty orbits (orbits with at least one hit)
non_empty_orbits = Pandas_DataFrame['TDC_CHANNEL'].notna()

# Aggregate the different orbits where at least one impact occurs.
non_empty_orbits_count = Pandas_DataFrame[non_empty_orbits]['ORBIT_CNT'].nunique()

# Print the result
print("Number of non-empty orbits:", non_empty_orbits_count)

#---------------------------------------------------------------------------------------------------------------
# exercise 5.PART SEVEN


import pandas as pd

# Set the file path where the data is saved
file_path = 'C:/Users/nahal/PycharmProjects/exercise5/project 7/.data/data_000637.txt'

# Define the names of the columns in the data
columns = ['HEAD', 'FPGA', 'TDC_CHANNEL', 'ORBIT_CNT', 'BX', 'TDC_MEAS']

# Specify the data types for each columns
dtypes = {'ORBIT_CNT': int, 'BX': int, 'TDC_MEAS': int}

# Read the data from the file into a table (DataFrame)
Pandas_DataFrame = pd.read_csv(file_path, names=columns, dtype=dtypes, skiprows=1)

# Identify rows where TDC_CHANNEL is 139
tdc_channel_value = 139
tdc_channel_new = Pandas_DataFrame['TDC_CHANNEL'] == tdc_channel_value

# Identify non-empty orbits for TDC_CHANNEL=139
tdc_channel_value = 139
tdc_channel_new = Pandas_DataFrame['TDC_CHANNEL'] == tdc_channel_value

non_empty_orbits = Pandas_DataFrame[tdc_channel_new & Pandas_DataFrame['TDC_CHANNEL'].notna()]
non_empty_orbits_new = non_empty_orbits['ORBIT_CNT'].unique()

# Count the number of unique orbits with at least one measurement from TDC_CHANNEL=139
count_tdc_new = len(non_empty_orbits_new)

# Print the result
print("Number of unique orbits with at least one measurement from TDC_CHANNEL=139 is", count_tdc_new)

#---------------------------------------------------------------------------------------------------------------
# exercise 5.PART EIGHT


import pandas as pd

# Set the file path where the data is saved
file_path = 'C:/Users/nahal/PycharmProjects/exercise5/project 8/.data/data_000637.txt'

# Define the names of the columns in the data
columns = ['HEAD', 'FPGA', 'TDC_CHANNEL', 'ORBIT_CNT', 'BX', 'TDC_MEAS']

# Specify the data types for certain columns
dtypes = {'ORBIT_CNT': int, 'BX': int, 'TDC_MEAS': int}

# Read the data from the file into a table (DataFrame)
Pandas_DataFrame = pd.read_csv(file_path, names=columns, dtype=dtypes, skiprows=1)

# Group the data by FPGA and TDC_CHANNEL, and count the occurrences
counts_fpga_tdc = Pandas_DataFrame.groupby(['FPGA', 'TDC_CHANNEL']).size()

# Separate the counts for each FPGA into two Series
fpga_zero = 0
if fpga_zero in counts_fpga_tdc.index.levels[0]:
    fpga_zero_counts = counts_fpga_tdc[fpga_zero]
else:
    fpga_0_counts = pd.Series(dtype=int)

fpga_one = 1
if fpga_one in counts_fpga_tdc.index.levels[0]:
    fpga_one_counts = counts_fpga_tdc[fpga_one]
else:
    fpga_one_counts = pd.Series(dtype=int)

# Print the resulting Series
print("Counts for TDC channels in FPGA 0:")
print(fpga_zero_counts)

print("\nCounts for TDC channels in FPGA 1:")
print(fpga_one_counts)

#---------------------------------------------------------------------------------------------------------------
