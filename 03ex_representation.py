# Exercise 1 (Number representation)

def convert(num, in_format, out_format):
  
  # Convert from decimal to other bases.
  if in_format == "dec":
    if out_format == "bin":
      return bin(num)[2:]
    elif out_format == "hex":
      return hex(num)[2:]
    else:
      raise ValueError("Unsupported output base: {}".format(out_format))
    
  # Convert from binary to other bases.
  elif in_format == "bin":
    if out_format == "dec":
      return int(num, 2)
    elif out_format == "hex":
      return hex(int(num, 2))[2:]
    else:
      raise ValueError("Unsupported output base: {}".format(out_format))
  
  # Convert from hexadecimal to other bases.
  elif in_format == "hex":
    if out_format == "dec":
      return int(num, 16)
    elif out_format == "bin":
      return bin(int(num, 16))[2:]
    else:
      raise ValueError("Unsupported output base: {}".format(out_format))
  else:
    raise ValueError("Unsupported input base: {}".format(in_format))

# Exercise 2 (32-bit floating point number)

def binary_to_floatingPoint(bin):
    if(len(bin) < 32):
      to_32bit = "0" * (32-len(bin))
      bin = to_32bit + bin
    if(len(bin) > 32):
      print("Maximum input size must be 32-bits.")
      return
    sign = int(bin[0])
    exponent = int(bin[1 : 9], 2)
    mantissa = int("1" + bin[9 : ], 2)
    return (-1) ** sign * mantissa / (1 << (len(bin) - 9 - (exponent - 127)))

binary = "110000101011000000000000"  
print(binary_to_floatingPoint(binary))


# Exercise 3 (Underflow and overflow)

def underflow_overflow_calc():
  
  underflow_limit = 1.0
  overflow_limit = 1.0

  while True:
    new_underflow_limit = underflow_limit / 2.0
    if(new_underflow_limit > float(0.0)):
      underflow_limit = new_underflow_limit
    else:
      break

  while True:
    new_overflow_limit = overflow_limit * 2.0
    if(new_overflow_limit < float('inf')):
      overflow_limit = new_overflow_limit
    else:
      break
      
  print("Approximate underflow limit:", underflow_limit)
  print("Approximate overflow limit:", overflow_limit)

underflow_overflow_calc()

# Exercise 4 (Machine precision)

def machine_precision_calc():
  
  underflow_limit = 1.0
  overflow_limit = 1.0

  n = 0
  while True:
    new_underflow_limit = underflow_limit - 1/pow(10,n)
    if(new_underflow_limit < underflow_limit):
      underflow_limit = new_underflow_limit
      n += 1
    else:
      break
  n = 0
  while True:
    new_overflow_limit = overflow_limit + 1/pow(10,n)
    if(new_overflow_limit > overflow_limit):
      overflow_limit = new_overflow_limit
      n += 1
    else:
      break
      
  print("Machine precision lower limit:", underflow_limit)
  print("Machine precision upper limit:", overflow_limit)

machine_precision_calc()

# Exercise 5 (Quadratic solution)

from math import sqrt

### (a)
def quadratic_formula(a, b, c):

  solution1 , solution2 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a) , (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
  return solution1, solution2

a = 0.001
b = 1000
c = 0.001

a_solutions = quadratic_formula(a, b, c)
# (-9.999894245993346e-07, -999999.999999)
print(a_solutions)
###

### (b)
def quadratic_formula_reexpressed(a, b, c):
  
  solution1 = -2 * c / (b + sqrt(b ** 2 - 4 * a * c))
  solution2 = -2 * c / (b - sqrt(b ** 2 - 4 * a * c))

  return solution1, solution2

b_solutions = quadratic_formula_reexpressed(a, b, c)
# (-1.000000000001e-06, -1000010.5755125057)
print(b_solutions)
# the re-expressed quadratic formula can introduce imprecision due to rounding errors when
# the discriminant (b ** 2 - 4 * a * c) is small.
###

### (c)
import math

def precise_quadratic_formula(a, b, c):
  
  discriminant = b ** 2 - 4 * a * c

  # if the discriminant is zero, then there is a single solution.
  if discriminant == 0:
    solution = (-b) / (2 * a)
    return solution, solution
  else:
    # if the discriminant is positive, then there are two real solutions.
    if discriminant > 0:
      solution1 = (-b + sqrt(discriminant)) / (2 * a)
      solution2 = (-b - sqrt(discriminant)) / (2 * a)
      return solution1, solution2
    else:
      # if the discriminant is negative, then there are two complex solutions.
      solution1 = (-b + 1j * sqrt(-discriminant)) / (2 * a)
      solution2 = (-b - 1j * sqrt(-discriminant)) / (2 * a)
      return solution1, solution2
###

# Exercise 6 (The derivative)

# function
def f(x):
    return x*(x-1)

# derivative at x=1
def derivative(f, delta):
    return (f(1+delta) - f(1)) / delta

print(derivative(f, 10**(-2)))
# the derivatives obtained analytically and computationally do not coincide because delta is too large.

print(derivative(f, 10**(-4)))
print(derivative(f, 10**(-6)))
print(derivative(f, 10**(-8)))
print(derivative(f, 10**(-10)))
print(derivative(f, 10**(-12)))
print(derivative(f, 10**(-14)))
# as delta decreases, the value of the derivative initially decreases, getting very close to the correct value, and then 
# increases and decreases again. this trend is due to the computational limit.

# Exercise 7 (Integral of a semicircle)

from math import sqrt
from math import pi
#a
def f(x):
    return sqrt(1 - x ** 2)

def integral(N):
    h = 2 / N
    sum = 0
    i =- 1
    while(i <= 1):
        sum += h * f(i)
        i += h
    return sum

print('Computed integral (N=100):',integral(100))
print('TrueValue - MyValue:',  "{:.2e}".format(abs(pi/2-integral(100))))

import time

#look for N s.t. time<1s
t = 0
n = 10000
while (t < 1.0):
    result = t
    start_time = time.process_time()
    integral(n)
    t = time.process_time() - start_time
    n += 10000

print('N (t<1s)', "{:.2e}".format(n-10000))
print('Computed integral (N=',"{:.2e}".format(n-10000),'):',integral(n-10000))
print('True Value - Calculated Value (N=',"{:.2e}".format(n-10000),':', "{:.2e}".format(abs(pi/2-integral(n-10000))))

#look for N s.t. time<1min
t = 0
n = 100000
while (t < 60.0):
    result = t
    start_time = time.process_time()
    integral(n)
    t = time.process_time() - start_time
    n += n
print('Computed integral (t=1min)', integral(n/2))
print('True Value - Calculated Value (t=1min)|:', "{:.2e}".format(abs(pi/2-integral(n/2))))
