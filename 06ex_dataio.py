#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.1
int_num=[1,2,3,4,5,6,7,8,9,10]

with open('data_int.txt', 'w') as file:
    for number in int_num:
        file.write(str(number)+'\n')


# In[3]:


#1.2
import numpy as np

float_matrix= np.random.rand(5,5)

np.savetxt('data_float.txt', float_matrix)


# In[4]:


#2
import json
import csv

data = json.load(open(r'data\user_data.json'))

output_data = [x for x in data if x['CreditCardType'] == 'American Express']

csv_file_name = 'american_express_data.csv'

with open(csv_file_name, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=output_data[0].keys())
    csv_writer.writeheader()
    csv_writer.writerows(output_data)

print(f'Data filtered by "American Express" saved to {csv_file_name}')


# In[19]:


#3
import pandas as pd
import json
file_name="data/mushrooms_categorized.csv"
data = pd.read_csv(file_name)
by_class= data.groupby('class').mean()
json_file="by_class.json"
by_class.to_json(json_file, orient='index')
print(json_file)
#print(by_class)
#print(data)


# In[6]:


#4
import pandas as pd
import sqlite3 as sql

conn=sql.connect('data/sakila.db')
cur = conn.cursor
query = "select * FROM actor"
actors=pd.read_sql_query(query,conn)
conn.close()
count=actor[actor['first_name'].str.starswith('A')].shape[0]
print(f'Total actors with a first name starting with A: {count}')


# In[11]:


#5
def binary_to_card(binary_str):
    decimal_value = int(binary_str, 2)
    decimal_value >>= 4  # Ignore the last 4 bits
    return chr(decimal_value + ord('0'))

# Convert binary data to credit card numbers
with open("data/credit_card.dat", 'rb') as file:
    for line in file:
        binary_line = ''.join(format(byte, '08b') for byte in line)
        credit_card_numbers = [binary_to_card(binary_line[i:i+6]) for i in range(0, len(binary_line)-4, 6)]
        print(' '.join(credit_card_numbers))


# In[13]:


#6
import struct
import os
df = pd.read_csv('data/data_000637.txt', nrows=10)

with open('data_000637_binary.bin', 'wb') as binary_file:
    for _, row in df.iterrows():
        word = (
            (int(row['HEAD']) << 62) |
            (int(row['FPGA']) << 58) |
            (int(row['TDC_CHANNEL']) << 49) |
            (int(row['ORBIT_CNT']) << 17) |
            (int(row['BX_COUNTER']) << 5) |
            (int(row['TDC_MEAS']) << 0)
        )
        binary_file.write(struct.pack('<q', word))
        
with open('data_000637_binary.bin', 'rb') as binary_file:
    for _ in range(len(df)):
        packed_data = binary_file.read(8)
        unpacked_data = struct.unpack('<q', packed_data)
        print(unpacked_data)
        
txt_file_size = os.path.getsize('data/data_000637.txt')
binary_file_size = os.path.getsize('data_000637_binary.bin')

print(f'Txt file size: {txt_file_size} bytes')
print(f'Binary file size: {binary_file_size} bytes')
print(f'Difference in size: {txt_file_size - binary_file_size} bytes')


# In[1]:





# In[ ]:




