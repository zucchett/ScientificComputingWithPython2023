##Number representation**

def get_input_base(input_value):
    if isinstance(input_value, int):
        return 10
    elif isinstance(input_value, str):
        if input_value.startswith("0x"):
            return 16
        elif input_value.startswith("0b"):
            return 2
        else:
            return 10
    else:
        raise ValueError("Invalid input format")

def convert_to_decimal(input_value, input_base):
    return int(input_value, input_base)

def get_output_representation(decimal_value, output_base):
    if output_base == 2:
        return bin(decimal_value)
    elif output_base == 10:
        return str(decimal_value)
    elif output_base == 16:
        return hex(decimal_value)
    else:
        raise ValueError("Invalid output base")

def convert_number(input_value, output_base):
    input_base = get_input_base(input_value)
    decimal_value = convert_to_decimal(input_value, input_base)
    result = get_output_representation(decimal_value, output_base)
    return result

#testing
input_value = "0b1010"
output_base = 10      
result = convert_number(input_value, output_base)
# Print the result
print(result)

##question 2

def check_length(binary_string):
    if len(binary_string) != 32:
        raise ValueError("Input binary string must be 32 bits long")

def extract_components(binary_string):
    sign_bit = int(binary_string[0], 2)
    exponent_bits = binary_string[1:9]
    mantissa_bits = binary_string[9:]
    return sign_bit, exponent_bits, mantissa_bits

def calculate_values(sign_bit, exponent_bits, mantissa_bits):
    sign = (-1) ** sign_bit
    exponent = int(exponent_bits, 2) - 127
    mantissa = 1.0

    for i in range(len(mantissa_bits)):
        if mantissa_bits[i] == '1':
            mantissa += 2 ** (-i - 1)

    return sign, exponent, mantissa

def binary_to_single_precision(binary_string):
    check_length(binary_string)
    sign_bit, exponent_bits, mantissa_bits = extract_components(binary_string)
    sign, exponent, mantissa = calculate_values(sign_bit, exponent_bits, mantissa_bits)

    float_value = sign * mantissa * (2 ** exponent)
    return float_value


##question 3
import math

def calculate_limits():
    underflow = 1.0
    overflow = 1.0

    # Find the underflow limit (minimum positive value)
    while underflow / 2 > 0:
        underflow/= 2

    # Find the overflow limit (maximum finite positive value)
    while not math.isinf(overflow * 2):
        overflow *= 2

    return underflow, overflow

underflow, overflow = calculate_limits()

print("Underflow:", underflow)
print("Overflow:", overflow)

##Question 4
def find_machine_precision():
    machine_precision = 1.0

    while 1.0 + machine_precision / 2.0 != 1.0:
        machine_precision /= 2.0

    return machine_precision



machine_precision = find_machine_precision()
    
print("Machine Precision:", machine_precision)

##Question 5
import math

def quadratic_solver(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    else:
        return None  # Complex roots, no real solutions

# (a) Compute the solutions for a=0.001, b=1000, and c=0.001
a = 0.001
b = 1000
c = 0.001
roots_a = quadratic_solver(a, b, c)
print("(a) Solutions for a=0.001, b=1000, c=0.001:", roots_a)

# (b) Modified standard formula
def quadratic_solver_changed(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (2*c) / (-b - math.sqrt(discriminant))
        root2 = (2*c) / (-b + math.sqrt(discriminant))
        return root1, root2

roots_b = quadratic_solver_changed(a, b, c)
print("(b) Solutions for a=0.001, b=1000, c=0.001 (modified formula):", roots_b)

# (c)Function that computes the roots accurately in all cases
def accurate_quadratic_solver(a, b, c):
    if a == 0:
        if b == 0:
            return None
        root = -c / b
        return root
    else:
        discriminant = b**2 - 4*a*c
        if discriminant >= 0:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            return root1, root2
        else:
            return None

roots_c = accurate_quadratic_solver(a, b, c)
print("(c) Solutions for a=0.001, b=1000, c=0.001 (accurate function):", roots_c)

#question 6

def f(x):
    return x * (x - 1)

def numerical_derivative(f, x, delta):
    return (f(x + delta) - f(x)) / delta

x = 1.0

#Calculating the derivative with delta = 1e-2
delta = 1e-2
approx_derivative = numerical_derivative(f, x, delta)

# Analytical derivative (true value)
true_derivative = 2 * x - 1

# Print the results
print("(a) Delta = {:.2e}".format(delta))
print("Approximate Derivative: {:.8f}".format(approx_derivative))
print("True Derivative: {:.8f}".format(true_derivative))
print("Error: {:.8e}".format(abs(approx_derivative - true_derivative)))
print()

# calculation for various delta values
delta_values = [1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]

for delta in delta_values:
    approx_derivative = numerical_derivative(f, x, delta)
    error = abs(approx_derivative - true_derivative)
    print("Delta = {:.2e}".format(delta))
    print("Approximate Derivative: {:.8f}".format(approx_derivative))
    print("Error: {:.8e}".format(error))




#question7
import timeit
import math

def compute_integral(N):
    h = 2.0 / N
    integral = 0.0
    for k in range(1, N + 1):
        x = -1.0 + (k - 0.5) * h
        y = math.sqrt(1 - x**2)
        integral += h * y
    return integral

true_value = math.pi / 2.0 

#Compute the integral with N=100 and compare to the true value
N = 100
result = compute_integral(N)
error = abs(result - true_value)
print(f"(a) N={N}, Computed Value: {result}, True Value: {true_value}, Error: {error}")

#Measure the time for different values of N
N_values = [1000, 10000, 100000, 1000000]
for N in N_values:
    time_taken = timeit.timeit(lambda: compute_integral(N), number=10)
    print(f"(b) N={N}, Time Taken (10 runs): {time_taken:.6f} seconds")

#Measure the time for a large N to see the gain in running it for 1 minute
large_N = 10000000
time_taken_large_N = timeit.timeit(lambda: compute_integral(large_N), number=1)
print(f"(c) N={large_N}, Time Taken (1 run): {time_taken_large_N:.6f} seconds")

