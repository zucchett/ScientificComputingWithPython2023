#---------------------------------------------------------------------------------------------------------------
# exercise 6.PART ONE.Text files


import numpy as np
import pandas as pd

# Create a list of integers and save it to a text file (data_int.txt)
list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Enter the file name and select "w" to open the file in write mode.
file_name = 'data_int.txt'

# To ensure the correct file working , open the file using a 'with' statement.
with open(file_name, 'w') as file:
    # Go over each number in the list once.
    for number in list:
        # Enter the number in the file and end it with a newline.
        file.write(f"{number}\n")

# Create a 5x5 matrix of random floats and save it to a text file (data_float.txt)
matrix = np.random.rand(5, 5)

# Save the matrix to a file named data_float.txt
np.savetxt('data_float.txt', matrix)

# Load the data from data_float.txt
loaded_data = np.loadtxt('data_float.txt')

# Convert the loaded data to a DataFrame
DataFrame = pd.DataFrame(loaded_data)

# Save the DataFrame to a CSV file named data_float.csv
DataFrame.to_csv('data_float.csv', index=False)

#---------------------------------------------------------------------------------------------------------------
# exercise 6.PART TWO. JSON files


import requests
import pandas as pd

# Download JSON data from the provided URL
url = "https://www.dropbox.com/s/sz5klcdpckc39hd/user_data.json?dl=1"  # dl=1 is used to directly download the file
response = requests.get(url)
data = response.json()

# Create a DataFrame from the JSON data
DataFrame = pd.DataFrame(data)

# Filter data by "CreditCardType" equal to "American Express"
filtered_data = DataFrame[DataFrame['CreditCardType'] == 'American Express']

# Save the filtered data to a new CSV file
filtered_data.to_csv('american_express_data.csv', index=False)

print("Data filtered and saved to american_express_data.csv")

#---------------------------------------------------------------------------------------------------------------
# exercise 6.PART THREE.CSV files with Pandas


import pandas as pd

# Load the CSV file into a DataFrame
url = "https://www.dropbox.com/s/kgshemfgk22iy79/mushrooms_categorized.csv?dl=1"
DataFrame = pd.read_csv(url)

# Explore and print the DataFrame
print("Exploring DataFrame:")
print(DataFrame.head())  # Display the first few rows of the DataFrame

# Calculate the average value of each feature, separately for each class, using groupby()
grouped_class = DataFrame.groupby('class')
average = grouped_class.mean()


# Print the average values
print("\nAverage values for each feature:")
print(average)

# Save the DataFrame to a JSON file
DataFrame.to_json('mushrooms_average_values.json', orient='records')

print("\nData saved to mushrooms_average_values.json")

#---------------------------------------------------------------------------------------------------------------
# exercise 6.PART FOUR.Reading a database


import pandas as pd
import sqlite3

# Connect to the Sakila database
db_path = "C:/Users/nahal/PycharmProjects/exercise6/project 4/sqlite3/.data/sakila.db"
connect = sqlite3.connect(db_path)

# Query the actors table and load it into a Pandas DataFrame
query_actors = "SELECT * FROM actor"
actors_DataFrame = pd.read_sql_query(query_actors, connect)

# Count actors with a first name that begins with 'A'
filtered_actors = actors_DataFrame['first_name'].str.startswith('A')
actors = actors_DataFrame[filtered_actors]
count_actors = actors.shape[0]

# Print the result
print(f"Number of actors with a first name starting with 'A': {count_actors}")

# Close the database connection
connect.close()

#---------------------------------------------------------------------------------------------------------------
# exercise 6.PART FIVE.Reading the credit card numbers


# Function to convert binary to decimal
def binary_to_decimal(binary_str):
    return int(binary_str, 2)

