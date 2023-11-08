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

# In[6]:


def convert_number(num, output_base):
    
    if num.startswith('0x'):
        num_base = 'hex'
    elif num.startswith('0b'):
        num_base = 'bin'
    else:
        num_base = 'dec'

    # Convert to decimal (if not already)
    if num_base != 'dec':
        if num_base == 'bin':
            decimal_value = int(num, 2)
        else:  # input_base == 'hex'
            decimal_value = int(num, 16)
    else:
        decimal_value = int(num)

    # Convert to the desired output base
    if output_base == 'bin':
        output_value = bin(decimal_value)
    elif output_base == 'hex':
        output_value = hex(decimal_value)
    elif output_base == 'dec':
        output_value = decimal_value
    else:
        return "Invalid output base"

    return output_value


n = input("Insert a number: ")
b = input("Insert the final base: ")
result = convert_number(n, b)
print(result)  


# 2\. **32-bit floating point number**
# 
# Write a function that converts a 32 bit binary string (for example, `110000101011000000000000`) into a single precision floating point in decimal representation. Interpret the various bits as sign, fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations.

# In[10]:


n = '10001100110000101011000000000000'

def float_to_dec(num_to_conv):
    
    sgn = (-1)**(int(num_to_conv[0]))
    
    exp = num_to_conv[1:9]
    man = num_to_conv[9:]
    
    exp_dec = int(exp,2) - 127
    mant_dec = 1.0 # implicit 1 
    
    for i in range(23):
        if man[i] == '1':
            mant_dec += (1/(2 ** (i+1)))
        
    res = sgn * mant_dec * (2 ** exp_dec)
    
    return res

float_to_dec(n)


# 3\. **Underflow and overflow**
# 
# Write a program to determine the approximate underflow and overflow limits (within a factor of 2) for floating point numbers on your computer. 
# 
# *Hint*: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed the under/over-flow limits.

# In[2]:


import sys

under = 1.0
over = 1.0

while under != 0:
    # first memorize the last value before going out to the cycle
    pre_u = under
    under /= 2

while over != float('inf'):
    pre_o = over
    over *= 2

print("Approximate underflow limit:", pre_u)
print("Approximate overflow limit:", pre_o)


# 4\. **Machine precision**
# 
# Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.
# 
# *Hint*: define a new variable by adding an increasingly smaller value and check when the addition starts to have no effect on the number.

# In[14]:


# starting point
n = 1.0
lim = 1.0

while n + lim != n:
    lim /= 2

print(lim)


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

# In[27]:


from math import sqrt

def quad_sol(a,b,c):
    x_1 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    x_2 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    return x_1,x_2

def quad_sol_mul(a,b,c):
    x_1 = ((-b - sqrt(b**2 - 4*a*c))*(-b+sqrt(b**b-4*a*c)))/((2*a)*(-b+sqrt(b**b-4*a*c)))
    x_2 = ((-b + sqrt(b**2 - 4*a*c))*(-b-sqrt(b**b-4*a*c)))/((2*a)*(-b-sqrt(b**b-4*a*c)))
    return x_1,x_2

quad_sol(0.001, 1000, 0.001)
#quad_sol_mul(0.001, 1000, 0.001)
# COMMENT about - OverflowError: int too large to convert to float
# the solutions from the first function are next to the limit
# in the second, even if mathematically is the same the function is 
# mutiplying by a large number the solution before the division
# so it comes the overflow

# version for all cases

def quadratic_roots(a, b, c):
    delta = b**2 - 4*a*c

    if delta > 0:
        root1 = (-b + sqrt(delta)) / (2*a)
        root2 = (-b - sqrt(delta)) / (2*a)
        return root1, root2
    elif delta == 0:
        root = -b / (2*a)
        return root
    else:
        # Complex roots
        real_part = -b / (2*a)
        imaginary_part = sqrt(abs(delta)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

# Example usage:
a = -1
b = -4
c = -20
roots = quadratic_roots(a, b, c)
print(roots)


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

# In[4]:


def function(x):
    return x*(x-1)

def derivative(x,n):
    delta = pow(10, n)
    res = (function(x+delta)-function(x))/delta
    return res

exp = [-2, -4, -6, -8, -10, -12, -14, -20]

for i in range(len(exp)):
    print("derivative at x=1 for delta=10^",exp[i], "is equal to ", derivative(1, exp[i]))

# the real solution is 1
# as the delta decreases the computation isn't fine enough to see that the numerator is different from 0
# so the derivative works only if the delta is not too small


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

# In[8]:


from math import sqrt
import timeit

def Riemann_integral(N):
    h = 2/N
    I = 0
    for i in range(1, N+1):
        I += h*sqrt(1-pow(-1+(2/N)*i,2))
    return I
N=100
res = Riemann_integral(N) # next to the real
print("Value area semicircle with N =",N, ": ", res)

execution_time = timeit.timeit("Riemann_integral(N)", globals=globals(), number=1)

print(f"Time with N={N}: {execution_time} seconds")

print("---------------------------------------------------------------------------")


# compute how much N increase if I want the integral in less than 1 second
t=0
while t <= 1.0:
    N=int(1.475*N)
    res = Riemann_integral(N)
    t = timeit.timeit("res = Riemann_integral(N)", globals=globals(), number=1)
    print("Value area semicircle with N =",N, ": ", res)
    print(f"Time with N={N}: {t} seconds")
    
print("---------------------------------------------------------------------------")

# compute how much N increase if I want the integral in less than 1 minute
t=0
while t <= 60.0:
    N=int(2.49*N)
    res = Riemann_integral(N)
    t = timeit.timeit("res = Riemann_integral(N)", globals=globals(), number=1)
    print("Value area semicircle with N =",N, ": ", res)
    print(f"Time with N={N}: {t} seconds")


# In[ ]:




