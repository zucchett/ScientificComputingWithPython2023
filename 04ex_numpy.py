import math
import numpy as np

# ################## exercise 1 ##################
# print("\n--- --- EXERCISE 1 --- ---")
# print("--- local and row mean ---\n")

# m = np.arange(12).reshape((3,4))
# print("\n", m, "\n")
# mean = np.mean(m)
# print("mean of the whole matrix:", mean, "\n")
# for i in range(m.shape[0]): print("mean of col", i, np.mean(m[i,:]))
# print()
# for i in range(m.shape[1]): print("mean of row", i, np.mean(m[:,i]))

# input("\npress ENTER to proceed to the next exercise...")

# ################## exercise 2 ##################
# print("\n--- --- EXERCISE 2 --- ---")
# print("--- outer product ---\n")

# u = np.array([1, 3, 5, 7])
# v = np.array([2, 4, 6, 8])

# print("calculate outer product with outer function in numpy: ")
# print(np.outer(u, v))
# print()

# print("calculate outer product with list comprehension: ")
# x = np.array([a*b for a in u for b in v]).reshape((len(u), len(u)))
# print(x)
# print()

# print("calculate outer product with broadcasting multiplication: ")
# uTile = np.tile(u, (4,1)).T
# print(uTile*v)
# print()

# input("\npress ENTER to proceed to the next exercise...")


# ################## exercise 3 ##################
# print("\n--- --- EXERCISE 3 --- ---")
# print("--- matrix masking ---\n")

# np.random.seed(42)
# m = np.random.rand(10, 6)*3
# print("uniform distributed matrix in (0,3):")
# print(m, '\n')

# mask = (m < 0.3)
# print("obtained mask:")
# print(mask, '\n')


# m[mask] = 0
# print("obtained matrix with entries <0.3 set to zero:")
# print(m)



# input("\npress ENTER to proceed to the next exercise...")

# ################## exercise 4 ##################
# print("\n--- --- EXERCISE 4 --- ---")
# print("--- trigonometric ---\n")

# v = np.linspace(0, 2*np.pi, 100)
# print("the generated matrix is:")
# print(v, "\n")

# print("printing each 10 elements (starting from the 10th):")
# print(v[9:100:10], "\n")

# print("printing in reverse:")
# print(v[::-1], "\n")

# smallDiff = [x for x in v if abs(np.sin(x) - np.cos(x))<0.1 ]
# print("print the values which difference bw cos and sin is less than 0.1:")
# print(smallDiff, "\n")

# import matplotlib.pyplot as plt
# plt.plot(v, np.cos(v), label="cos")
# plt.plot(v, np.sin(v), label="sin")
# plt.legend(loc="upper right")
# for xVal in smallDiff:
#     plt.axvline(x=xVal, color = "red")
# plt.show()


# input("\npress ENTER to proceed to the next exercise...")

# ################## exercise 5 ##################
# print("\n--- --- EXERCISE 5 --- ---")
# print("--- multiplication table ---\n")

# m = np.array([x*y for x in range(1,11) for y in range(1,11)]).reshape(10,10)
# tr = np.trace(m)
# antiDiag = np.fliplr(m).diagonal()
# upAntiDiag = [m[x, x-1] for x in range(1,10)]
# print(m)
# print("trace:", tr)
# print("anti diagonal:", antiDiag)
# print("diagonal offset of 1:", upAntiDiag)


# input("\npress ENTER to proceed to the next exercise...")

# ################## exercise 6 ##################
# print("\n--- --- EXERCISE 6 --- ---")
# print("--- route 66 distances ---\n")

# cities = np.array([["CH", "SP", "SL", "TU", "OkC", "AM", "SF", "ALB", "FLS", "LA"]])
# citiess = np.array([["-", "CH", "SP", "SL", "TU", "OkC", "AM", "SF", "ALB", "FLS", "LA"]])
# positions = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
# print(positions[:, np.newaxis])
# distances = np.abs(positions - positions[:, np.newaxis])
# test = np.concatenate((cities, distances))
# test = np.concatenate((citiess.T, test), axis=1)
# print("distances between cities:\n",test)
# print("distances in km:\n",distances*1.609344)


# input("\npress ENTER to proceed to the next exercise...")

################## exercise 7 ##################
print("\n--- --- EXERCISE 7 --- ---")
print("--- prime siege ---\n")




input("\npress ENTER to proceed to the next exercise...")

