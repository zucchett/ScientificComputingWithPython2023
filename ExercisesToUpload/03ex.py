#***************************Ex 1*******************************
def convert(x, to_representation):
    try:
        # Determine the input representation
        if to_representation == "dec":
            return int(x)  # Convert from any base (bin, hex, or dec) to decimal
        elif to_representation == "bin":
            return bin(x)  # Convert from any base to binary
        elif to_representation == "hex":
            return hex(x)  # Convert from any base to hexadecimal
        else:
            return "Invalid output representation"
    except ValueError:
        return "Invalid input value"
    
# Example usage:
input_value = 0x1A  # This can be in bin, dec, or hex
output_representation = "hex"  # Choose the desired output representation

# Convert and print in hexadecimal representation
result = convert(input_value, output_representation)
print(result)

output_representation = "bin"  # Choose the desired output representation

# Convert and print in binary representation
result = convert(input_value, output_representation)
print(result) 

output_representation = "dec"  # Choose the desired output representation

# Convert and print in decimal representation
result = convert(input_value, output_representation)
print(result)

#***************************Ex 2*******************************
import sys

def convertSinglePrecisionFloating(x):
    # Define the structure of a single-precision floating-point number:
    # - 1 bit for sign
    # - 8 bits for the exponent
    # - 23 bits for the mantissa (fraction)

    # Extract the sign bit (the leftmost bit)
    x_sign = x & 2**(x.bit_length() - 1)
    sign = x_sign >> (x.bit_length() - 1)

    # Extract the exponent (the next 8 bits)
    x_signless = x ^ x_sign  # Clear the sign bit
    exp = x_signless >> 16

    # Extract the mantissa (the remaining 23 bits)
    temp_exp = exp << 16
    mantissa = x_signless ^ temp_exp

    print("Sign bit: ", sign)
    print("Exponent bits: ", exp)
    print("Mantissa bits: ", mantissa)

    sign_rep = ''

    if sign == 1:
        sign_rep = '-'

    # Display the number in a human-readable format
    print("The number is: ", sign_rep, "1.", mantissa, "e^", exp)

convertSinglePrecisionFloating(0b110000101011000000000000)

#***************************Ex 3*******************************
def find_overflow_underflow_limits():
    # Initialize variables for underflow and overflow limits
    underflow_limit = 1.0
    overflow_limit = 1.0

    # Initialize temporary variables to store the limits once reached
    temp_u = 0
    temp_o = 0

    # Flags to track if underflow and overflow limits have been reached
    reach_u = False
    reach_o = False

    # Continue the loop until both underflow and overflow limits are reached
    while (not reach_u or not reach_o):
        # Double one variable to find the overflow limit
        if not reach_o:
            overflow_limit *= 2.0

        # Halve the other variable to find the underflow limit
        if not reach_u:
            underflow_limit /= 2.0

        # Check if we have exceeded the underflow or overflow limits (within a factor of 2)
        if underflow_limit == 0.0 and not reach_u:
            reach_u = True
        if overflow_limit == float("inf") and not reach_o:
            reach_o = True

        # If not reached, store the current values of underflow and overflow limits
        if not reach_u:
            temp_u = underflow_limit
        if not reach_o:
            temp_o = overflow_limit

    # Print the approximate overflow and underflow limits
    print("Overflow limit (approximately):", temp_o)
    print("Underflow limit (approximately):", temp_u)

find_overflow_underflow_limits()

#***************************Ex 4*******************************
def machine_precision():
    # Initialize a value that will decrease and an increasingly smaller value
    increasingly_smaller_value = 1.0
    current_value = 100.0
    temp_value = current_value
    temp_smaller_value = increasingly_smaller_value

    # Continue the loop indefinitely until the precision limit is reached
    while True:
        # Decrease the current value by the increasingly smaller value
        current_value -= increasingly_smaller_value

        # Halve the increasingly smaller value
        increasingly_smaller_value /= 2

        # Check if the current value has stopped changing
        if temp_value == current_value:
            break

        # Update the temporary values for comparison
        temp_value = current_value
        temp_smaller_value = increasingly_smaller_value

    # Print the approximate machine precision
    print("Machine precision (approximately):", temp_smaller_value)

machine_precision()

#***************************Ex 5*******************************
import math

# Function to find the quadratic solutions using the standard formula
def quadratic_solution(a, b, c):
    # Calculate the discriminant
    determinant = math.sqrt(b**2 - 4 * a * c)
    
    # Calculate the two solutions using the standard formula
    numerator_one = -b + determinant
    numerator_two = -b - determinant
    denominator = 2 * a
    
    x1 = numerator_one / denominator
    x2 = numerator_two / denominator

    return x1, x2

