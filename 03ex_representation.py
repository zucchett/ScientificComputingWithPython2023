#---------------------------------------------------------------------------------------------------------------
#exercise3 part1.Number representation


# Function to convert binary to decimal
def bin_to_dec(input_number):
    # Convert the input_number binary number (input_number) to a decimal integer (base 2)
    decimal_string = str(int(input_number, 2))
    return decimal_string

# Function to convert binary to hexadecimal
def bin_to_hex(input_number):
    # Convert the binary input_number (input_number) to a hexadecimal string (base 16)
    # 'int(input_number, 2)' converts binary to decimal, and 'format(..., 'x')' converts decimal to hexadecimal.
    hexadecimal_string = format(int(input_number, 2), 'x')
    return hexadecimal_string

# Function to convert decimal to binary
def dec_to_bin(input_number):
    # Convert an integer to a binary string with a fixed width of 8 characters
    # making sure the binary representation is always 8 characters long
    # if needed, extended with zeros at the beginning.
    binary_string = format(int(input_number), '08b')
    return binary_string

# Function to convert decimal to hexadecimal
def dec_to_hex(input_number):
    # Convert an integer to a hexadecimal string and remove the '0x' prefix
    # The code format(int(input_number), 'x') removes the '0x' prefix
    # because the 'x' format specifier does not include the '0x' prefix
    hexadecimal_string = format(int(input_number), 'x')
    return hexadecimal_string

# Function to convert hexadecimal to binary
def hex_to_bin(input_number):
    # Convert a hexadecimal string to a binary string without the '0b' prefix
    binary_string = format(int(input_number, 16), 'b')
    return binary_string

# Function to convert hexadecimal to decimal
def hex_to_dec(input_number):
    # Convert the input_number hexadecimal string to a decimal integer
    decimal_number = int(input_number, 16)
    # Convert the decimal integer back to a string for consistency
    decimal_string = str(decimal_number)
    return decimal_string

def convert_number(input_number, output_format):
    conversion_functions = {
        ('bin', 'dec'): bin_to_dec,
        ('bin', 'hex'): bin_to_hex,
        ('dec', 'bin'): dec_to_bin,
        ('dec', 'hex'): dec_to_hex,
        ('hex', 'bin'): hex_to_bin,
        ('hex', 'dec'): hex_to_dec,
    }

    if (input_format, output_format) in conversion_functions:
        return conversion_functions[(input_format, output_format)](input_number)
    else:
        return "Conversion not supported."

# Example usage:
input_number = input("Enter number: ")
input_format = input("Enter number format: ")
output_format = input("Enter output format: ")
result = convert_number(input_number, output_format)
print(f"{input_number} in {output_format} is: {result}")

#---------------------------------------------------------------------------------------------------------------
#exercise3 part two.32-bit floating point number


def check_input_length(binary_str):
    return len(binary_str) == 32

def convert_binary_to_float(binary_str):
    if len(binary_str) != 32:      # Check if the input is not 32 bits long
        print("Input must be maximum 32 bits.")
        return None

    # Check if the number is positive (0) or negative (1)
    sign = int(binary_str[0])  # 0 for positive, 1 for negative

    # Set the value to zero
    value = 0
    # Extract the exponent bits (bits 1 to 8)
    for i in range(1, 9):
        bit_value = int(binary_str[i])
        # Combine the bit_value with the current value
        value = (value * 2) + bit_value
    # Convert the binary value to its decimal value
    value = int(value)

    # Remove (bits 9 to 31) of the fraction
    fraction = binary_str[9:32]

    # set the value to determine the real exponent as per IEEE 754
    real_exponent = value - 127

    # Calculate the mantissa (the actual value)
    mantissa = 1.0
    for i in range(1, 24):  # There are 23 bits in the fraction part
        if i <= len(fraction) and fraction[i - 1] == '1':
            mantissa += 1 / (2 ** i)

    # Calculate the final decimal value based on sign, exponent, and mantissa
    decimal_value = (-1 if sign == 1 else 1) * (2 ** real_exponent) * mantissa
    return decimal_value

# Example usage:
binary_str = "110000101011000000000000"
if check_input_length(binary_str):
    decimal_float = convert_binary_to_float(binary_str)
    print(decimal_float)
else:
    print("Input must be maximum 32 bits.")

#---------------------------------------------------------------------------------------------------------------
# exercise 3 part three.underflow and overflow


# set variables with 1.0
variable1 = 1.0  #underflow
variable2 = 1.0   #overflow

# underflow limit
# minimize the smallest positive number (underflow limit)
while variable1 / 2.0 != 0.0:
    variable1 /= 2.0

# overflow limit
# minimize the largest positive number
while variable2 * 2.0 != float('inf'):
    variable2 *= 2.0

# Print the results
print("Underflow Limit is:", variable1)
print("Overflow Limit is:", variable2)

#---------------------------------------------------------------------------------------------------------------
# exercise 3 part four. Machine precision


# Set machine precision to 1.0
# smallest positive number that can be represented in the floating-point format
# without affecting the result when added to 1.0. Starting with 1.0
machine_precision = 1.0

# Keep making the machine precision smaller and smaller
# by dividing it by 2 until it's so small that adding it to 1.0
# has no effect on the result.
while 1.0 + machine_precision != 1.0:
    machine_precision /= 2

