#EXERCISE 1
import sys

def converter(input, outputType):
    if "x" in input:
        x = int(input,16)
        typeIn = "hex"

    elif "b" in input:
        x = int(input,2)
        typeIn = "bin"
    
    else:
        typeIn = "int"
        x = int(input)

    if (outputType == "bin"):
        return print(f'{input} [{typeIn}] --> {bin(x)} [{outputType}]')
        
    if (outputType == "dec"):
         return print(f'{input} [{typeIn}] --> {x} [{outputType}]')

    if (outputType == "hex"):
        return print(f'{input} [{typeIn}] --> {hex(x)} [{outputType}]')

x = input("What do you want to convert: ") 
baseOut = input("In which representation (bin, hex, dec) : ")
converter(x,baseOut)


#EXERCISE 2
print("\n")

def singPrec(input):
    newIn = ""

    for i in range(len(input),32):
        newIn += "0"
        
    for i in range(0,len(input)):
        newIn += input[i]

    #bit 0 = sign
    sign = newIn[0]

    #bits from 1 to 8 = exponent
    exponentCalc = int(newIn[1:9],2)

    #bits from 9 to 31
    mantissa = newIn[9:32]
    mantissaCalc = 1
    for x in range(1,24):
        mantissaCalc += int(mantissa[x-1]) * 2**(-x)
    
    #special values
    if (sign == "0" and exponentCalc == 255 and (mantissaCalc - 1) == 0):
        return("+INF")
    elif (sign == "1" and exponentCalc == 255 and (mantissaCalc - 1) == 0):
        return("-INF")
    elif (exponentCalc == 255 and (mantissaCalc - 1) > 0):
        return("NaN")
    
    if sign == "0":
        singPrecCalc = mantissaCalc * 2**(exponentCalc-127)
        return print("The single precision floating point number is :",singPrecCalc)
        
    elif sign == "1":
        singPrecCalc = -mantissaCalc * 2**(exponentCalc-127)
        return print("The single precision floating point number is :",singPrecCalc)
 
input32 = input("Insert 32 bits (for example 110000101011000000000000): ")
singPrec(input32)


#EXERCISE 3
print("\n")
#overflow limit
var = float(1) #starting point
list1 = [var]
i = 0
flag = False

while( flag == False):
    #print(var)
    var = var *2
    list1.append(var)
    old = list1[i]
    
    if ( old.hex() == var.hex() ):
        flag = True
    i = i+1
print("Overflow limit: ",list1[i-2])

#underflow limit
var = float(1) #starting point
list2 = [var]
i = 0
flag = False

while( flag == False):
    #print(var)
    var = var / 2
    list2.append(var)
    old = list2[i]
    
    if ( old.hex() == var.hex() ):
        flag = True
    i = i+1
print("Underflow limit: ",list2[i-2])


#EXERCISE 4
print("\n")
#underflow limit
var = float(1) #starting point
list2 = [var]
i = 0
flag = False
print("Initial number: ",var)

while( flag == False):
    var = var + 1/ (10**i)
    print("+ increment of ",1/ (10**i),"-->",var.hex())
    list2.append(var)
    old = list2[i]
    
    if ( old.hex() == var.hex() ):
        flag = True
    i = i+1
print("    No more effects on the number")
print("Machine precision: ",1/ (10** (i-2)) )

#EXERCISE 5
print("\n")
import math
import cmath
#a)
def quad_res(a,b,c):
    x1 = ( - b + math.sqrt(b**2 - 4 * a * c) ) / (2*a)
    x2 = ( - b - math.sqrt(b**2 - 4 * a * c) ) / (2*a)
    return x1,x2
    
print("Result with the standard formula: \n ",quad_res(0.001,1000,0.001), "\n")

#b)
def quad_res_mod2(a,b,c):
    z1 =  (2 * c) / ( - b - math.sqrt(b**2 - 4 * a * c) )
    z2 =  (2 * c) / ( - b + math.sqrt(b**2 - 4 * a * c) )
    return z1,z2
    
