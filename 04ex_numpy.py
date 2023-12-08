import numpy.random as npr
import matplotlib.pyplot as plt
import numpy as np
import timeit

def ex1():
    print("1. Reductions")
    m = np.arange(12).reshape((3,4))
    sum_col = 0 
    sum = 0 
    for i in m:
        for j in i:
            sum += j
    
    mean = sum/len(m)/len(m[0])
            
    print("Array\n", m)
    print("Total mean ", mean) 

    for i in m:
        sum_col += i
    for idx, i in enumerate(sum_col, start=1):
        mean_col = i/len(m)
        print(f"Mean in {idx} column:", mean_col )

    for idx, i in enumerate(m, start=1):
        sum_row = 0
        for j in i:
            sum_row += j
        print(f"Mean in {idx} raw:", sum_row/len(m[0]))


def ex2():
    print("2. Outer product")
    u = np.array([1, 3, 5, 7])
    v = np.array([2, 4, 6, 8])
    print( u,"\n",v)

    outer_product = np.outer(u, v)
    print("Outer product using outer in numpy\n", outer_product)

    new_arr = np.zeros((len(u), len(v)))
    for i in range(len(new_arr)):
        for j in range(len(new_arr[i])):
            new_arr[i,j] = u[i]*v[j]

    print("Outer product using for loop \n", new_arr.astype(int))

    outer_product_brodcast = u[:, np.newaxis] * v
    print("Outer product using broadcasting \n", outer_product_brodcast)




def ex3():
    print("3. Matrix masking")
    arr = np.random.uniform(0, 3, size=(10, 6))
    print("Array before the mask\n", arr)
    
    filtered_arr = arr.copy()
    filtered_arr[arr < 0.3] = 0
    print("Filtered Array\n", filtered_arr)


def ex4():
    
    print("4. Trigonometric functions")
    arr = np.linspace(0, 2 * np.pi, 100)
    print("Array\n", arr)
    
    arr_ten = arr[9::10]
    print("Evry tenth extracted elements\n", arr_ten)

    arr_reverse = arr[::-1]
    print("Reverse array\n", arr_reverse)

    arr_sin = np.zeros((len(arr)))
    arr_cos = np.zeros((len(arr)))

    for i in range(len(arr)):
        arr_sin[i] = np.sin(arr[i])
    print("Sin array\n", arr_sin)

    for i in range(len(arr)):
        arr_cos[i] = np.cos(arr[i])
    print("Cos array\n", arr_cos)

    condition = np.abs(arr_sin - arr_cos) < 0.1
    abs_differ = arr[condition]
    print("Absolute difference < 0.1\n", abs_differ)
	

    plt.figure(num='Sin and Cos Functions', figsize=(8, 6))
    plt.plot(arr, arr_sin, label='sin(x)')
    plt.plot(arr, arr_cos, label='cos(x)')
    
    plt.scatter(abs_differ, np.sin(abs_differ), color='red', label='|sin(x) - cos(x)| < 0.1')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Sin and Cos Functions')
    plt.legend()
    plt.grid(True)
    plt.show()

    

def ex5():
    print("5. Matrices")
    arr = np.arange(1, 11)
    mult_table = arr[:, None] * arr[None, :]
    print ("Multiplication table\n", mult_table)
    print ("The trace of the matrix\n", mult_table.trace())
    print ("The anti-diagonal matrix\n", np.flipud(mult_table).diagonal())
    shifted_matrix = mult_table[1:, :]
    print ("The diagonal offset by 1 upwards\n", shifted_matrix.diagonal())


def ex6():
    print("6. Broadcasting")
    arr = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
    distances_miles = np.abs(arr - arr[:, np.newaxis])
    print("Distances among each city along Route 66 in miles\n", distances_miles)
    distances_km = distances_miles * 1.60934
    print("Distances among each city along Route 66 in km\n", distances_km)
    
    


def ex7(n):
    print("7. Prime numbers sieve")
    mask = np.concatenate(([False, False], np.ones(n - 1, dtype=bool)))
    
    def prime(n):
        for i in range(2, n):
            mask[2*i::i] = False
        return np.nonzero(mask[:n+1])[0]

    print("Prime numbers in range 0 -", n , "\n", prime(n))
    print("Time for first case")
    # %timeit prime(n)
    time = timeit.timeit(lambda: prime(n), number=100)
    print(str(time))
    
    def sieve(n):
        for p in range(2, int(np.sqrt(n)) + 1):
            if mask[p]:
                for i in range(p * p, n, p):
                    mask[i] = False
    
        return np.nonzero(mask)[0]
    print("\nPrime numbers in range 0 -", n , "\n", sieve(n))
    print("Time for the sieve of Eratosthenes")
    # %timeit sieve(n)
    time = timeit.timeit(lambda: sieve(n), number=100)
    print(str(time))



def ex8():
    print("8. Diffusion using random walk")
    walkers = 1000
    steps = 200
    walk = npr.randint(0, 2, size=(walkers * steps))
    walk[walk == 0] = -1
    walk = walk.reshape(walkers, steps)
    
    end_distances = walk.sum(axis=1)  
    print("Sums of values for each walker at the last step")
    print(end_distances)

    distances_step = walk.cumsum(axis=1)
    print("Distance matrix for each step of each walker")
    print(distances_step)
    
    distances_squared = np.square(distances_step)
    print("Squared distances for each step of each walker:")
    print(distances_squared)
    
    print("Average values of squared distances at each step:")
    mean_distances_squared = distances_squared.mean(axis=0)
    print(mean_distances_squared)


    plt.figure(num='Average Distance', figsize=(8, 6))
    plt.plot(np.arange(steps), mean_distances_squared, label='Average Distances')
    plt.title('Average Distances over Time')
    plt.xlabel('Step')
    plt.ylabel('Average Distance')
    plt.legend()
    plt.grid(True)
    plt.show()
	
	
ex1()
ex2()
ex3()
ex4()
ex5()
ex6()
ex7(211)
ex8()