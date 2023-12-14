import numpy as np
import pandas as pd
import json
import csv
import sqlite3 as sql
import struct
import os

def ex1():
	print("1. Text files")
	array = np.random.randint(0, 1001, size=77)
	string_w = " ".join(map(str, array))

	with open("data_int.txt", "w") as file:
		file.write(string_w)
	print("List of integers from file")
	with open("data_int.txt", "r") as file:
		data = file.read()
	print(data) 

	float_matrix = np.random.rand(5, 5)
	np.savetxt("data_float.txt", float_matrix)
	
	print("Matrix 5x5 float")
	with open("data_float.txt", "r") as file:
		data = file.read()
	print(data) 

	csv_file = pd.read_csv("data_float.txt")
	csv_file.to_csv("data_float.csv", sep=" ", index=False)
	print("Data from csv file")
	with open("data_float.csv", "r") as file:
		data = file.read()
	print(data) 
	
def ex2():
	print("2. JSON files")
	with open("user_data.json") as json_file:
		data = json.load(json_file)

	data_filter = [item for item in data if item["CreditCardType"] == "American Express"]

	with open("ae_users.csv", "w", newline="") as csv_file:
		csv_writer = csv.DictWriter(csv_file, fieldnames=data[0].keys(), delimiter="\t")
		csv_writer.writeheader()
		csv_writer.writerows(data_filter)

	with open("ae_users.csv", "r") as csv_file:
		print(csv_file.read())
	
def ex3():
	print("3. CSV files with Pandas")
	data = pd.read_csv('mushrooms_categorized.csv')
	print("Exploring DataFrame:")
	print(data) 

	average_value = data.groupby('class').mean()
	print("\nThe average value of each feature, separately for each class")
	print(average_value)

	average_value.to_json('mushrooms_average_values.json')

def ex4():
	print("4. Reading a database")
	conn = sql.connect('sakila.db')
	query = "SELECT * FROM actor"
	actors_data = pd.read_sql_query(query, conn)

	count_actors_with_A = actors_data[actors_data['first_name'].str.startswith('A')].shape[0]

	print("The amount of actors have a first name that begins with A:", count_actors_with_A)
	
def ex5():
	print("5. Reading the credit card numbers")
	cards= open('credit_card.dat')
	binary_data = cards.read().split('\n')
	n = 6
	for item in binary_data:
		card_number = ""
		for index in range(0, len(item), n):
			binary = item[index: index + n]
			decimal = int(binary, 2)
			card_number += chr(decimal)
		print(card_number)

def ex6():
    
	print("Write data to a binary file")
	datatxt = pd.read_csv('data_000637.txt', nrows=10)
	binary_file = open("data_000637.dat", 'wb')
	for i in range(len(datatxt)):
		word = ((datatxt.iloc[i, 0] & 0x3) << 62 |
				(datatxt.iloc[i, 1] & 0xF) << 58 |
				(datatxt.iloc[i, 2] & 0x1FF) << 49 |
				(datatxt.iloc[i, 3] & 0xFFFFFFFF) << 17 |
				(datatxt.iloc[i, 4] & 0xFFF) << 5 |
				(datatxt.iloc[i, 5] & 0x1F))
		binary_file.write(struct.pack('<q', word))
	binary_file.close()
	print("Print data from txt file\n", datatxt)

	data = {}

	with open('data_000637.dat', 'rb') as file:
		file_content = file.read()
		word_counter = 0
		word_size = 8 
		for i in range(0, len(file_content), word_size):
			word_counter += 1
			if word_counter > 10: break
			word = struct.unpack('<q', file_content[i : i + word_size])[0] # get an 8-byte word
			head     = (word >> 62) & 0x3
			fpga     = (word >> 58) & 0xF
			tdc_chan = (word >> 49) & 0x1FF
			orb_cnt  = (word >> 17) & 0xFFFFFFFF
			bx       = (word >> 5 ) & 0xFFF
			tdc_meas = (word >> 0 ) & 0x1F
			#if i == 0: print ('{0}\t{1}\t{2}\t{3}\t{4}\t{5}'.format('HEAD', 'FPGA', 'CHANNEL', 'ORBIT_CNT', 'BX_CNT', 'TDC_MEAS'))
			#print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}'.format(head, fpga, tdc_chan, orb_cnt, bx, tdc_meas))
			entry = {'HEAD' : head, 'FPGA' : fpga, 'CHANNEL' : tdc_chan, 'ORBIT_CNT' : orb_cnt, 'BX_CNT' : bx, 'TDC_MEAS' : tdc_meas}
			#df = df.append(entry, ignore_index=True)
			data[word_counter] = entry
			
	df = pd.DataFrame(data).T
	
	print("Data from dat file\n", df)
	
	
	text_size = os.path.getsize('data_000637.txt')
	binary_size = os.path.getsize('data_000637.dat')
	print("size on disk text file: ", text_size)
	print("size on disk binary file: ", binary_size)
	
ex1()
ex2()
ex3()
ex4()
ex5()
ex6()