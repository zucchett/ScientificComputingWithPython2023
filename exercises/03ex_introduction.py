import sys
import struct
import math

# 1. Number representation
print('1. NUMBER REPRESENTATION')


def convert_number(number, input_type, output_type):
    if input_type not in ('bin', 'dec', 'hex') or output_type not in ('bin', 'dec', 'hex'):
        raise ValueError("Invalid input or output representation")

    if input_type == 'bin':
        number = int(number, 2)
    elif input_type == 'hex':
        number = int(number, 16)

    if output_type == 'bin':
        return bin(number)[2:]  # Remove the '0b' prefix for binary representation
    elif output_type == 'hex':
        return hex(number)[2:]  # Remove the '0x' prefix for hexadecimal representation
    else:
        return str(number)  # Output type is decimal by default


# Test the function
input_number = '101010'  # Binary representation of 42
input_type = 'bin'
output_type = 'dec'
result = convert_number(input_number, input_type, output_type)
print(f"{input_number} in {input_type} is {result} in {output_type}")

input_number = '2A'  # Hexadecimal representation of 42
input_type = 'hex'
output_type = 'bin'
result = convert_number(input_number, input_type, output_type)
print(f"{input_number} in {input_type} is {result} in {output_type}")

# 2. 32-bit floating point number
print('2. 32-BIT FLOATING POINT NUMBER ')

import struct


def binary_to_single_precision_float(binary_str):
    if len(binary_str) != 32:
        raise ValueError("Input binary string must be 32 bits long")

    try:
        # Convert the binary string to a 32-bit integer
        int_value = int(binary_str, 2)

        # Pack the integer as a 32-bit single-precision float
        float_bytes = struct.pack('I', int_value)

        # Unpack the bytes as a float
        float_result = struct.unpack('f', float_bytes)[0]

        return float_result
    except struct.error:
        raise ValueError("Invalid binary representation")


# Test the function
binary_str = "110000101011000000000000"
try:
    float_value = binary_to_single_precision_float(binary_str)
    print(f"The binary {binary_str} is equivalent to the float {float_value:.6f}")
except ValueError as e:
    print(f"Error: {e}")

# 3. Underflow and overflow
print('3. UNDERFLOW AND  OVERFLOW')

underflow_limit = sys.float_info.min
overflow_limit = sys.float_info.max

print("Underflow Limit:", underflow_limit)
print("Overflow Limit:", overflow_limit)

# 4. Machine precision
print('4. MACHINE PRECISION')
machine_precision = 1.0

while 1.0 + machine_precision / 2.0 != 1.0:
    machine_precision /= 2.0

print("Machine Precision:", machine_precision)

# 5. Quadratic solution
print('5. QUADRATIC SOLUTION')


def quadratic_solver(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    else:
        return None  # No real solutions


# Compute the solutions for a=0.001, b=1000, and c=0.001
a = 0.001
b = 1000
c = 0.001

solutions = quadratic_solver(a, b, c)
print("Solutions:", solutions)


def quadratic_solver_reexpressed(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:
        root = math.sqrt(discriminant)
        x1 = (-2 * c) / (b + root)
        x2 = (-2 * c) / (b - root)
        return x1, x2
    else:
        return None  # No real solutions


# Compute the solutions for a=0.001, b=1000, and c=0.001 using the re-expressed formula
a = 0.001
b = 1000
c = 0.001

solutions_reexpressed = quadratic_solver_reexpressed(a, b, c)
print("Solutions (Re-expressed formula):", solutions_reexpressed)
# Compute the solutions using the original formula for comparison
solutions_original = quadratic_solver(a, b, c)
print("Solutions (Original formula):", solutions_original)


def quadratic_solver_accurate(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root = math.sqrt(discriminant)
        x1 = (-b - root) / (2 * a)
        x2 = (-b + root) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x1 = -b / (2 * a)
        return x1
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return complex(real_part, imaginary_part)


# Compute the solutions for a=0.001, b=1000, and c=0.001
a = 0.001
b = 1000
c = 0.001

solutions_accurate = quadratic_solver_accurate(a, b, c)
print("Solutions (Accurate):", solutions_accurate)

#  6. The derivative
print('6. THE DERIVATIVE')

print('result a')


def f(x):
    return x * (x - 1)


# Calculate the derivative at x = 1 using finite difference with delta = 1e-2
x = 1.0
delta = 1e-2

numerical_derivative = (f(x + delta) - f(x)) / delta

# Analytical derivative of f(x) at x = 1
analytical_derivative = 2 * x - 1

# Print both results
print("Numerical Derivative:", numerical_derivative)
print("Analytical Derivative:", analytical_derivative)

print('result b')


def f(x):
    return x * (x - 1)


def numerical_derivative(x, delta):
    return (f(x + delta) - f(x)) / delta


def analytical_derivative(x):
    return 2 * x - 1


# Point where we want to calculate the derivative
x = 1.0

# List of delta values to test
delta_values = [1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]

# Analytical derivative at x = 1
analytical_result = analytical_derivative(x)

# Calculate and compare numerical derivatives for different delta values
for delta in delta_values:
    numerical_result = numerical_derivative(x, delta)
    accuracy = abs(analytical_result - numerical_result)
    print(f"Delta = {delta:.0e}: Numerical Derivative = {numerical_result}, Accuracy = {accuracy:.2e}")

# 7. INTEGRAL OF A SEMICIRCLE
print('7. INTEGRAL OF A SEMICIRCLE')


def semicircle(x):
    return math.sqrt(1 - x ** 2)


N = 100  # Number of slices
h = 2 / N  # Width of each slice
integral = 0

for k in range(N):
    x_k = -1 + k * h
    y_k = semicircle(x_k)
    integral += h * y_k

# True value of the integral
true_value = math.pi / 2

# Compare the results
print("Approximate Value:", integral)
print("True Value:", true_value)
