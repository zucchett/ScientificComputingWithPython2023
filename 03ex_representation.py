######### Q1

def convert_number(number, input_type, output_type):
    if input_type not in ('bin', 'dec', 'hex') or output_type not in ('bin', 'dec', 'hex'):
        return "Invalid input or output type"

    if input_type == 'bin':
        number = int(number, 2)  # Convert binary to decimal
    elif input_type == 'dec':
        number = int(number)  # Convert decimal to decimal
    elif input_type == 'hex':
        number = int(number, 16)  # Convert hexadecimal to decimal

    if output_type == 'bin':
        return bin(number)[2:]  # Convert decimal to binary and remove '0b' prefix
    elif output_type == 'dec':
        return str(number)  # Keep it as decimal
    elif output_type == 'hex':
        return hex(number)[2:]  # Convert decimal to hexadecimal and remove '0x' prefix

    return "Conversion not supported"


number = input("Enter a number: ")
input_type = input("Enter the input type (bin, dec, or hex): ")
output_type = input("Enter the output type (bin, dec, or hex): ")

result = convert_number(number, input_type, output_type)
print(f"{number} ({input_type}) -> {result} ({output_type})")


######### Q2

import struct

f = int('00111101110011001100110011001100', 2)
a = struct.unpack('f', struct.pack('I', f))[0]
formatted_a = f"{a:.1f}"
print(formatted_a)

f = int('10111101110011001100110011001100', 2)
a = struct.unpack('f', struct.pack('I', f))[0]
formatted_a = f"{a:.1f}"
print(formatted_a)


######### Q3

underflow_limit = 1.0
overflow_limit = 1.0
while underflow_limit / 2 != 0.0:
    underflow_limit /= 2
while overflow_limit * 2 != float('inf'):
    overflow_limit *= 2
print("Approximate underflow limit:", underflow_limit)
print("Approximate overflow limit:", overflow_limit)


######### Q4

machine_precision = 1.0
while 1.0 + machine_precision != 1.0:
    machine_precision /= 2
print("Machine precision:", machine_precision)


######### Q5

import math
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return -x1, -x2
    else:
        return "No real roots"

a = 0.001
b = 1000
c = 0.001

# (a) Compute the solutions using the standard formula
solutions = solve_quadratic(a, b, c)
print("(a) Solutions using the standard formula:", solutions)

# (b) Re-express the formula and compute the solutions
# By multiplying both the numerator and denominator by -b ± sqrt(b^2 - 4ac)
numerator = [(-b + math.sqrt(b**2 - 4*a*c)), (-b - math.sqrt(b**2 - 4*a*c))]
denominator = 2 * a

solutions_b = [-num / denominator for num in numerator]
print("(b) Solutions using the re-expressed formula:", solutions_b)

# The solutions obtained in (a) and (b) should be the same, as (b) essentially simplifies the same formula.
# This is because multiplying both the numerator and denominator by the same value doesn't change the result.
# The solutions in (b) should be identical to those in (a).

##### (c)

import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        sqrt_discriminant = math.sqrt(discriminant)
        if b >= 0:
            x1 = (-b - sqrt_discriminant) / (2*a)
            x2 = (2*c) / (-b - sqrt_discriminant)
        else:
            x1 = (2*c) / (-b + sqrt_discriminant)
            x2 = (-b + sqrt_discriminant) / (2*a)
    elif discriminant == 0:
        x1 = -b / (2*a)
        x2 = x1
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        x1 = complex(real_part, imaginary_part)
        x2 = complex(real_part, -imaginary_part)

    return -x1, -x2

a = 0.001
b = 1000
c = 0.001

solutions = solve_quadratic(a, b, c)
print("Solutions using the accurate method:", solutions)




######### Q6

def f(x):
    return x * (x - 1)
def numerical_derivative(x, delta):
    return (f(x + delta) - f(x)) / delta
def analytical_derivative(x):
    return 2 * x - 1
x = 1.0 
delta_values = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]
for delta in delta_values:
    numerical_result = numerical_derivative(x, delta)
    analytical_result = analytical_derivative(x)
    error = abs(numerical_result - analytical_result)
    print(f"For delta = {delta}, Numerical derivative = {numerical_result}, Analytical derivative = {analytical_result}, Error = {error}")


######### Q7


import math
import timeit
def semicircle(x):
    return math.sqrt(1 - x**2)
def compute_integral(N):
    a = -1 
    b = 1   
    h = (b - a) / N  
    integral = 0
    for k in range(1, N + 1):
        xk = a + k * h
        yk = semicircle(xk)
        integral += h * yk
    return integral
true_value = math.pi / 2
# (a) Compute the integral with N = 100
N = 100
result = compute_integral(N)
error = abs(result - true_value)
print(f"For N = {N}, Computed Integral = {result}, True Value = {true_value}, Error = {error}")
# (b) Measure the time to compute the integral with various N values
N_values = [100, 1000, 10000, 100000]
for N in N_values:
    time_taken = timeit.timeit(lambda: compute_integral(N), number=1)
    print(f"For N = {N}, Time Taken = {time_taken:.6f} seconds")


