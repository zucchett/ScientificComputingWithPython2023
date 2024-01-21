import numpy as np
import pandas as pd
import json 
import sqlite3 as sql
import struct
import os

integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
with open('data_int.txt', 'w') as file:
    for number in integer_list:
        file.write(f"{number}\n")

float_matrix = np.random.rand(5, 5)
np.savetxt('data_float.txt', float_matrix, fmt='%f')

loaded_data = np.loadtxt('data_float.txt')
np.savetxt('data_float.csv', loaded_data, delimiter=',', fmt='%f')

##############################END OF TXT FILES.#######################################

with open('user_data.json', 'r') as json_file:
    data = json.load(json_file)

filtered_data = [entry for entry in data if entry.get('CreditCardType') == 'American Express']
filtered_df = pd.DataFrame(filtered_data)
filtered_df.to_csv('american_express_data.csv', index=False)
#print(filtered_df)

##############################END OF JSON FILES.#######################################

file_path = 'mushrooms_categorized.csv'
df = pd.read_csv(file_path)

print("DataFrame Info:")
print(df.info()) 
print("\nDataFrame Head:")
print(df.head())

average_values = df.groupby('class').mean()
print("\nAverage Values for Each Class:")
print(average_values)
average_values.to_json('average_values_per_class.json')

##############################END OF CSV FILES.#######################################

conn = sql.connect('sakila.db')
query = "SELECT count(*) FROM actor where first_name LIKE 'A%'"
actors_df = pd.read_sql_query(query, conn)
conn.close()

print("Number of actor starting with A:",actors_df.iloc[0,0])

##############################END OF READING A DATABASE.#######################################

with open('credit_card.dat', 'rb') as file:
    for line in file:
        binary_data = line.rstrip().decode()
        binary_data = binary_data[:-4]
        blocks = [binary_data[i:i + 6] for i in range(0, len(binary_data), 6)]
        card_number = ''.join(chr(int(block, 2)) for block in blocks)
        print(card_number)

##############################END OF READING CARD NUMBERS.#######################################

data = pd.read_csv('data/data_000637.txt', nrows=10, delimiter=',')

with open('data_000637.bin', 'wb') as binary_file:
    for index, row in data.iterrows():
        word = 0
        for i, value in enumerate(row):
            word |= (int(value) << (i * 8)) 
        
        binary_file.write(struct.pack('<q', word))

txt_file_size = os.path.getsize('data/data_000637.txt')
bin_file_size = os.path.getsize('data_000637.bin')

print("Size of txt file:", txt_file_size, "bytes")
print("Size of binary file:", bin_file_size, "bytes")