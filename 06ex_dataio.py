#### Q1

import numpy as np
int_matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
np.savetxt("data_int.txt", int_matrix, fmt='%d')  # Specify fmt='%d' for integers
with open("data_int.txt", 'r') as file_int:
    data_int = file_int.read()
print("Data from data_int.txt:")
print(data_int)
print("Type integer data:")
# Display the content of the file using the 'type' command on Windows (The cat command is commonly used on Unix-like systems)
!type data_int.txt
float_matrix = np.random.rand(5, 5)
np.savetxt("data_float.txt", float_matrix)
with open("data_float.txt", 'r') as file_float:
    data_float = file_float.read()
print("\nData from data_float.txt:")
print(data_float)
print("Type float data:")
!type data_float.txt
# Step 3: Load the text file and convert it to a CSV file
loaded_data = np.loadtxt("data_float.txt")
np.savetxt("data_float.csv", loaded_data, delimiter=",", fmt='%.6f')
print("\nType CSV data:")
!type data_float.csv


#### Q2


import csv
import json # import the JSON module
data = json.load(open('user_data.json'))
print("Type:", type(data))  # Type: <class 'list'>
print("Keys:", data[0].keys())  # Keys: dict_keys(['ID', 'JobTitle', 'EmailAddress', 'FirstNameLastName', 'CreditCard', 'CreditCardType'])
print("Number of Entries:", len(data))  # 200
# Check if there are any missing values for a specific attribute
missing_credit_cards = any('CreditCard' not in entry for entry in data)
print("Are there missing credit card values?", missing_credit_cards)  # False
# # Assuming 'CreditCardType' is an attribute, print all its values
# credit_card_types = [entry['CreditCardType'] for entry in data]
# print("Credit Card Types:", credit_card_types)
# # Print unique values for a specific attribute
# unique_job_titles = set(entry['JobTitle'] for entry in data)
# print("Unique Job Titles:", unique_job_titles)
# Filter data by "CreditCardType" equals to "American Express"
filtered_data = [entry for entry in data if entry['CreditCardType'] == 'American Express']
# credit_card_types2 = [entryy['CreditCardType'] for entryy in filtered_data]
# print("Credit Card Types:", credit_card_types2)  # All of them American Express
# Save the filtered data to a new CSV file
csv_file_path = 'american_express_data.csv'
fields = filtered_data[0].keys()  # Assuming all entries have the same fields
with open(csv_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=fields)
    # Write the header
    csv_writer.writeheader()  # shows columns names fieldnames'e göre sırayla
    # Write the data
    csv_writer.writerows(filtered_data)  
print(f"Filtered data saved to {csv_file_path}")
!type american_express_data.csv


#### Q3

import pandas as pd
# import requests
# url = "https://www.dropbox.com/s/kgshemfgk22iy79/mushrooms_categorized.csv"
# response = requests.get(url)
# data = response.text
# # Print the first 10 lines of the data
# print('\n'.join(data.split('\n')[:10]))
# Update Dropbox
dropbox_url = "https://www.dropbox.com/s/kgshemfgk22iy79/mushrooms_categorized.csv"
direct_download_url = dropbox_url.replace("www.dropbox.com", "dl.dropboxusercontent.com")
# CSV dosyasını okuyun
df = pd.read_csv(direct_download_url)
#print("DataFrame:")
#print(df.head()) 
#print(df.columns)  # 23 column
#print(df.dtypes)  # all int64
# Calculate the average value of each feature, separately for each class using groupby
average_by_class = df.groupby('class').mean()
print("\nAverage Values by Class:")
print(average_by_class)
# Save the DataFrame to a JSON file
json_file_path = 'mushrooms_average_values.json'
average_by_class.to_json(json_file_path)
print(f"\nDataFrame saved to {json_file_path}")
!type mushrooms_average_values.json


#### Q4

# import dependencies
import sqlite3 as sql
import pandas as pd

# # create a connection to the database and a cursor to execute queries
# conn = sql.connect('sakila.db')
# cur = conn.cursor()
# # query data from database: select all content from the table "actor"
# query = "SELECT * FROM actor"
# results = cur.execute(query).fetchall()
# # create a DataFrame from the DB data
# df = pd.DataFrame(results)
# # close the cursor and connection
# cur.close()
# conn.close()

# # create a connection to the database and a cursor to execute queries
# conn = sql.connect('sakila.db')
# # read the 'actors' table into a Pandas DataFrame
# actors_df = pd.read_sql_query("SELECT * FROM actors", conn)
# # close the database connection
# conn.close()
# # count actors with first name starting with 'A'
# actors_with_A_count = actors_df[actors_df['first_name'].str.startswith('A', na=False)].shape[0]
# # print the result
# print(f"The number of actors with a first name starting with 'A' is: {actors_with_A_count}")



#### Q5