# Function to read credit card numbers from a binary file
def read_credit_card_numbers(file_path):
    # Open the binary file in read mode
    with open(file_path, 'rb') as file:
        # Loop in each line in the file
        for line in file:
            stripped_line = line.rstrip()  # Remove trailing whitespaces and newline
            binary_numbers = stripped_line[:-1]  # Remove the last character (padding)

            block_size = 6  # Number of bits in each block
            blocks = []  # List to store the blocks

            # Loop through the binary_numbers string in steps of block_size
            start_index = 0
            end_index = len(binary_numbers)
            step = block_size

            for i in range(start_index, end_index, step):
                # Extract a block of size block_size from the binary_numbers string
                start_index = i
                end_index = i + block_size
                block = binary_numbers[start_index:end_index]

                # Add the block to the list of blocks
                blocks.append(block)

            # Convert each block from binary to decimal
            decimal_numbers = []  # List to store the decimal numbers

            for block in blocks:
                decimal_number = binary_to_decimal(block)
                decimal_numbers.append(decimal_number)

            # Join the decimal numbers to form the credit card number
            string_numbers = map(str, decimal_numbers)  # Convert decimal numbers to strings
            credit_card = ''.join(string_numbers)  # Join the strings to form the credit card number

            # Print the credit card number
            print(credit_card)

# Main part of the program
if __name__ == "__main__":
    # Provide the correct file path or download the file from the given link
    file_path = "C:/Users/nahal/PycharmProjects/exercise6/project 5/credit_card.dat"
    # Call the function to read and process credit card numbers
    read_credit_card_numbers(file_path)

#---------------------------------------------------------------------------------------------------------------
# exercise 6.PART SIX.Write data to a binary file


import pandas as pd
import struct
import os

# File paths
text_file_path = ".data/data_000637.txt"
binary_file_path = ".data/data_000637.bin"

# a) Convert text file to binary:
# Read the first 10 lines from the text file using Pandas
dataframe = pd.read_csv(text_file_path, nrows=10, header=None, delimiter='\t', skiprows=1)

# Print the DataFrame to understand its structure
print("DataFrame from Text File:")
print(dataframe)

# Function to pack values into a single 64-bit word
def pack_values(data1, data2):
    int_data1 = int(data1) << 32
    float_data2 = struct.unpack('!I', struct.pack('!f', float(data2)))[0]
    packed_data = int_data1 | float_data2
    return packed_data

# Open the binary file for writing
with open(binary_file_path, 'wb') as binary_file:
    # Check if the DataFrame has at least two columns
    if len(dataframe.columns) < 2:
        print("\nError: DataFrame must have at least two columns.")
    else:
        # Iterate over each row in the DataFrame
        for row in dataframe.itertuples(index=False):
            # Access each column using dot notation
            data1, data2 = row[0], row[1]
            # Rest of your code inside the loop
            packed_word = pack_values(data1, data2)
            binary_file.write(struct.pack('<q', packed_word))

# b) Check binary file consistency:
# Function to unpack values from a 64-bit word
def unpack_values(word):
    integer_part = word & 0xFFFFFFFF
    packed_float = struct.pack('!I', integer_part)
    data2 = struct.unpack('!f', packed_float)[0]
    data1 = word >> 32
    return data1, data2

# Read the binary file and compare the content with the original data
with open(binary_file_path, 'rb') as binary_file:
    while True:
        # Read 8 bytes (64 bits) from the binary file
        packed_word = binary_file.read(8)
        # Check if there is no more data to read
        if not packed_word:
            break
        # Unpack values and print
        unpacked_data1, unpacked_data2 = unpack_values(struct.unpack('<q', packed_word)[0])
        formatted_string = f"\nUnpacked Data1: {unpacked_data1}, Unpacked Data2: {unpacked_data2}"
        print(formatted_string)

# c) Difference in size on disk:
# Get the size of the text file
text_file_size = os.path.getsize(text_file_path)

# Get the size of the binary file
binary_file_size = os.path.getsize(binary_file_path)

# Print the results
print(f"\nSize of Text File: {text_file_size} bytes")
print(f"Size of Binary File: {binary_file_size} bytes")

#---------------------------------------------------------------------------------------------------------------
