#!/usr/bin/env python
# coding: utf-8

# 1\. **Text files**
# 
# Perform the following operations on plain `txt` files:
# 
# + create a list of integrer numbers and then save it to a text file named `data_int.txt`. Run the `cat` command to print the content of the file.
# + create a matrix of 5x5 floats and then save it to a text file named `data_float.txt`. Use the `cat` command to print the content of the file.
# + load the `txt` file of the previous point and convert it to a `csv` file by hand.

# In[20]:
print("************************************1.*************************************************************************")

import numpy as np
import csv
import pandas as pd

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
with open("data_int.txt", "w") as file:
    for num in int_list:
        file.write(str(num) + "\n")

with open("data_int.txt", "r") as file:
    print(file.read())

float_matrix = np.random.random((5, 5))
with open("data_float.txt", "w") as file:
    for row in float_matrix:
        file.write("\t".join(map(str, row)) + "\n")

with open("data_float.txt", "r") as file:
    print(file.read())

with open("data_float.txt", "r") as file:
    lines = file.readlines()

csv_content = [line.strip().split("\t") for line in lines]

with open("data_float.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(csv_content)
    
    
csv_test = pd.read_csv("data_float.csv", delimiter=",", header=None)
csv_test.head()


# 2\. **JSON files**
# 
# Load the file `user_data.json`, which can be found at:
# 
# - https://www.dropbox.com/s/sz5klcdpckc39hd/user_data.json
# 
# and filter the data by the "CreditCardType" when it equals to "American Express". Than save the data to a new CSV file.

# In[2]:

print("************************************2.*************************************************************************")
user_data = pd.read_json(open('user_data.json'))
user_data_filtered = user_data[user_data['CreditCardType'] == 'American Express']
user_data_filtered.to_csv("user_data_filtered.csv",index=False)

csv_test = pd.read_csv("user_data_filtered.csv")
print("Size of the filtered user_data: "+str(csv_test['CreditCardType'].count()))
csv_test_american_express = (csv_test['CreditCardType'] == "American Express").sum()
print("Size of the users that CreditCardType = American Express: "+str(csv_test_american_express))    
    


# 3\. **CSV files with Pandas**
# 
# Load the file from this url:
# 
# - https://www.dropbox.com/s/kgshemfgk22iy79/mushrooms_categorized.csv
# 
# with Pandas. 
# 
# + explore and print the DataFrame
# + calculate, using `groupby()`, the average value of each feature, separately for each class
# + save the file in a JSON format.

# In[3]:
print("************************************3.*************************************************************************")

import pandas as pd

df = pd.read_csv("mushrooms_categorized.csv")

print("DataFrame Info:")
print(df.info())
print("\nDataFrame Head:")
print(df.head())


average_values = df.groupby("class").mean()

print("\nAverage Values for Each Feature, Separately for Each Class:")
print(average_values)


df.to_json("mushrooms_categorized.json", orient="records", lines=True)
print("\nDataFrame saved to mushrooms_categorized.json in JSON format.")




# 4\. **Reading a database**
# 
# Get the database `sakila.db` from the lecture `06_dataio.ipynb`, and import the table `actors` as a Pandas dataframe. Using the dataframe, count how many actors have a first name that begins with `A`.
# 
# *Hint:* use the Series `.str` method to apply the Python string methods to the elements of a Series, see [documentation](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.html).

# In[4]:

print("************************************4.*************************************************************************")
import sqlite3

database_path = "sakila.db" 
table_name = "actor"
conn = sqlite3.connect(database_path)
query = f"SELECT * FROM {table_name};"
actor_df = pd.read_sql_query(query, conn)
actor_with_A_count = actor_df[actor_df['first_name'].str.startswith('A')].shape[0]
print(f"Number of actors with first names starting with 'A': {actor_with_A_count}")
conn.close()



# 5\. **Reading the credit card numbers**
# 
# Get the binary file named `credit_card.dat` from this address:
# 
# - https://www.dropbox.com/s/8m0syw2tkul3dap/credit_card.dat
# 
# and convert the data into the real credit card number, knowing that:
# - each line corresponds to a credit card number, which consists of 16 characters (which are numbers in the 0-9 range) divided in 4 blocks, with a whitespace between each block
# - each character is written using a 6 bit binary representation (including the whitespace)
# - the final 4 bits of each line are a padding used to determine the end of the line, and can be ignored
# 
# *Hint*: convert the binary numbers to the decimal representation first, and then use the `chr()` function to convert the latter to a char

# In[19]:

print("************************************5.*************************************************************************")
card_numbers = []
with open('credit_card2.dat', 'r') as outfile:
    for i in outfile:
        card_number = ""
        for j in range(0, len(i)-6, 6):
            binary_to_decimal = int(i[j:j+6],2)
            card_number = card_number + chr(binary_to_decimal)
        card_numbers.append(card_number)
 
print(card_numbers)



# 6\. **Write data to a binary file**
# 
# a) Start from the `data/data_000637.txt` file that we have used during the previous lectures, and convert it to a binary file according to the format defined below:

# In[6]:

print("************************************6.*************************************************************************")
from IPython.display import Image
Image("images/data_format.png")


# *Hints*:
# - Read the first 10 lines using Pandas
# - Iterate over the DataFrame rows
# - For every row, "pack" the values (features) into a single 64-bit word, according to the format specified above. Use bit-wise shifts and operators to do so.
# - Write each 64-bit word to a binary file. You can use `struct` in this way:
# ```
# binary_file.write( struct.pack('<q', word) )
# ```
# where `word` is the 64-bit word.
# - Close the file after completing the loop.
# 
# b) Check that the binary file is correctly written by reading it with the code used in the lecture `06_dataio.ipynb`, and verify that the content of the `txt` and binary files is consistent.
# 
# c) What is the difference of the size on disk between equivalent `txt` and binary files?

# In[7]:
print("************************************7.*************************************************************************")

import pandas as pd
import struct


def txt_to_binary(input_txt_path, output_binary_path):
    df = pd.read_csv(input_txt_path, sep=',', header=None, skiprows=1) 
    
    with open(output_binary_path, 'wb') as binary_file:
        for _, row in df.iterrows():
            values = [int(value) for value in row]
            values += [0] * (8 - len(values))                        
            word = (values[0] << 56) | (values[1] << 48) | (values[2] << 40) | (values[3] << 32) | (values[4] << 24) | (values[5] << 16) | (values[6] << 8) | values[7]                        
            binary_file.write(struct.pack('<Q', word))

def read_binary_file(binary_file_path):
    with open(binary_file_path, 'rb') as binary_file:
        while True:
            data = binary_file.read(8)
            if not data:
                break  
            word = struct.unpack('<Q', data)[0]
            print(word)


input_txt_path = 'data_000637.txt'
output_binary_path = 'binary_output.bin'
txt_to_binary(input_txt_path, output_binary_path)



# In[8]:


import os

txt_file_path = 'data_000637.txt'
binary_file_path = 'binary_output.bin'
txt_size = os.path.getsize(txt_file_path)
binary_size = os.path.getsize(binary_file_path)
print(f"Size of txt file: {txt_size} bytes")
print(f"Size of binary file: {binary_size} bytes")
size_difference = txt_size - binary_size
print(f"Difference in size on disk: {size_difference} bytes")


# In[ ]:




