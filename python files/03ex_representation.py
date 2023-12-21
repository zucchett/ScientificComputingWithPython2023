#LECOCQ Arthur
from math import sqrt,pi
from time import time

def ex1(number,outputType):
    if(number[1]=="b"):
        number = int(number,2)
        print("Bin")
    elif(number[1]=="x"):
        number = int(number,16)
        print("Hex")
    else:
        number = int(number)
        print("Int")

    match(outputType):
        case "int":
            temp = int(number)
        case "hex":
            temp = hex(number)[2:]
        case "bin":
            temp = bin(number)[2:]
        case _:
            return(ValueError)
    return(str(temp))

def ex2(bin):
    if(len(bin)!=32):
        return(ValueError)
    
    sign = -1 if bin[0] == '1' else 1
    exponent = int(bin[1:9], 2) - 127
    mantissa = 1.0
    for i, bit in enumerate(bin[9:], start=1):
        mantissa += int(bit) * 2 ** (-i)
    result = sign * mantissa * (2 ** exponent)
    return(result)

def ex3a():
    underflow = 1.0
    step = 1.0
    while underflow / 2 > 0:
        underflow /= 2
        if underflow == 0.0:
            break
    return underflow

def ex3b():
    overflow = 1.0
    while overflow * 2 != float('inf'):
        overflow *= 2
    return overflow

def ex3():
    underlim = ex3a()
    overlim = ex3b()
    print("Underflow : "+str(underlim))
    print("Overflow : "+str(overlim))

def ex4():
    epsilon = 1
    while 1.0 + epsilon != 1.0:
        machine_epsilon = epsilon
        epsilon /= 2
    print("Precision : ",str(machine_epsilon))
    return machine_epsilon

def ex5a(a,b,c):
    if(b**2<4*a*c):
        return(None)
    elif(b**2==4*a*c):
        x=-b/(2*a)
        return([x])
    delta = sqrt(b**2-4*a*c)
    x1 = (-b-delta)/(2*a)
    x2 = (-b+delta)/(2*a)
    return([x1,x2])

def ex5b(a,b,c):
    if(b**2<4*a*c):
        return(None)
    elif(b**2==4*a*c):
        x=-b/(2*a)
        return([x])
    delta = sqrt(b**2-4*a*c)
    x1 = -2*c/(b-delta)
    x2 = -2*c/(b+delta)
    return([x1,x2])

def ex5(a,b,c):
    # diffent values as the expression is different for both function
    # and as the expressions are different, the way to be calculated by Python is different
    # due to the approximations made
    precision1 = ex5a(a,b,c)[0]-ex5b(a,b,c)[0]
    precision2 = ex5a(a,b,c)[1]-ex5b(a,b,c)[1]
    return([precision1,precision2])

def ex6a(x):
    return(x*(x-1))

def ex6b(x,delta):
    return((ex6a(x+delta)-ex6a(x))/delta)

def ex6(x):
    deltas = [10**-2,10**-4,10**-6,10**-8,10**-10,10**-12,10**-14]
    for delta in deltas:
        print(ex6b(x,delta))

def ex7a(x):
    return(sqrt(1-x**2))

def ex7b(n):
    h = 2/n
    I = 0
    for k in range(1,n+1):
        I += h*ex7a(k/n)
    return(I)

def ex7():
    I = pi/2
    n = [10**2,10**3,10**4,10**5,10**6,10**7,10**8,10**9]
    for n in n :
        a = time()
        print(ex7b(n))
        b = time()
        print(str(b-a)+" secondes for n="+str(n))
        print(abs(ex7b(n)-pi/2))

    # 1.5602085158895234
    # 5.3882598876953125e-05 secondes for n=100
    # 0.010587810905373196
    # 1.5697777334555143
    # 0.0001747608184814453 secondes for n=1000
    # 0.0010185933393822566
    # 1.5706957388056586
    # 0.0017290115356445312 secondes for n=10000
    # 0.00010058798923795464
    # 1.5707863082009788
    # 0.015010833740234375 secondes for n=100000
    # 1.0018593917804353e-05
    # 1.5707953262069105
    # 0.10876107215881348 secondes for n=1000000
    # 1.0005879860219835e-06
    # 1.5707962267761797
    # 1.0651531219482422 secondes for n=10000000
    # 1.0001871686426966e-07
    # 1.5707963167946077
    # 10.772490978240967 secondes for n=100000000
    # 1.0000288819256298e-08
    # 1.570796325794828
    # 108.00215792655945 secondes for n=1000000000
    # 1.000068472478688e-09


if __name__ == '__main__':
    intA = "314"
    intB = hex(int("007"))
    intC = bin(int("416"))
    print(ex1(intA,"bin"))
    print(ex1(intA,"hex"))
    print(ex1(intA,"int"))
    print()
    print(ex1(intB,"bin"))
    print(ex1(intB,"hex"))
    print(ex1(intB,"int"))
    print()
    print(ex1(intC,"bin"))
    print(ex1(intC,"hex"))
    print(ex1(intC,"int"))
    bin1 = "11000010101100000101110101000000"
    bin2 = "01000010101100000101110101000000"
    print(ex2(bin1))
    print(ex2(bin2))
    ex3()
    ex4()
    print(ex5(0.001,1000,0.001))
    ex6(1) # values for 10**-2 are different due to the approximation made by the computer
           # to calculate the derivative of the function by the way it is expressed
    ex7()
    