#LAB 3
#ex1:
print("1 ------ Number representation")
import math
def convert(a,type):
    if type == "bin" :
        return bin(a)
    elif type == "dec":
        return a
    elif type == "hex":
        return hex(a)
    return 0

print("bin:",convert(5,"bin"))
print("dec:",convert(12,"dec"))
print("hex:",convert(17, "hex"))

#ex2:
print("2 ------ Number representation ")

import struct

def binary_to_float(a):
    if len(binary_str) != 32:
        raise ValueError("Binary string must be 32 bits long")

    sign_bit = int(a[0])
    exponent_bits = a[1:9]
    mantissa_bits = a[9:]
    sign = -1 if sign_bit == 1 else 1
    exponent = int(exponent_bits, 2) - 127
    mantissa = 1.0 
    for i, bit in enumerate(mantissa_bits):
        mantissa += int(bit) * 2**(-1 - i)

    result = sign * mantissa * 2**exponent
    return result

binary_str = "11000000101011000000000000000000"
print(binary_to_float(binary_str))


#ex3:
print("3 ------ Underflow and overflow ")

def underflow_limit():
    x = 1.0
    while (x / 2.0) > 0:
        x /= 2.0
    return x

def overflow_limit():
    x = 1.0
    while (x * 2.0) < float('inf'):
        x *= 2.0
    return x


print("Underflow Limit:", underflow_limit())
print("Overflow Limit:", overflow_limit())

#ex4:
print("4 ------ Machine precision")

def floating_precision_limit():
    x = 1.0
    e = 1.0
    while (x + e) != x:
        e *= 0.5
    return e

print(floating_precision_limit())

#ex5:
print("5 ------ Quadratic solution")

def quadratic_solutions(a,b,c):
    x1 = (-b + math.sqrt(b**2-(4*a*c)))/(2*a)
    x2 = (b + math.sqrt(b**2-(4*a*c)))/(2*a)
    return(x1,x2)

def quadratic_solutions_2(a,b,c):
    x1 = ((-b + math.sqrt(b**2-(4*a*c)))*(-b + math.sqrt(b**2-(4*a*c))))/((2*a)*(-b + math.sqrt(b**2-(4*a*c))))
    x2 = ((b + math.sqrt(b**2-(4*a*c)))*(b + math.sqrt(b**2-(4*a*c))))/((2*a)*(b + math.sqrt(b**2-(4*a*c))))
    return(x1,x2)


def quadratic_solutions_accurate(a, b, c):
    if a == 0:
        return "Coefficient 'a' cannot be zero"
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root1 = -b / (2*a)
        return root1
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        return complex(real_part, imaginary_part)

print(quadratic_solutions_2(0.001,1000,0.001))
print(quadratic_solutions_2(0.001,1000,0.001))
print(quadratic_solutions_accurate(0.001,1000,0.001))
print(f"I don't see any difference")

#ex6:
print("6 ------ The derivative")

def function(x):
    return x * (x - 1)

def derivative(delta):
    x = 1
    der = (function(x + delta) - function(x)) / delta
    return der

numerical_derivative = derivative(1e-2)
analytical_derivative = 2 * 1 - 1

print(f"(a) Numerical Derivative (delta = 1e-12): {numerical_derivative}")
print(f"    Analytical Derivative: {analytical_derivative}")
print(f"The limit cannot be calculated precisely with informatics models, we need to approximate")

delta_values = [1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]
for delta in delta_values:
    numerical_derivative = derivative(delta)
    print(f"(b) Numerical Derivative (delta = {delta}): {numerical_derivative}")
print(f"The accuracy is higher when we are near delta = 1e-08 but increase when we increase or decrease delta")

#ex7:
print("7 ------ Integral of a semicircle")

import timeit
def compute_integral(N):
    h = 2 / N
    integral = 0
    for k in range(1, N + 1):
        x_k = -1 + k * h
        y_k = math.sqrt(1 - x_k**2)
        integral += h * y_k
    return integral

true_value = math.pi / 2
result_a = compute_integral(100)

print("(a) Result with N = 100", result_a)
print("    Absolute Error:", abs(result_a - true_value))

def time_for_N(N):
    return timeit.timeit(f'compute_integral({N})', globals=globals(), number=10)

max_N_1_second = 1
while time_for_N(max_N_1_second) < 1:
    max_N_1_second *= 2

max_N_1_minute = 1
while time_for_N(max_N_1_minute) < 60:
    max_N_1_minute *= 2

print("(b) Maximum N for < 1 second:", max_N_1_second)
res_1_second = compute_integral(max_N_1_second)
print(res_1_second)
print("    Maximum N for 1 minute:", max_N_1_minute)
res_1_minute = compute_integral(max_N_1_minute)
print(res_1_minute)
print("difference:" ,res_1_minute - res_1_second)
print(f"The gain is very little for the ressources needed")
