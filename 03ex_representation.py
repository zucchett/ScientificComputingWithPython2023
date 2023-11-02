import math, timeit

###################1. Number representation####################
print("###################START 1. Number representation###################")

def convert_numbers(num, output_format):
    if output_format == 'bin':
        return bin(num)[2:]
    elif output_format == 'hex':
        return hex(num)[2:]
    elif output_format == 'dec':
        return str(num)
    
num = 10
print("Number:", num)
print("Bin Converted:",convert_numbers(num,'bin'))
print("Hex Converted:",convert_numbers(num,'hex'))

###################2. 32-bit floating point number####################
print("###################START 2. 32-bit floating point number###################")

def binary_to_float(binary_str):

    sign_bit = int(binary_str[0])
    exponent_bits = binary_str[1:9]
    mantissa_bits = binary_str[9:]
    if sign_bit:
        sign = -1
    else:
        sign = 1
    exponent = int(exponent_bits, 2) - 127
    mantissa = sum(int(bit) * 2**-(i+1) for i, bit in enumerate(mantissa_bits))
    value = sign * (1.0 + mantissa) * 2**exponent

    return value

binary_str = "110000101011000000000000"
decimal_value = binary_to_float(binary_str)
print(f"The decimal representation of "+str(binary_str)+" is "+str(decimal_value))

###################3. Underflow and overflow####################
print("###################START 3. Underflow and overflow###################")

def find_limits():
    underflow_limit = 1.0
    overflow_limit = 1.0

    while underflow_limit / 2 != 0.0:
        underflow_limit /= 2

    while overflow_limit * 2 != float('inf'):
        overflow_limit *= 2

    return underflow_limit, overflow_limit

underflow_limit, overflow_limit = find_limits()

print("Underflow limit: "+str(underflow_limit))
print("Overflow limit: "+str(overflow_limit))

###################4. Machine precision####################
print("###################START 4. Machine precision###################")

def machine_precision():
    limit = 1.0
    num = 1.0

    while num + limit != num:
        limit /= 2

    return limit

machine_precision_limit = machine_precision()

print("Machine Precision: "+str(machine_precision_limit))

###################5. Quadratic solution####################
print("###################START 5. Quadratic solution###################")

def quadratic_solution(a,b,c):
    x1 = (-b+math.sqrt((b**2) - (4*a*c)))/(2*a)
    x2 = (-b-math.sqrt((b**2) - (4*a*c)))/(2*a)
    return x1, x2

print("(a)",quadratic_solution(0.001,1000,0.001))

def quadratic_solution_b(a,b,c):
    x1 = (4*a*c)/((2*a)*(-b-math.sqrt((b**2) - (4*a*c))))
    x2 = (4*a*c)/((2*a)*(-b+math.sqrt((b**2) - (4*a*c))))
    return x1, x2

print("(b)",quadratic_solution_b(0.001,1000,0.001))
#We see that in both cases there are precision errors

def quadratic_solution_fixed(a,b,c):
    x1 = (4*a*c)/((2*a)*(-b-math.sqrt((b**2) - (4*a*c))))
    x2 = (4*a*c)/((2*a)*(-b+math.sqrt((b**2) - (4*a*c))))
    return round(x1), round(x2)

print("(c)",quadratic_solution_fixed(0.001,1000,0.001))

###################6. The derivative####################
print("###################START 6. The derivative###################")

def f(x):
    return x * (x - 1)

def calculate_derivative(x, delta):
    derivative = (f(x + delta) - f(x)) / delta
    return derivative

x = 1
print("(a)",calculate_derivative(x,1e-2))
print("The true derivative is 1, although, because we get some precision errors, using delta = 1e-2 we get 1,01 as result.")
deltas = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]

for delta in deltas:
    approx_derivative = calculate_derivative(x, delta)
    print(f"Delta = {delta:.0e}: Approximate Derivative = {approx_derivative}")

print("The accuracy gets better the smaller delta gets, and that's expected.")

###################7. Integral of a semicircle####################
print("###################START 7. Integral of a semicircle###################")

def semicircle_function(x):
    return math.sqrt(1 - x**2)

def compute_integral(N):
    h = 2 / N
    integral = 0
    for k in range(1, N + 1):
        x_k = -1 + (k - 0.5) * h
        y_k = semicircle_function(x_k)
        integral += h * y_k
    return integral

N = 100
result = compute_integral(N)
true_value = math.pi / 2

print(f"Approximate Integral with N = {N}: {result}")
print(f"True Value of the Integral: {true_value}")
print(f"Absolute Error: {abs(result - true_value)}")

def time_integral_computation(N):
    return compute_integral(N)

max_N_one_second = 1
while True:
    execution_time = timeit.timeit(lambda: time_integral_computation(max_N_one_second), number=1)
    if execution_time < 1.0:
        max_N_one_second *= 2
    else:
        break

max_N_one_minute = 1
while True:
    execution_time = timeit.timeit(lambda: time_integral_computation(max_N_one_minute), number=1)
    if execution_time < 60.0:
        max_N_one_minute *= 2
    else:
        break

print(f"Maximum N for 1-second computation: {max_N_one_second}")
print(f"Maximum N for 1-minute computation: {max_N_one_minute}")
