#!/usr/bin/env python
# coding: utf-8

# You can solve these exercises in the room or at home. For this week, and the next 3 weeks, exercises have to be solved by creating a single dedicated `.py` file called `03ex_representation.py`.
# 
# You can divide the individual exercises in the source code with appropriate comments (`#`).
# 
# The exercises need to run without errors with `python3 03ex_representation.py`.

# 1\. **Number representation**
# 
# Write a function that converts integer numbers among the bin, dec, and hex representations (bin<->dec<->hex).
# Determine the input type in the function, and pass another argument to choose the output representation.

# In[1]:


def number_representation(number, mode):
    base = -1
    if mode == 'bin':
        return bin(int(number))
    if mode == 'dec':
        return int(number)
    if mode == 'hex':
        return hex(int(number)) 
    return(int(number, base))          

print(number_representation('106', 'hex'))


# 2\. **32-bit floating point number**
# 
# Write a function that converts a 32 bit binary string (for example, `110000101011000000000000`) into a single precision floating point in decimal representation. Interpret the various bits as sign, fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations.

# In[3]:


def converter(number):
    return(float(int(number, 2)))

print(converter('110000101011000000000000'))


# 3\. **Underflow and overflow**
# 
# Write a program to determine the approximate underflow and overflow limits (within a factor of 2) for floating point numbers on your computer. 
# 
# *Hint*: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed the under/over-flow limits.

# In[10]:


undflow = 1
ovflow = 1
for i in range(1023):
    undflow = undflow / 2
    ovflow  = ovflow  * 2
scientific_undflow="{:e}".format(undflow)
scientific_ovflow="{:e}".format(ovflow)
print(f'\nThe over flow is: {scientific_ovflow}')
print(f'The under flow is: {scientific_undflow}')
print(f'I do the loop for 1023 times to reach the overflow and underflow.\n')


# 4\. **Machine precision**
# 
# Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.
# 
# *Hint*: define a new variable by adding an increasingly smaller value and check when the addition starts to have no effect on the number.

# In[11]:


var = 2
add = 1e-1
for i in range(20):
    var = var + add
    add = add * 1e-1
    print(f'Step {i}')
    print(var)
    
print("After 14 steps there is no difference in numbers.")


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

# In[12]:


import math

def quadratic(a, b, c):
    delta = math.sqrt((b**2) - (4*a*c))
    roots = []
    roots.append((-b + delta) / (2 * a))
    roots.append((-b - delta) / (2 * a))
    return roots

print(quadratic(0.001, 1000, 0.001))


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

# In[13]:


def f(x):
    return x * (x - 1)

def f_derivative(x, sigma = 0.0001):
    if sigma < 0.00000000000001:
        raise Exception('Can not devide by zero')
    return (f(x + sigma) - f(x)) / sigma   

print(f_derivative(1))


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
