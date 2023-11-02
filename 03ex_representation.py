
#***************************************** NUMBER REPRESENTATION *****************************************
print('\n \n# ------------  NUMBER REPRESENTATION ------------ # \n \n')

def convert_in(number, output):
    if output == 'dec':
        return str(number)
    elif output == 'bin':
        return bin(number)
    elif output == 'hex':
        return hex(number)

import random
#test
number1 = random.randint(1, 6021)
output1 = "dec"
output2='bin'
output3='hex'
test1 = convert_in(number1, output1)
test2 = convert_in(number1, output2)
test3 =convert_in(number1, output3)
print(" Let's test NUMBER REPRESENTATION with a random  number each time  " , number1)
print("The converted integer for the output : ",output1 ," is " , test1)
print("The converted integer for the output :",output2 ," is " , test2)
print("The converted integer for the output : ",output3 ," is " , test3)


#***************************************** 32-bit floating point number *****************************************
print('\n \n# ------------ 32-bit floating point number------------ # \n \n')

def Binary_to_float(string):
    if len(string) != 32:
        print("The input binary string need to be 32 characters long")
    sign_bit = int(binary_str[0])
    exponent_bits = binary_str[1:9]
    fraction_bits = binary_str[9:]
    exponent = int(exponent_bits, 2) - 127

    fraction = 1.0
    for i in range(len(fraction_bits)):
        if fraction_bits[i] == '1':
            fraction += 1.0 / (2**(i + 1))

    res = (-1)**sign_bit * 2**exponent * fraction

    return res

#test

binary_str = ''.join(random.choice('01') for _ in range(32))
decimal_res = Binary_to_float(binary_str)
print(" The decimal representation of : ", binary_str, " is :", decimal_res)



#***************************************** Underflow and overflow *****************************************
print('\n \n# ------------ Underflow and overflow------------ # \n \n')


import sys
def Underflow_overflow():
    underflow_max =overflow_max= 1

    while underflow_max / 2 > 0.0:
        underflow_max /= 2

    while overflow_max * 2 < sys.float_info.max:
        overflow_max *= 2

    return underflow_max, overflow_max

underflow, overflow = Underflow_overflow()
print("The  underflow limit:", underflow , " And the overflow limit:", overflow)



#***************************************** Machine precision *****************************************
print('\n \n# ------------ Machine precision------------ # \n \n')

def Machine_precision():
    epsilon = 1

    if 1.0 + epsilon > 1.0:
        epsilon /= 2.0
    return epsilon

res = Machine_precision()
print("The smallest positive number that can be accurately represented in mymachine is :", res)



#***************************************** Quadratic solution *****************************************
print('\n \n# ------------Quadratic solution------------ # \n \n')


import math
def Quadratic(a, b, c):
    solution = set()
    dalta = b ** 2 - 4 * a * c

    if dalta >= 0:
        x1 = (-b - math.sqrt(dalta)) / (2 * a)
        x2 = (-b + math.sqrt(dalta)) / (2 * a)
        solution.add(x1)
        solution.add(x2)

    return solution
    # a/use the function to compute the solution for $a=0.001$, $b=1000$ and $c=0.001$
print("Using the function to compute the solution for $a=0.001$, $b=1000$ and $c=0.001$ :", Quadratic(0.001,1000,0.001))
# b part

def Quadratic_b(a, b,c):
    solution = set()
    dalta = math.sqrt(b ** 2 - 4 * a * c)

    if dalta >= 0:
        x1 = (2 * c) / (-b - dalta)
        x2 = (2 * c) / (-b + dalta)
        solution.add(x1)
        solution.add(x2)

    return solution

print(" For the question b after The re-express the standard solution formula the result for a=0.001 , b=1000 and c = 0.001 is :", Quadratic_b(0.001,1000,0.001))

# for a i found solution={-9.999894245993346e-07, -999999.999999} and for b i found
#solution = {-1.000000000001e-06, -1000010.575512505 this is due to the numerical precision of floating-point calculations
# . Both The 2 formulas are always used in math with a good precision but the differences in the results are within the range of numerical precision and should not be a cause for concern.

# C :


def Quadratic_c(a, b, c):
    dalta = b**2 - 4*a*c

    if dalta > 0:
        x1 = (-b - math.sqrt(dalta)) / (2*a)
        x2 = (-b + math.sqrt(dalta)) / (2*a)
        return {x1, x2}
    elif dalta == 0:
        solution = -b / (2*a)
        return {solution}
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(dalta)) / (2*a)
        x1 = complex(real_part, imaginary_part)
        x2 = complex(real_part, -imaginary_part)
        return {x1, x2}


print(" So finaly the accurate solution of the quadratic is:",  Quadratic_c(0.001, 1000, 0.001))



#***************************************** The derivative *****************************************
print('\n \n# ------------The derivative------------ # \n \n')


def Derivative(x):
    return x*(x-1)

#Question a
print("result question a")
x=1
delta = 0.01
print(" The derivative of X is ", Derivative(x))
derivate= (Derivative(x + delta) - Derivative(x)) / delta
print(" The derivative of X with delta = 0.01 ", derivate)
# there is a small diff :
# there is a small diff : i found that  The derivative of X is  0
#  and The derivative of X with delta = 0.01  1.010000000000001
# The small difference is due to the finite precision of floating-point arithmetic in my computer , this gives better precision


# Quuestion b
print("result question b")

list_delta = [0.0001, 0.000001, 0.00000001, 0.0000000001]
list_derivative = []

for delta in list_delta:
    derivative = (Derivative(x + delta) - Derivative(x)) / delta
    list_derivative.append(derivative)

print("For a list of Dalta we have this derivative : ", list_derivative)


# here i found derivative :  [1.0000999999998899, 1.0000009999177333, 1.0000000039225287, 1.000000082840371]
#These results indicate how the approximation of the derivative changes as the delta is getting smaller.
# The values approach 1, which is the true derivative of the function x.




#***************************************** Integral of a semicircle *****************************************
print('\n \n# ------------Integral of a semicircle------------ # \n \n')


def integral(n):
    width = 2/ n
    integral = 0

    for i in range(n):
        x = -1 + i * width
        y = math.sqrt(1 - x**2)
        area = width * y
        integral += area
    return integral

import timeit

n = 100
res = integral(n)
print(" The result for n =", n, "is", res)
print(" The true value is", math.pi / 2)

time_1s = timeit.timeit(lambda: integral(n), number=1)
print("Time to compute for n =", n, "is", time_1s, "seconds")

max_n_for_1s = int(n * time_1s)
print("The maximum n for 1 second:", max_n_for_1s)

n = 100000000
time_1min = timeit.timeit(lambda: integral(n), number=1)
print("The time to compute for n is", time_1min, "seconds")
