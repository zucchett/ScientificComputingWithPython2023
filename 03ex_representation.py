#!/usr/bin/env python
# coding: utf-8

# You can solve these exercises in the room or at home. For this week, and the next 3 weeks, exercises have to be solved by creating a single dedicated `.py` file called `03ex_representation.py`.
# 
# You can divide the individual exercises in the source code with appropriate comments (`#`).
# 
# The exercises need to run without errors with `python3 03ex_representation.py`.

# In[1]:


import math as m # We import math because it will be useful later


# 1\. **Number representation**
# 
# Write a function that converts integer numbers among the bin, dec, and hex representations (bin<->dec<->hex).
# Determine the input type in the function, and pass another argument to choose the output representation.

# In[2]:


print("\n--- 1. Number representation ---\n")

def NumberRepresentation(number, output_type):
    if output_type not in ["dec", "bin", "hex"] :
        return "Error : Incorrect output type (dec, bin or hex) => " + output_type + "."
    
    # Determine the input type
    if type(number) == int :
        input_type = "dec"
    elif type(number) == str and "0b" in number :
        input_type = "bin"
        number = int(number, 2)
    elif type(number) == str and "0x" in number :
        input_type = "hex"
        number = int(number, 16)
    else:
        return "Error : The number entered is in the wrong format (int, bin or dex)."

    # Convert to the desired output type
    if output_type == "bin":
        return bin(number)
    elif output_type == "hex":
        return hex(number)
    else:
        return number

print("Let's take 7 as the input number.\n")
print("=> 7 in binary gives :", NumberRepresentation(7, "bin"))
print("=> 7 in hexadecimal gives :", NumberRepresentation(7, "hex"))
print("=> 0b111 in decimal gives :", NumberRepresentation("0b111", "dec"))
print("=> 0x7 in decimal gives :", NumberRepresentation("0x7", "dec"))
print("=> 0b111 in hexadecimal gives :", NumberRepresentation("0b111", "hex"))
print("=> 0x7 in binary gives :", NumberRepresentation("0x7", "bin"))


# 2\. **32-bit floating point number**
# 
# Write a function that converts a 32 bit binary string (for example, `110000101011000000000000`) into a single precision floating point in decimal representation. Interpret the various bits as sign, fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations.

# In[3]:


print("\n--- 2. 32-bit floating point number ---\n")

def SinglePrecisionFloatingPoint(binary_string):
    if len(binary_string) > 32:
        return "Error: The binary string must be 32 bits long."
    elif len(binary_string) < 32:
        add = 32 - len(binary_string)
        binary_string = '0' * add + binary_string

    sign = int(binary_string[0])
    exponent = int(binary_string[1:9], 2)
    mantissa = binary_string[9:]

    final_mantissa = 0
    for i in range(1, len(mantissa) + 1):
        if mantissa[i-1] == "1":
            final_mantissa += 2 ** (-i)

    if sign == 0:
        sign = 1
    else:
        sign = -1
        
    value = sign * (1 + final_mantissa) * (2 ** (exponent - 127))

    return value

# Test
binary_str = "110000101011000000000000"
print("For the following 32-bit :", binary_str, ", we obtain the value :", SinglePrecisionFloatingPoint(binary_str))


# 3\. **Underflow and overflow**
# 
# Write a program to determine the approximate underflow and overflow limits (within a factor of 2) for floating point numbers on your computer. 
# 
# *Hint*: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed the under/over-flow limits.

# In[4]:


print("\n--- 3. Underflow and overflow ---\n")

def Underflow_Overflow():
    underflow_limit, overflow_limit = 1.0, 1.0
    
    # Underflow
    while underflow_limit != 0:
        prev_underflow = underflow_limit
        underflow_limit = underflow_limit/2
        
    # Overflow
    while overflow_limit != float('inf'):
        prev_overflow = overflow_limit
        overflow_limit = overflow_limit*2

    return prev_underflow, prev_overflow

underflow, overflow = Underflow_Overflow()
print("=> Underflow limit :", underflow)
print("=> Overflow limit : ", overflow)


# 4\. **Machine precision**
# 
# Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.
# 
# *Hint*: define a new variable by adding an increasingly smaller value and check when the addition starts to have no effect on the number.

# In[5]:


print("\n--- 4. Machine precision ---\n")

def MachinePrecision():
    precision = 1.0
    while (1.0 + precision/2) != 1.0:
        precision = precision*0.1
    return precision

precision = MachinePrecision()
print("=> Machine precision :", precision)


