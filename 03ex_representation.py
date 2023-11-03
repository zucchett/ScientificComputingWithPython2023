#1.Write a function that converts integer numbers among the bin, dec, and hex representations (bin<->dec<->hex).
Determine the input type in the function, and pass another argument to choose the output representation.
def convert_base(input_number, output_base):
    if not (input_number, int):
        raise ValueError("Input must be an integer")
    
    if output_base not in ('bin', 'dec', 'hex'):
        raise ValueError("Output base must be 'bin', 'dec', or 'hex'")

    if output_base == 'bin':
        return bin(input_number)[2:]  
    elif output_base == 'dec':
        return str(input_number)  
    elif output_base == 'hex':
        return hex(input_number)[2:]  
# Example usage:
input_number = 42
output_base = 'hex'

result = convert_base(input_number, output_base)
print(f"{input_number} in {output_base} is {result}")




#3. Write a program to determine the approximate underflow and overflow limits (within a factor of 2) for floating point numbers on your computer.

#find the under flow
underflow_limit = 1.0
while underflow_limit / 2 > 0.0:
    underflow_limit /= 2

# find the overflow limit
overflow_limit = 1.0
while not float('inf') == overflow_limit * 2:
    overflow_limit *= 2

print("Approximate Underflow Limit:", underflow_limit)
print("Approximate Overflow Limit:", overflow_limit)

#4. Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.
machine_epsilon = 1.0

while 1.0 + machine_epsilon > 1.0:
    machine_epsilon /= 2

print("Machine Epsilon:", machine_epsilon)

#5. Write a function that takes in input three parameters  𝑎,  𝑏 and  𝑐 and prints out the two solutions to the quadratic equation  𝑎𝑥2+𝑏𝑥+𝑐=0 using the standard formula
import math

def quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    else:
        return "math error"

# (a) Using the standard formula
a1 = 0.001
b1 = 1000
c1 = 0.001
solution_a = quadratic_equation(a1, b1, c1)

print("Solution (Standard Formula) for a=0.001, b=1000, c=0.001:")
print(solution_a)

# (b) Re-expressing the formula
def quadratic_reexpressed(a, b, c):
    root_common = -b / (2*a)
    discriminant_sqrt = math.sqrt(b**2 - 4*a*c)
    root_diff = discriminant_sqrt / (2*a)
    root1 = root_common + root_diff
    root2 = root_common - root_diff
    return root1, root2

solution_b = quadratic_reexpressed(a1, b1, c1)

print("\nSolution (Re-expressed Formula) for a=0.001, b=1000, c=0.001:")
#re-expressed formula simplifies the computation by avoiding the need to compute the discriminant and the square root separately
print(solution_b)


#6.Write a program that implements the function  𝑓(𝑥)=𝑥(𝑥−1)
def f(x):
    return x * (x - 1)

def calculate_derivative(x, delta):
    return (f(x + delta) - f(x)) / delta

x = 1
delta = 1e-2

numeric_derivative = calculate_derivative(x, delta)

# analytical derivative of f(x) = x(x - 1) is 2x - 1
analytical_derivative = 2 * x - 1

print("Numeric derivative:", numeric_derivative)
print("Analytical derivative:", analytical_derivative)

#b. Repeat the calculation for  𝛿=10−4,10−6,10−8,10−10,10−12 and  10−14. How does the accuracy scale with  𝛿?
deltas = [1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]

for delta in deltas:
    numeric_derivative = calculate_derivative(x, delta)
    print(f"Delta = {delta}: Numeric derivative = {numeric_derivative}")

#7.Write a program to compute the integral with  𝑁=100. How does the result compare to the true value?

import math

def semicircle_function(x):
    return math.sqrt(1 - x**2)

def riemann_integral(N):
    h = 2 / N
    integral_sum = 0
    for k in range(1, N + 1):
        x_k = -1 + (k - 0.5) * h
        y_k = semicircle_function(x_k)
        integral_sum += h * y_k
    return integral_sum

# Calculate the integral with N = 100
N = 100
result = riemann_integral(N)

true_value = math.pi / 2

print(f"Approximate Integral (N = {N}): {result}")
print(f"True Value: {true_value}")

