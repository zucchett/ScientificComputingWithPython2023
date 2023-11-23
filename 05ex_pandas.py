import numpy as np
import pandas as pd

FILE = "./data/data_000637.txt"
NROWMIN = 10000

# Hour, Min, Sec :
ORBIT_TIME = 1 # to multiply by by 360.000 to have a hour
BX_TIME = 25 # to multiply by by 60.000 to have a minute
TDC_TIME = 25/30 # to multiply by 1000 to have a second


def fromFileCreateDataFrame(iFile):
    oDataFrame = pd.read_csv(iFile, sep=",")
    nRowMax = max(NROWMIN, len(oDataFrame))
    return oDataFrame[:nRowMax]


def estimationBXinOrbit(iDataFrame):
    colOrbit = iDataFrame["BX_COUNTER"]
    oCount = 0
    for value in colOrbit:
        if value == 0:
            oCount += 1
    return(oCount)

def addAbsoluteTime(ioDataFrame):
    OrbitCol = ioDataFrame["ORBIT_CNT"]
    BXCol = ioDataFrame["BX_COUNTER"]
    TDCCol = ioDataFrame["TDC_MEAS"]

    ref = OrbitCol[0]*ORBIT_TIME*360000+BXCol[0]*BX_TIME*6000+TDCCol[0]*TDC_TIME*1000
    TimeInNs = []

    for i in range(len(OrbitCol)):
        TimeInNs.append(abs(OrbitCol[i]*ORBIT_TIME*360000+BXCol[i]*BX_TIME*6000+TDCCol[i]*TDC_TIME*1000-ref))

    ioDataFrame.insert(len(ioDataFrame.columns),"ABS_TIME",TimeInNs)

    return(ioDataFrame)

def changeFormat(ioDataFrame):
    ioDataFrame["ABS_TIME"] = pd.to_datetime(ioDataFrame["ABS_TIME"],origin=ioDataFrame["ABS_TIME"][0])
    ioDataFrame["ABS_TIME"] = ioDataFrame["ABS_TIME"].dt.strftime("%H:%M:%S:%f")
    return(ioDataFrame)

def noisyChannel(iDataFrame,iNumberOfChannels):
    groupedByTDCChannel = iDataFrame.groupby("TDC_CHANNEL").agg(countChannels=("TDC_CHANNEL","count"))
    print(groupedByTDCChannel.sort_values(by="countChannels",ascending=False)[:iNumberOfChannels])

def nonEmptyOrbitsCount(iDataFrame):
    orbits = iDataFrame["ORBIT_CNT"].unique()
    print(pd.DataFrame({"ORBIT_CNT":orbits}))

def uniqueOrbitsFromChannel(iDataFrame,iChannelNumber):
    filteredDataFrame = iDataFrame[iDataFrame.TDC_CHANNEL == iChannelNumber]
    nonEmptyOrbitsCount(filteredDataFrame)

def serieFPGA(iDataFrame,iValue):
    filteredDataFrame = iDataFrame[iDataFrame.FPGA == iValue]
    values = filteredDataFrame.TDC_CHANNEL.value_counts()
    index =  filteredDataFrame.TDC_CHANNEL.unique()
    newDataFrame = pd.DataFrame({"TDC_CHANNEL":values},index=index).reindex(index.sort())
    return(newDataFrame)

if __name__ == "__main__":
    # Question 1
    dataFrame = fromFileCreateDataFrame(FILE)
    print(dataFrame)

    # Question 2
    ORBIT_TIME = estimationBXinOrbit(dataFrame)

    # Question 3
    dataFrame = addAbsoluteTime(dataFrame)
    print(dataFrame)

    # Question 4
    dataFrame = changeFormat(dataFrame)
    print(dataFrame)

    # Question 5
    noisyChannel(dataFrame,3)

    # Question 6
    nonEmptyOrbitsCount(dataFrame)

    # Question 7
    uniqueOrbitsFromChannel(dataFrame,139)

    # Question 8
    serieZero = serieFPGA(dataFrame,0)
    print(serieZero)
    serieOne = serieFPGA(dataFrame,1)
    print(serieOne)
