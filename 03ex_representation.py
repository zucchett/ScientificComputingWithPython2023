#Number Reprpesentation
print('\n\n___________________Number Representation___________________\n')


def converter(n, out_base):
    try:
        if n[:2] == '0X':
            n_dec = int(n, 16)
        elif n[:2] == '0B':
            n_dec = int(n, 2)
        else:
            n_dec = int(n)
    except ValueError:
        print('\n\nError! Invalid input format. Please enter a number')
        return None  
    
    if out_base == 16:
        return hex(n_dec)
    elif out_base == 2:
         return bin(n_dec)
    elif out_base == 10:
         return n_dec        
       
the_input = input('\ntype a number taking into accout that: \nif the base is 2 it must contain "0B" at the beginning \nif the base is 16 it must contain "0X" at the beginning\n\n')


try:
    the_out_base = int(input('\ntype the new base you want to convert the number to (2, 10 or 16):   '))
    result = converter(the_input, the_out_base)
    if result is not None:
        print('\nthe number ', the_input, ' converted in base ', the_out_base, ' is ', result)
except:
    print('\nError! Invalid output base')
    
    
#32-bit floating point number
print('\n\n___________________32-bit floating point number___________________\n')


def single_precision_converter(the_number):

        sign_bit = the_number[0]
        exponent_bits = the_number[1:9]
        mantissa_bits = the_number[9:]
       
        try:
            exponent_dec = int(exponent_bits, 2)
            mantissa_dec = int(mantissa_bits, 2) * 2**(-len(mantissa_bits))
        
            float_number = (1 + mantissa_dec) * 2**(exponent_dec - 127)
            if sign_bit == '1':
                float_number = -float_number
        
            return float_number
        except: 
            print('\nError! The string must contain only 0 and 1 values')
            return None
  

input_number1 = '110000101011000000000000'
input_number2 = '11000001001101110101010101101011'
input_number3 = '01000011000001011010111010110110'
input_number4 = '01001001110101011010100010111110'

result1 = single_precision_converter(input_number1)
if result1 is not None:
    print('\nThe string ', input_number1, ' represents the flaoting number ', result1)
    
result2 = single_precision_converter(input_number2)
if result2 is not None:
    print('\nThe string ', input_number2, ' represents the flaoting number ', result2)
    
result3 = single_precision_converter(input_number3)
if result3 is not None:
    print('\nThe string ', input_number3, ' represents the flaoting number ', result3)
    
result4 = single_precision_converter(input_number4)
if result4 is not None:
    print('\nThe string ', input_number4, ' represents the flaoting number ', result4)
    
    
#Underflow and overflow
print('\n\n___________________Underflow and overflow___________________\n')


over_limit = float(1)

while over_limit != float('inf'):
    previous_over_limit = over_limit
    over_limit = over_limit * 2

print("\nOverflow limit (accuracy factor 2):", previous_over_limit)


under_limit = float(1)

while under_limit != float(0):
    previous_under_limit = under_limit
    under_limit = under_limit / 2
    
print("\nUnderflow limit (accuracy factor 2):", previous_under_limit)


#Machine precision
print('\n\n___________________Machine precision___________________\n')

number1 = 1.0
number2 = 0.1

while number1-number2 != number1:
    previous_number2 = number2
    number2 = number2/10
    
print('\nPrecison limit: (accuracy factor 10)', previous_number2)


#Quadratic solution
print('\n\n___________________Quadratic solution___________________\n')
from math import sqrt 

a = 0.001
b = 1000
c = 0.001

def quadratic_solver1(a, b, c):
    try:
        delta = b**2 - 4*a*c
        if delta < 0:
            print('Error! Delta is less than zero')
            return None
        
        x1 = (- b - sqrt(delta))/(2*a)
        x2 = (- b + sqrt(delta))/(2*a)
        
        return [x1, x2]
    except:
        print('Error! Input values not allowed')
        return None
        
