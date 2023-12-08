import numpy as np
import numpy.random as npr
from time import time

def ex1():
    m = np.arange(12).reshape((3,4))

    print(m)

    avg = 0
    avgRow = 0
    avgCol = 0

    avg = sum(sum(m))/(m.shape[0]*m.shape[1])
    print("Mean : ",avg)

    avg = np.mean(m)
    print("Mean : ",avg)

    for i in range(m.shape[0]):
        avgRow = sum(m[i])/len(m[i])
        print("Mean on rows ",i," : ",avgRow)

    for i in range(m.shape[1]):
        avgCol = sum(np.transpose(m)[i])/len(np.transpose(m)[i])
        print("Mean on columns ",i," : ",avgCol)

def ex2():
    u = np.array([1, 3, 5, 7])
    v = np.array([2, 4, 6, 8])

    m = np.outer(u,v)
    print(m)

    m = np.array([[i*j for i in u]for j in v])
    print(m)

    m = u[:,np.newaxis]*v
    print(m)

def ex3():
    m = np.random.uniform(0,3,size=(10,6))
    print(m)
    mask = m<.3
    m[mask] = 0
    print(m)

def ex4():
    m = np.linspace(0,2*np.pi,100)
    print(m)
    print(m[9::10])
    print(m[::-1])
    extract = []
    for i in m:
        if abs(np.sin(i)-np.cos(i))<.1:
            extract.append(i)
    print(extract)
    print([np.cos(i) for i in extract])
    print([np.sin(i) for i in extract])

def ex5():
    u = np.arange(1,11)
    v = np.arange(1,11)
    m = np.outer(u,v)
    print(m)
    print(np.trace(m))
    print(np.diag(m[::-1]))
    print(np.diag(m[1:]))

def ex6():
    positions_miles = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
    positions_km = positions_miles * 1.60934
    grid = np.abs(positions_miles[:, np.newaxis] - positions_miles)
    print("Grid in miles")
    print(grid)
    grid = np.abs(positions_km[:, np.newaxis] - positions_km)
    print("Grid in km")
    print(grid)

def prime(nb):
    if nb<2:
        return False
    for i in range(2,nb):
        if nb%i==0:
            return False
    return True

def sieve(m):
    if(len(m)<2):
        return [True for i in range(len(m))]
    mask = [False for i in range(len(m))]
    mask[0] = True
    mask[1] = True
    # mask[:2]=True # Doesn't work, idk why
    for i in range(2,len(m)):
        if(mask[i]):
            continue
        for j in range(i+1,len(m)):
            if(mask[j]):
                continue
            if(m[j]%i==0):
                mask[j]=True
    return(mask)
           


def ex7(n):
    m = np.arange(n+1)
    mSieve = np.arange(n+1)
    a=time()
    mask = [not(prime(i)) for i in m]
    b=time()
    print(b-a,"secondes for conditional list")
    m[mask] = 0
    # print(m)
    a=time()
    maskSieve = sieve(mSieve)
    b=time()
    print(b-a,"secondes for sieve")
    mSieve[maskSieve]=0
    # print(mSieve)

def ex8(walkers,steps):
    m = npr.randint(-1,2,size=(walkers,steps))
    mDist = np.arange(walkers)
    print(m)
    for i in range(walkers):
        dist = m[i].sum()
        mDist[i] = dist
        print("For walker n°",i,"distance =",dist)
    mDistSqr = [i**2 for i in mDist]
    print(mDistSqr)
    for i in range(steps):
        avg = np.transpose(m)[i].sum()/steps
        print("For step n°",i,"mean =",avg)

if __name__ == '__main__':
    ex1()
    ex2()
    ex3()
    ex4()
    ex5()
    ex6()
    ex7(99)
    # for n = 100000
    # 24.12833595275879 secondes for conditional list
    # 11.692285060882568 secondes for sieve
    ex8(1000,200)