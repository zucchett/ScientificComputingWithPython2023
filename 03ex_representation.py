#!/usr/bin/env python
# coding: utf-8

# You can solve these exercises in the room or at home. For this week, and the next 3 weeks, exercises have to be solved by creating a single dedicated `.py` file called `03ex_representation.py`.
# 
# You can divide the individual exercises in the source code with appropriate comments (`#`).
# 
# The exercises need to run without errors with `python3 03ex_representation.py`.

#%%

# 1\. **Number representation**
# 
# Write a function that converts integer numbers among the bin, dec, and hex representations (bin<->dec<->hex).
# Determine the input type in the function, and pass another argument to choose the output representation.

#%%


def convert_number(number, output_base):
        input_base = 10
        number=str(number)
        
        if number.startswith('0x'): #The input number is in hex representation
            input_base = 16
        elif number.startswith('0b'): #The input number is in bin representation
            input_base = 2

        
        dec_number = int(str(number), input_base) #We convert the number into decimal

       
        if output_base == 'bin':
            return bin(dec_number)
        elif output_base == 'dec':
            return str(dec_number)
        elif output_base == 'hex':
            return hex(dec_number)
        else:
            return "Invalid output base"


''' Examples : '''
    
    
a_dec = 45
a_bin = convert_number(a_dec, 'bin')
a_hex = convert_number(a_dec, 'hex')
print(f'Decimal representation of a = {a_dec}\nBinary representation of a = {a_bin}\nHexadecimal representation of a = {a_hex}')

b_hex = '0x45fab'
b_bin = convert_number(b_hex, 'bin')
b_dec = convert_number(b_hex, 'dec')
print(f'\nDecimal representation of b = {b_dec}\nBinary representation of b = {b_bin}\nHexadecimal representation of b = {b_hex}')

#%%

# 2\. **32-bit floating point number**
# 
# Write a function that converts a 32 bit binary string (for example, `110000101011000000000000`) into a single precision floating point in decimal representation. Interpret the various bits as sign, fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations.

#%%


def Floating_Point_Number(number):
    if len(number)!=32 or type(number)!=str:
        print("The number must be a 32 bit binary string")
    else:
        s = int(number[0]) #The sign is store in the first bit
        e = number[1:9] #The fractional part of the Mantissa is store on 8 bits
        f = number[9:] #The exponantial part of the Mantissa is store on 23 bits
        
        sign = -1 if s else 1 # If the first bit is 0 -> sign +, else sign -
        exp = int(e, 2) # We convert the exponantial part of the Mantissa into decimal
        frac = sum(int(x)*2**(-i) for i,x in enumerate(f,1))
        
        return sign*2**(exp-127)*(1+frac)
            
        
#Example

bin_1 = '11000010101100000101100000000000'
bin_1_fp = Floating_Point_Number(bin_1)
print(f"bin_1 = {bin_1}\nSingle precision floating point of bin_1 in decimal representation = {bin_1_fp} ")

#%%

# 3\. **Underflow and overflow**
# 
# Write a program to determine the approximate underflow and overflow limits (within a factor of 2) for floating point numbers on your computer. 
# 
# *Hint*: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed the under/over-flow limits.

#%%


#Underflow limit :

Underflow = 1.0
while Underflow/2.0 != 0.0:
    Underflow= Underflow /2.0
    
Overflow = 1.0
while Overflow*2.0 != float('inf'):
    Overflow = Overflow*2.0

print(f"Underflow limit = {Underflow}\nOverflow limit = {Overflow}")


#%%

# 4\. **Machine precision**
# 
# Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.
# 
# *Hint*: define a new variable by adding an increasingly smaller value and check when the addition starts to have no effect on the number.

#%%


variable=1
Machine_precision=1

while variable+Machine_precision != variable:
    variable = variable+Machine_precision
    Machine_precision = Machine_precision/2

print(f"Machine precision for floating point numbers = {Machine_precision}")


#%%

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

#%%


#a)
import math as m

def Quadratic_Equation(a, b, c):
    disc = b**2-4*a*c
    if disc<0:
        print("No real solutions")
    else:
        num_1 = -b+m.sqrt(disc)
        deno = 2*a
        num_2 = -b-m.sqrt(disc)
        x1 = num_1/deno
        x2 = num_2/deno
    return (x1, x2)

a, b, c = 0.001, 1000, 0.001
res_1 = Quadratic_Equation(a,b,c)
print(res_1)


#%%

#b)

def Quadratic_Equation2(a, b, c):
    disc = b**2-4*a*c
    if disc < 0:
        print("No real solutions")
    else:
        num = 2*c
        deno_2 = -b+m.sqrt(disc)
        deno_1 = -b-m.sqrt(disc)
        x1 = num/deno_1
        x2 = num/deno_2
    return (x1, x2)

