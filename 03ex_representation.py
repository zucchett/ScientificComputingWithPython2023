import math as m
import numpy as np
import time 
import timeit
import cmath as cm

#------------TASK 1------------#

def convert_num_to_bin_hex(num:int, choose_conv):
    if (choose_conv == 'b'):
        bin_num = bin(num)
        return bin_num

    if (choose_conv == 'h'):
        hex_num = hex(num)

        return hex_num 

hex_n1 = convert_num_to_bin_hex(11,'h')
bin_n1 = convert_num_to_bin_hex(11,'b')
print(f'Task 1: \n Decimal representation of {bin_n1} : {int(bin_n1, 2)} \n')
print(f'Decimal representation of {hex_n1} : {int(hex_n1, 16)} \n')

#------------TASK 2------------#

def convert_32_bit_to_float(bin_str):
    bias = 127
    if len(bin_str) != 32:  
        raise ValueError("Input must be a 32-bit binary string")

    #Extract the sign bit, exponent bits, and mantissa bits as integers
    s = int(bin_str[0], 2)
    e_int = int(bin_str[1:9], 2)
    frac_int = int(bin_str[9:], 2)

    sign = (-1) ** s

    exponent = e_int - bias

    # Calculate the mantissa
    mantissa = 1.0
    for i in range(1, 24):  # 24 bits in the mantissa for single-precision
        if frac_int & (1 << (23 - i)):
            mantissa += 2 ** (-i)

    # Calculate the final floating-point value
    float_num = sign * mantissa * 2 ** exponent

    return float_num

x = '11000010101100000000000011100101'
print(f'Task 2: \n The binary string {x} converted to floating point: {convert_32_bit_to_float(x)} \n') 


#------------TASK 3------------#
# Initialize variables to 1
def over_under_flow(underflow_limit, overflow_limit):
    if (underflow_limit) > 0:
        #Halve the underflow limit until it reaches zero
        while underflow_limit / 2 > 0:
            underflow_limit /= 2

    else:
        while underflow_limit / 2 < 0:
            underflow_limit /= 2
        
    if (overflow_limit) > 0:  
        #Double the overflow limit until it reaches infinity
        while overflow_limit * 2 != float('inf'):
            overflow_limit *= 2

    else:
        while overflow_limit * 2 != float('-inf'):
            overflow_limit *= 2

    return underflow_limit, overflow_limit


num = 1.0

underflow_lim, overflow_lim = over_under_flow(num, num)
print(f"Task 3: \n Approximate Underflow Limit: {underflow_lim} \n Approximate Overflow Limit: {overflow_lim} \n")


#------------TASK 4------------#
num = 1.0
machine_p = 1.0

def machine_precision(orig_num, machine_p):
    while orig_num + machine_p != orig_num:
        machine_p /= 2
    return machine_p


print(f"Task 4: \n Machine Precision: {machine_precision(num, machine_p)} \n")
#------------TASK 5------------#

def quadratic_solution(a,b,c):
    if (type(a) or type(b) or type(c)) == str:
        raise ValueError("Input must be a number")
    square = m.sqrt(b**2 - 4*a*c)
    sol_1 = (-b + square) / 2*a
    sol_2 = (-b - square) / 2*a

    return sol_1, sol_2

#------a------#
a = 0.001
b = 1000
c = 0.001
sol1, sol2 = quadratic_solution(a,b,c)
print(f'Task 5a: \n One solution is: {sol1} and the other is: {sol2}')

#uttrykk, x2 = c/(a*x1), if (pos-pos ca like store: ikke nøyaktig minus), check if b is neg --> hvis neg så 
# blir det pos og da vil du ikke at x1 skal være pos-pos så kalkulerer du x2 ut fra dette 

#------b------#

def re_express_quad(a,b,c):
    if b < 0:
        sol_1 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
    else:
        sol_1 = (-b - np.sqrt(b**2 - 4*a*c))/(2*a)
    sol_2 = c /(a*sol_1) #sol_1 * sol_2 = a/c

    return sol_1, sol_2

sol_1, sol_2 = re_express_quad(a,b,c)

print(f'Task 5b: \n One solution is: {sol_1} and the other is: {sol_2} \n')
#By putting the same sign in front of the root as (-b) in re_express_quad one avoids the cancellation error: when
#you take one large positive number and subtracting another large positive number you can get precision errors.
#This results in different results from the two functions. 

print(f'Task 5c:')

def all_quadratic_sol(a,b,c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0: 
        sol1, sol2 = re_express_quad(a,b,c)
        print('Has two roots')
        return sol1, sol2
    
    if discriminant == 0:
        sol = -b/2*a
        print('Has a double root')
        return sol, None

    if discriminant < 0:
        print('Has two complex roots')
        if b < 0:
            sol_1i = (-b + cm.sqrt(discriminant))/(2*a)
            sol_2i = c /(a*sol_1i) 
        else:
            sol_1i = (-b - cm.sqrt(discriminant))/(2*a)
            sol_2i = c /(a*sol_1i) 
        return sol_1i, sol_2i

x_1, x_2 = all_quadratic_sol(a,b,c)
print(f'Root 1: {x_1} and root 2: {x_2} \n')

a = 1
b = 2
c = 1
x_1, x_2 = all_quadratic_sol(a,b,c)

print(f'Root 1: {x_1} and root 2: {x_2} \n')

a = 4
b = 2
c = 1
x_1, x_2 = all_quadratic_sol(a,b,c)

print(f'Root 1: {x_1} and root 2: {x_2} \n')

#------------TASK 6------------#
def f(x):
    func = x * (x - 1)
    return func
#------a------#
def calculate_derivative(func, delta, x):
    derivative_func = (func(x + delta) - func(x)) / delta
    return derivative_func

x = 1
delta = 10**(-2)

derivative = calculate_derivative(f, delta, x)

print(f"Task 6: \n The derivative of f(x) at x = {x} is approximately {derivative} \n")

#The derivative of x(x-1) = 2x-1. If x = 1 --> 2*1 - 1 = 1, It will not agree completely because 
#when I calculate it manually I don´t calculate the function for different delta. 
#My program estimates the derivative by making a small change in delta and seeing how much the output changes. 
#This is like finding the slope of a curve by drawing a line between two points on the curve.

#------b------#

def different_delta_val(lower_lim, upper_lim, func, x):
    for i in range(lower_lim, upper_lim + 1, 2):
        exponent = -i
        delta = 10 ** exponent
        derivative = calculate_derivative(func, delta, x)
        print(f'The derivative using 10^{exponent} is: {derivative}')
        print(f'And the distance from the true value 1 is: {derivative - 1} \n')

different_delta_val(4, 14, f, x)

#The accuracy when scaling delta is increasing (i.e. it is closer to the true value),
#and then it is decreasing again. That probably has something to do with when you subtract a number with another almost alike number
#some problems with accuracy occurs

#------------TASK 7------------#
def calculate_integral(N):
    h = 2 / N
    x_values = np.linspace(-1, 1, N)
    y_values = np.sqrt(1 - x_values**2)
    I = h * np.sum(y_values)
    return I

#------a------#
true_I = np.pi / 2
N = 100

result = calculate_integral(N)
print(f'The result of the integral with N = {N} is: {result} \n The distance from the true value is: {true_I - result} \n')
#The distance is smaller when N increases

#------b------#
def calculate_time_for_N(N):
    time_taken = timeit.timeit(lambda: calculate_integral(N), number=1)
    result = calculate_integral(N)
    return time_taken, result

def find_N_for_time(max_time):
    N = 100
    run_time, result = calculate_time_for_N(N)

    while run_time < max_time:
        if run_time >= max_time:
            break
        N *= 2
        run_time, result = calculate_time_for_N(N)

    return N, run_time, result


max_time_1_sec = 1 
N_for_1_sec, run_time_1_sec, result_1_sec = find_N_for_time(max_time_1_sec)
print(f'N for less than 1-second computation: {N_for_1_sec}, and the runtime was: {run_time_1_sec}')
print(f'Result for N={N_for_1_sec}: {result_1_sec} \n')

#Commented out the 1-minute part because it takes some time
'''
max_time_1_minute = 60  
N_for_1_minute, run_time_1_min, result_1_min = find_N_for_time(max_time_1_minute)
print(f'N for 1-minute computation: {N_for_1_minute}, and the runtime was: {run_time_1_min}')
print(f'Result for N={N_for_1_minute}: {result_1_min}')
#When making the code run for 1 minute you get a value that is closer to the real value of I,
#but the code that runs for 1 second is also pretty accurate
'''