import numpy as np
import csv
from random import randrange
from os import system
import pandas as pd
from IPython.display import Image
Image("images/data_format.png")

# 1. Text files
# 1.1crete and save data_int.txt
list = []
for i in range(100):
    list.append(randrange(100))
print(list)

txt_file = open("data_int.txt", "w")
for element in list:
    txt_file.write(str(element) + " ")
txt_file.close()

system("cat data_int.txt")


# 5x5 floats
matrix = np.random.rand(5, 5)
txt_file2 = open("data_float.txt", "w")
for element in matrix:
    txt_file2.write(str(element) + " ")
txt_file2.close()
system("cat data_float.txt")


# txt convert to csv
with open('data_float.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('data_float.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)
system("cat data_float.csv")

# 2 JSON files
file = pd.read_json("user_data.json")
print(file)
file = file[(file['CreditCardType'] == "American Express")]
print(file)



# 3. CSV files with Pandas
data = pd.read_csv("mushrooms_categorized.csv")
data =data.groupby('class').mean()
print(data)
data.to_json('mushrooms_categorized.json')

system("cat mushrooms_categorized.json")

# 4. Reading a database



# 5. Reading the credit card numbers
import pandas as pd
file_name = 'credit_card.dat'
credit_cards = []
with open(file_name, mode='r') as f:
    for line in f:
        n = 6
        bin_chars = [line[i:i + n] for i in range(0, len(line) - 5, n)]

        card_number = ""
        for char in bin_chars:
            card_number += chr(int(char, 2))

        credit_cards.append(card_number)

print(credit_cards)


# 6. Write data to a binary file