res_2 = Quadratic_Equation2(a,b,c)
print(res_2)

error_x1 = 100*(res_2[0]-res_1[0])/res_2[0]
error_x2 = 100*(res_2[1]-res_1[1])/res_2[1]
print(f"Error between method 1 and method 2 for x1 = {round(error_x1,5)} %")
print(f"Error between method 1 and method 2 for x2 = {round(error_x2,5)} %")

'''
By rearranging the terms of the equation, we find a little difference when we computs the roots x1 and x2. This computing error is due to the
Substration of two very close values with b=1000 and sqrt(b**2 - 4*a*c) which is very close to b because a and c are very small values (0.01). 
'''


#%%

#c)

def Quadratic_accurate(a, b, c):
    if b<0:
        x1 = Quadratic_Equation(a,b,b)[0]
        x2 = Quadratic_Equation2(a, b, c)[1]
    
    else:
        x1 = Quadratic_Equation2(a,b,b)[0]
        x2 = Quadratic_Equation(a, b, c)[1]
    return(x1, x2)

res_accurate = Quadratic_accurate(a, b, c)
print(res_accurate)

'''
By avoid the substraction between very close values, we can increase the accuracy of the result. In this way, we choose x1 and x2 from one of the two
previous methods depending to the sign of b.
'''

#%%

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

#%%

#a)

def f_1(x):
    return x*(x-1)

def df_1(x, delta):
    return (f_1(x+delta)-f_1(x))/delta

df = df_1(1, 0.01)

print(f"The derivative on the function f at the point x = 1 is : {df}")

#Analytically, we have df(x) = 2*x-1 so df(1)=1. We have this little difference due to the substration of two very close values when
#we compute (f_1(x+delta)-f_1(x))


#%%

#b)

delta=[10**(-i) for i in range(2,16,2)] 
df_acc = [(i,df_1(1, i)) for i in delta] #Solutions for delta = = 10^{−4}, 10^{−6}, 10^{−8}, 10^{−10}, 10^{−12} and $10^{−14}$
print(f"Values of the integral for several values of delta = {df_acc}")
df_precision=[(x[0],abs(x[1]-1)) for x in df_acc] #Error of the solution compared to the analytics value
print(f"\nPrecision of the result for several values of delta = {df_precision}")

#We can clearly see that the accuracy of the result increase until delta = 10e-8 and for delta < 10e-8, the result become less and less accurate surlely due to the underflow limit

#%%

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

#%%


#a)
import numpy as np

def Semi_circle(x):
    return m.sqrt(1-x**2)

def Riemann(N, func):
    return sum((2/N)*func(i) for i in np.linspace(-1, 1, N))


N = 100

Int_Semi_Circle = Riemann(N, Semi_circle)
analytics_solution = np.pi/2

error_Int = 100*(analytics_solution-Int_Semi_Circle)/analytics_solution

print(f"Integral of a semi circle of radius 1 with 𝑁=100 = {Int_Semi_Circle}")
print(f"Computing error of this method = {round(error_Int,3)} %")

# We got a relativ erro of 1.1% compared to the analytics solution. The error is due to the choice of N who is too little to obtain a precise solution
#%%

#b)

import timeit


starttime = timeit.default_timer()
time = timeit.default_timer() - starttime

time_limit = 1
N = 100

while time<=time_limit:
    N=N*2
    Int_Semi = Riemann(N, Semi_circle)
    time = timeit.default_timer() - starttime
    print(f"I = {Int_Semi}, in {time} s")
    
error_Int = 100*(analytics_solution-Int_Semi)/analytics_solution
print(f"Final for N = {N}: I = {Int_Semi}, with an error = {round(error_Int,5)} %, in {time} s")

#Final for N = 3276800: I = 1.570795367263933, with an error = 6.10856383609798e-05 %, in 1.9885912999998254 s
#So we can considerably increase the precision of the integral by inscreasing the value of N. We got an error of 6*10e-5 for N = 10e6 in 1s.


#%%

#c)

starttime = timeit.default_timer()
time = timeit.default_timer() - starttime

N = int(10e6)
time_limit=60

while time<=time_limit:
    N=N*2
    Int_Semi = Riemann(N, Semi_circle)
    time = timeit.default_timer() - starttime
    print(f"I = {Int_Semi}, in {time} s")
    
error_Int = 100*(analytics_solution-Int_Semi)/analytics_solution
print(f"Final for N = {N}: I = {Int_Semi}, with an error = {error_Int} %, in {time} s")

#Final for N = 80000000: I = 1.5707963071571445, with an error = 1.2501781266065152e-06 %, in 83.34383220000018 s
#Between 1s and 1min, the error decrease from 6e-05 to 1.2e-06 so the gain compared to the compute time is not verry worth.

