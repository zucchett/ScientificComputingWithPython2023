import math
from math import sqrt
import timeit

def ex1(x, output):
    try:
        if output == "bin":
            return bin(x)
        elif output == "dec":
            return int(x)
        elif output == "hex":
            return hex(x)
    except: 
        str = "Entered parameters are wrong"
        return str


def ex2(binary_string):
    print("2. 32-bit floating point number")
    if len(binary_string) > 32:
        print("Something wrong")
        
    while len(binary_string) != 32:
        binary_string = "0" + binary_string

    
    sign = binary_string[0]
    exponent = binary_string[1:9]
    mantissa = binary_string[9:]

    if sign == "1":
        sign = int(sign)*(-1)
    else:
        sign = int(sign) + 1

    exponent = int(exponent) - 127
    
    mant = 1
    for i in range(len(mantissa)):
        mant += int(mantissa[i]) * 2**(-i - 1)

    print(sign * mant * 2**exponent)
    print("\n#################################\n")


def ex3():
    print("3. Underflow and overflow")
    def under_limit():
        underflow_limit = 1.0
        halving_factor = 0.5
        x = 0

        while underflow_limit > 0:
            underflow_limit *= halving_factor
            print(underflow_limit)
            x += 1
        
        print("\n Underflow: "+ str(x) + "\n")

    def over_limit():
        overflow_limit = 1.0
        double_factor = 2
        x = 0
    
        while overflow_limit < float('inf'):
            overflow_limit *= double_factor
            print(overflow_limit)
            x += 1
    
        print("\nOverflow: "+ str(x))
        
    under_limit()
    over_limit()
    print("\n#################################\n")

def ex4():
    print("4. Machine precision:") 
    precision = 1.0
    smallest_increment = 1.0
    x = 0

    while precision + 1 != 1:
        smallest_increment = precision
        precision /= 2
        x += 1

    print(smallest_increment/2)
    print(x)
    print("\n#################################\n")

def ex5():
    print("5. Quadratic solution") 
    a = 0.001
    b = 1000
    c = 0.001
    
    def quadratic_calculator_a(a,b,c):
        d = math.sqrt(b**2 - 4*a*c)
        
        x1 = (-b - d)/(2*a)
        print(x1)
    
        x2= (-b + d)/(2*a)
        print(x2)
        print("\n")
    
    def quadratic_calculator_b(a,b,c):
        d = math.sqrt(b**2 - 4*a*c)
        
        x1 = ((-b - d)*(-b + d))/((2*a)*(-b + d))
        print(x1)
        print("More accurate " + str(round(x1, 6)))
    
        x2 = ((-b + d)*(-b - d))/((2*a)*(-b - d))
        print(x2)
    
    quadratic_calculator_a(a,b,c)
    quadratic_calculator_b(a,b,c)
    print("During the calculation in second case we perform additional arithmetic operations that can introduce small rounding errors, maybe it is because we use mory memory space during calculations. To correct this we can use function round.")
    print("\n#################################\n")

def ex6():
    print("6. The derivative")
    
    def f(x):
        return x * (x - 1)
    
    def calculate_derivative(x, delta):
        der = (f(x + delta) - f(x)) / delta
        return der
    
    def true_derivative(x):
        return 2 * x - 1
    
    x = 1  
    delta = [10**-2, 10**-4, 10**-6, 10**-8, 10**-10, 10**-12, 10**-14 ] 
    
    print("Approximate derivative delta equal to 10^-2 at x = 1 is " + str(calculate_derivative(x, delta[0])))
    print("True derivative at x = 1 is " + str(true_derivative(x)))
    
    absolute_error = abs(calculate_derivative(x, delta[0]) - true_derivative(x))
    print("Absolute error: " + str(absolute_error))

    for i in delta:
        print(calculate_derivative(x, i))

    print("\nWhen floating-point numbers are used, calculations that involve numbers with a higher number of decimal places may not produce accurate results. This is because the binary representation of such numbers does not provide sufficient precision for storing them accurately.")
    print("\n#################################\n")

def ex7():
    print("7. Integral of a semicircle")
    def integral(N):
        integral = 0
        x = -1
        for i in range (N):
            x += 1/N
            integral = integral + (sqrt(1 - x**2))*2/N
        return integral

           
    print("The result integral with  N=100 " + str(integral(100)))
    time = timeit.timeit(lambda: integral(100), number = 1)
    print("Time for integral with  N=100: " + str(time))

    print("N can be increased approx up to 2600000 if the computation needs to be run in less than a second") 
    print("The result integral with  N=2600000 " + str(integral(2600000)))
    time = timeit.timeit(lambda: integral(2600000), number = 1)
    print("Time for integral with  N=2600000 : " + str(time))
    print ("The gain in running it for 1 minute does not make sense because results are very close")
    

    

    

print("1. Number representation")        
print(ex1(7, "hex"))
print(ex1(0b11011, "dec"))
print(ex1(0x1b, "bin"))
print(ex1("hhjj", "bin"))
print("\n#################################\n")

binary_string = "110000101011000000000000"  
ex2(binary_string)

ex3()
ex4()
ex5()
ex6()
ex7()


