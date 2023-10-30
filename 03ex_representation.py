#1)Number representation
print("Program 1 begins")
def convert_number(input_number, output_base):
    # Determine the input base from the input_number format
    if input_number.startswith("0b"):
        input_base = 2
        input_number = input_number[2:]  # Remove the "0b" prefix
    elif input_number.startswith("0x"):
        input_base = 16
        input_number = input_number[2:]  # Remove the "0x" prefix
    else:
        input_base = 10  # Default to decimal

    # Ensure that the input is in a valid format
    try:
        input_number = int(input_number, input_base)
    except ValueError:
        return "Invalid input number format"

    # Convert to the desired output representation
    if output_base == 2:
        output_number = bin(input_number)
    elif output_base == 10:
        output_number = str(input_number)
    elif output_base == 16:
        output_number = hex(input_number)
    else:
        return "Invalid output base"

    return output_number

# Get input from the user
input_number = input("Enter an integer number (in bin(0b), dec, or hex(0x) format): ")
output_base = int(input("Enter the desired output base (2 for binary, 10 for decimal, 16 for hexadecimal): "))

result = convert_number(input_number, output_base)
print("Converted number:", result)

print("Program 1 ends\n")

#2)32 bit floating point number
print("Program 2 begins")
import struct

def binary_string_to_float(binary_str):
    # Ensure the binary string is 32 characters long
    if len(binary_str) != 32:
        print("Invalid input: Binary string must be 32 characters long.")
        return None

    try:
        # Convert binary string to a 32-bit integer
        int_value = int(binary_str, 2)
    except ValueError:
        print("Invalid input: Binary string contains non-binary characters.")
        return None

    # Pack the integer into a 4-byte binary representation and unpack it as a float
    float_value = struct.unpack('f', struct.pack('I', int_value))[0]

    return float_value

# Example usage with both valid and invalid input:
binary_str1 = "01000000101011000000000000000000"  # Valid 32-bit binary string
binary_str2 = "110000101011000000000000"  # Invalid: Too short
binary_str3 = "01000200101011000000000000000000"  # Invalid: Contains non-binary characters

float_result1 = binary_string_to_float(binary_str1)
print("Single-precision float 1:", float_result1)

float_result2 = binary_string_to_float(binary_str2)
if float_result2 is not None:
    print("Single-precision float 2:", float_result2)

float_result3 = binary_string_to_float(binary_str3)
if float_result3 is not None:
    print("Single-precision float 3:", float_result3)

print("Program 2 ends\n")
#3)Underflow and Overflow
print("Program 3 begins")
import sys

# Initialize two variables
underflow_limit = 1.0
overflow_limit = 1.0

# Define a factor for halving and doubling
factor = 2.0

# Find the underflow limit
while underflow_limit / factor != 0.0:
    underflow_limit /= factor

# Find the overflow limit
while overflow_limit * factor != float('inf'):
    overflow_limit *= factor

# Print the results
print(f"Approximate underflow limit: {underflow_limit}")
print(f"Approximate overflow limit: {overflow_limit}")
print("Program 3 ends\n")
#4)Machine Precision
print("Program 4 begins")
machine_precision = 1.0

while 1.0 + machine_precision != 1.0:
    machine_precision /= 2

print(f"Machine Precision: {machine_precision}")

print("Program 4 ends\n")

#5)Quadratic solution
print("Program 5 begins")
import math

