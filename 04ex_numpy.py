import numpy as np
import timeit
import matplotlib.pyplot as plt

# 1. Reductions
m = np.arange(12).reshape((3, 4))
print(m)
total_mean = np.mean(m)
row_mean = np.mean(m, axis=1)
column_mean = np.mean(m, axis=0)

print(f"total mean is {total_mean},the mean for each row is {row_mean},the mean for each column is{column_mean}")



# 2. Outer product

u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])

# (2.1. Using the function `outer` in numpy)
outer_np = np.outer(u, v)
print(outer_np)

# (2.2. Using a nested `for` loop or a list comprehension)
demo = []
for x in range(len(u)):
    temp = []
    for y in range(len(v)):
        temp.append(u[x]*v[y])
    demo.append(temp)

list_outer = np.array(demo)
print(list_outer)

#qs: how to use list comprehension to write the list
# outer_list = np.array([u[x]*v[y]]for x in range(len(u)) for y in range(len(v)) if y == 4)
# print(outer_list)

# (2.3. Using numpy broadcasting operations)
u2 = u.reshape(-1, 1) #
uu = np.repeat(u2, 4, axis=1)
uuv_ba = uu*v
print(uuv_ba)








# 3. Matrix masking
a = np.random.uniform(0, 3, [6, 10])
print(a, '\n')
a[a < 0.3] = 0
print(f"the result of using mask is {a}")



# 4. Trigonometric functions
# np.linspace(tart, stop, num=50, endpoint=True, retstep=False, dtype=None)
tri = np.linspace(0, 2 / np.pi, num=100, endpoint=True)

#Extract every 10th element using the slice notation
tri_ten =np.split(tri, 10)
tt = tri[::10]

print(tri_ten)

#Reverse the array using the slice notation
res = tri[::-1]
print(res)

#Extract elements where the absolute difference between the `sin` and `cos` functions evaluated for that element is < 0.1
mask = (abs(np.sin(tri) - np.cos(tri) < 0.1))
tri[mask]

#Optional**: make a plot showing the sin and cos functions and indicate where they are close
sin = np.sin(tri)
cos = np.cos(tri)
plt.plot(tri, sin, tri, cos)
plt.title("plot of the sin and cos")



# 5. Matrices
def mult_table(n):
    temp = np.arange(1, n + 1)
    print(temp, temp[:, None])
    return temp * temp[:, None]

mult_ten = mult_table(10)

mat_trace = np.trace(mult_ten)

anti_diag = np.fliplr(mult_ten).diagonal()

up_diag = np.diagonal(mult_ten, offset=1)
print(f"the 10 by 10 multiplication table\n{mult_ten}\n"
      f"the trace of the matrix\n{mat_trace}\n"
      f"the anti-diagonal matrix\n{anti_diag}\n "
      f"the diagonal offset by 1 upwards \n{up_diag} ")




# 6. Broadcasting
miles = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])

dist_miles = np.abs(miles - miles[:, np.newaxis])

# print("Distance in miles: \n", dist_miles)
print(miles[:, np.newaxis])

dist_km = dist_miles * 1.60934
print("\nDistance in km: \n", dist_km.round())


# 7. Prime numbers sieve
a = np.random.randint(0, 9, 15) # 15 random int between 0 and 21
print("original array:", a, '\n')

# create a mask to filter multiples of 3
mask = (a % 3 == 0)
print("the mask:", mask, '\n')

filtered_a = a[mask]
# equivalent to a[a % 3 == 0]
print("the filtered array:", filtered_a, '\n')

# verify that fancy indexing creates copies
print("are a and filtered_a the same object?", np.may_share_memory(a, filtered_a), '\n')

# Indexing with a mask can be very useful to assign a new value to a sub-array
a[a % 3 == 0] = -1
print("the modified array:", a, '\n')


N = np.arange(2, 100)
for i in range(98):
    if(N[i] != False):
        for j in range(i + 1, 98):
            if(N[j] % N[i] == 0):
                N[j] = False
mask = (N != 0)
filtered = N[mask]
print("Prime numbers\n", filtered)

def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        if (prime[p] == True):

            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1

    prime[0] = False
    prime[1] = False

    for p in range(n + 1):
        if prime[p]:
            print(p)

starttime = timeit.default_timer()
SieveOfEratosthenes(1000)
print("The time difference is :", timeit.default_timer() - starttime)



# 8. Diffusion using random walk

walkers = np.random.randint(0, 2, size=(10, 2))
walkers = walkers * 2 - 1
