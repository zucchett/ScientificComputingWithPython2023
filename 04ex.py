import numpy as np
import math
import timeit

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
table = np.zeros((10, 10), "int")
for i in range(1, 11):
    table[i-1] = np.arange(i, 11*i, i)
print(table, "\n")
print("Trace of that matrix: ", np.trace(table), "\n")
diag2=[]
for c in range(table.shape[1]-1):
    diag2.append(table[c,c+1])
print(diag2)

#Esercizio 6
print("\nEsercizio 6: \n")
cities = ["Chicago", "Springfield", "Saint-Louis", "Tulsa", "Oklahoma City", "Amarillo", "Santa Fe", "Albuquerque", "Flagstaff", "Los Angeles"]
distances = [0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448]
grid = np.zeros((len(cities), len(cities)))
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        grid[i][j] = distances[j]-distances[i]
        grid[j][i] = grid[i][j]
KMgrid=grid*0.6213712
print(grid)

#Esercizio 7
print("\nEsercizio 7: \n")
def measure_time(func):
    def wrapper(*args, **kwargs):
        Tstart = timeit.default_timer()
        result = func(*args, **kwargs)
        Tend = timeit.default_timer()
        Texec = Tend - Tstart
        print("This function took {:.6f} seconds to run.".format(Texec))
        return result
    return wrapper

@measure_time
def prime_n(array):
    primes = []
    for x in array:
        if x==1 or x==0:
            is_prime=False
        else:
            is_prime=True
        for i in range(2, int(x/2)+1):
            if x % i == 0:
                is_prime = False
        if is_prime:
            primes.append(x)
    return primes

@measure_time
def sieve_prime(array):
    max_num = max(array)
    sieve = np.ones(max_num + 1, dtype=bool)
    sieve[:2] = False
    for n in range(2, int(np.sqrt(max_num)) + 1):
        if sieve[n]:
            sieve[n * n::n] = False
    return array[sieve]
    
N=2000
numbers = np.arange(N)
print("Prime numbers:\n", prime_n(numbers))
print("Prime numbers using sieve of eratosthenes:\n", sieve_prime(numbers))

'''
The time of execution of the function prime_n grows with proportion to N^2 (with N=100 the time is 0.000641, with N=1000 is 0.057 and with N=2000 is 0.237), while sieve_prime's execution time is almost linear in the dimension of N (with N=100 the time is 0.000076, with N=1000 is 0.000108 and with N=2000 is 0.000199).
'''

#Esercizio 8
print("\nEsercizio 8: \n")

walkers, times = 1000, 200
steps = np.random.randint(2, size=(walkers, times))*2-1
progress = np.zeros(steps.shape, "int")
for i in range(walkers):
    for j in range(times):
        progress[i, j]=progress[i, j-1]+steps[i, j]
print("Total walked distance of each walker:\n", progress[:, times-1])
square_prog = progress * progress
mean_step=np.zeros(times)
for c in range(times):
    mean_step[c]=sum(square_prog[:, c])/walkers
print("Mean of squared distances at each time's step:\n", mean_step)