def quadratic_solver(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        # Two real and distinct solutions
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        # One real solution (a repeated root)
        root1 = -b / (2 * a)
        return root1,
    else:
        # Complex solutions
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        return (real_part + imaginary_part * 1j, real_part - imaginary_part * 1j)

# (a) Compute the solutions for a=0.001, b=1000, and c=0.001
solutions_a = quadratic_solver(0.001, 1000, 0.001)
print("Solutions (a):", solutions_a)

# (b) Re-express the standard solution formula and compute solutions
def modified_quadratic_solver(a, b, c):
    numerator_plus = -b + math.sqrt(b ** 2 - 4 * a * c)
    numerator_minus = -b - math.sqrt(b ** 2 - 4 * a * c)
    denominator = 2 * a
    root1 = numerator_plus / denominator
    root2 = numerator_minus / denominator
    return root1, root2

solutions_b = modified_quadratic_solver(0.001, 1000, 0.001)
print("Solutions (b):", solutions_b)

# Explanation for (b): The solutions obtained in (a) and (b) are the same because the formula in (b) is mathematically equivalent to the standard formula in (a). Multiplying the numerator and denominator by the same value does not change the result.

# (c) Function to compute roots accurately in all cases
def accurate_quadratic_solver(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Infinite solutions (all real numbers)"
            else:
                return "No real solutions"
        else:
            return -c / b,  # One real solution

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b - math.sqrt(discriminant)) / (2 * a)
        root2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root1 = -b / (2 * a)
        return root1,
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        return (real_part + imaginary_part * 1j, real_part - imaginary_part * 1j)

# Example usage for (c):
solutions_c = accurate_quadratic_solver(0.001, 1000, 0.001)
print("Solutions (c):", solutions_c)

print("Program 5 ends\n")
#6)The Derivative
print("Program 6 begins")
def f(x):
    return x * (x - 1)

def calculate_derivative_numerical(x, delta):
    # Numerical approximation of the derivative
    derivative_approx = (f(x + delta) - f(x)) / delta
    return derivative_approx

def calculate_derivative_analytical(x):
    # Analytical derivative of f(x) = x(x - 1)
    derivative_analytical = 2 * x - 1
    return derivative_analytical

x = 1.0
delta = 1e-2  # Delta value

# Calculate the derivative using numerical approximation
derivative_numerical = calculate_derivative_numerical(x, delta)

# Calculate the derivative using the analytical method
derivative_analytical = calculate_derivative_analytical(x)

# Print the results
print(f"Numerical derivative (delta={delta}): {derivative_numerical}")
print(f"Analytical derivative: {derivative_analytical}")

# Calculate and print the absolute error
absolute_error = abs(derivative_analytical - derivative_numerical)
print(f"Absolute error: {absolute_error}")

#The numerical and analytical derivatives won't agree perfectly due to the approximation introduced by the finite delta value (1e-2).
# The smaller the delta, the closer the numerical approximation will be to the analytical value. Numerical differentiation introduces
#truncation error, which decreases as the delta value approaches zero.

#b)With different delta
def f(x):
    return x * (x - 1)

def calculate_derivative_numerical(x, delta):
    # Numerical approximation of the derivative
    derivative_approx = (f(x + delta) - f(x)) / delta
    return derivative_approx

def calculate_derivative_analytical(x):
    # Analytical derivative of f(x) = x(x - 1)
    derivative_analytical = 2 * x - 1
    return derivative_analytical

x = 1.0
delta_values = [1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]

for delta in delta_values:
    # Calculate the derivative using numerical approximation
    derivative_numerical = calculate_derivative_numerical(x, delta)

    # Calculate the derivative using the analytical method
    derivative_analytical = calculate_derivative_analytical(x)

    # Calculate and print the absolute error
    absolute_error = abs(derivative_analytical - derivative_numerical)
    print(f"Delta = {delta}: Numerical derivative = {derivative_numerical}, Analytical derivative = {derivative_analytical}, Absolute error = {absolute_error}")

print("Program 6 ends\n")
#7)Integral of a Semicircle
print("Program 7 begins")
import math

def semicircle_function(x):
    return math.sqrt(1 - x**2)

def riemann_integral_semicircle(N):
    h = 2 / N
    integral = 0

    for k in range(N):
        xk = -1 + k * h
        yk = semicircle_function(xk)
        integral += yk * h

    return integral

# True value of the integral
true_value = math.pi / 2

# Calculate the integral with N=100
N = 100
approximate_value = riemann_integral_semicircle(N)

# Print the results
print(f"Approximate integral with N={N}: {approximate_value}")
print(f"True value of the integral: {true_value}")
print(f"Absolute error: {abs(approximate_value - true_value)}")

#b)Value of N
import math
import timeit

def semicircle_function(x):
    return math.sqrt(1 - x**2)

def riemann_integral_semicircle(N):
    h = 2 / N
    integral = 0

    for k in range(N):
        xk = -1 + k * h
        yk = semicircle_function(xk)
        integral += yk * h

    return integral

# Set a target time for computation (1 second)
target_time = 1.0
N = 1  # Initial N
elapsed_time = 0

while elapsed_time < target_time:
    N *= 2
    time_required = timeit.timeit(lambda: riemann_integral_semicircle(N), number=1)
    elapsed_time = time_required

# Print the result for N that fits within one second
print(f"Maximum N for computation in < 1 second: {N}")
print(f"Elapsed time for N={N}: {elapsed_time} seconds")

# Measure the time for one minute
N = 1
elapsed_time = 0
target_time = 60.0  # 1 minute

while elapsed_time < target_time:
    N *= 2
    time_required = timeit.timeit(lambda: riemann_integral_semicircle(N), number=1)
    elapsed_time = time_required

# Print the result for N that fits within one minute
print(f"Maximum N for computation in < 1 minute: {N}")
print(f"Elapsed time for N={N}: {elapsed_time} seconds")
print("Program 7 ends\n")


