################################ 05_pandas ###################################################
from os import system
import numpy as np
import csv
import pandas as pd
import sqlite3 as sql

print("============== 1. Text files ==============")
list = [i for i in range(100)]
with open(r'C:\Users\LENOVO\PycharmProjects\computervisionLAB\data_int.txt', 'w') as fp:
    for i in list:
        fp.write("%s\n" % i)
    print('Done')
#system("cat data_int.txt")
matrix = np.random.random((5, 5))
np.savetxt('data_float.txt', matrix, fmt='%f')
#system("cat data_float.txt")

with open('data_float.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('data_float.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('title', 'intro'))
        writer.writerows(lines)
print("============== 2. JSON files ==============")

FilePath = 'user_data.json'
df = pd.read_json(FilePath)
new_df = df[df['CreditCardType'] == 'American Express']
new_df.to_csv("data.csv")

print("============== 3. CSV files with Pandas ==============")
df = pd.read_csv('mushrooms_categorized.csv')
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
average_values = df.groupby('class').mean()
print("Average values of each feature, separately for each class = ", average_values)
average_values.to_json('mushrooms_categorized.json')

print("============== 4. Reading a database ==============")
# Since I am using Pycharm, I downloaded the database using jupyter notebook then I added it to this directory so I can use it
conn = sql.connect('sakila.db')
cur = conn.cursor()
query = "SELECT * FROM actor;" # Selecting all attributes (*) from the table actors.
df4 = pd.read_sql_query(query, conn) # loading the result to a dataframe.
conn.close() #close the database connection
a_actors = df4[df4['first_name'].str.startswith('A')] # returns a dataframe from df4 that cntains only the actors that their names starts with a.
nb_a_actors = len(a_actors)
print("The number of actors with that their first name starts with a:", nb_a_actors)

print("============== 5. Reading the credit card numbers ==============")
file = 'credit_card.dat'
with open(file, 'rb') as file:
    data = file.read().decode('utf-8')
lines = data.splitlines()
print(lines)
credit_card = []
for line in lines:
    l = line[:-4] # Remove the last 4 bits (padding) and split the line into blocks
    blocks = [l[i:i+6] for i in range(0, len(l), 6)]
    card_number = ''.join([chr(int(block, 2)) for block in blocks])
    credit_card.append(card_number)

print("============== 6. Write data to a binary file ==============")
import struct
file= 'data_000637.txt'
data1=[]
df = pd.read_csv(file, sep=",", nrows=10) #Reading the first 10 lines using Pandas
print(df)
with open(file, 'wb') as binary_file:
    for _, row in df.iterrows(): #iterating the dataframe using iterrows predefined function.
        pack_val = struct.pack('<q',int(row['HEAD']) << 48 | int(row['FPGA']) << 32 | int(row['TDC_CHANNEL']) << 16 | int(row['ORBIT_CNT']))
        binary_file.write(pack_val)
        unpacked_values = struct.unpack('<q', pack_val)
        data1.append(unpacked_values[0])

print("done!")
df_txt = pd.read_csv(file,sep=",")

if list(df_txt['HEAD']) ==data1:
    print("the data consistency is verified!")
else:
    print("error!")
import os

text_size = os.path.getsize(file)
binary_size = os.path.getsize(file)
print(f"Size on disk for text file: ", text_size)
print(f"Size on disk for binary file: ", binary_size)


