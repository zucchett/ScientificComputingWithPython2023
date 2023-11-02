#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:08:07 2023

@author: annamatzen
"""

###
## Exercise 1: Number representation

def numb_rep(y, k):  # Input y has to be an integer, k can be one of three strings "d", "h" or "b".
    if type(y) == bin and k == "d":
        print("This is the decimal representation of", y, ": ", int(y,2))
    
    elif type(y) == bin and k == "h":
        y_dec = int(y,2)
        print("This is the hexadecimal representation of", y, ": ", hex(y_dec))
        
    elif type(y) == hex and k == "d":
        print("This is the decimal representation of", y, ": ", int(y,16))
        
    elif type(y) == hex and k == "b":
        y_dec1 = int(y,16)
        print("This is the binary representation of", y, ": ", bin(y_dec1))
    
    elif type(y) == int and k == "b":
        print("This is the binary representation of", y, ": ", bin(y))
    
    elif type(y) == int and k == "h":
        print("This is the hexadecimal representation of", y, ": ", hex(y))
    
    elif type(y) == int and k == "d":
        print("This is the decimal representation of", y, ":", y)
    
    else:
        print("This is the same representation of", y, ":", y)


numb_rep(78, "d")
numb_rep(23, "h")
numb_rep(4, "b")

###
## Exercise 2: 32-bit floating point number

def convertion_bit(n):
    bias = 127
    sign = int(n[0])
    exponent_input = n[1:9]
    fraction_input = n[9:32]

    
    exponent_list = list(exponent_input)
    exponent_str = [int(x) for x in exponent_list]
    exponent = ((exponent_str[7])*2**0+(exponent_str[6])*2**1+(exponent_str[5])*2**2+(exponent_str[4])*2**3+(exponent_str[3])*2**4+(exponent_str[2])*2**5+(exponent_str[1])*2**6+(exponent_str[0]*2**7))
   
    
    fraction_list = list(fraction_input)
    fraction_ints = [int(x) for x in fraction_list]
    
    fraction = 1
    for n in range(len(fraction_ints)):
        fraction += fraction_ints[n]/(2**(n+1))
    
    float_point = ((-1)**sign)*fraction*(2**(exponent-bias))
    print("This is the 32-bit floating point number:",float_point)


n = "110000101011000000000000"
convertion_bit(n)

n1 = "10111111011011101100000100100100"
convertion_bit(n1)

n2 = "00110101000010101000001010000000"
convertion_bit(n2)


###
## Exercise 3: Underflow and overflow

var1 = 1.0
var2 = 1.0

while var1 / 2 != 0.0:
    var1 = var1 / 2

while var2 * 2 != float('inf'):
    var2 = var2 * 2

print("Last value before underflow:",var1)
print("Last value before overflow:",var2)
# We see that underflow for this computer is reached at the limit of 5e-324
# The overflow for this computer is reached at the limit 8.98846567431158e+307
# Running the sys.float_info, the result shows that the overflow is set to max=1.7976931348623157e+308
# which is one decimal off of the computed result.



###
## Exercise 4: Machine precision

# Addding an increasingly small number to 7
var7 = 1.0
small = 10**1

while 7.0 + small != 7.0:
    var7 = small
    small = small * 10**-1

print("The precision of this machine for floating point numbers is:", small)




###
## Exercise 5: Quadratic solution
import math

def quadratic(a,b,c):
    if (b**2-4*a*c) < 0:
        return "There are no reel roots to this problem, only imaginary"
    elif (b**2-4*a*c) == 0:
        xw = -c / b
        return xw
    else:
        xpos = (-b + math.sqrt(b**2-4*a*c))/(2*a)
        xneg = (-b - math.sqrt(b**2-4*a*c))/(2*a)
    return xpos, xneg

# a
print("These are the two solutions to the quadratic function:", quadratic(0.001, 1000, 0.001))

# b
def new_quadratic(a,b,c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) * (-b + math.sqrt(b**2 - 4*a*c)) / ((2*a) * (-b + math.sqrt(b**2 - 4*a*c)))
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) * (-b + math.sqrt(b**2 - 4*a*c)) / ((2*a) * (-b + math.sqrt(b**2 - 4*a*c)))
    return x1,x2
print("These are the two solutions to the re-expressed standard function:", new_quadratic(0.001, 1000, 0.001))

# We see that we get two very similar solutions. This is due to the fact that we are multiplying
# the fraction with the same mulitplier, which equals to multiplying the fraction by 1. 
# The only difference we see is the addition of "0001" to the second solution -999999.9999990001.
# This is due to the fact that the representation of the solution may be different, now the
# solution is computed from other floats, that are not exactly the same as the standard formula. 


# c
def accurate_roots(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Infinite number of solutions"
            else:
                return "The equation is inconsistent"
        else:
            xw = -c / b
            return xw
    else:
        d = b**2 - 4*a*c
        if d < 0:
            return "There are no reel roots to this problem, only imaginary"
        else:
            xpos = (-b + math.sqrt(d)) / (2*a)
            xneg = (-b - math.sqrt(d)) / (2*a)
            return xpos, xneg

print("These are the solutions found by the accurate function:", accurate_roots(0.001, 1000, 0.001))

# The solution is the same as in the previous functions. 



###
## Exercise 6: The derivative

def f(x):
    return x*(x-1)

# a
x = 1
d = 10**(-2)
print("This is the derivative for delta = 10^(-2):")
print((f(x+d)-f(x))/d)

# The solution found by the program is 1.010000000000001, which compared with the analytical
# solution, which is 1, is not accurately the same. This is due to the fact that the delta
# value is chosen as a finite value, which returns the average rate of change in the funciton.

# b
print("These are the derivatives for increasing values of delta:")
d = 10**(-4)
print((f(x+d)-f(x))/d)

d = 10**(-6)
print((f(x+d)-f(x))/d)

d = 10**(-8)
print((f(x+d)-f(x))/d)

d = 10**(-10)
print((f(x+d)-f(x))/d)

d = 10**(-12)
print((f(x+d)-f(x))/d)

d = 10**(-14)
print((f(x+d)-f(x))/d)

# We see that the accuracy of the result increases as the value of delta decreases. 
# When the value of delta is set too small, we see issues with rounding (the last result).



###
## Exercise 7: Integral of a semicircle

def riemann(N):
    I = 0
    for k in range(1, N+1):
        I += 2/N * math.sqrt(1-(-1 + k * 2/N)**2)
    return I

# a
N = 100
print("Computed result with N = 100:", riemann(N))
print("True value:", math.pi/2)

# The results are close, but is inaccurate on the third decimal.

# b
import timeit
print("N set to 3 before time exceeds 1 second: ", timeit.timeit(lambda:riemann(3)))
# From this timeit function, the conclusion is made that the function cannot take in more than
# N = 3 before the running time exceeds 1 second. This may be due to the construction of the function
# or the wrong use of the timeit function itself. 

N2 = 200
print("Computed result with N = 200:", riemann(N2))
print("True value:", math.pi/2)
print("N increased to 200 before time exceeds 1 minute: ", timeit.timeit(lambda:riemann(200)))
# The running time reaches almost 1 minute at N = 200, gaining more accuracy, but also
# having a longer running time. 








        