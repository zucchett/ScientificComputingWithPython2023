import math
import timeit
import numpy as np

#Exercise 1
def base_convert(x,out_type):
    # Check the input base
    input_type = 0
    if x[0:2] == "0b":
        if set(x[2:]).issubset({'0','1'}):
            input_type = 2
            print("Bin input")

    elif x[0:2] == "0x":
        if set(x[2:]).issubset({'0','1','2','3','4','5','6','7','8','9',
                               'A','B','C','D','E','F',
                               'a','b','c','d','e','f'}):
            input_type = 16
            print("Hex input")

    else:
        if set(x).issubset({'0','1','2','3','4','5','6','7','8','9'}):
            input_type = 10
            print("Dec input")

    if input_type == 0:
        return print("No valid input")

    # Check the output base
    if out_type == "2":
        print(bin(int(x,input_type)))

    elif out_type == "10":
        print(int(x,input_type))

    elif out_type == "16":
        print(hex(int(x,input_type)))

    else:
        print("No valid output base")

def exercise1():
    x = input("Input a value: ") 
    out_type = input("Output representation: ")
    base_convert(x,out_type)


#Exercise2
def exercise2():
    bin_str = '110000101011000000000000'

    if not set(bin_str).issubset({'0','1'}):
        return print("Invalid input binary string")

    s = bin_str[0]
    e = bin_str[1:9]
    m = bin_str[9:]

    print("Sign: ",s)
    print("Exponent: ",e)
    print("Mantissa: ",m)

    if s == '1':
        dec_str = f"-1.{int(m,2)}*2^{int(e,2)}"
    else:
        dec_str = f"1.{int(m,2)}*2^{int(e,2)}"

    print("Single precision decimal representation: ",dec_str)


#Exercise 3
def exercise3():
    temp = 1.0
    underflow_limit = temp

    while temp > 0:
        underflow_limit = temp
        temp /= 2

    temp = 1.0
    overflow_limit = temp

    while temp < float('inf'):
        overflow_limit = temp
        temp *= 2

    print("Underflow limit: ", underflow_limit)
    print("Overflow limit: ", overflow_limit)


#Exercise 4
def exercise4():
    machine_precision = 1.0
    prev = 1.0
    act = prev + machine_precision

    while abs(prev - act) > 0:
        prev = act
        act += machine_precision
        machine_precision /= 2

    print("Machine precision for floating point numbers: ",machine_precision)


#Exercise 5
def solve_quadratic_a(a,b,c):
    delta = b**2 - 4*a*c

    if delta < 0:
        return print("No real solution")

    return ( (-b+math.sqrt(delta))/(2*a) , (-b-math.sqrt(delta))/(2*a) )

def solve_quadratic_b(a,b,c):
    delta =  b**2 - 4*a*c

    if delta < 0:
        return print("No real solution")

    num_plus = (-b + math.sqrt(delta)) * (-b - math.sqrt(delta))
    den_plus = (2*a)*(-b - math.sqrt(delta))

    num_minus = (-b - math.sqrt(delta)) * (-b + math.sqrt(delta))
    den_minus = (2*a)*(-b + math.sqrt(delta))
    return (num_plus/den_plus , num_minus/den_minus)


def solve_quadratic_c(a,b,c):
    delta =  b**2 - 4*a*c

    if delta < 0:
        return print("No real solution")

    num_plus = (-b + math.sqrt(delta))
    den_plus = (2*a)
    x1 = (num_plus/den_plus)*((-b + math.sqrt(delta))/(-b + math.sqrt(delta)))

    num_minus = (-b - math.sqrt(delta))
    den_minus = (2*a)
    x2 = (num_minus/den_minus)*((-b - math.sqrt(delta))/(-b - math.sqrt(delta)))

    return (x1,x2)

def exercise5():
    a,b,c = 0.001, 1000, 0.001
    print("a) ",solve_quadratic_a(a,b,c))
    print("b) ",solve_quadratic_b(a,b,c))
    # The above solutions differ from a very small amount
    # This is because mixing round off given by multiplying numerator and denominator separately
    print("c) ",solve_quadratic_c(a,b,c))


#Exercise6
def f6(x):
    return x*(x-1)

def exercise6():
    # (a)
    x, delta = 1, 0.01
    df = (f6(x+delta)-f6(x))/delta #f'(1) = 2*1 - 1 = 1
    dist = (df-1)**2

    print(f"delta: {delta}\t df/dx: {df}\t accuracy: {dist}")

    # (b)
    deltas = [10**-4, 10**-6, 10**-8, 10**-10, 10**-12, 10**-14]
    for d in deltas:
        dfs = ((f6(x+d)-f6(x))/d)
        dist = (dfs-1)**2
        print(f"delta: {d}\t df/dx: {dfs}\t accuracy: {dist}")

    # From an analytical point of view delta has to be infinetisimally small
    # Given that the float representation is finite we can achieve
    # only an approximation of the real value which becomes more accurate
    # as delta gets smaller and smaller


#Exercise 7
def f7(x):
    return math.sqrt(1-x**2)

def riemann_integral(N):
    h = 2/N
    I = 0

    # Pre calculate the funtion values
    yk = []
    for i in np.linspace(-1,1,N):
        yk.append(f7(i))

    # Riemann definition of integral
    for k in range(0,N):
        I += h*yk[k]

    return I

def exercise7():
    I = riemann_integral(100)
    I_approx = 1.570779632679

    print(f"Using the Riemann definition of integral I' = {I}")
    print("The riemann result differ from I of : ", abs(I-I_approx))

    timer = timeit.timeit("riemann_integral(2500000)",'from __main__ import riemann_integral',number=1)
    print(f"With N = {2500000} the computation needs {timer} s < 1 s")

    # Uncomment to run it for one minute
    #I1 = riemann_integral(60*3000000)
    #print("In running for 1 minute the result differ from I of : ", abs(I1-I_approx))
    print("There is a gain of five orders of magnitude in running it for 1 minute (the difference from I is ~1.6685389012449647e-05")


exercise1()
exercise2()
exercise3()
exercise4()
exercise5()
exercise6()
exercise7()
