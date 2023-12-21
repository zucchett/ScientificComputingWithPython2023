import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools
import seaborn as sns
import pickle
import scipy

FILE = "data/regression_generated.csv"
DATASET = "data/residuals_261.pkl"


def scatterPlots(iFilename, iFeatures):
    dataFrame = pd.read_csv(iFilename)
    combinations = list(itertools.combinations(iFeatures, 2))
    plt.figure(figsize=(10, 10))
    for combo in range(len(combinations)):
        plt.subplot(len(combinations), 1, combo + 1)
        plt.scatter(
            dataFrame[combinations[combo][0]], dataFrame[combinations[combo][1]]
        )
        plt.xlabel(combinations[combo][0])
        plt.ylabel(combinations[combo][1])
        plt.plot()
    plt.tight_layout()
    plt.show()


def twoCategoriesScatterPlot(
    mean_1, standarDeviation_1, len_1, mean_2, standarDeviation_2, len_2
):
    dataset_1 = np.random.normal(mean_1, standarDeviation_1, len_1)
    dataset_2 = np.random.normal(mean_2, standarDeviation_2, len_2)

    plt.scatter(np.arange(len_1), dataset_1, label="Dataset 1", color="blue")
    plt.scatter(np.arange(len_2), dataset_2, label="Dataset 2", color="red")
    plt.show()


def profilePlot(iFilename):
    with open(iFilename, "rb") as file:
        data = pickle.load(file).item()
    dataFrame = pd.DataFrame(
        {"residuals": data["residuals"], "distances": data["distances"]}
    )
    print(dataFrame)
    cleanDataFrame = dataFrame[abs(dataFrame["residuals"]) < 2]
    sns.jointplot(x="distances", y="residuals", data=cleanDataFrame, kind="reg")
    plt.show()

    plt.figure(figsize=(15, 10))
    plt.subplot(2, 1, 1)
    plt.hist(cleanDataFrame["distances"], bins=25, edgecolor="black")
    plt.title("Distances histogram")

    bins = np.linspace(
        cleanDataFrame["distances"].min(), cleanDataFrame["distances"].max(), 10
    )
    slices = np.digitize(cleanDataFrame["distances"], bins)
    print(bins)
    print(slices)
    x = [(bins[i] + bins[i + 1]) / 2 for i in range(len(bins) - 1)]
    y = [cleanDataFrame["residuals"][slices == i].mean() for i in range(1, len(bins))]
    err_y = [cleanDataFrame["residuals"][slices == i].std() for i in range(1, len(bins))]
    plt.subplot(2, 1, 2)
    plt.scatter(cleanDataFrame["distances"], cleanDataFrame["residuals"])
    plt.errorbar(x, y, yerr=err_y, fmt="o", color="red", ecolor="grey")
    plt.tight_layout()
    plt.show()


def KDE(len, mean, standarDeviation):
    data = np.random.normal(mean, standarDeviation, len)
    histogram, bins, _ = plt.hist(data, bins=int(np.sqrt(len)))
    binCenters = (bins[1:] + bins[:-1]) / 2
    error = np.sqrt(histogram)

    plt.errorbar(binCenters, histogram, yerr=error, fmt="o")
    plt.xlabel("Values")
    plt.ylabel("Frequencies")    

    defaultValue = 1.06*data.std()*np.power(len,-1/5)
    xRange = np.linspace(data.min(),data.max(),len)
    xGaussianValues = [scipy.stats.norm.pdf(xRange,loc=value,scale=defaultValue) for value in data]
    gaussianSum = np.sum(xGaussianValues,axis=0)

    integral = scipy.integrate.trapz(histogram,x=binCenters)
    integralGaussian = scipy.integrate.trapz(gaussianSum,x=xRange)
    gaussianSumNormalized = gaussianSum*integral/integralGaussian

    plt.plot(xRange,gaussianSumNormalized,color="red")

    plt.show()


if __name__ == "__main__":
    scatterPlots(FILE,["features_1","features_2","features_3"])
    twoCategoriesScatterPlot(50,10,300,40,20,300)
    profilePlot(DATASET)
    KDE(100, 10, 2)
