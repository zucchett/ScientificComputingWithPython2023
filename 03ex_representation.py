print("\nExercise 1")

'''
1. Number representation

Write a function that converts integer numbers among the bin, dec, and hex representations (bin<->dec<->hex). Determine the input type in the function, and pass another argument to choose the output representation.

'''

def convert_integer(x):
	print( "Binary:",bin(x), ", Decimal:",int(x), "Hexadecimal:",hex(x))

x= 23
convert_integer(x)


print("\nExercise 2")
'''
2. 32-bit floating point number

Write a function that converts a 32 bit binary string (for example, 110000101011000000000000) into a single precision floating point in decimal representation. Interpret the various bits as sign, fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations.

'''
a ="11000000101100000000000000000000"
print("Binary string",a)
print("Length of binary string:",len(a))
def convert_2_float(a):
	# xfloat = (-1)^s * 1.f * 2^(e-bias)
	xf = (-1.0)**int(a[0])
	# compute 1.f = 1 + m(n- 1)/2 + m(n- 2)/4 + ...
	f1 = 1.0
	for i in range(9, len(a)-1):
		f1 = f1 + int(a[i])/(2**(i-8))
	exp = int(a[1 : 9],2)
	return xf*f1*2**(exp-127)

		
print("The float precision value:",convert_2_float(a))

print("\nExercise 3")
'''
3. Underflow and overflow

Write a program to determine the approximate underflow and overflow limits (within a factor of 2) for floating point numbers on your computer.

Hint: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed the under/over-flow limits.

'''
#underflow
x = float(1.0)
x_prev = float(x)
i = 0
while x != 0:
	x_prev = x
	x = x * 2**(-i) #halving
	i = i + 1
print("Underflow:",x_prev)

#overflow 
x = float(1.0)
x_prev = float(0)
i = 1
while x < float('inf'):
	x_prev = x
	x = x * 2**(i) #doubling
	i = i + 1

print ("Overflow:",x_prev)

print("\nExercise 4")

'''
4. Machine precision

Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.

Hint: define a new variable by adding an increasingly smaller value and check when the addition starts to have no effect on the number.

'''


def machine_precision():
    epsilon = 1.0

    while 1.0 + epsilon != 1.0:
        epsilon /= 2.0

    return epsilon

print(f"The machine precision is approximately {machine_precision()}")

print("\nExercise 5")

'''
5. Quadratic solution

Write a function that takes in input three parameters 𝑎
, 𝑏 and 𝑐 and prints out the two solutions to the quadratic equation 𝑎𝑥2+𝑏𝑥+𝑐=0 using the standard formula:
𝑥=−𝑏±𝑏2−4𝑎𝑐⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯√2𝑎

(a) use the function to compute the solution for 𝑎=0.001
, 𝑏=1000 and 𝑐=0.001

(b) re-express the standard solution formula by multiplying the numerator and the denominator by −𝑏∓𝑏2−4𝑎𝑐⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯√
and again find the solution for 𝑎=0.001, 𝑏=1000 and 𝑐=0.001

. How does it compare with what has been previously obtained, and why? (add the answer to a Python comment)

(c) write a function that computes the roots of a quadratic equation accurately in all cases
'''

a = 0.001
b = 1000
c = 0.001

print("\n a)\n")
from math import sqrt
# Compute x1 and x2 with standard fnction
x1 = (-b - sqrt(b**2 - 4* a*c))/(2*a)
x2 = (-b + sqrt(b**2 - 4* a*c))/(2*a)
print("x1:",x1)
print("x2:",x2)


print("\n b)\n")
x1 = (-b - sqrt(b**2 - 4* a*c))*(-b + sqrt(b**2 - 4* a*c))/(2*a*(-b - sqrt(b**2 - 4* a*c)))
x2 = (-b + sqrt(b**2 - 4* a*c))*(-b - sqrt(b**2 - 4* a*c))/(2*a*(-b + sqrt(b**2 - 4* a*c)))
print("x1:",x1)
print("x2:",x2)
print("After multiplication, x2 shows  -999999.9999990001 instead of -999999.999999 ")



print("\n c)\n")
import numpy

# After importing numpy, the longdouble type allow to make calculation with 128 bit
a_ext = numpy.longdouble(0.001)
b_ext = numpy.longdouble(1000)
c_ext = numpy.longdouble(0.001)
x1_ext = (-b_ext - sqrt(b_ext**2 - 4* a_ext*c_ext))/(2*a_ext)
x2_ext = (-b_ext + sqrt(b_ext**2 - 4* a_ext*c_ext))/(2*a_ext)
print(x1_ext)
print(x2_ext)

print("\nExercise 6")

'''
6. The derivative

Write a program that implements the function 𝑓(𝑥)=𝑥(𝑥−1)

(a) Calculate the derivative of the function at the point 𝑥=1

using the derivative definition:

d𝑓d𝑥=lim𝛿→0𝑓(𝑥+𝛿)−𝑓(𝑥)𝛿

with 𝛿=10−2

. Calculate the true value of the same derivative analytically and compare it with the answer your program gives. The two will not agree perfectly. Why?

(b) Repeat the calculation for 𝛿=10−4,10−6,10−8,10−10,10−12
and 10−14. How does the accuracy scale with 𝛿?
'''
def f(x):
    return (x*(x-1))

# define function to compute derviate
def der(x, d):
	return (f(x+d) - f(x))/d

print("\n a)\n")
x = 1
d = pow(10,-2)
print(der(x, d))

print("\n b)\n")
for i in range(6):
	d = d*10**(-2)
	print("When delta: ","{:.2e}".format(d), ", the result is:",der(x, d))

print("\nExercise 7")

'''
7. Integral of a semicircle

Consider the integral of the semicircle of radius 1:
𝐼=∫1−1(⎯⎯√1−𝑥2)d𝑥
which is known to be 𝐼=𝜋2=1.57079632679...

.

Alternatively we can use the Riemann definition of the integral:
𝐼=lim𝑁→∞∑𝑘=1𝑁ℎ𝑦𝑘

with ℎ=2/𝑁
the width of each of the 𝑁 slices the domain is divided into and where 𝑦𝑘 is the value of the function at the 𝑘−

th slice.

(a) Write a program to compute the integral with 𝑁=100

. How does the result compare to the true value?

(b) How much can 𝑁
be increased if the computation needs to be run in less than a second? What is the gain in running it for 1 minute? Use timeit to measure the time.
'''

print("\n a)\n")
N = 100
I = 0
for i in range(1, N+1, 1):
	x = -1 + 2*i/(N) 
	I = I + 2/N * sqrt (1 - x**2)
print("I:",I)
print("Result difference is:", numpy.pi/2-I)
# the difference is 0.0016620712456461018

print("\n b)\n")

import timeit
starting_time = timeit.default_timer()
N = 10**6
I = 0
for i in range(1, N+1, 1):
	x = -1 + 2*i/(N) 
	I = I + 2/N * sqrt (1 - x**2)
print("I:",I)
I1 = I

print("Time difference :", timeit.default_timer() - starting_time, " seconds")

starting_time = timeit.default_timer()
N = 10**8
I = 0
for i in range(1, N+1, 1):
	x = -1 + 2*i/(N) 
	I = I + 2/N * sqrt (1 - x**2)
print("I:",I)
#trying N=10^8 for the limit to run for 1 min
print("Time difference :", timeit.default_timer() - starting_time, " seconds")

##################





