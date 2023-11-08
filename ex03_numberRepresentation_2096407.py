# Riccardo Principe 2096407 Homework3
# EXERCISE 1
print('\n' + 'Exercise 1' + '\n')

def convert(n,how):
    if 'x' in n:
        print('n is a exadecimal')
        n = int(n,16)
    elif 'b' in n:
        print('n is a binary')
        n = int(n,2)
    else:
        print('n is a decimal')
        n = int(n)
        
    if how == 'bin':
        print(bin(n))
    elif how == 'dec':
        print(int(n))
    elif how == 'exa':
        print(hex(n))
    else:
        print('type not valid')
        
number = input('Give me a number (int, 0b001, 0xA3B): ')
how = input('Give me the type: ')
convert(number,how)
print('-------------------------------' + '\n')

# EXERCISE 2
print('\n' + 'Exercise 2' + '\n')

def convertFloatingPoint(n):
    sign = 0 if n[0] == '0'else 1
    exp = int(n[1:9],2)
    exp = int(exp)
    exponent = exp if exp < 127 else exp-127
    mant = n[9:]
    mantissa = 0
    for i in range(len(mant)):
        if mant[i] == '1':
            mantissa += 2**(-i-1)
    number = ((-1)**sign)*(1+mantissa)*(2**exponent)
    return number

num = '01000011010101000000000000000000'
print(convertFloatingPoint(num))
print('-------------------------------' + '\n')

# EXERCISE 3
print('\n' + 'Exercise 3' + '\n')
def lim_inf():
    l_inf = 1.0
    while l_inf / 2 > 0:
        l_inf /= 2
    return l_inf

def lim_sup():
    l_sup = 1.0
    while l_sup * 2 < float('inf'):
        l_sup *= 2
    return l_sup

inferior_limit = lim_inf()
superior_limit = lim_sup()

print("Inferior Limit: ", inferior_limit)
print("Superior Limit: ", superior_limit)
print('-------------------------------' + '\n')

# EXERCISE 4
print('\n' + 'Exercise 4' + '\n')
def find_machine_precision():
    epsilon = 1.0

    while 1.0 + epsilon != 1.0:
        epsilon /= 2.0

    return epsilon

machine_precision = find_machine_precision()

print("Machine Precision: ", machine_precision)
print('-------------------------------' + '\n')

# EXERCISE 5
print('\n' + 'Exercise 5' + '\n')
import math

def quadratic_standard(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None  # No real solutions
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2

def quadratic_reexpressed(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    else:
        root1 = (2 * c) / (-b - math.sqrt(discriminant))
        root2 = (2 * c) / (-b + math.sqrt(discriminant))
        return root1, root2

# (c) Write a function to compute the roots accurately
def quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    else:
        if b >= 0:
            root1 = (-b - math.sqrt(discriminant)) / (2 * a)
            root2 = (2 * c) / (-b - math.sqrt(discriminant))
        else:
            root1 = (2 * c) / (-b + math.sqrt(discriminant))
            root2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    
# (a) Compute the solutions for a=0.001, b=1000, and c=0.001
a = 0.001
b = 1000
c = 0.001
solutions = quadratic_standard(a, b, c)
print("Standard formula (a):", solutions)

# (b) Compute the solutions using the re-expressed formula
solutions_reexpressed = quadratic_reexpressed(a, b, c)
print("Re-expressed formula (b):", solutions_reexpressed)

# (b) Comparison and explanation
print("Comparison (a vs. b)")
print("Standard Formula (a):", solutions)
print("Re-expressed Formula (b):", solutions_reexpressed)

# Explanation: The re-expressed formula is mathematically equivalent to the standard formula.
# However, when computing solutions for small values of 'a' and 'c' and a large value of 'b',
# numerical precision issues can lead to differences in results. This is because the
# intermediate values can become very small or very large, causing loss of precision
# when performing arithmetic operations.


# (c) Compute the solutions using the accurate function
solutions_accurate = quadratic(a, b, c)
print("Accurate function (c):", solutions_accurate)
print('-------------------------------' + '\n')

# EXERCISE 6
print('\n' + 'Exercise 6' + '\n')
def function(x):
    return x * (x - 1)

def numerical_derivative(x, delta):
    f_x = function(x)
    f_x_plus_delta = function(x + delta)
    derivative = (f_x_plus_delta - f_x) / delta
    return derivative

# True analytical derivative
def true_derivative(x):
    return 2 * x - 1

x = 1.0
true_value = true_derivative(x)

print("Analytical Derivative (True Value):", true_value)

# (a) Calculate the derivative for delta = 1e-2
delta = 1e-2
approx_derivative = numerical_derivative(x, delta)
print(f"Approximate Derivative (delta = {delta}):", approx_derivative)

# (b) Repeat for different values of delta
deltas = [1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]

for delta in deltas:
    approx_derivative = numerical_derivative(x, delta)
    print(f"Approximate Derivative (delta = {delta}):", approx_derivative)
print('-------------------------------' + '\n')

# EXERCISE 7
print('\n' + 'Exercise 7' + '\n')
import timeit

def semicircle(x):
    return math.sqrt(1 - x**2)

def riemann_integral(N):
    h = 2 / N
    integral = 0
    for k in range(1, N + 1):
        xk = -1 + (k - 0.5) * h
        yk = semicircle(xk)
        integral += h * yk
    return integral

# (a) Compute the integral with N = 100
N = 100
result = riemann_integral(N)
true_value = math.pi / 2

print(f"Approximate Integral (N = {N}): {result}")
print(f"True Value: {true_value}")
print(f"Absolute Error: {abs(result - true_value)}")

# (b) Measure the time for different values of N
def time_integral(N):
    return timeit.timeit(lambda: riemann_integral(N), number=1)

max_N_for_1_second = 10000  # Adjust as needed
max_N_for_1_minute = 500000  # Adjust as needed

time_1_second = time_integral(max_N_for_1_second)
time_1_minute = time_integral(max_N_for_1_minute)

print(f"Maximum N for 1 second: {max_N_for_1_second}, Time: {time_1_second} seconds")
print(f"Maximum N for 1 minute: {max_N_for_1_minute}, Time: {time_1_minute} seconds")
