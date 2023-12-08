#SOLUTION NUMBER 1

import numpy as np

# Create a list of integers
int_num = list(range(10))  #

# Save the matrix to
with open('data_int.txt', 'w') as f:
    for num in int_num:
        f.write(str(num))
        print()

# Create a 5x5 matrix of floats filled with zeros and save it to the file below
Float_M = np.zeros((5, 5), dtype=float)
np.savetxt('data_float.txt', Float_M, fmt='%.2f')

# Load the text file
with open('data_float.txt', 'r') as file:
    content = file.read()

# Convert and save the text content to a CSV format
csv_content = content.replace(' ', ',')
with open('data.csv', 'w') as file:
    file.write(csv_content)

### print the text using git bash
# cat data_int.txt
# cat data_float.txt
# cat data.csv

/////////////////END OF NUMBER 1///

#SOLUTION NUMBER 2

import json
import csv
#Filtering data
data = json.load(open('C:\\Users\\dell\\Desktop\\data\\user_data.json'))
filtered = [dict for dict in data if dict['CreditCardType']=='American Express']
print("Filtered data: \n", filtered)

#Writing the result in csv file
writer = csv.DictWriter(open('filtered.csv', 'a'), filtered[0].keys())
for dict in filtered:
    writer.writerow(dict)
/////////END OF SOLUTION 2///

#SOLUTION NUMBER 3
import pandas as pd
import json

df = pd.read_csv("C:\\Users\\dell\\Desktop\\data\\mushrooms_categorized.csv")

means = df.groupby(["class"]).agg('mean')
print(means)

# Save the means DataFrame to a JSON file
means.to_json("C:\\Users\\dell\\Desktop\\data\\mushrooms_means.json")

print("Means DataFrame saved to mushrooms_means.json")

///////////////END OF SOLUTION 3////

#SOLUTION NUMBER 4
import pandas as pd
import sqlite3

# Connect to the sakila.db database
conn = sqlite3.connect('https://github.com/zucchett/ScientificComputingWithPython2023/blob/main/06ex_dataio.ipynb.db')

# Query the actors table and import the data into a DataFrame
query = "SELECT * FROM actor"
actors_df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Count the number of actors with the first name starting with 'A'
count_actors_starting_with_A = len(actors_df[actors_df['first_name'].str.startswith('A')])

print(f"The number of actors with the first name starting with 'A' is: {count_actors_starting_with_A}")
///////END OF SOLUTION 4////

#SOLUTION NUMBER 5

import sqlite3
import pandas as pd

with open('C:\\Users\\dell\\Desktop\\data\\credit_card.dat','rb') as file:
    while True:
        file_content=file.readline()
        # read the file dividing the sequences of 6 bits
        ints=[]
        try:
            for i in range(0,19*6,6):
                if (i==24 or i==54 or i==84):
                    continue
                ints.append(int(file_content[i:i+6], 2))
        except ValueError:
            break
        print("-". join(str(j) for j in ints))

/////////////////////////////END OF NUMBER 5/////

#SOLUTION NUMBER 6

import pandas as pd
import struct
import os

# Read the first 10 lines using Pandas
file_path = 'C:\\Users\\dell\\Desktop\\data\\data_000637.txt'
data = pd.read_csv(file_path, nrows=10, header=None, delimiter='\t')

# Function to convert row values to a 64-bit word
def convert_to_word(row):
    word = 0
    for val in row:
        # Pack values into a single 64-bit word using bitwise shifts and OR operator
        word = (word << 8) | val
    return word

# Convert and write data to a binary file
binary_file_path = 'C:\\Users\\dell\\Desktop\\data\\data_000637.bin'
with open(binary_file_path, 'wb') as binary_file:
    for _, row in data.iterrows():
        word = convert_to_word(row)
        binary_file.write(struct.pack('<q', word))

# Read binary file and print contents
with open(binary_file_path, 'rb') as binary_file:
    content = binary_file.read()
    print(content)

    # Check file sizes

    txt_file_size = os.path.getsize(file_path)
    bin_file_size = os.path.getsize(binary_file_path)
    print(f"Size of text file: {txt_file_size} bytes")
    print(f"Size of binary file: {bin_file_size} bytes")
//////////////////END OF SOLUTION 6/////