# 5\. **Quadratic solution**
# 
# Write a function that takes in input three parameters $a$, $b$ and $c$ and prints out the two solutions to the quadratic equation $ax^2+bx+c=0$ using the standard formula:
# $$
# x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
# $$
# 
# (a) use the function to compute the solution for $a=0.001$, $b=1000$ and $c=0.001$
# 
# (b) re-express the standard solution formula by multiplying the numerator and the denominator by $-b\mp\sqrt{b^2-4ac}$ and again find the solution for $a=0.001$, $b=1000$ and $c=0.001$. How does it compare with what has been previously obtained, and why? (add the answer to a Python comment)
# 
# (c) write a function that computes the roots of a quadratic equation accurately in all cases

# In[6]:


print("\n--- 5. Quadratic solution ---\n")

print("\n--- a. ---\n")

def QuadraticSolution(a, b, c):
    discriminant = b**2-4*a*c
    if discriminant < 0:
        return "No real solutions."
    else:
        x1 = (-b-m.sqrt(discriminant))/(2*a)
        x2 = (-b+m.sqrt(discriminant))/(2*a)
        return x1, x2

    
a = 0.001
b = 1000
c = 0.001

solutions = QuadraticSolution(a, b, c)

print("Solutions of Quadractic Problem : ")
print("=> x1 =", solutions[0])
print("=> x2 =", solutions[1])


# In[7]:


print("\n--- b. ---\n")

def QuadraticSolution2(a, b, c):
    discriminant = b**2-4*a*c
    if discriminant < 0:
        return "No real solutions."
    else:
        x1 = (2*c)/(-b-m.sqrt(discriminant))
        x2 = (2*c)/(-b+m.sqrt(discriminant))
        return x1, x2

a = 0.001
b = 1000
c = 0.001
solutions2 = QuadraticSolution2(a, b, c)

print("Solutions of Quadractic Problem 2 : ")
print("=> x1 =", solutions2[0])
print("=> x2 =", solutions2[1])

# WHY ???
# Using the formula re-expressed with the conjugate, we obtain a more accurate estimate of the solution x1.
# This gain in precision is due to floating-point computer technology, which can sometimes introduce errors when manipulating very close numbers.
# When two almost equal values are subtracted, the significant digits are lost. So, if the two subtracted values had to be rounded to fit into a 32-bit floating-point number, the difference is imprecise. In our case, we prefer to add two positive numbers or subtract two negative numbers. Referring to the standard solution, we can see that one of the solutions is problematic depending on whether b is positive or negative. We therefore need to adapt the method by using the conjugate depending on whether b is positive or negative, depending on which of the two solutions is involved.

print("""
WHY ???
Using the formula re-expressed with the conjugate, we obtain a more accurate estimate of the solution x1.
This gain in precision is due to floating-point computer technology, which can sometimes introduce errors when manipulating very close numbers.
When two almost equal values are subtracted, the significant digits are lost. So, if the two subtracted values had to be rounded to fit into a 32-bit floating-point number, the difference is imprecise. In our case, we prefer to add two positive numbers or subtract two negative numbers. Referring to the standard solution, we can see that one of the solutions is problematic depending on whether b is positive or negative. We therefore need to adapt the method by using the conjugate depending on whether b is positive or negative, depending on which of the two solutions is involved.
""")


# In[8]:


print("\n--- c. ---\n")

def QuadraticSolution3(a, b, c):
    discriminant = b**2-4*a*c
    if discriminant < 0:
        return "No real solutions."
    else:
        if b == 0 :
            x = -b/(2*a)
            return x,x
        if b > 0 :
            x1 = (-b-m.sqrt(discriminant))/(2*a)
            x2 = (2*c)/(-b-m.sqrt(discriminant))
            return x1, x2
        else:
            x1 = (2*c)/(-b+m.sqrt(discriminant))
            x2 = (-b+m.sqrt(discriminant))/(2*a)
            return x1, x2

a = 0.001
b = 1000
c = 0.001
solutions3 = QuadraticSolution3(a, b, c)

print("Solutions of Quadractic Problem 3 : ")
print("=> x1 =", solutions3[0])
print("=> x2 =", solutions3[1])


# 6\. **The derivative**
# 
# Write a program that implements the function $f(x)=x(x−1)$
# 
# (a) Calculate the derivative of the function at the point $x = 1$ using the derivative definition:
# 
# $$
# \frac{{\rm d}f}{{\rm d}x} = \lim_{\delta\to0} \frac{f(x+\delta)-f(x)}{\delta}
# $$
# 
# with $\delta = 10^{−2}$. Calculate the true value of the same derivative analytically and compare it with the answer your program gives. The two will not agree perfectly. Why?
# 
# (b) Repeat the calculation for $\delta = 10^{−4}, 10^{−6}, 10^{−8}, 10^{−10}, 10^{−12}$ and $10^{−14}$. How does the accuracy scale with $\delta$?

