#1
print("#1")
def convert_number(num, output_type):
    if isinstance(num, str):
            num = num.strip() 
            if num.startswith('0x'):
                input_type = 'hex'
                num = num[2:]  
            elif num.startswith('0b'):
                input_type = 'bin'
                num = num[2:]  
            else:
                input_type = 'dec'
        
    elif isinstance(num, int):
            input_type = 'dec'

    if input_type == 'dec':
        if output_type == 'bin':
            return bin(num)[2:]
        elif output_type == 'hex':
            return hex(num)[2:]
    
    elif input_type == 'bin':
        if output_type == 'dec':
            return str(int(num, 2))
        elif output_type == 'hex':
            return hex(int(num, 2))[2:]
    
    elif input_type == 'hex':
        if output_type == 'dec':
            return str(int(num, 16))
        elif output_type == 'bin':
            return bin(int(num, 16))[2:]

print(convert_number('0b1010', 'dec'))


#2
print("\n#2")
def bin_to_float(string):
    if string[0] == '0':
        sign = '+'
    else:
        sign = '-'

    exp_component = string[1:9]
    exponent = int(exp_component, 2)

    mantissa = 1
    for i,j in enumerate(string[9:]):
        n = int(j)/(2**(i+1))
        mantissa += n

    number = mantissa*(2**(exponent-127))
    print(f'sign: {sign}')
    print(f'factional part of mantissa: {mantissa-1}')
    print(f'exponent: {exponent}')
    
    return sign + str(number)

binary_value = '110000101011000000000000'
print(bin_to_float(binary_value))


#3
print("\n#3")
value = 1.0
while value / 2.0 != 0.0:
    value /= 2.0
print("Approximate Underflow Limit:", value)

value = 1.0
while value * 2.0 != float('inf'):
    value *= 2.0
print("Approximate Overflow Limit:", value)

#4
print("\n#4")
value = 1.0
while 1.0 + value != 1.0:
    value /= 2.0
print("Machine Precision:", value)

#5
import math
#a
def quadratic(a, b, c):
    if (b ** 2 - 4 * a * c) < 0:
        return "No real roots"
    else:
        x1 = (-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
        x2 = (-b-math.sqrt((b**2)-(4*a*c)))/(2*a)
        return x1, x2

#b
print("\n#5b")
def quadratic_2(a, b, c):
    if (b ** 2 - 4 * a * c) < 0:
        return "No real roots"
    else:
        x1 = (2 * c) / (-b - math.sqrt((b**2)-(4*a*c)))
        x2 = (2 * c) / (-b + math.sqrt((b**2)-(4*a*c)))
        return x1, x2
        
print('a: ', quadratic(0.001, 1000, 0.001))
print('b: ', quadratic_2(0.001, 1000, 0.001))

## Comparison of the first and second results:
# First result (quadratic): (x1 = -9.999894245993346e-07, x2 = -999999.999999).
# Second result (quadratic_2): (x1 = -1.000000000001e-06, x2 = -1000010.5755125057)
# There is a noticeable difference between x1 and x2 values of both solutions.
# Second result slighly larger in magnitude than first result.

# Both results have issues with precision due to limitations in floating-point representation.
# when we subract two numbers of almost equal magnitude, we lose precision 
# For x2 of the qudratic function, we perform subtraction between numbers of similar magnitudes in the numerator
# and for x1 in the quadratic_2 function we perform a subraction between numbers of close magnitudes in the denominator
# and this leads to the loss of precision in both cases

#c
print("\n#5c")
def quadratic_accurate(a, b, c):
    if (b ** 2 - 4 * a * c) < 0:
        return "No real roots"
    else:        
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = c / (a * x1)
        return x1, x2

print('c: ', quadratic_accurate(0.001, 1000, 0.001))


#6
#a
print("\n#6a")
def func(x):
    return x * (x-1)

def derivative(x, delta):
    derivative = (func(x + delta) - func(x)) / delta
    return derivative

def analytical_derivative(x):
    return 2 * x - 1

# Point of interest
x = 1

numerical_derivative = derivative(x, 1e-2)
true_derivative = analytical_derivative(x)
error = abs(numerical_derivative - true_derivative)
    
print(f"Delta = {1e-2}:")
print(f"Numerical Derivative: {numerical_derivative}")
print(f"True Derivative: {true_derivative}")
print(f"Error: {error}\n")

# There is a difference in the results from the analytical method and the numerical method because, 
# of limitations due to the machine precision of the computer's float representation, 
# so extremely small delta values might not result in significant improvements.

#b
print("\n#6b")
delta_values = [1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]
# Calculate and compare derivatives for different delta values
for delta in delta_values:
    numerical_derivative = derivative(x, delta)
    true_derivative = analytical_derivative(x)
    error = abs(numerical_derivative - true_derivative)
    
    print(f"Delta = {delta}:")
    print(f"Numerical Derivative: {numerical_derivative}")
    print(f"True Derivative: {true_derivative}")
    print(f"Error: {error}")
    print()
    
#from the results above, 
#the error gets bigger as delta gets larger which means that the accuracy improves as delta decreases.

#7
import timeit
print("\n#7a")
#(a)
# Function to calculate the integral using the Riemann sum
def integral(N):
    h = 2 / N
    integral = 0.0
    for k in range(1, N + 1):
        x_k = -1 + k * h
        y_k = (1 - x_k ** 2) ** 0.5
        integral += h * y_k
    return integral

# True value of the integral
true_value = 1.57079632679

# Integral with N = 100
computed_integral = integral(100)

error_100 = abs(computed_integral - true_value)
print(f"Integral with N = {100}: {computed_integral}")
print(f"True value: {true_value}")
print(f"Error (N = 100): {error_100}")

# For N=100, the difference between the true value and the computed value is 0.001662071240749574

print("\n#7b")
# (b)
N = 100
max_execution_time = 1.0  # 1 second

while True:
    N *= 2
    time_N = timeit.timeit("integral(N)", globals=globals(), number=1000)
    
    if time_N >= max_execution_time:
        N //= 2
        break

print(f"Maximum N for 1-second execution: {N}")

# Calculate execution time for the maximum N within 1 second
time_max_N = timeit.timeit("integral(N)", globals=globals(), number=1000)

# to run for less than a minute, the maximum value of N is 800
# and the gain after running for N=800 is 0.0015885779968440872
error_800 = abs(integral(800)-true_value)

# Calculate the gain in running for 1 minute
print(f"Result, after running for 1-minute: {integral(800)}")
print(f"Error (N = 800): {error_800}")
print(f"Gain: {abs(error_800 - error_100)}")
