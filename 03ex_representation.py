#EXERCISES WEEK No 3
#Suly Vannesa Cifuentes Bohorquez
#Student ID: 2080663

import math # Ex5
import numpy as np # Ex5
#-------------------------------------- EX. #1 Number representation-------------------------------------

print("\nEXERCISE # 1 \n")

def conv_integer_rep(input_value, output_format): 
    ##Define the function input value to convert, and output, if we want bin, dec, or hex
    try:
        if output_format not in ["bin", "dec", "hex"]:
            raise ValueError("Output format must be 'bin', 'dec', or 'hex'.") ## Error control 

        if isinstance(input_value, int):  ##Compare if it's a decimal
            if output_format == "bin":
                result = bin(input_value)
            elif output_format == "dec":
                result = input_value
            elif output_format == "hex":
                result = hex(input_value)
            return result
        
        elif isinstance(input_value, str): ## here we check if the value is a tring and then it its bin or hex
            input_value = input_value.strip()

            if input_value.startswith("0b"):
                if output_format == "dec":
                    result = int(input_value, 2)
                elif output_format == "hex":
                    result = hex(int(input_value, 2))
                else:
                    result = input_value
            elif input_value.startswith("0x"):
                if output_format == "dec":
                    result = int(input_value, 16)
                elif output_format == "bin":
                    result = bin(int(input_value, 16))
                else:
                    result = input_value
            else:
                if output_format == "bin":
                    result = bin(int(input_value))
                elif output_format == "hex":
                    result = hex(int(input_value))
                else:
                    result = int(input_value)
            return result
        else:
            raise ValueError("Input must be an integer or a string.") ## Error control 
    except ValueError as e:
        return str(e)

# Input for the number and output format
input_value = input("Enter an integer or its representation: ")
output_format = input("Enter the output format you want (bin, dec, or hex): ")

result = conv_integer_rep(input_value, output_format) ## Call the function to convert the number
print(f"Converted number: {result}")


#-------------------------------------- EX. #2 32-bit floating point number-------------------------------------

print("\nEXERCISE # 2 \n")


## Definition taken from https://www.geeksforgeeks.org/ieee-standard-754-floating-point-numbers/

def bin_to_float(binary_str): 
    ## def function to convert from bin to float with . number
    
    try:
        if len(binary_str) != 32:
            raise ValueError("Input binary must be 32 bit.") ## Error control

        # Here we separate the bit string
        sign_bit = int(binary_str[0])
        exponent_bit = binary_str[1:9]
        fraction_bit = binary_str[9:]

        # Convert sign of the mantissa where 0 represents a positive number while 1 represents a negative number.
        sign = -1 if sign_bit == 1 else 1

        # The exponent value: A bias is added to the actual exponent in order to get the stored exponent.
        exponent = int(exponent_bit, 2) - 127

        # Calculate the fraction value
        fraction = 1
        for i in range(len(fraction_bit)):
            fraction += int(fraction_bit[i]) * 2 ** -(i + 1)

        # The mantissa is part of a number in scientific notation or a floating-point number,
        #consisting of its significant digits. Here we have only 2 digits, i.e. O and 1
        decimal_value = sign * fraction * 2 ** exponent

        return decimal_value
    except ValueError as e:
        return str(e)

#capture  the value to convert
binary_str = input("Enter a 32-bit binary to convert: ")

#call the function 
result = bin_to_float(binary_str)
print(f"Converted decimal value: {result:.10f}")

#-------------------------------------- EX. #3 Underflow and overflow-------------------------------------
print("\nEXERCISE # 3 \n")

##overflow and underflow happen when we assign
#a value that is out of range of the declared data type of the variable. 


def find_underflow_lim():
    
    #first we defined the function to find the underflow
    #this occurs when a number is too close to zero that can't be represented
    
    underflow_limit = 1.0 #Initial Limit
    halved_value = 1.0

    while underflow_limit > 0:
        halved_value /= 2.0 ##simulates the process of the limit getting closer to 0
        if underflow_limit - halved_value == 0:  ##when it's zero means that the limit has been reached
            break
        underflow_limit = halved_value

    return underflow_limit

def find_overflow_lim():
       #first we defined the function to find the overflow
       #occurs when the number is too big to be represented accurately 
       
    overflow_limit = 1.0
    doubled_value = 1.0

    while overflow_limit < float('inf'):
        doubled_value *= 2.0
        if overflow_limit == doubled_value: ## does the opposite to the underflow function duplicating the value
            break
        overflow_limit = doubled_value

    return overflow_limit

underflow_lim = find_underflow_lim()
overflow_lim = find_overflow_lim()

#Print the results
print(f"Underflow limit: {underflow_lim}")
print(f"Overflow limit: {overflow_lim}")

#-------------------------------------- EX. #4 Machine precision-------------------------------------
print("\nEXERCISE # 4 \n")

#The machine precision or Machine epsilon (ϵm) is defined as
#the distance (gap) between 1 and the next largest floating point number.

def find_machine_p():
    machine_precision = 1.0
    increment = 1.0

    while 1.0 + increment != 1.0:
        machine_precision = increment
        increment /= 2.0 # decreces the increment value to find the smallest gap

    return machine_precision

machine_precision = find_machine_p()

print(f"Machine precision: {machine_precision:.10f}")


#-------------------------------------- EX. #5 Quadratic solution-----------------------------------------

print("\nEXERCISE # 5 \n")

## part A
def quadratic_stand(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check if the discriminant is non-negative
    if discriminant >= 0:
        # Compute the two solutions
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    else:
        return "No real solutions"

# a=0.001, b=1000, and c=0.001
a = 0.001
b = 1000
c = 0.001
solutions = quadratic_stand(a, b, c)
print("Standard Formula Solutions:")
print("Root 1:", solutions[0])
print("Root 2:", solutions[1])

## Part B
def quadratic_reex(a, b, c):
    
    discriminant = b**2 - 4*a*c
    
    if discriminant >= 0:
        root1 = (-2*c) / (-b + math.sqrt(discriminant))
        root2 = (-2*c) / (-b - math.sqrt(discriminant))
        return root1, root2
    else:
        return "No real solutions"

#  a=0.001, b=1000, and c=0.001 using re-expressed formula
solutions_reexpressed = quadratic_reex(a, b, c)
print("\nRe-expressed Formula Solutions:")
print("Root 1:", solutions_reexpressed[0])
print("Root 2:", solutions_reexpressed[1])

### Part C

def quadratic_numpy(a, b, c):
    
    roots = np.roots([a, b, c])
    return tuple(roots)

solutions_numpy = quadratic_numpy(a, b, c)
print("\nNumpy Solutions:")
print("Root 1:", solutions_numpy[0])
print("Root 2:", solutions_numpy[1])

#-------------------------------------- EX. #6 The derivate-----------------------------------------

print("\nEXERCISE # 6 \n")

def function(x):
    return x * (x - 1)

def derivative_def(x, s):
    f_x = function(x)
    f_x_s = function(x + s)
    df_dx = (f_x_s - f_x) / s
    return df_dx

def true_derivative(x):
    return 2 * x - 1

x = 1

print("Derivative:", true_derivative(x))

s_values = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]

for s in s_values:
    approximate_derivative = derivative_def(x, s)
    print(f"Approximate Derivative (s = {s}):", approximate_derivative)


#-------------------------------------- EX. #7 Integral of a semicircle-----------------------------------------




