#Exe06
##q1
# Creating a list of integers
integer_list = [x for x in range(20)]
# Writing the list of integers to a text file 'data_int.txt'
with open('data_int.txt', 'w') as file:
    for number in integer_list:
        file.write(f"{number}\n")
# Creating a 5x5 matrix of floats
float_matrix = [[0.1 * (i * 5 + j) for j in range(5)] for i in range(5)]
# Writing the matrix of floats to a text file 'data_float.txt'
with open('data_float.txt', 'w') as file:
    for row in float_matrix:
        file.write(' '.join(map(str, row)) + '\n')
#!cat data_int.txt
#!cat data_float.txt


##q2
import json
import pandas as pd
data = json.load(open('data/user_data.json'))
filtered_data=[d for d in data if d['CreditCardType']=='American Express']
df = pd.DataFrame(filtered_data)
df.to_csv("CreditCardType.csv")
cards=pd.read_csv('CreditCardType.csv')
cards

##3
import pandas as pd
import numpy as np
import json
df= pd.read_csv('data/mushrooms_categorized.csv')
mushrooms_mean=df.groupby(['class']).mean()
json = mushrooms_mean.to_json()
json

##4
import sqlite3 as sql
# create a connection to the database and a cursor to execute queries
conn = sql.connect('data/sakila.db.1')
cur = conn.cursor()
# query data from database: select all content from the table "actor"
query = "SELECT * FROM actor "
results = cur.execute(query).fetchall()
#print(results)
# create a DataFrame from the DB data
df = pd.DataFrame(results)
# close the cursor and connection
cur.close()
conn.close()
# print dataframe
df
# Counting actors with a first name that begins with 'A'
count_actors_with_A = df[df[1].str.split().str[0].str.startswith('A')].shape[0]
print(f"The number of actors with a first name starting with 'A' is: {count_actors_with_A}")

##5
with open('data/credit_card.dat','rb') as credit_card_dat:
    line = credit_card_dat.readlines() 
    for row in line:
        if(len(row) > 5): 
            utf_2_strng = row.decode("utf-8")
            utf_2_strng = utf_2_strng[0:114]   
            start_digit = 0
            digit_space = 6
            card_digits=[]
            for i in range(19):
                end_digit = start_digit + digit_space
                digits_4 = utf_2_strng[start_digit:(start_digit + digit_space)]
                card_digits.append(digits_4)
                start_digit = start_digit + digit_space                
            credit_card = ""
            counter = 1
            for i in range(0,19):
                credit_card = credit_card + chr(int(card_digits[i],2))
            print("The Credit Card Number is :",credit_card)


##6
import pandas as pd
import struct
import os

df = pd.read_csv('data/data_000637.txt')
# Writing packed values to a binary file
binary_file_path = 'data/data_000637.dat'  # Adjust the file path as needed
with open(binary_file_path, 'wb') as binary_file:
    for _, row in df.iterrows():
        packed_word = (
            (int(row['HEAD']) & 0b11) << 62 |
            (int(row['FPGA']) & 0b11111) << 58 |
            (int(row['TDC_CHANNEL']) & 0x1FF) << 49 |
            (int(row['ORBIT_CNT']) & 0xFFFFFFFF) << 17 |
            (int(row['BX_COUNTER']) & 0xFFF) << 5 |
            (int(row['TDC_MEAS']) & 0x1F)
        )
        binary_file.write(struct.pack('<q', packed_word))
# Reading and unpacking 64-bit words from the binary file
data = {}
with open('data/data_000637.dat', 'rb') as file:
    file_content = file.read()
    word_counter = 0
    word_size = 8  # size of the word in bytes
    for i in range(0, len(file_content), word_size):
        word_counter += 1
        if word_counter > 10:
            break
        word = struct.unpack('<q', file_content[i: i + word_size])[0]  # get an 8-byte word
        head = (word >> 62) & 0x3
        fpga = (word >> 58) & 0x1F
        tdc_chan = (word >> 49) & 0x1FF
        orb_cnt = (word >> 17) & 0xFFFFFFFF
        bx = (word >> 5) & 0xFFF
        tdc_meas = (word >> 0) & 0x1F
        entry = {'HEAD': head, 'FPGA': fpga, 'CHANNEL': tdc_chan, 'ORBIT_CNT': orb_cnt, 'BX_CNT': bx, 'TDC_MEAS': tdc_meas}
        data[word_counter] = entry

print(data)

txt_size = os.path.getsize('data/data_000637.txt')
bin_size = os.path.getsize('data/data_000637.bin')

print("Sizes:")
print("Text file size:", txt_size)
print("Binary file size:", bin_size)

