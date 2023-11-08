import timeit
import math
print("ESERCIZIO 1") #ESERCIZIO 1

def convert_number(number, from_base, to_base):
    if from_base == "dec":
        if to_base == "bin":
             result = bin(number)
        elif to_base == "hex":
             result = hex(number) 
        else:
            result = number  
    elif from_base == "bin":
        if to_base == "dec":
             result = int(number, 2) 
        elif to_base == "hex":
             result = hex(int(number, 2)) 
        else:
            result = number  
    elif from_base == "hex":
        if to_base == "dec":
            result = int(number, 16)  
        elif to_base == "bin":
            result = bin(int(number, 16)) 
        else:
            result = number  
  
    return result


input_number = "10010"
from_base = "bin"
to_base = "dec"
print(convert_number(input_number, from_base, to_base))

print("ESERCIZIO 2") #ESERCIZIO 2

def conversion(binary_str):

    sign_bit = int(binary_str[0])
    exponent_bits = binary_str[1:9]
    fractional_bits = binary_str[9:]

    exponent = int(exponent_bits, 2) - 127
    mantissa = 1

    for i in range(23):
        if fractional_bits[i] == '1':
            mantissa += 2**-(i + 1)

    result = (-1)**sign_bit * 2**exponent * mantissa
    return result


binary_string = "11000010101100000000000000000000"
decimal_result = conversion(binary_string)
print("Decimal result:", decimal_result)

print("ESERCIZIO 3") #ESERCIZIO 3

N = 2000
underflow = 1
overflow = 1
counter = 0
try:
    for i in range(N):
        underflow = underflow / 2
        overflow = overflow * 2
        print("|%2d"%i, "\t\t", "|%2.5e"%underflow,"|", "\t\t", "|%2.5e"%overflow,"|")
        counter = i
except:
    print("overflow limit = ", overflow, " underflow limit = ", underflow)

print("ESERCIZIO 4") #ESERCIZIO 4

def machine_precision():
    epsilon = 1.0
    while 1.0 + epsilon > 1.0:
        previous_epsilon = epsilon
        epsilon /= 2.0
    return previous_epsilon

print("Machine Precision = ", machine_precision())

print("ESERCIZIO 5") #ESERCIZIO 5

def quadratic_solution(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    elif discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x1 = (-b) / (2*a)
        x2 = (-b )/ (2*a)
        return x1, x2
    
roots = quadratic_solution(0.001, 1000, 0.001)
print("Roots using standard formula = ", roots)


def quadratic_solution_reexpressed(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    elif discriminant > 0:
        x1 = ((-b + math.sqrt(discriminant)) * (-b - math.sqrt(discriminant))) / ((2*a) * (-b - math.sqrt(discriminant)))
        x2 = ((-b - math.sqrt(discriminant)) * (-b + math.sqrt(discriminant))) / ((2*a) * (-b + math.sqrt(discriminant)))
        return x1, x2
    elif discriminant == 0:
        x1 = (b**2) / (2*a)
        x2 = (b**2 )/ (2*a)
        return x1, x2

roots_reexpressed = quadratic_solution_reexpressed(0.001, 1000, 0.001)
print("Roots using re-expressed formula:", roots_reexpressed)
#The roots computed using the re-expressed formula are quite different from the roots obtained using the standard formula. The difference is due to the limited precision of floating-point arithmetic. When b is very large compared to a and c (as in this case), the term b^2 - 4ac can become very close to b^2. As a result, taking the square root of this value can lead to a loss of precision, which affects the accuracy of the computed roots.

def quadratic_solution_final(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    elif discriminant > 0:
        if b >= 0:
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            x1 = (2*c) / (-b - math.sqrt(discriminant))
        else:
            x2 = (2*c) / (-b + math.sqrt(discriminant))
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x1 = (b**2) / (2*a)
        x2 = (b**2 )/ (2*a)
        return x1, x2

roots_accurate = quadratic_solution_final(0.001, 1000, 0.001)
print("Accurate roots:", roots_accurate)

print("ESERCIZIO 6") #ESERCIZIO 6

def f(x):
    return x * (x - 1)

def numerical_derivative(x, delta):
    derivative = (f(x + delta) - f(x)) / delta
    return derivative

def analytical_derivative(x):
    return 2 * x - 1

x = 1
true_derivative = analytical_derivative(x)

print("Analytical Derivative at x=1:", true_derivative)

delta1 = 1e-2
print(f"Numerical Derivative (delta={delta1}):", numerical_derivative(1,delta1))
print("\nThe two values will not agree perfectly due to the approximation introduced by finite δ.\nThe smaller the δ, the closer the numerical derivative will be to the true derivative, \nbut it may never be exactly the same due to finite precision in numerical calculations.\n")

deltas = [1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]

for delta in deltas:
    numerical_derivatives = numerical_derivative(x, delta)
    print(f"Numerical Derivative (delta={delta}):", numerical_derivatives)

    error = abs(numerical_derivatives - true_derivative)
    print(f"Error (delta={delta}):", error)
    print()

print("As δ gets smaller (closer to zero), the accuracy of the numerical derivative improves, and the error decreases.\nHowever, there may still be a limit to how accurate the numerical derivative can be due to the finite precision of floating-point arithmetic in the computer.")

print("ESERCIZIO 7") #ESERCIZIO 7

def semicircle(x):
    return (1 - x**2)**0.5

def riemann_integral(N):
    h = 2 / N
    integral_result = 0
    for k in range(N):
        x_k = -1 + k * h
        y_k = semicircle(x_k)
        integral_result += h * y_k
    return integral_result
N = 100

result = riemann_integral(N)
print(f"Integral with N={N}: {result}")
true_value = 1.57079632679

error = abs(result - true_value)
print(f"Error compared to the true value: {error}")
print("\nWith N=100, we get a relatively accurate approximation.\n")


threshold_time = 1.0
N_max = 4894304
N_max_new = 0
while True:
    execution_time = timeit.timeit("riemann_integral(N_max)", globals=globals(), number=1)
    if execution_time > threshold_time:
        N_max_new = N_max-100
        break
    N_max += 100

print(f"Maximum N for < 1 second: {N_max_new}")

execution_time_N_max = timeit.timeit("riemann_integral(N_max_new)", globals=globals(), number=1)
print(f"Execution time for N={N_max_new}: {execution_time_N_max:.6f} seconds")
integral_result_N_max = riemann_integral(N_max)
print("integral result for N =", N_max_new, ": ",integral_result_N_max)

# 1 minute
N_1_minute = N_max_new * int(60 / execution_time_N_max)
print(f"Maximum N for 1 minute: {N_1_minute}")

integral_result_N_1min = riemann_integral(N_1_minute)
print("integral result for N =", N_1_minute, ": ",integral_result_N_1min)
print("\nThe gain in running it for 1 minute would be that you can achieve a more accurate result by using a larger N")