import pandas as pd
dosya_yolu = "credit_card.dat"
veri_df = pd.read_csv(dosya_yolu, sep='\t', header=None)  # Eğer dosya sekme ile ayrılmışsa sep='\t' kullanılabilir
#print(veri_df)
print(veri_df.shape)  # (51, 1)
# #print(veri_df.isnull().sum())  # 0
secili_indeksler = [0, 1, 8, 49, 50]
for indeks in secili_indeksler:
    satir = veri_df.iloc[indeks, 0]
    uzunluk = len(satir)
    print(f"{indeks}. satırın uzunluğu: {uzunluk}")  # 118 hepsi
toplam_karakter_sayisi = 0
for satir in veri_df.iloc[:, 0]:
    toplam_karakter_sayisi += len(satir)
print(f"Toplam karakter sayısı: {toplam_karakter_sayisi}")  # 5904
veri_df.iloc[:, 0] = veri_df.iloc[:, 0].apply(lambda x: x[:-4])  # her satır 114 oldu son satır gitti toplamda 50 satır kaldı
veri_df.drop(50, inplace=True)
# Sütun adını "credit_card" olarak güncelle
veri_df.columns = ["credit_card"]
# bosluk_sayisi = veri_df[0].apply(lambda x: x.count('1000001'))
# toplam_bosluk_sayisi = bosluk_sayisi.sum()
# print(f"Toplam boşluk sayısı: {toplam_bosluk_sayisi}")
# veri_df['uc_bosluk_var_mi'] = bosluk_sayisi == 3
# print(veri_df[['uc_bosluk_var_mi']])
# # Her bir satırdaki binary sayıları decimal sayılara çevir
# veri_df["credit_card"] = veri_df["credit_card"].apply(lambda x: int(x[:-4], 2) if x[:] else None)
# # NaN (Not a Number) olan değerleri filtrele
# veri_df = veri_df.dropna()
# print(veri_df)
# Decimal sayıları karakterlere çevir ve gerçek kredi kartı numarasını oluştur
#veri_df["real_credit_card"] = veri_df["decimal_numbers"].apply(lambda x: ''.join([chr(int(x[i:i+6], 2)) for i in range(0, 24, 6)]))
#veri_df["real_credit_card"] = veri_df["decimal_numbers"].apply(lambda x: ''.join([chr(int(str(x)[i:i+6], 2)) for i in range(0, 24, 6)]))
#print(veri_df["real_credit_card"])



#### Q6

from IPython.display import Image
import pandas as pd 
import struct
# # Step a: Write data to a binary file
# def txt_to_binary(input_txt, output_binary):
#     # Read the first 10 lines using Pandas
#     #df = pd.read_csv(input_txt, sep='\t', nrows=10)
#     df = pd.read_csv(input_txt, sep=',', nrows=10, header=None)
#     # Add 'HEAD' as a column based on the index
#     df['HEAD'] = df.index
#     # Print column names to check
#     print("Column names in the DataFrame:", df.columns)
#     # Open the binary file for writing
#     with open(output_binary, 'wb') as binary_file:
#         # Iterate over DataFrame rows
#         for index, row in df.iterrows():
#             # Print the row to check its structure
#             print("Row:", row)
#             # Pack values into a single 64-bit word
#             word = (int(row['HEAD']) << 48) | (int(row['FPGA']) << 40) | (int(row['TDC_CHANNEL']) << 32) | \
#                    (int(row['ORBIT_CNT']) << 0) | (int(row['BX_COUNTER']) << 16) | (int(row['TDC_MEAS']) << 8)
#             # Write the 64-bit word to the binary file
#             binary_file.write(struct.pack('<q', word))
#     print("Binary file created successfully.")
# # Step b: Check the consistency by reading the binary file
# def read_binary_and_compare(input_binary, input_txt):
#     # Read the binary file
#     with open(input_binary, 'rb') as binary_file:
#         # Unpack 64-bit words and print them
#         while True:
#             data = binary_file.read(8)
#             if not data:
#                 break
#             word = struct.unpack('<q', data)[0]
#             print(f"Read from binary: {word}")
#     # Read the txt file and compare
#     df_txt = pd.read_csv(input_txt, sep='\t', nrows=10)
#     print("\nContent of the txt file:")
#     print(df_txt)
# # Step c: Calculate the size difference between txt and binary files
# def compare_file_sizes(input_txt, input_binary):
#     size_txt = pd.read_csv(input_txt, sep='\t').memory_usage(index=False, deep=True).sum()
#     size_binary = os.path.getsize(input_binary)
#     print(f"\nSize of txt file on disk: {size_txt} bytes")
#     print(f"Size of binary file on disk: {size_binary} bytes")
#     print(f"Difference in size: {size_txt - size_binary} bytes")
# # Example usage
# input_txt_file = 'data_000637.txt'
# output_binary_file = 'data_000637.bin'
# # Step a: Write data to a binary file
# txt_to_binary(input_txt_file, output_binary_file)
# # Step b: Check the consistency by reading the binary file
# read_binary_and_compare(output_binary_file, input_txt_file)
# # Step c: Calculate the size difference between txt and binary files
# compare_file_sizes(input_txt_file, output_binary_file)
# file_name = "data_000637.txt" 
# data = pd.read_csv(file_name) 
# df = data.head(10)
# print(df)
#Image("images/data_format.png")

