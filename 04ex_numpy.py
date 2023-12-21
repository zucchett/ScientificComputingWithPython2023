import timeit
import numpy as np
import matplotlib.pyplot as plt
#Ex1
print(" Ex1 : ")
m = np.arange(12).reshape((3,4))
print(" total mean = "+ str(m.mean()))
for i in range (np.shape(m)[0]):
    print(" mean for row "+ str(i)+ " = "+ str(m[i,:].mean()))
for i in range (np.shape(m)[1]):
    print(" mean for column "+ str(i)+ " = "+ str(m[:,i].mean()))
print('------------------------------------------- ')
print('------------------------------------------- ')
#Ex2
print(" Ex2 : ")
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])
print(" outer methode : ")
print(np.outer(u,v))
m = np.array([[u_i * v_j for v_j in v] for u_i in u])

print(" nested loop methode : ")
print(m)

print(" broadcasting operations methode : ")
print(u[:, np.newaxis] * v[np.newaxis, :])
print('------------------------------------------- ')
print('------------------------------------------- ')
#Ex3
print("Ex3 : ")
m = np.random.uniform(0, 3, size=(10, 6))
print(" m before filter : ")
print(m)
m[m<0.3] = 0
print(" m after filter : ")
print(m)
print('------------------------------------------- ')
print('------------------------------------------- ')
#Ex4
print("Ex4 : ")
u = np.linspace(0, 2* np.pi, num = 100)

print('Array of 100 number between 0 and  2 pi : \n ', u)
print('------------------------------------------- ')
print('Extracting every 10th element : ', u[0::10])
print('------------------------------------------- ')
print('Reversing the array using the slice notation : \n', u[::-1])
print('------------------------------------------- ')

mask = np.abs(np.sin(u) - np.cos(u)) < 0.1
print('Elements where the absolute difference between the sin and cos functions evaluated for that element is < 0.1 : \n', u[mask] )

plt.figure(figsize=(10, 10))
plt.plot(u, np.sin(u), label='sin', color='blue')
plt.plot(u, np.cos(u), label='cos', color='orange')
plt.ylabel('Sin - cos')
plt.legend()
plt.show()
print('------------------------------------------- ')
print('------------------------------------------- ')

#Ex5
print("Ex 5 : ")

m = np.outer(np.arange(1,11),np.arange(1,11))

print('10 by 10 multiplication table : \n ',m)
print(' ------------------------------------------- ')
print('Trace : ', m.trace() )
print(' ------------------------------------------- ')
print('Anti-diagonal : ', np.fliplr(m).diagonal())
print(' ------------------------------------------- ')
print('Diagonal offset by 1 upwards : ', m[1:,:].diagonal())
print('------------------------------------------- ')
print('------------------------------------------- ')


#Ex6
milesstones  = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])

distanceMiles = np.abs(milesstones  - milesstones[:, np.newaxis])
distanceKm = distanceMiles * 1.60934 

print('2D grid of distances among each city along Route 66 : \n',distanceMiles )
print('\n ------------------------------------------- \n')
print('2D grid of distances in Km : \n ',distanceKm  )
print('------------------------------------------- ')
print('------------------------------------------- ')

#Ex7
N = 99

def prime(N):
    mask = np.ones(N+1,  dtype=bool)
    for p in range(2,N+1):
        mask[p+1:N+1] *= np.invert((np.arange(p+1, N+1) % p == 0))
    return np.where(mask)


def sieveOfEratosthenes(N):
    mask = np.ones(N+1,  dtype=bool)
    p=2
    while(p*p <=N):
        mask[p+1:N+1] *= np.invert((np.arange(p+1, N+1) % p == 0))
        p +=1
    return np.where(mask)

    

print("the prime numbers in the 0-N range with a sieve (mask) : \n ", prime(N))
print('\n ------------------------------------------- \n')

print("the prime numbers in the 0-N with optimization suggested in the sieve of Eratosthenes : \n ", sieveOfEratosthenes(N))
print('\n ------------------------------------------- \n')

for i in range(100,1000,100):
    start=timeit.default_timer()
    sieveOfEratosthenes(i)
    end=timeit.default_timer()
    print('The execution time for N = ',i,' is : ',end-start)
print('------------------------------------------- ')
print('------------------------------------------- ')

#EX8
walkers = 1000
steps = 200

randomwalks = 2* np.random.random_integers(0,1,(walkers, steps)) - 1 
print(np.shape(randomwalks))
distance = np.cumsum(randomwalks, axis=1)
print(np.shape(distance))
msd = np.mean(distance**2, axis=0)
print(np.shape(msd))

plt.figure(figsize=(10, 10))
plt.plot(np.arange(steps), msd)
plt.xlabel('time')
plt.ylabel('average distance')
plt.show()
