#Ex1
def ex1(input, output_type):
    
    if isinstance(input, str): #checking if input is a string
        if input.startswith('0b'):
            input_type = 'bin'
        elif input.startswith('0x'):
            input_type = 'hex'
        else:
            input_type = 'dec'
    elif isinstance(input, int): #checking if input is an integer
        input_type = 'dec'
    else:
        print("Input must be a string or integer")

    if input_type == 'bin':
        input = int(input, 2)
    elif input_type == 'hex':
        input = int(input, 16)

    if output_type == 'bin':
        return bin(input)
    elif output_type == 'hex':
        return hex(input)
    elif output_type == 'dec':
        return str(input)
    else:
        raise ValueError("Output type must be 'bin', 'dec', or 'hex'")

input = '0xF'
print("Input:{}".format(input))
print("Output (Binary): {}".format(ex1(input, 'bin')))
print("Output (Decimal): {}".format(ex1(input, 'dec')))

#----------------------------------------------------------------
#Ex2
def ex2(binary_str):
    bias = 127
    sign = int(binary_str[0], 2) # 1bit
    exponent = int(binary_str[1:9], 2) #8 bits
    mantissa = int(binary_str[9:], 2) #23 bits
    
    if exponent == 0 and mantissa == 0:
        return 0.0 if sign == 0 else -0.0
    
    f = 1.0;
    for i in range(1, 24): 
        f += ((mantissa >> (23 - i)) & 1) * 2**(-i)
    result = (-1)**sign * 2**(exponent - 127) * f
    return result

binary_str = "11000010101100000000000000000000"  # Example binary string
result = ex2(binary_str)
print(result)

#----------------------------------------------------------------
#Ex3
overflow= 1.0
underflow=1.0

while underflow / 2 >  0.0:
    underflow /= 2
while overflow * 2 < float('inf'):
    overflow *= overflow
print("Underflow limit:", underflow)
print("Overflow limit:", overflow)

#----------------------------------------------------------------
#Ex4
machine_precision= 1.0
while 1.0 + machine_precision / 2 > 1.0:
    machine_precision /= 2

print("Machine precision = ", machine_precision)

#----------------------------------------------------------------
#Ex5
import math

def ex5_a(a,b,c):
    delta = b**2 - 4*a*c
    if delta < 0:
        print("No real solution found")
    else:
        x1 = (-b + math.sqrt(delta)) / 2*a
        x2 = (-b - math.sqrt(delta)) / 2*a
        print("first solution X1:", x1)
        print("second solution X2:", x2)
print ("solutions with the first formula:")
ex5_a(0.001,1000,0.001)

def ex5_b(a,b,c):
    delta = b**2 - 4*a*c
    denominator = -b + math.sqrt(delta)
    if denominator == 0:
        print ("No real solution found")
    else:
        x1 = 2*c / denominator 
        x2 = 2*c / (-b - math.sqrt(delta))
        print("X1:", x1)
        print("X2:", x2)
print ("solutions with the second formula:")
ex5_b(0.001,1000,0.001)

def ex5_c(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        print("No real solution found")
    elif delta == 0:
        X = -b/(2*a)
        print("Only 1 solution:", X)
    else:
        x1 = (-b + math.sqrt(delta)) / 2*a
        x2 = (-b - math.sqrt(delta)) / 2*a
        print("first solution X1:", x1)
        print("second solution X2:", x2)
ex5_c(0.001,1000,0.001)

#----------------------------------------------------------------
#Ex6
def f(x):
    return x*(x-1)
def numerical_derivative_f(x,epsilon):
    return (f(x+epsilon) - f(x))/ epsilon
def analytical_derivative_f(x):
    return 2*x - 1
epsilon = 1e-2
print("For epsilon = 1e-2:")
print ("Analytical derivative of f at the point x=1 = ", analytical_derivative_f(1))
print ("Numerical derivative of f at the point x=1 = ", numerical_derivative_f(1, epsilon))
print ("Error= ", abs(analytical_derivative_f(1) - numerical_derivative_f(1, epsilon)))

#The numerical derivative and the analytical derivative didn't match perfectly because we can't make delta exactly zero, so there's always a small error in our calculation.
print("----------------------------------------------------------------")

epsilons = [1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]
for e in epsilons: 
    print("For epsilon = :" , e)
    print ("Numerical derivative of f at the point x=1 = ", numerical_derivative_f(1, e))
    print ("Error= ", abs(analytical_derivative_f(1) - numerical_derivative_f(1, e)))

#The smaller we make delta, the more accurate our approximation becomes, and the closer our numerical derivative gets to the true value (analytical derivative).

#----------------------------------------------------------------
#Ex7
import math
import timeit

#7a

def semi_cercle_integral(x):
    return math.sqrt(1 - x**2)

def Riemann_integral(N):
    h= 2/N
    res = 0
    for k in range (N):
        xk = -1 + k*h
        yk = semi_cercle_integral(xk)
        res += h*yk
    return res

N = 100
true_value = math.pi /2
print ("For N = 100 the integral = ", Riemann_integral(N))
print ("True value = ", true_value)

#7b
while True:
    execution_time = timeit.timeit(lambda: Riemann_integral(N), number=1)
    if execution_time > 1: #less than a second 
        break
    N *= 2
print ("For computation in less than a second the largest N is ", N )

#for 1 minute
G = N*60 //execution_time
print ("The gain in running in 1 minute is ", G)

