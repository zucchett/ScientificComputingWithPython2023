import sys
import math
import struct
import numpy as np
import timeit

#Exercise 1
print('Exercise 1')

def convert(stringa, integer):
    
    if stringa == 'bin':
        stringa = 'binary'
        num = bin(integer)
    if stringa == 'hex':
        stringa = 'hexadecimal'
        num = hex(integer)
    if stringa == 'dec':
        stringa = 'decimal'
        num = int(integer)
        
    print('Number', integer, 'changed to', stringa,':', num)
    
convert('bin', 7)
convert('hex', 7)
convert('dec', 7)
print('')

#Exercise 2
print('Exercise 2')

def bin_to_float(b):
    
    res = [int(x) for x in str(b)]
    list(map(int, res))
    res = res[::-1]
    
    num = 0
    i = 0 
    while i < len(res)-1:
        num = num + (res[i]*(2**i))
        i = i + 1
        
    num1 = num*((-1)**res[len(res)-1])
    
    return num1

print('110000101011000000000000 converted to float is: ', bin_to_float(110000101011000000000000))

print('')

#Exercise 3
print('Exercise 3')

def overflow(j):
    while True:
        temp1 = j
        j = j*2
        if (j == float('inf')):
            break
    return temp1 

def underflow(t):
    while t>0:
        temp2 = t
        t = t/2
    return temp2

print('Overflow limit:', overflow(1.0))
print('Underflow limit:', underflow(1))

print('')

#Exercise 4
print('Exercise 4') 

def prec(x):
    done = True
    temp = 1
    while done:
        temp = temp/2
        n = x
        x = x + temp
        if x == n:
            done = False
    return temp

print('Machine precision is: ', prec(11))
print('')

#Exercise 5
print('Exercise 5')

def QuadraticSolution(a, b, c):
    x1 = (-b+(b**2-4*a*c)**(1/2))/(2*a)
    x2 = (-b-(b**2-4*a*c)**(1/2))/(2*a)
    return x1, x2

print('x1 and x2:',QuadraticSolution(00.1, 1000, 0.001))

def QuadraticSolution2(a, b, c):
    d1 = (-b+(b**2-4*a*c)**(1/2))
    d2 = (-b-(b**2-4*a*c)**(1/2))
    x1 = (d1*d1)/((2*a)*d1)
    x2 = (d2*d2)/((2*a)*d2)
    return x1, x2

print('x1* and x2*:',QuadraticSolution2(00.1, 1000, 0.001))
print('')

'''
The solutions from both methods are similar but the second one is less
accurate and that involves a small rounding error.
'''
print('')

#Exercise 6
print('Exercise 6')

def f(x):
    return x*(x-1)

def der(f, x, delta):
    result = ((f(x + delta) - f(x))/ delta)
    return result

def analytic_der(x):
    return 2*x-1

print('Value of the derative using the function:')
print('10^-2 ->', der(f, 1, delta = 10**(-2)))
print('10^-4 ->', der(f, 1, delta = 10**(-4)))
print('10^-6 ->', der(f, 1, delta = 10**(-6)))
print('10^-8 ->', der(f, 1, delta = 10**(-8)))
print('10^-10 ->', der(f, 1, delta = 10**(-10)))
print('10^-12 ->', der(f, 1, delta = 10**(-12)))
print('10^-14 ->', der(f, 1, delta = 10**(-14)))
print('Value of the derative analytically:', analytic_der(1))

print('The value of the derivative grows exponentially closer to the analytical value with smaller delta')
print('')

#Exercise 7
print('Exercise 7')

def semicircle(y):
    
    f = (1 - y**2)**(1/2)
    return f

def integral(function, N):
    
    h = 2/N
    I = 0
    k = 1
    while k <N+1:
        I = I + h*function(k*h - 1)
        k += 1
    return I

print('The result is:',integral(semicircle, 100), 'which is similar to the true value:', math.pi/2)
print('Percentage of similarity:', (integral(semicircle, 100)/(math.pi/2))*100,'%')

def N_increase(): 
    i = 100
    time = 0
    while time < 1:
        i += 1000000
        time = timeit.timeit(lambda: integral(semicircle, i), number=1)       
    return i, time
    

def N_60(N):
    t_init = timeit.default_timer()
    result = integral(semicircle, N*60)
    t_end = timeit.default_timer()

    return result

temp = N_increase()
print('Maximum increase of N while staying under',math.trunc(temp[1]), 'second is:', temp[0])
N2 = N_60(temp[0])
print('Result after 1 minute of computing:',N2,'with a percentage of similarity:',(N2/(math.pi/2))*100,'%')



