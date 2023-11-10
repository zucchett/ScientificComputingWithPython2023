import numpy as np
import math

#Esercizio 1
print("Esercizio 1: \n")

m = np.arange(12).reshape((3,4))
print("Media di m: ", m.mean())
print("Media delle colonne di m: ", m.mean(0))
print("Media delle righe di m: ", m.mean(1))

#Esercizio 2
print("\nEsercizio 2: \n")

u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])
print("Outer product with np.outer:\n", np.outer(u,v))
for_outer = np.zeros((len(u), len(v)))
for i in range(len(u)):
    for j in range(len(v)):
        for_outer[i, j]=u[i]*v[j]
print("Outer product with for:\n", for_outer)
tiled_u = np.tile(u, (len(u), 1))
tiled_v = np.tile(v, (len(v), 1))
tiled_outer = tiled_v*tiled_u.T
print("Outer product with numpy.tile:\n", tiled_outer)

#Esercizio 3
print("\nEsercizio 3: \n")

a = 3*np.random.rand(10, 6)
mask = (a>0.3)
print(a[mask])

#Esercizio 4
print("\nEsercizio 4: \n")

a = np.linspace(0, 2*math.pi, 100)
print(a,"\n")
print(a[::10],"\n")
print(a[::-1], "\n")
mask = (np.sin(a) - np.cos(a)<0.1)
print(a[mask])

#Esercizio 5
print("\nEsercizio 5: \n")

#Esercizio 6
print("\nEsercizio 6: \n")

#Esercizio 7
print("\nEsercizio 7: \n")

#Esercizio 8
print("\nEsercizio 8: \n")

