## Exercise 1
def convert_number(number, output_type):
    if isinstance(number, int):
        if output_type == "bin":
            return bin(number)
        elif output_type == "dec":
            return number
        elif output_type == "hex":
            return hex(number)
        else:
            return "Sorry, but I can only convert to 'bin', 'dec', or 'hex'."

    elif isinstance(number, str):
        number = number.strip()

        if output_type == "bin":
            return bin(int(number, 2))
        elif output_type == "dec":
            return int(number, 2)
        elif output_type == "hex":
            return hex(int(number, 2))
        else:
            return "Sorry, but I can only convert to 'bin', 'dec', or 'hex'."

    else:
        return "I can only handle integers or binary/decimal/hexadecimal strings bro. Try again!"


## Exercise 2
def binary_to_float(binary_string):
    sign = int(binary_string[0])
    exponent = int(binary_string[1:9], 2) - 127
    mantissa = 1.0

    for i in range(9, 32):
        mantissa += int(binary_string[i]) * 2 ** -(i - 8)

    result = (-1) ** sign * mantissa * 2 ** exponent
    return result


## Exercise 3
def find_limits():
    underflow_limit = 1.0
    overflow_limit = 1.0

    while underflow_limit / 2.0 != 0.0:  # We keep dividing by 2 until we reach underflow
        underflow_limit /= 2.0

    while overflow_limit * 2.0 != float('inf'):  # We keep multiplying by 2 until we reach overflow
        overflow_limit *= 2.0

    return underflow_limit, overflow_limit

underflow, overflow = find_limits()
print("The approximate underflow limit is:", underflow)
print("The approximate overflow limit is:", overflow)


## Exercise 4
def find_precision():
    precision = 1.0

    while 1.0 + precision != 1.0:  # We keep adding an increasingly smaller value until it has no effect
        precision /= 2.0

    return precision * 2.0  # We multiply by 2 to get a good approximation

machine_precision = find_precision()
print("The approximate machine precision is:", machine_precision)


## Exercise 5 (a)
def solve_quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        print("No real solutions exist for this quadratic equation human!")
    else:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        print("The solutions to the quadratic equation are:")
        print("Root 1:", root1)
        print("Root 2:", root2)

a = 0.001
b = 1000
c = 0.001

solve_quadratic_equation(a, b, c)


## Exercise 5 (b)
def solve_quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        print("No real solutions exist for this quadratic equation, hooman. Meow!")
    else:
        root1 = (-2 * c) / (b + (b ** 2 - 4 * a * c) ** 0.5)
        root2 = (-2 * c) / (b - (b ** 2 - 4 * a * c) ** 0.5)
        print("The solutions to the quadratic equation are:")
        print("Root 1:", root1)
        print("Root 2:", root2)

a = 0.001
b = 1000
c = 0.001

solve_quadratic_equation(a, b, c)

# The results are slightly different because of limitations of floating-point arithmetic. Computers store and perform calculations on numbers using a finite number of bits, leading to rounding errors and loss of precision.


## Exercise 6
def f(x):
    return x * (x - 1)

def derivative(x, delta):
    return (f(x + delta) - f(x)) / delta

x = 1
deltas = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]

for delta in deltas:
    approx_derivative = derivative(x, delta)
    true_derivative = 2 * x - 1

    print(f"For delta = {delta}, the approximate derivative is {approx_derivative}.")
    print(f"The true derivative is {true_derivative}.")

    if approx_derivative == true_derivative:
        print("Oh, you got lucky! The approximate and true derivatives are the same.")
    else:
        print("The approximate and true derivatives won't agree perfectly because of the approximation error.")

    print("---------------------------------------------------------")

# As the value of delta decreases, the accuracy of the approximation increases


## Exercise 7
import math
import timeit

def semicircle(x):
    return math.sqrt(1 - x**2)

def riemann_integral(N):
    h = 2 / N
    integral_sum = 0

    for k in range(N):
        x_k = -1 + (k * h) + (h / 2)
        y_k = semicircle(x_k)
        integral_sum += y_k * h

    return integral_sum

N = 100
approx_integral = riemann_integral(N)
true_integral = math.pi / 2

print(f"For N = {N}, the approximate integral is {approx_integral}.")
print(f"The true integral is {true_integral}.")

error = abs(approx_integral - true_integral)
print(f"The error in the approximation is {error}.")

time_taken = timeit.timeit(lambda: riemann_integral(N), number=1)
print(f"The computation took {time_taken} seconds.")
