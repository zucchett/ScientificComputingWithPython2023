# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:57:02 2023

@author: andre
"""

# Exercises week 3
# Scientific computing with python(23/24)
# Written by Andrea Sandbu Numme 

# ex01

def convertion(x):
    if x.startswith("0x"):
        x = int(x[2:], 16)
        
    elif x.startswith("0b"):
        int(x[2:], 2)
        
    elif all(i in '01' for i in x):
        x = int(x, 2)
        
    else:
        try:
            x = int(x)
        except ValueError:
            x = int(x)
    
    y = int(input('What type do you want the output to be (bin = 1 / dec = 2 / hex = 3):')) 

    if y == 1: 
        return bin(x)
    elif y == 2:
        return int(x)
    elif y == 3:
        return hex(x) 

x = input('Write input for exercise 1: ')

output_representation = convertion(x)
print('Chosen representation of the input value is: ', output_representation)


# ex02 


def conv_bin(in_bin):
    sign = int(in_bin[0],2) #integer out of bin number 1 
    
    ex = int(in_bin[1:9],2) - 127 #extract the middle bits for the exponent and make it unbiased 
    
    mantissa_bits = in_bin[9:] #extract the bits used for fractions 
    mantissa_ints = [int(i) for i in mantissa_bits] #change all values to ints
    
    mantissa = 1
    
    for i in range(len(mantissa_ints)):
        mantissa += mantissa_ints[i] * 2**(-i - 1)
    
    x_float = (-1) ** sign * mantissa * 2**ex
    
    print('Decimal representation of the binary number is: ', x_float)

in_bin = "110000101011000000000000"
conv_bin(in_bin)



# ex03 

#underflow
underflow = 1.0
for i in range(15000):
    test = underflow/2.0 
    if test == 0: #when underflow, it gives 0 
        print('Last value before underflow:', underflow)
        break
    
    underflow = test

#overflow
overflow = 1.0

while overflow * 2.0 < float('inf'): #float('inf') gives infenitly large value
    overflow *= 2.0
    
print('Last value before overflow:', overflow)


# ex04
machine_precision = 1.0
smaller_value = 1.0

while 1.0 + smaller_value != 1.0: #stops when the small number has no effect on the original number
    machine_precision = smaller_value
    smaller_value /= 2.0
    
print('The machine precision:', machine_precision)



# ex05 

import math 
# 05_a 
def quadratic_sol(a,b,c):
    dis = (b**2) - (4*a*c)
    if dis < 0 : #check if it has real roots or not
        return "imaginary roots"
    elif dis == 0:
        x = -b / 2*a
        print('Only one solution:', x)
    else:
        
        x1 = ((-b)+ math.sqrt(dis)) / (2*a)
        x2 = ((-b) - math.sqrt(dis)) / (2*a)
        print('Solution one:', x1)
        print('Solution two:', x2)

a = 0.001
b = 1000
c = 0.001
quadratic_sol(a,b,c)

#05_b
def quadratic_sol1(a1,b1,c1):
    dis1 = (b1**2) - (4*a1*c1)
    if dis1 < 0 : #check if it has real roots or not
        return "imaginary roots"
    elif dis1 == 0:
        x3 = -b1 / 2*a1
        print('Only one solution:', x3)
    else:

        x12 = (((-b1)+ math.sqrt(dis1))*((-b1)+ math.sqrt(dis1))) / ((2*a1)*((-b1) + math.sqrt(dis1))) 
        x22 = (((-b1)+ math.sqrt(dis1))*((-b1) - math.sqrt(dis1))) / ((2*a1)*((-b1) + math.sqrt(dis1))) 

        print('Solution one 05_b:', x12)
        print('Solution three 05_b:', x22)



a1 = 0.001
b1 = 1000
c1 = 0.001
quadratic_sol1(a1,b1,c1)



#05_c
def accurate_roots(a2, b2, c2):
    dis = (b2**2) - (4*a2*c2)

    if dis > 0:
        #root_dis = math.sqrt(dis)
        x1 = ((-b)+ math.sqrt(dis)) / (2*a2)
        x2 = ((-b)- math.sqrt(dis)) / (2*a2)      
        print("Roots:", x1, x2)
    elif dis == 0:
        x = -b2 / (2 * a2)
        print("Roots:", x)
    else:
        reals = -b2 / (2 * a2)
        imags = math.sqrt(abs(dis)) / (2 * a2)
        x1 = complex(reals, imags)
        x2 = complex(reals, -imags)
        print("Roots:", x1, x2)


a2 = 0.001
b2 = 1000
c2 = 0.001


accurate_roots(a2, b2, c2)


# ex06 

def f(x):
    return x*(x-1)

def calc_der(delta, x):
    der = []
    for i in range(len(delta)):
        num = f(x + delta[i]) - f(x)
        der.append(num / delta[i])
    return der

x = 1
delta = [10**(-2)]
result = calc_der(delta, x)
print('Result from delta = 10^-2:', result)

"""
If calculated analytically, the derivative would be equal to 1:
    f(x) = x*(x-1)
    f'(x) = 2*x-1
    f'(1) = 2*1-1 = 1
    
The analytical answer deviates with ~0.01 from the program answer. 
This deviation is the same as the delta input. If the delta was smaller,
the deviation would also be smaller. 
"""

deltas = [10**(-4), 10**(-6), 10**(-8), 10**(-10), 10**(-12), 10**(-14)]
result2 = calc_der(deltas, x)
print('Result from different delta-values:', result2)

"""
When the delta-value gets smaller, the accuracy gets closer to 1. 
The last delta value gives an answer <1.
"""

# ex07 


def functi(x):
    y = math.sqrt(abs(1-x**2))
    return y
def integrand(N):
    h = 2/N
    integral = 0
    
    for k in range(1, N+1):
        x = k * h
        y = functi(x)
        integral += h * y
    
    return integral

N = 100
result = integrand(N)
print(result)

import timeit

timed_int = timeit.timeit("integrand(1295)", globals=globals(), number=1000)
print('Time for integral:', timed_int, 's')

"""
If the calculation should last less than a second, N <= 1295 (although the 
  timing changes everytime, after 10 tries, it did not exceed) 
The bigger N is, the closer the value comes to the value of I = pi/2 
"""