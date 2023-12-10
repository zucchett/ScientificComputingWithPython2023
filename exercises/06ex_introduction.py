import json
import csv
import pandas as pd
import sqlite3 as sql
import struct

# 2. JSON files
print('JSON files')
json_filename = "data/user_data.json"
with open(json_filename, "r") as json_file:
    user_data = json.load(json_file)

filtered_data = [user for user in user_data if user.get("CreditCardType") == "American Express"]
csv_filename = "data/american_express_users.csv"
with open(csv_filename, "w", newline="") as csvfile:
    fieldnames = user_data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for user in filtered_data:
        writer.writerow(user)

print(f"Filtered data saved to {csv_filename}")

# 3. CSV files with Pandas
print('3. CSV files with Pandas')
url = "data/mushrooms_categorized.csv"
mushrooms_df = pd.read_csv(url)

print("DataFrame Info:")
print(mushrooms_df.info())
print("\nDataFrame Head:")
print(mushrooms_df.head())

average_values = mushrooms_df.groupby('class').mean()
print("\nAverage Values for Each Class:")
print(average_values)
json_filename = "data/mushrooms_average_values.json"
average_values.to_json(json_filename, orient='index')

print(f"\nDataFrame with average values saved to {json_filename} in JSON format.")

# 4.Reading a database
print("4.Reading a database")
conn = sql.connect('data/sakila.db')
actors_df = pd.read_sql_query("SELECT * FROM actor", conn)
conn.close()
count_a_actors = actors_df['first_name'].str.startswith('A').sum()

print(f"Number of actors with a first name starting with 'A': {count_a_actors}")

# 5. Reading the credit card numbers
print('Reading the credit card numbers')


def binary_to_decimal(binary_str):
    return int(binary_str, 2)


file_path = 'data/credit_card.dat'
with open(file_path, 'rb') as file:
    lines = file.readlines()
for line in lines:
    binary_string = line.rstrip(b'\n').decode('utf-8')[:-4]
    decimal_numbers = [int(binary_string[i:i + 6], 2) for i in range(0, len(binary_string), 6)]

    credit_card_number = ''.join(map(chr, decimal_numbers))

    print(f"Credit Card Number: {credit_card_number}")

# 6. Write data to a binary file
print('Write data to a binary file')
file_path = 'data/data_000637.txt'
df = pd.read_csv(file_path, nrows=10, delim_whitespace=True)

binary_file_path = 'data/data_000637_binary.bin'

with open(binary_file_path, 'wb') as binary_file:
    for row in df.to_records(index=False):

        if len(row) == 1:
            word = struct.pack('<Q', int(row[0]))
        else:
            word = struct.pack('<QQQQ', *[int(val) for val in row])
        binary_file.write(word)
print(f"Binary file '{binary_file_path}' created successfully.")
