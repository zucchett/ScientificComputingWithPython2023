import numpy as np
import pandas as pd
import sqlite3 as sql
import json

FILE1 = "data/data_int.txt"
FILE2 = "data/data_float.txt"
FILE3 = "data/data_000637.txt"
FILE4 = "data/user_data.json"
FILE5 = "data/mushrooms_categorized.csv"
FILE6 = "data/sakila.db"
FILE7 = "data/credit_card.dat"

def intData(iNumber):
    with open(FILE1,"w") as file:
        for value in range(iNumber):
            file.write(str(value)+"\n")

def intFloat(iSize):
    matrix = np.random.rand(iSize,iSize)
    with open(FILE2,"w") as file:
        file.write(str(matrix)+"\n")

def convertTxtToCSV(iFilename):
    fileNameCSV = iFilename[:len(iFilename)-3]+"csv"
    
    with open(FILE3,"r") as txtFile:
        lines = txtFile.readlines()

    with open(fileNameCSV,"w") as CSVFile:
        for line in lines:
            CSVFile.write(line.replace(" ",","))

def AmericanExpressIntoCSV(iFilename):
    fileNameCSV = "data/american_express_user_data.csv"

    jsonContentFile = json.load(open(iFilename))
    filteredContent = [element for element in jsonContentFile if element["CreditCardType"]=="American Express"]
    dataFrame = pd.DataFrame(filteredContent)
    dataFrame.to_csv(fileNameCSV,index=False)

def AverageAndJSON(iFilename):
    fileNameJSON = "data/average_mushrooms_categorized.json"

    dataFrame = pd.read_csv(iFilename)
    print(dataFrame)

    filteredContent = dataFrame.groupby("class").mean()
    print(filteredContent)

    with open(fileNameJSON,"w") as JSONFile:
        JSONFile.write(filteredContent.to_json(orient="records"))

def countStartLetterName(iDataFrame,iLetter):
    count = iDataFrame[iDataFrame[1].str.startswith(iLetter)][1].count()
    print(count,"names starting with letter",iLetter)

def readingDataBase(iFilename):
    # print()
    connection = sql.connect(iFilename)
    cursor = connection.cursor()
    query = "select * from actor"
    results = cursor.execute(query).fetchall()
    dataFrame = pd.DataFrame(results)
    print(dataFrame)
    countStartLetterName(dataFrame,"A")
    cursor.close()
    connection.close()

def slicingLine(iLine,iStep):
    binLineBlocks = [iLine[i:i+iStep] for i in range(0,len(iLine),iStep)]
    cardNumber = ""
    for block in binLineBlocks:
        if block == "100000":
            cardNumber+=" "
        cardNumber+=chr(int(block,2))
    print(cardNumber)

def convertCreditCardNumber(iFilename):
    with open(iFilename,"r") as binFile:
        content = binFile.readlines()
    for line in content:
        slicingLine(line,6)

if __name__ == "__main__":
    intData(100)
    intFloat(5)
    convertTxtToCSV(FILE3)
    AmericanExpressIntoCSV(FILE4)
    AverageAndJSON(FILE5)
    readingDataBase(FILE6)
    convertCreditCardNumber(FILE7)