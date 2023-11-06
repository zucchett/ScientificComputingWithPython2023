#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1
def converts(input_num, output_base):
    if isinstance(input_num,int):
        if output_base == 'bin':
            return bin(input_num)[2:]
        elif output_base == 'dec':
            return str(input_num)
        elif output_base == 'hex':
            return hex(input_num)[2:]
        else:
            return("Wrong representation")
        
input_num = 432
output_representation = 'hex'
result = converts(input_num, output_representation)
print(f"{input_num} in {output_representation} is: {result}")

input_num = 4223
output_representation = 'bin'
result = converts(input_num, output_representation)
print(f"{input_num} in {output_representation} is: {result}")

input_num = 19382
output_representation = 'dec'
result = converts(input_num, output_representation)
print(f"{input_num} in {output_representation} is: {result}")


# In[ ]:


#2

def convert(input_number):
    sign = 1
    if input_number[0] == '1':
        sign = -1
    exponent = input_number[1:9]
    exp = 0
    for i, n in enumerate(exponent):
        exp += int(n) * pow(2, 7 - i)
    exp -= 127
    mantissa = input_number[9:]
    fraction = 0
    for i, n in enumerate(mantissa):
        fraction += int(n) * pow(2, (i + 1) * -1)
    x = sign * (fraction + 1) * pow(2, exp)
    return x


# In[ ]:


#3

import math

def check():
    x = 1.0
    y = 1.0
    i = 0
    j = 0
    while x != math.inf:
        x *= 2
        i += 1
    while y != 0:
        y /= 2
        j += 1
    print(i, j)
    
check()   


# In[ ]:


#4

import math

def check():
    prev = 1.0
    curr = 1.5
    i = 1
    while curr != prev:
        i += 1
        prev = curr
        curr += pow(2, -i)
    print(i)
    
check()


# In[ ]:


#5
import cmath

def quadratic_standard(a, b, c):
    delta = b**2 - 4*a*c
    x1 = (-b + cmath.sqrt(delta)) / (2*a)
    x2 = (-b - cmath.sqrt(delta)) / (2*a)
    print("Solutions:")
    print("x1 =", x1)
    print("x2 =", x2)

quadratic_standard(0.001, 1000, 0.001)

def quadratic_modified(a, b, c):
    x1 = (-b + cmath.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - cmath.sqrt(b**2 - 4*a*c)) / (2*a)
    print("\nModified Solutions:")
    print("x1 =", x1)
    print("x2 =", x2)

quadratic_modified(0.001, 1000, 0.001)

def quadratic_accurate(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + cmath.sqrt(delta)) / (2*a)
        x2 = (-b - cmath.sqrt(delta)) / (2*a)
    elif delta == 0:
        x1 = x2 = -b / (2*a)
    else:
        real_part = -b / (2*a)
        imaginary_part = cmath.sqrt(abs(delta)) / (2*a)
        x1 = complex(real_part, imaginary_part)
        x2 = complex(real_part, -imaginary_part)
    print("\nAccurate Solutions:")
    print("x1 =", x1)
    print("x2 =", x2)

quadratic_accurate(0.001, 1000, 0.001)


# In[ ]:


#6
def function(x):
    return x * (x - 1)

def numerical_derivative(f, x, delta):
    return (f(x + delta) - f(x)) / delta

# (a)
x_value = 2.0
delta_a = 1e-2
numerical_result_a = numerical_derivative(function, x_value, delta_a)

analytical_result = 2 * x_value - 1

print("(a) For delta =", delta_a)
print("Numerical Result:", numerical_result_a)
print("Analytical Result:", analytical_result)
print("Difference:", abs(numerical_result_a - analytical_result))

# (b) 
delta_values = [1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]

for delta in delta_values:
    numerical_result = numerical_derivative(function, x_value, delta)
    print(f"\n(b) For delta = {delta}")
    print("Numerical Result:", numerical_result)
    print("Difference:", abs(numerical_result - analytical_result))


# In[ ]:


#7

import math
import numpy
import timeit
# (a)
def integral():
    N = 100
    h = 2/N
    S = 0
    for i in numpy.arange(-1.0, 1.0, h):
        y = math.sqrt(1 - pow(i, 2))
        S += h * y
    print(S)
    
integral()

original_N = 100
original_time = timeit.timeit(lambda: integral(original_N), number=1)
print(f"Original Time (N={original_N}): {original_time} seconds")

# (b)
max_time_allowed = 1.0
N = og_N
while True:
    N *= 2
    current_time = timeit.timeit(lambda: integral(N), number=1)
    if current_time > max_time_allowed:
        break

print(f"\nMaximum N for less than 1 second: {N}")
print(f"Time for N={N}: {current_time} seconds")


target_time = 60.0
N = og_N
while True:
    N *= 2
    current_time = timeit.timeit(lambda: integral(N), number=1)
    if current_time > target_time:
        break

print(f"\nN for 1 minute runtime: {N}")
print(f"Time for N={N}: {current_time} seconds")

