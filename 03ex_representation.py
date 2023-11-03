import math
import timeit

#Exercice1

def convert_number(input_number, output_format):
    if output_format == 'bin':
        return bin(input_number)
    elif output_format == 'hex':
        return hex(input_number)
    elif output_format == 'dec':
        if isinstance(input_number, str):
            if input_number.lower().startswith('0x'):
                return int(input_number, 16)
            elif input_number.startswith('0b'):
                return int(input_number, 2)
            else:
                return int(input_number)
        else:
            return input_number
#Exercice2
def binary_to_float(binary_str):   
    sign = (-1) ** int(binary_str[0])
    exponent = int(binary_str[1:9], 2) - 127
    mantissa_bits = binary_str[9:]
    mantissa = 1.0
    for i, bit in enumerate(mantissa_bits):
        mantissa += int(bit) * 2 ** -(i + 1)

    return sign * 2 ** exponent * mantissa

#Exercice3
def find_under_over_flow():
    underflow = 1.0
    while underflow / 2.0 != 0.0:
        underflow /= 2.0
    overflow = 1.0
    while overflow * 2.0 != float('inf'):
        overflow *= 2.0
    return underflow,overflow

#Exercice4
def find_machine_precision():
    precision = 1.0
    smaller_value = 1.0

    while 1.0 + smaller_value != 1.0:
        precision = smaller_value
        smaller_value /= 10.0

    return precision

#Exercice5


def first_formula(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return None  
    else:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        return root1, root2


a = 0.001
b = 1000
c = 0.001
first_solutions = first_formula(a, b, c)
print("Solutions with the 1st formula:", first_solutions)


def second_formula(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return None  
    else:
        root1 = 2*c / (-b - math.sqrt(d))
        root2 = 2*c / (-b + math.sqrt(d))
        return root1, root2


second_solutions = second_formula(a, b, c)
print("Solutions with the 2nd Formula:", second_solutions)


def third_formula(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return None  # No real roots
    else:
        if b >= 0:
            root1 = (-b - math.sqrt(d)) / (2 * a)
            root2 = (2 * c) / (-b - math.sqrt(d))
        else:
            root1 = (2 * c) / (-b + math.sqrt(d))
            root2 = (-b + math.sqrt(d)) / (2 * a)
        return root1, root2


third_solutions = third_formula(a, b, c)
print("Solutions 3rd Formula:", third_solutions)

#Exercice6

def f(x):
    return x*(x-1)
def numerical_derivative_f(x,ep):
    return (f(x+ep) - f(x))/ ep
def analytical_derivative_f(x):
    return 2*x - 1
ep = 1e-2
print("For ep = 1e-2:")
print ("Analytical derivative of f at the point x=1 = ", analytical_derivative_f(1))
print ("Numerical derivative of f at the point x=1 = ", numerical_derivative_f(1, ep))
print ("Error= ", abs(analytical_derivative_f(1) - numerical_derivative_f(1, ep)))

#The numerical derivative and the analytical derivative are not the same since delta will never reach 0,  so there's always a small error.


eps = [1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]
for e in eps: 
    print("For ep = :" , e)
    print ("Numerical derivative of f at the point x=1 = ", numerical_derivative_f(1, e))
    print ("Error= ", abs(analytical_derivative_f(1) - numerical_derivative_f(1, e)))

#The closer is delta to 0, the closer is the numerical derivative to the analytical derivative.


#Exercice7
def semi_cercle(x):
    return math.sqrt(1 - x**2)

def Riemann(N):
    h= 2/N
    r = 0
    for k in range (N):
        xk = -1 + k*h
        yk = semi_cercle(xk)
        r += h*yk
    return r

N = 100
true_value = math.pi /2
print ("For N = 100 the Reimann integral = ", Riemann(N))
print ("True value = ", true_value)

#7b
while True:
    execution_time = timeit.timeit(lambda: Riemann(N), number=1)
    if execution_time > 1: 
        break
    N *= 2
print ("computation < 1s, the largest N is ", N )


G = N*60 //execution_time
print ("The gain in running in 1 minute is ", G)