def quadratic_solver2(a, b, c):
    try:
        delta = b**2 - 4*a*c
        if delta < 0:
            print('Error! Delta is less than zero')
            return None
        
        x1 = (- b - sqrt(delta))*(- b + sqrt(delta))/((2*a)*(- b + sqrt(delta)))
        x2 = (- b + sqrt(delta))*(- b - sqrt(delta))/((2*a)*(- b - sqrt(delta)))
        
        return [x1, x2]
    except:
        print('Error! Input values not allowed')
        return None
    
solutions1 = quadratic_solver1(a, b, c)
print('\nFirst function')
if solutions1 is not None:
    print('The first solution for a = ', a, ' b = ', b, ' c = ', c, ' is x1 = ', solutions1[0])
    print('The second solution for a = ', a, ' b = ', b, ' c = ', c, ' is x2 = ', solutions1[1])    
    
solutions2 = quadratic_solver2(a, b, c)
print('\nSecond function')
if solutions2 is not None:
    print('The first solution for a = ', a, ' b = ', b, ' c = ', c, ' is x1 = ', solutions2[0])
    print('The second solution for a = ', a, ' b = ', b, ' c = ', c, ' is x2 = ', solutions2[1])
    
#We can notice that the values of x1 computed by the two functions are different: this is because the new operations at numerator and denominator introduce an approximation error. The reason why this apporximation error comes out conists in the accuracy limit of binary floating number representation.  

import cmath
def quadratic_solver3(a, b, c):
    try:
        delta = b**2 - 4*a*c
    
        x1 = (- b - cmath.sqrt(delta))/(2*a)
        x2 = (- b + cmath.sqrt(delta))/(2*a)
        
        return [x1, x2]
    except:
        print('Error! Input values not allowed')
        return None
    
solutions3 = quadratic_solver3(a, b, c)
print('\nThird function')
if solutions3 is not None:
    print('The first solution for a = ', a, ' b = ', b, ' c = ', c, ' is x1 = ', solutions3[0])
    print('The second solution for a = ', a, ' b = ', b, ' c = ', c, ' is x2 = ', solutions3[1])    


    
#The derivative
print('\n\n___________________The derivative___________________\n')

def the_function(x):
    try:
        return x*(x-1)
    except:
        print('Input value is not valid')
        return None
  
value_in_one = the_function(1)

deltas_list = [1e-2,1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]
derivatives_list = []
for delta in deltas_list: 
    value_close_one = the_function(1 + delta)
    value_derivative = (value_close_one - value_in_one) / delta
    derivatives_list.append(value_derivative)

for delta, derivative in zip(deltas_list, derivatives_list):
    print('\nThe derivative of the function in 1 when delta is ', delta, ' is ', derivative)
    print('Error: ', 1 - derivative)
    
#From the ouput we can notice that the error decreases when delta goes from 0.01 to 1e-08, but for smaller values of delta the accuracy is worse. 



#Integral of a semicircle
print('\n\n___________________Integral of a semicircle___________________\n')
from math import sqrt
import timeit

def semicircle_function(x):
    return sqrt(1.0 - x**2)

def riemann_integral(N, f):
    summation = 0
    h = 2.0 / N
    x = -1
    for i in range(N):
        summation = summation + f(x)
        x = x + h
    
    return (summation * h)

N = 100
result = riemann_integral(100, semicircle_function)
print('Integral with N = 100: ', result)
print('The obatained value differs from the expected one by ', 1.57079632679 - result)
print('\n\n')

a = timeit.timeit(stmt='riemann_integral(N, semicircle_function)', globals=globals(), number=1)
while a<1:
    print('Integral with N = '+str(N)+' computed in time '+str(a))
    N = N+300000
    a = timeit.timeit(stmt='riemann_integral(N, semicircle_function)', globals=globals(), number=1)
    
N = N-300000

print("\nThe max value of N which requires less than one second is approximately: \n"+str(N)+", for this value of N the integral result is: "+str(riemann_integral(N, semicircle_function)))
print("N was increased with a step equal to 300000")

print("Difference between the expected result and the one obtained with the largest N is: ", 1.57079632679 - riemann_integral(N, semicircle_function))
#Of course, if the execution time can last for 1 minute we can use a smaller intervals for the rectangles in the sum and this means a better accuracy in the computation