# In[9]:


print("\n--- 6. The derivative ---\n")

print("\n--- a. ---\n")

# We define the function f(x) = x(x-1)
def f(x):
    return x * (x - 1)

# We define the derivative function of f
def df(f, x, delta):
    return (f(x + delta) - f(x)) / delta

x = 1
delta = 10**-2
numerical_derivative = df(f, x, delta)

# The derivative of f(x) is 2x-1
analytical_derivative = 2*x-1

print("Taking x = 1, we find the following values :")
print("=> Numerical derivative :", numerical_derivative)
print("=> Analytical derivative :", analytical_derivative)

# WHY ???
# The numerical method is an approximation and may introduce errors. In fact, we pass through a limit to obtain the value of the derivative at x=1, which leads to this lack of precision. 
# The analytical method, on the other hand, gives a precise value, as it is based on the precise derivative of the function at x = 1.
# The difference between the actual value and the numerical value is therefore due to the error created by the method.

print("""\n\nWHY ???
The numerical method is an approximation and may introduce errors. In fact, we pass through a limit to obtain the value of the derivative at x=1, which leads to this lack of precision. 
The analytical method, on the other hand, gives a precise value, as it is based on the precise derivative of the function at x = 1.
The difference between the actual value and the numerical value is therefore due to the error created by the method.
""")


# In[10]:


print("\n--- b. ---\n")

deltas = [10**-i for i in range(4, 15, 2)]

for delta in deltas:
    numerical_derivative = df(f, x, delta)
    print("Numerical derivative with delta =", delta, " :", numerical_derivative)

# WHY ???
# As delta decreases, the numerical derivative approaches the real value of the analytical derivative, which is 1. 
# However, as delta continues to decrease, and delta becomes extremely small, the result no longer corresponds and loses precision due to rounding errors.

print("""\n\nWHY ???
As delta decreases, the numerical derivative approaches the real value of the analytical derivative, which is 1. 
However, as delta continues to decrease, and delta becomes extremely small, the result no longer corresponds and loses precision due to rounding errors. 
""")


# 7\. **Integral of a semicircle**
# 
# Consider the integral of the semicircle of radius 1:
# $$
# I=\int_{-1}^{1} \sqrt(1-x^2) {\rm d}x
# $$
# which is known to be $I=\frac{\pi}{2}=1.57079632679...$.
# 
# Alternatively we can use the Riemann definition of the integral:
# $$
# I=\lim_{N\to\infty} \sum_{k=1}^{N} h y_k 
# $$
# 
# with $h=2/N$ the width of each of the $N$ slices the domain is divided into and where
# $y_k$ is the value of the function at the $k-$th slice.
# 
# (a) Write a program to compute the integral with $N=100$. How does the result compare to the true value?
# 
# (b) How much can $N$ be increased if the computation needs to be run in less than a second? What is the gain in running it for 1 minute? Use `timeit` to measure the time.

# In[11]:


print("\n--- 7. Integral of a semicircle ---\n")

print("\n--- a. ---\n")

def IntSemicircle(N):
    h = 2/N
    value = 0
    for k in range(N):
        x = -1+k*h
        y = m.sqrt(1-x**2)
        value += h*y
    return value

N = 100
value1 = IntSemicircle(N)
value2 = m.pi / 2

print("Value obtained via Riemann and the integral with N =", N, " :", value1)
print("True value :", value2)

# We can see that the two values obtained are very close with: 0.0016620712456461018 difference.
# We can therefore conclude that the main error between the two results is the rounding done automatically by the computer, which accumulates with each iteration.

print("""
We can see that the two values obtained are very close with:""", value2 - value1, """difference.
We can therefore conclude that the main error between the two results is the rounding done automatically by the computer, which accumulates with each iteration.
""")


# In[12]:


print("\n--- b. ---\n")

import timeit

target_time = 1.0 # For 1 second

N = 100  
time = timeit.timeit(lambda: IntSemicircle(N), number=1)

# Increase N while measuring execution time until it's close to the target time
while time < target_time:
    N = N*2
    time = timeit.timeit(lambda: IntSemicircle(N), number=1)

# Calculate the gain in running it for 1 minute
time_min = N * 60 / time
value = IntSemicircle(N)

print("=> Number N compute in less than 1 second :", N)
print("=> Integral value after one minute computation :", value)
print("=> Estimated number of N to compute in 1 minute :", int(time_min))