# Print the machine precision
print("Machine Precision: ", machine_precision)

#---------------------------------------------------------------------------------------------------------------
# exercise 3 part five.Quadratic solution


# Function to calculate the square
def sqrt(n):
    if n < 0:
        return "Negative! No solutions"
    elif n == 0:
        return 0
    else:
        return pow(n, 0.5)

# Function to solve the quadratic equation
def quadratic_solver(a, b, c):
    # Calculate the discriminant
    discriminant = pow(b, 2) - 4 * a * c

    # Managing Special Situations
    if a == 0:
        if b == 0:
            if c == 0:
                return "answer is infinte!"
            else:
                return "there is no solution!"
        else:
            x = -c / b
            return x
    else:
        if discriminant < 0:
            return "there is no solution!"
        else:
            # Calculate the square root accurately
            delta = sqrt(discriminant)
            x1 = (-b - delta) / (2 * a)
            x2 = (-b + delta) / (2 * a)
            return x1, x2

# Test the function with the given values
a = 0.001
b = 1000
c = 0.001

result_a = quadratic_solver(a, b, c)
print("a is : ", result_a)

# formula function
def quadratic_solver_reexpressed(a, b, c):
    # Calculate the discriminant
    discriminant = pow(b, 2) - 4 * a * c

    # check special cases
    if a == 0:
        if b == 0:
            if c == 0:
                return "answer is infine!"
            else:
                return "no answers!"
        else:
            x = -c / b
            return x
    else:
        if discriminant < 0:
            return "no answers!"
        else:
            delta = sqrt(discriminant)  # Calculate the square root accurately
            x1 = (2 * c) / (-b - delta)
            x2 = (2 * c) / (-b + delta)
            return x1, x2

result_b = quadratic_solver_reexpressed(a, b, c)
print("b is:", result_b)

#---------------------------------------------------------------------------------------------------------------
# exercise 3 part six.The derivative


# Define the function f(x)
def f(x):
    return x * (x - 1)

# Function to calculate the derivative
def calculate_derivative(x, sigma):
    # Approximate the derivative using the definition
    derivative = (f(x + sigma) - f(x)) / sigma
    return derivative

# Point as the question asked
x = 1.0
# Set the true derivative value for f(x) = x(x-1) at x = 1
true_derivative = 1.0

# List of sigma values to test as the question asked
sigma_values = [pow(10, -2), pow(10, -4), pow(10, -6), pow(10, -8), pow(10, -10), pow(10, -12), pow(10, -14)]

# Calculate and compare derivatives for different sigma values
for sigma in sigma_values:
    # Compare the numerical and analytical derivatives to find the error.
    absolute_error = abs(calculate_derivative(x, sigma) - (x * 2 - 1))
    print(f"Sigma = {sigma} ->\n Approximate Derivative = {calculate_derivative(x, sigma)},"
          f"\n True Derivative = {x * 2 - 1},\n Absolute Error = {absolute_error}\n")

#---------------------------------------------------------------------------------------------------------------
# exercise 3 part seven.Integral of a semicircle


# Import the timeit module to measure execution time
import timeit

# Define a function for semicircle
def semicircle(x):
    return pow(1 - pow(x, 2), 0.5)

# Function to compute the integral
# here is using the Trapezoidal Rule
def compute_integral_trapezoidal(N):
    # Define the limits of integration
    a = -1
    b = 1

    # Calculate the width of each part
    # h is space between points along the x - axis
    # N is the number of subdivisions
    h = (b - a) / N

    # set the integral result
    integral = 0

    # making a loop in the parts and calculate the area
    for k in range(N):
        x2 = a + k * h  # x-coordinate of the part
        y2 = pow(1 - pow(x2, 2), 0.5)  # Value of the function at the part
        integral += (y2 + pow(1 - pow(x2 + h, 2), 0.5)) * h / 2
    return integral

# True value of the integral
value = 1.57079632679

# answer to (a) Compute the integral with N=100
N = 100
integral_result_trapezoidal = compute_integral_trapezoidal(N)
# Calculate the absolute error as the difference between the computed result and the true value.
error_trapezoidal = abs(integral_result_trapezoidal - value)
# Display the computed result, true value, and absolute error.
print("Computed Result:", integral_result_trapezoidal)
print("True Value:", value)
print("Absolute Error:", error_trapezoidal)

# (b) Measure the time for N to run in less than a second and for 1 minute
# Find the maximum N value that runs in under 1 second
# Set the upper limit for N
N_upper_limit = 1000000  # This limit corresponds to 1 million
max_time_seconds = 1
N = 1  # Start with N=1
# Loop to find the maximum N running in less than 1 second
for N in range(1, int(N_upper_limit) + 1):
    # Measure the time taken to compute the integral with N using the Trapezoidal Rule
    time_taken = timeit.timeit(lambda: compute_integral_trapezoidal(N), number=1)
    # Check if the time taken exceeds the maximum allowed time (max_time_seconds)
    if time_taken > max_time_seconds:
        # If it does, exit the loop to find the maximum feasible N
        break
# Calculate the gain in running for 1 minute
gain_factor = 60 / time_taken
# Display the maximum feasible N and the gain factor
print(f"Maximum N running in less than 1 second: {N}")
print(f"Gain in running for 1 minute: {gain_factor}x")

#---------------------------------------------------------------------------------------------------------------