print("Result with the modified formula: \n ",quad_res_mod2(0.001,1000,0.001),"\n")

print("Are the two results equal?",quad_res(0.001,1000,0.001) == quad_res_mod2(0.001,1000,0.001))

"""
The obtained results are not the same because, since floats can have only a limited number of meaningful decimal places. 
This will yield to different results for the rounding error. 
"""

#c)
def quad_res_c(a,b,c):
    x1 = ( - b + cmath.sqrt(b**2 - 4 * a * c)) / (2*a)
    x2 = ( - b - cmath.sqrt(b**2 - 4 * a * c)) / (2*a)
    return x1,x2
    
a = int(input("Insert a: "))
b = int(input("Insert b: "))
c = int(input("Insert c: "))

print(quad_res_c(a,b,c))

#EXERCISE 6
print("\n")
#a)
def func_f(x):
    return x * (x - 1)

def der(delta):
    return (func_f(1+delta) - func_f(1))  / delta

print("Delta = ", 10**-2)
print("Result = ",der(10**-2), "      Error: ",1 - der(10**-2))
print("\n")

"""
The true value of the derivative is 1. The two results are not the same since our value for the delta is 10**-2.
Using the derivative function we are making an approximation (the value of the delta it's not precisely 0).
"""

#b)
deltaVect = [10**-4, 10**-6, 10**-8, 10**-10, 10**-12, 10**-14]
errorVect = []
for i in range(0,len(deltaVect)):
    errorVect.append(1 - der(deltaVect[i]))
    print("Delta = ", deltaVect[i])
    print("Result = ", der(deltaVect[i]), "      Error: ", 1 - der(deltaVect[i]))
    print("\n")

"""
The error between the true value and the function is decreasing passing from a delta = 10**-2 to a delta= 10**-8 (the one with minimal error).")
Then, starting from delta = 10**-8 the error restart to increase until the last value. This is due to fact that python has a limited machine precision and the result will be affected by rounding errors.
"""


#EXERCISE 7
#a)
print("\n")
import math
import timeit

def Riemann(N):
    sum = 0
    k = -1
    for i in range(1,N-1):
        fK = math.sqrt(1 - k**2)
        sum += 2/N * fK
        k += 2/N
    return sum
print("Using the Riemann integral with N = 100: ",Riemann(100))
print("True value (π/2): ", math.pi/2)
print("Error: ",math.pi/2 - Riemann(100))

"""
The result it's not equal to the true value since in the Riemann formula N tends to infinite and we are defining N = 0.

"""

#b)
print(" Trying to run the following code (commented) I obtained the following results: ")
print("For N = 781250 -->  Time =  0.9509137819983152")

import math
import timeit

setup = """import math
def Riemann(N):
    sum = 0
    k = -1
    for i in range(1,N-1):
        fK = math.sqrt(1 - k**2)
        sum += 2/N * fK
        k += 2/N
    return sum
"""
stmt = """Riemann(100)"""

"""

time = 0
N = 400000
while (time < 1):
    N = N + int(N/4)
    newStmt = 'Riemann({0})'.format(str(N))
    time = timeit.timeit(stmt = newStmt, setup = setup, number = 1)
    print("For N =",N, "-->  Time = ", time)
"""

print("For N = 25194240 -->  Time =  59.86323061999974")


"""
time = 0
N = 20155392
while (time < 60):
    N = N + int(N/4)
    newStmt = 'Riemann({0})'.format(str(N))
    time = timeit.timeit(stmt = newStmt, setup = setup, number = 1)
    print("For N =",N, "-->  Time = ", time)
"""

print("Using the Riemann integral with N = 781250: ",Riemann(781250))
print("True value (π/2): ", math.pi/2)
print("Error: ",math.pi/2 - Riemann(781250))

print("Using the Riemann integral with N = 25194240: ",Riemann(25194240))
print("True value (π/2): ", math.pi/2)
print("Error: ",math.pi/2 - Riemann(25194240))

"""
The result using the Riemann integral for N = 25194240 is more accurate. The gain obtained is in the accuracy of the result, since of value of N is increasing.
"""
