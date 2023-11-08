import numpy as np
import timeit

# Task 1. Number representation
def convert_number(num, new_format):
    num_str = str(num)
    if(num_str.startswith('0b', 2)):
        dec_num = int(num_str)
    elif(num_str.startswith('0x', 16)):
        dec_num = int(num_str)
    else: dec_num = int(num_str)

    if new_format == 'bin':
        return bin(dec_num)
    elif new_format == 'hex':
        return hex(dec_num)
    elif new_format == 'dec':
        return str(dec_num)
    else:
        raise ValueError("Invalid output format. Choose among 'bin', 'dec', or 'hex'.")
    
print('Task 1')
print(convert_number(1001, 'hex'))
print(convert_number(16, 'bin'))
print(convert_number(0x43b4, 'dec'))

# Task 2. Number representation
def bin_to_single_precision_float(bin_num):
    sign_bit = int(bin_num[0])
    exponent_bits = bin_num[1:9]
    mantissa_bits = bin_num[9:]

    sign = (-1) ** sign_bit
    exponent = int(exponent_bits, 2) - 127
    mantissa = 1 + sum([(int(bit) * (2 ** (-idx))) for idx, bit in enumerate(mantissa_bits, start=1)])

    single_precision_float_value = sign * mantissa * (2 ** exponent)
    return single_precision_float_value

print('Task 2')
binary_num = "110000101011000000000001100"
print(bin_to_single_precision_float(binary_num))


# Task 3. Underflow and overflow
def find_limits():
    underflow = 1.0
    overflow = 1.0
    previous_overflow = 0.5

    while underflow > 0:
        previous_underflow = underflow
        underflow /= 2.0

    while True:
        previous_overflow = overflow
        overflow *= 2.0

        if overflow > 1e308:  # Function would not run with a higher number
            break


    print(f"Approximate underflow limit: {previous_underflow}")
    print(f"Approximate overflow limit: {previous_overflow}")

print('Task 3')
find_limits()

# Task 4. Machine precision
def machine_precision():
    num = 1
    precision = 0.1
    while ((num + precision)!= num):
        precision /= 2.0

    print(f"Machine precision : {precision*2}")

print('Task 4')
machine_precision()

# Task 5. Quadratic solution
#Task 5a
def Quadratic_solution_a(a, b, c):
    x_1 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
    x_2 = (-b - np.sqrt(b**2 - 4*a*c))/(2*a)
    return x_1, x_2

#Task 5b
def Quadratic_solution_b(a, b, c):
    #by putting the same sign in front of the root as (-b) one avoids the cancellation error.
    if b < 0:
        x_1 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
    else:
        x_1 = (-b - np.sqrt(b**2 - 4*a*c))/(2*a)
    x_2 = c /(a*x_1)

    return x_1, x_2

#Task 5c
def Quadratic_accurate(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None, None 
    if abs(b + discriminant) < abs(b - discriminant):
        return Quadratic_solution_b(a, b, c)
    else:
        return Quadratic_solution_a(a, b, c)


print('Task 5')
print(Quadratic_solution_a(0.001, 1000, 0.001))
print(Quadratic_solution_b(0.001, 1000, 0.001))
print(Quadratic_accurate(0.001, 1000, 0.001))

# Task 6. The derivative
def f(x):
    return x*(x-1)

def derivative(x, delta):
    return (f(x + delta) - f(x)) / delta

# Analytical derivative of f(x) gives 2x-1

print('Task 6')
print('Analytical derivative of f(x) in x=1 gives 2*1-1 = 1 ')
print(f'Calculated derivative of f(x) in x = 1, with delta=10**-2: {derivative(1, 10**-2)}')
print(f'Calculated derivative of f(x) in x = 1, with delta=10**-4: {derivative(1, 10**-4)}')
print(f'Calculated derivative of f(x) in x = 1, with delta=10**-6: {derivative(1, 10**-6)}')
print(f'Calculated derivative of f(x) in x = 1, with delta=10**-8: {derivative(1, 10**-8)}')
print(f'Calculated derivative of f(x) in x = 1, with delta=10**-10: {derivative(1, 10**-10)}')
print(f'Calculated derivative of f(x) in x = 1, with delta=10**-12: {derivative(1, 10**-12)}')
print(f'Calculated derivative of f(x) in x = 1, with delta=10**-14: {derivative(1, 10**-14)}')
print('As delta decreases, the accuracy will initially increase.  However, after a certain threshold, the accuracy will decrease due to the subtractive cancellation and finite precision issues.')


# Task 7. Integral of a semicircle
def compute_integral(N):
    h = 2/N
    total = 0
    for k in range(N):
        x_k = -1 + h * (k + 0.5)
        y_k = np.sqrt(1 - x_k**2)
        total += h * y_k
    return total

print('Task 7a')
print(f"Integral value with N=100 is: {compute_integral(100)}")
print(f'Difference to the true value: {(np.pi/2)-compute_integral(100)}')

print('Task 7b')
N = 100
while True:
    elapsed_time = timeit.timeit(lambda: compute_integral(N), number=1)
    if elapsed_time > 1: 
        break
    N *= 2

print(f'Maximum N that can be computed within 1 second is roughly {N//2}')

N_1_min = N*60
print(f'Maximum N that can be computed within 1 second is roughly {N_1_min//2}')
print('Integral value with N=60*1638400 (1 minute) gave the result: 1.5707963267957112')
print(f'Difference to the true value in that case: -8.146816554699399e-13')

'''
res_1min = compute_integral(N_1_min)
print(f"Integral value with N=60*1638400 (1 minute) is: {res_1min}")
print(f'Difference to the true value: {(np.pi/2)-res_1min}')
'''