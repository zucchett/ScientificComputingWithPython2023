#%% 1. Number representation

def conversion(number, output_type):
    if isinstance(number, str):
        if number[:2] == '0b':
            number = int(number, 2)
        elif number[:2] == '0x':
            number = int(number, 16)
        else:
            raise ValueError("The number should be a bin, an int or a hex")
        
    if output_type == "bin":
        return bin(number)
    elif output_type == "dec":
        return number
    elif output_type == "hex":
        return hex(number)
    else:
        raise ValueError("The output type should be bin, int, hex")

print(conversion("0b101001110", "dec"))
print(conversion("0b101001110", "hex"))
print(conversion(334, "hex"))
print(conversion(334, "bin"))
print(conversion("0x14E", "bin"))
print(conversion("0x14E", "dec"))

#%% 2. 32-bit floating point number

def binary_to_float(binary_number):
    # Masks
    sign_mask = 2**31
    expo_mask = sum([2**i for i in range(23, 31)])
    mant_mask = sum([2**i for i in range(23)])

    # Masked numbers
    sign = (int(binary_number, 2) & sign_mask) >> 31
    expo = (int(binary_number, 2) & expo_mask) >> 23
    mant = (int(binary_number, 2) & mant_mask) / (2**23) #>> 0

    return (-1)**sign * (1+mant) * 2**(expo-127)

print(binary_to_float("110000101011000000000000"))

#%% 3. Underflow and overflow

underflow_limit = 1.0
overflow_limit = 1.0

while underflow_limit / 2 > 0:
    underflow_limit /= 2

while overflow_limit * 2 != float('inf'):
    overflow_limit *= 2

print("Approximate underflow limit :", underflow_limit)
print("Approximate overflow limit :", overflow_limit)

#%% 4. Machine precision

number = 1.0
epsilon = 1.0

while number + epsilon > number:
    epsilon /= 2

print("Machine precision :", epsilon)

#%% 5. Quadratic solution

from math import *

def quadratic_solution_a(a, b, c):
    delta = b**2 - 4*a*c
    if delta >= 0:
        x1 = (-b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)
        return x1, x2

def quadratic_solution_b(a, b, c):
    delta = b**2 - 4*a*c
    if delta >= 0:
        x1 = (-2 * c) / (b - sqrt(delta))
        x2 = (-2 * c) / (b + sqrt(delta))
        return x1, x2
    
def quadratic_solution_c(a, b, c):
    if b == 0:
        return -b / (2 * a)
    elif b > 0:
        return quadratic_solution_b(a, b, c)[0], quadratic_solution_a(a, b, c)[1]
    else:
        return quadratic_solution_a(a, b, c)[0], quadratic_solution_b(a, b, c)[1]

print(f"Solutions 1: {quadratic_solution_a(a=0.001, b=1000, c=0.001)}")
print(f"Solutions 2: {quadratic_solution_b(a=0.001, b=1000, c=0.001)}")
# In this example, 4ac is very small in front of b^2. b^2 - 4ac then almost gives |b|.
# By subtracting b - sqrt(b^2 - 4ac) with b > 0, we then risk a loss of information.
# It is therefore necessary to avoid at all costs subtractions between b and sqrt(b^2 - 4ac).
# This is why the x1 of formula 1 and the x2 of formula 2 are less precise.
# We must therefore adapt the formula to use according to the sign of b (in our positive case).
print(f"Solutions 3: {quadratic_solution_c(a=0.001, b=1000, c=0.001)}")

#%% 6. The derivative

def f(x):
    return x * (x-1)

def f_prime(x, delta):
    return (f(x+delta) - f(x)) / delta

# a)
x = 1
delta = 1e-2
approx_derivative = f_prime(x, delta)
print(f"Approximative derivative = {approx_derivative}")
true_derivative = 2 * x - 1
print(f"Analytical derivative = {true_derivative}")
# When using δ = 1e-2, the program provides an approximate derivative that will not be equal to the true value due to the finite difference approximation.
# The error arises because δ is a finite value

# b)
deltas = [1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]
for delta in deltas:
    approx_derivative = f_prime(x, delta)
    print(f"\u03B4 = {delta}:\tApproximate Derivative = {approx_derivative}\tError = {abs(approx_derivative - true_derivative)}")
# The accuracy of the approximate derivative improves, and the error between the approximate and true derivatives decreases.
# This is because the finite difference approximation becomes more accurate as δ approaches zero, and the calculated derivative gets closer to the true derivative value.

#%% 7. Integral of a semicircle

import timeit

# a)
def riemann_integral(N):
    h = 2 / N
    I = 0
    for k in range(N + 1):
        x = k * h - 1
        y = sqrt(1 - x**2)
        I += h * y
    return I

N = 100
print(f"Riemann integral: I = {riemann_integral(N)}")
# The error should be relatively large because N = 100 provides only a coarse approximation.

# b)
max_N_1s = 100  # Starting value
while True:
    if timeit.timeit(lambda: riemann_integral(max_N_1s * 2), number=1) > 1:
        break
    max_N_1s *= 2
    elapsed_time_1s = timeit.timeit(lambda: riemann_integral(max_N_1s), number=1)
print(f"Max N for 1 second: {max_N_1s}, Elapse time: {elapsed_time_1s}, I = {riemann_integral(max_N_1s)}")

max_N_1min = max_N_1s  # Starting value
while True:
    if timeit.timeit(lambda: riemann_integral(max_N_1min * 2), number=1) > 60:
        break
    max_N_1min *= 2
    elapsed_time_1min = timeit.timeit(lambda: riemann_integral(max_N_1min), number=1)
print(f"Max N for 1 minute: {max_N_1min}, Elapse time: {elapsed_time_1min}, I = {riemann_integral(max_N_1min)}")

# Results:
# Max N for 1 second: 3276800, Elapse time: 0.7343630000250414, I = 1.5707963265146427
# Max N for 1 minute: 209715200, Elapse time: 47.38940989994444, I = 1.5707963267947422
# The gain in running it for 1min is a better accuracy of the result, but it is not very relevant if we compare the time of running.
