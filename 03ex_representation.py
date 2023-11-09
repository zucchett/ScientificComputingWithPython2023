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

print("****1.*************************************************************************")
a=int(input("input must be integer : "))
b=str(input("please chose bin or hex or dec : "))
def converts_num(a,b):
    if b=="dec":        
        print("decimal:",a)
        
    elif b=="bin":        
        a_bin = bin(a)
        print("bin:",a_bin)
        
    elif b=="hex":
        a_hex = hex(a)
        print("hex:",a_hex)
        
    else:
        print("!!!Second input must be bin or hex or dec!!!")
converts_num(a,b)


# 2\. **32-bit floating point number**
# 
# Write a function that converts a 32 bit binary string (for example, `110000101011000000000000`) into a single precision floating point in decimal representation. Interpret the various bits as sign, fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations.

# In[18]:

print("****2.*************************************************************************")
def convertToInt(binary):
    
    sign_bit = int(binary[0])

    exponent_bias = int(binary[1 : 9], 2)

    exponent_unbias = exponent_bias - 127

    mantissa_str = binary[9 : ]
 
    power_count = -1

    mantissa_int = 0
 
    for i in mantissa_str:
 
        mantissa_int += (int(i) * pow(2, power_count))
 
        power_count -= 1
         
    result = pow(-1, sign_bit) * (mantissa_int + 1) * pow(2, exponent_unbias)
                          
    return result

example_str = '110000101011000000000000'
 
res = convertToInt(example_str)

print("Result :",res)


# 3\. **Underflow and overflow**
# 
# Write a program to determine the approximate underflow and overflow limits (within a factor of 2) for floating point numbers on your computer. 
# 
# *Hint*: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed the under/over-flow limits.

# In[3]:

print("****3.overflow*************************************************************************")
import math 
a = 1.0
while True:
    
    
    b = a * 2
    
    if math.isinf(b):
        print(f"Overflow limit reached: {a}")
        break
    a = b


# In[4]:

print("****3.underflow*************************************************************************")
a = 1.0
while True:
    
    
    b = a / 2
    
    if b == 0:
        print(f"Underflow limit reached: {a}")
        break
    a = b


# 4\. **Machine precision**
# 
# Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.
# 
# *Hint*: define a new variable by adding an increasingly smaller value and check when the addition starts to have no effect on the number.

# In[5]:
print("****4.*************************************************************************")

for a in range(300):
    x = float("1.0e"+str(a))
    if x == x+1:
        print(f"After {x} addition has no effect.")
        break


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
print("****5.a*************************************************************************")

import math
# a
def quadratic_solver(a,b,c):

    d = (b**2) - (4*a*c)
    
    d = math.sqrt(d)
    
    x1 = (-b-d)/(2*a)
    x2 = (-b+d)/(2*a)
    
    return x1,x2

print(quadratic_solver(0.001,1000,0.001))


# In[7]:

print("****5.b*************************************************************************")
# b
# This is done to avoid potential loss of precision when calculating roots, but the result remains unchanged.
def quadratic_solver_extended(a,b,c):

    d = (b**2) - (4*a*c)
    
    d = math.sqrt(d)

    x1 = ((-b-d) * (-b-d))/((2*a) * (-b-d))
    x2 = ((-b+d) * (-b+d))/((2*a) * (-b+d))

    return x1,x2

print(quadratic_solver_extended(0.001,1000,0.001))


# In[8]:

print("****5.c*************************************************************************")
# 
import math

def solve_quadratic(a, b, c):
    d = b ** 2 - 4 * a * c

    if d > 0:
        d = math.sqrt(d)
        if b >= 0:
            x1 = (-b - d) / (2 * a)
            x2 = (c / (a * x1))
        else:
            x2 = (-b + d) / (2 * a)
            x1 = (c / (a * x2))
        return x1, x2
    elif d == 0:
        x1 = -b / (2 * a)
        return x1
    
print(solve_quadratic(0.001,1000,0.001))



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
print("****6.a*************************************************************************")

def fx(x):
    
    return x * (x-1)

def derivative_of_fx(x):
    
    return (2 * x) - 1

def derivate_with_definition(omega,x):
    
    derivative = (fx(x+omega) - fx(x)) / omega
    
    return derivative

print(derivative_of_fx(1))
print(derivate_with_definition(1e-2,1))

#Because of omega's value.


# In[10]:

print("****6.b*************************************************************************")
omegas = [1e-4,1e-6,1e-8,1e-10,1e-12,1e-14]
x = 1
for omega in omegas:
    print(f"For omega {omega} and x {x} derivative is: {derivate_with_definition(omega,x)}.")

#Until 1e-10 accuracy scale increasing but after this accuracy scale decreasing.


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

# In[2]:
print("****7.a*************************************************************************")

import math

def semicircle(x):
    
    return ((1 - x**2))**(1/2)

def riemann_integral(N):
    
    h = 2 / N
    
    x = -1 
    
    integral = 0
    
    for i in range(1,N):
        
        x = x + h

        y = semicircle(x)
        
        integral += h*y
    
    return integral

print(riemann_integral(100))
print("****7.b*************************************************************************")

# In[ ]:


print('for 1 sec. result is better but for 1 min. result is worse')


# In[ ]:


print('riemann_integral(3500000) # 1 second\n#963 ms ± 12.5 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)')


# In[4]:


print('riemann_integral(200000000) # 1 min\n#57.2 s ± 848 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)')


# In[14]:


import math
res_1_sec = riemann_integral(3500000)
res_1_min = riemann_integral(200000000)
res_exact = math.pi / 2


# In[ ]:

print('res_exact=1.5707963267948966    res_1_sec=1.5707963265223677    res_1_min=1.5707963241309673')