# Function to find the quadratic solutions with multiplication optimization
def quadratic_solution_two(a, b, c):
    # Calculate the discriminant
    determinant = math.sqrt(b**2 - 4 * a * c)
    
    # Calculate the two solutions using the optimized formula
    numerator_one = -b + determinant
    numerator_two = -b - determinant
    denominator = 2 * a
    
    numerator_mul = numerator_one * numerator_two

    denominator_one = denominator * numerator_two
    denominator_two = denominator * numerator_one

    x1 = numerator_mul / denominator_one
    x2 = numerator_mul / denominator_two

    return x1, x2

# Function to find the accurate quadratic solutions considering different cases
def accurate_quadratic_solution(a, b, c):
    # Calculate the discriminant
    determinant = math.sqrt(b**2 - 4 * a * c)
    
    if b >= 0:
        # Calculate the two solutions when b is non-negative
        x1 = (-b - determinant) / (2 * a)
        x2 = (2 * c) / (-b - determinant)
    else:
        # Calculate the two solutions when b is negative
        x1 = (2 * c) / (-b + determinant)
        x2 = (-b + determinant) / (2 * a)

    return x1, x2

x1, x2 = quadratic_solution(0.001,1000,0.001)
print("Quadratic solution standard: ")
print ("x1 = ", x1)
print ("x2 = ", x2)

x1, x2 = quadratic_solution_two(0.001,1000,0.001)
print("Quadratic solution with multiplication: ")
print ("x1 = ", x1)
print ("x2 = ", x2)

x1, x2 = accurate_quadratic_solution(0.001,1000,0.001)
print("Accurate quadratic solution: ")
print ("x1 = ", x1)
print ("x2 = ", x2)

#***************************Ex 6*******************************
# Define the function f(x) = x * (x - 1)
def f(x):
    return x * (x - 1)

# Define a function to numerically calculate the derivative at a given point x using a small delta
def numerical_derivative(x, delta):
    # Calculate the derivative using the forward difference formula
    approximate_derivative = (f(x + delta) - f(x)) / delta
    return approximate_derivative

# Set the value of x where you want to calculate the derivative
x = 1

# The true derivative of f(x) = x(x-1) at x = 1 is known to be 1
true_derivative = 1

# List of delta values to use for approximation
deltas = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]

# Iterate over the different delta values and calculate the approximate derivative
for delta in deltas:
    approx_derivative = numerical_derivative(x, delta)
    # Print the result with delta and the approximate derivative
    print(f"Delta = {delta}: Approximate Derivative = {approx_derivative}")

#***************************Ex 7*******************************
import math
import timeit

# Define the semicircle function
def semicircle(x):
    return math.sqrt(1 - x**2)

# Define a function to compute the Riemann integral
def riemann_integral(N):
    h = 2 / N  # Calculate the width of each subinterval
    integral = 0

    # Iterate over subintervals and calculate the area using Riemann sums
    for k in range(1, N + 1):
        x_k = -1 + k * h  # Calculate the x-coordinate of the sample point
        y_k = semicircle(x_k)  # Calculate the y-coordinate using the semicircle function
        integral += h * y_k  # Add the area of the subrectangle to the integral

    return integral

# True value of the integral (known value for semicircle)
true_value = math.pi / 2

# (a) Compute the integral with N = 100
N = 100
result_N100 = riemann_integral(N)
error_N100 = abs(result_N100 - true_value)

# Print the result and the error
print(f"(a) Result with N = 100: {result_N100}, Error: {error_N100}")

# (b) Measure the time for different values of N

# Function to measure the time taken to compute the Riemann integral for a given N
def time_integral(N):
    return timeit.timeit(lambda: riemann_integral(N), number=1)

# Function to find the maximum N that can be computed within a specified time
def timer_integral(N, seconds):
    while time_integral(N) < seconds:
        N *= 2  # Double N to see if it fits within the time constraint
    while time_integral(N) > seconds:
        N *= 0.9  # Reduce N by a factor to approach the time constraint
        N = int(N)  # Ensure N remains an integer
    return N, time_integral(N)

N, time_taken = timer_integral(100, 1)
print(f"(b) Maximum N within 1 second: {N}, Time taken: {time_taken} seconds")

N, time_taken = timer_integral(100, 60)
print(f"(b) Maximum N within 1 second: {N}, Time taken: {time_taken} seconds")