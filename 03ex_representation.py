print("Exercise 1")

'''
1. Number representation

Write a function that converts integer numbers among the bin, dec, and hex representations (bin<->dec<->hex). Determine the input type in the function, and pass another argument to choose the output representation.

'''

def convert_integer(x):
	print( bin(x), int(x), hex(x))

x= 23
convert_integer(x)

print("Exercise 2")
'''
2. 32-bit floating point number

Write a function that converts a 32 bit binary string (for example, 110000101011000000000000) into a single precision floating point in decimal representation. Interpret the various bits as sign, fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations.

'''

a =110000101011000000000000

def convert_2_float(a):
	
	print(float(a))

	s = 
	x = pow(-1,s)*(1 +f)*pow(2,e-bias)
		
convert_2_float(a)

print("Exercise 3")
'''
3. Underflow and overflow

Write a program to determine the approximate underflow and overflow limits (within a factor of 2) for floating point numbers on your computer.

Hint: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed the under/over-flow limits.

'''
def 
	under_limit,over_limit = 1

	while True:
		under_value = under_limit /2
		if under_value ==0.0:
			break
		else:
			under_limit = under_value

	while True:
		over_value = over_limit *2
		if over_value ==0.0:
			break
		else:
			over_limit = over_value
	print
print("Exercise 4")

'''
4. Machine precision

Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.

Hint: define a new variable by adding an increasingly smaller value and check when the addition starts to have no effect on the number.

'''


print("Exercise 5")

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


print("Exercise 6")

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


print("Exercise 7")

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
