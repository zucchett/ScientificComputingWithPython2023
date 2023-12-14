#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('mkdir data_lab/')

# check the content (it's empty now of course)
get_ipython().system('ls -ltr data_lab/')

# in the case you need to move there:
get_ipython().system('cd data_lab/')


# 1\. **Text files**
# 
# Perform the following operations on plain `txt` files:
# 
# + create a list of integrer numbers and then save it to a text file named `data_int.txt`. Run the `cat` command to print the content of the file.
# + create a matrix of 5x5 floats and then save it to a text file named `data_float.txt`. Use the `cat` command to print the content of the file.
# + load the `txt` file of the previous point and convert it to a `csv` file by hand.

# In[ ]:


import numpy as np

max_n = 101
numbers = [x for x in range(1, max_n)]
file_name = 'data_int.txt'

# Writing the list of numbers to the file
with open(file_name, mode='w') as outfile:
    for num in numbers:
        outfile.write(str(num) + ', ')

# Using cat command to print the content of the file
get_ipython().system('cat data_int.txt')

matrix = np.random.rand(5, 5)
np.savetxt('data_float.out', matrix)

# Using cat command to print the content of the file
get_ipython().system("cat 'data_float.out'")

# Read the text file
with open("data_float.out", "r") as txt_file:
    content = txt_file.read()

# Replace spaces with commas
csv_content = content.replace(" ", ",")

# Write the CSV content to a new file
with open("data_float.csv", "w") as csv_file:
    csv_file.write(csv_content)
    
get_ipython().system('cat "data_float.csv"')


# 2\. **JSON files**
# 
# Load the file `user_data.json`, which can be found at:
# 
# - https://www.dropbox.com/s/sz5klcdpckc39hd/user_data.json
# 
# and filter the data by the "CreditCardType" when it equals to "American Express". Than save the data to a new CSV file.

# In[ ]:


get_ipython().system('wget https://www.dropbox.com/s/sz5klcdpckc39hd/user_data.json -P data_lab/')


# In[ ]:


import json
import csv

with open('data_lab/user_data.json', 'r') as file:
    data = json.load(file)
    
filtered_data = [item for item in data if item.get('CreditCardType') == 'American Express']

csv_file = 'data_lab/AmericanExpress.csv'
with open(csv_file, 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=filtered_data[0].keys())
    csv_writer.writeheader()
    csv_writer.writerows(filtered_data)


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

# In[ ]:


get_ipython().system('wget https://www.dropbox.com/s/kgshemfgk22iy79/mushrooms_categorized.csv -P data_lab/')


# In[ ]:


import csv
import pandas as pd
import json

df = pd.read_csv('data_lab/mushrooms_categorized.csv')
print(df)

average_data = df.groupby('class').mean()

json_file_path = 'data_lab/avg_mushrooms.json'
df.to_json(json_file_path, orient='records', lines=True)


# 4\. **Reading a database**
# 
# Get the database `sakila.db` from the lecture `06_dataio.ipynb`, and import the table `actors` as a Pandas dataframe. Using the dataframe, count how many actors have a first name that begins with `A`.
# 
# *Hint:* use the Series `.str` method to apply the Python string methods to the elements of a Series, see [documentation](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.html).

# In[ ]:


import sqlite3 as sql

conn = sql.connect('data/sakila.db')
cur = conn.cursor()

# query data from database: select all content from the table "actor"
query = "SELECT * FROM actor"
actors = cur.execute(query).fetchall()

# create a DataFrame from the DB data
df = pd.DataFrame(actors)

# close the cursor and connection
cur.close()
conn.close()

# show df
print(df)

count_actors_with_a = df.iloc[:, 1].str.startswith('A').sum()

print(f"Number of actors with a first name starting with 'A': {count_actors_with_a}")


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

# In[1]:


get_ipython().system('wget https://www.dropbox.com/s/8m0syw2tkul3dap/credit_card.dat -P data_lab/')


# In[9]:


def binary_to_decimal(binary_str):
    decimal_num = int(binary_str, 2)
    return decimal_num

with open('data_lab/credit_card.dat', 'r') as file:
    for line in file:
        # Remove trailing whitespace and padding
        line = line.strip()[:-4]
                
        # Split the line into 6-bit chunks
        chunks = [line[i:i+6] for i in range(0, len(line), 6)]

        # Convert each 6-bit chunk to decimal and then to character
        credit_card_number = ''.join([chr(binary_to_decimal(chunk)) for chunk in chunks])

        if credit_card_number == "": 
            break
        
        print(f"Credit Card Number: {credit_card_number}")


# 6\. **Write data to a binary file**
# 
# a) Start from the `data/data_000637.txt` file that we have used during the previous lectures, and convert it to a binary file according to the format defined below:

# In[13]:


import numpy as np
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

# In[ ]:


get_ipython().system('cd')
get_ipython().system('cd data/')


# In[ ]:


import pandas as pd

file_path = 'data/data_000637.txt'

df = pd.read_csv(file_path, nrows=10)

