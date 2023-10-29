import math 
import timeit

################## EXERCISE 1 ##################
print("\n##### 03ex_numberRepresentation #####")
print("\n##### EXERCISE 1 #####")

# function that accepts a number in
# binary, decimal or hexadecimal 
# representation and converts it
# into the desidered form 
def convertion(number, rep):
    try:
        # input is binary
        if(number[0:2] == "0b" or number [0:3] == "-0b"):
            curr_rep = "bin"
        # input is hexadeciaml
        elif(number[0:2] == "0x" or number [0:3] == "-0x"):
            curr_rep = "hex"
        # input is decimal
        else:
            test = int(number)
            curr_rep = "dec"
            
        # dec->bin
        if(curr_rep == "dec" and rep == "bin"):
            print("The binary representation of your number is:", bin(int(number)))
        # dec->hex
        elif(curr_rep == "dec" and rep == "hex"):
            print("The hexadecimal representation of your number is:", hex(int(number)))
        # bin->dec
        elif(curr_rep == "bin" and rep == "dec"):
            print("The decimal representation of your number is:", int(number,2))
        # bin->hex
        elif(curr_rep == "bin" and rep == "hex"):
            print("The hexadecimal representation of your number is:", hex(int(number,2)))  
        # hex->dec
        elif(curr_rep == "hex" and rep == "dec"):
            print("The decimal representation of your number is:", int(number,16))
        # hex->bin
        elif(curr_rep == "hex" and rep == "bin"):
            print("The binary representation of your number is:", bin(int(number,16)))
        elif(curr_rep == rep):
            print("Your number is already in this representation")
        else:
            print("Please, enter a valid representation")
    except:
        print("Something goes wrong...")
        
                
# example
n = "253"
print("Example, using the decimal", n,":")
convertion(n, "bin")
convertion(n, "hex")
   
# testing
x = input("Enter your number: ")
print("For the type enter \"bin\" for binary, \"dec\" for decimal or \"hex\" for hexadecimal")
type = input("Enter the desidered representation: ")
convertion(x,type)


input("\npress enter to go on...")


################## EXERCISE 2 ##################
print("\n\n##### EXERCISE 2 #####")

def sinPrecFloat(number):
    try:
        # taking the sign
        if number[0] == "0":
            s = 1
        elif number[0] == "1":
            s = -1
        else:
            print("Please, enter a valid value")
            return 
        
        # taking the exponent
        e = number[1:9]
        e = "0b" + e
        e = int(e,2)
        
        # taking the fractional part of the mantissa
        f = number[9:]
        mantissa = 1
        for i in range(23):
            mantissa += int(f[i])/(2**(i+1))

        # computing the result
        return s*(mantissa)*(2**(e-127))
    except:
        print("Something goes wrong...")
        

# example
x = "00000011111000000000000000000000"
print("Testing with", x,":")
print("The single precision floating point in decimal representation is:", sinPrecFloat(x), "\n")

# testing 
mystring  = input("Please, enter a 32-bit binary string: ")
if(len(mystring) != 32):
    print("Your string is not 32 bits long")
    print("I will proceed to fill the remaining bits to zero")
    mystring = mystring.ljust(32, '0')
    print("The resulting string is:", mystring)
print("The single precision floating point in decimal representation is:", sinPrecFloat(mystring))

input("\npress enter to go on...")



################## EXERCISE 3 ##################
print("\n\n##### EXERCISE 3 #####")

def findLimits():

    # Overflow computation
    over = 1.0
    iterations = 1500
    i = 1
    final_iter = -1
    max_value = -1

    while i < iterations:
        temp = over
        over = over * 2
        # overflow condition for float
        if over == float('inf'):
            final_iter = i
            i = iterations
            max_value = temp
        else:
            i += 1
    if max_value != -1 and final_iter != -1:
        print("The maximum founded values is", max_value, "at iteration",final_iter)
    else:
        print("Overflow computation: something goes wrong...")

    # Underflow computation
    under = 1.0
    iterations = 1500
    i = 1
    final_iter = -1
    min_value = -1

    while i < iterations:
        temp = under
        under = under / 2
        # underflow condition for float
        if under == 0.0:
            final_iter = i
            i = iterations
            min_value = temp
        else:
            i += 1
    if min_value != -1 and final_iter != -1:
        print("The minimum founded values is", min_value, "at iteration",final_iter)
    else:
        print("Underflow computation: something goes wrong...")

# testing
findLimits()


input("\npress enter to go on...")



################## EXERCISE 4 ##################
print("\n\n##### EXERCISE 4 #####")

# initial parameters
x = 100
i = 1
max = 20

print("We start from a value of", x, "and, at each iteration, we subtract an increasingly smaller value.\n")
print("Process...")

# computing loop
while i < max:
    y = x - 0.1 * 10**-(i-1)
    print(y)
    if y == x:
        print("\nThe final index is:", i)
        print("In conclusion, the maximum accuracy is achieved by", i, "decimals.")
        i = max
    else: 
        i += 1


input("\npress enter to go on...")




################## EXERCISE 5 ##################
print("\n\n##### EXERCISE 5 #####")


# part a)
def quadratic1(a, b, c):
    try:
        numerator1 = (-b - math.sqrt(b**2 - 4*a*c))
        numerator2 = (-b + math.sqrt(b**2 - 4*a*c))
        denominator = 2*a

        x1 = numerator1 / denominator
        x2 = numerator2 / denominator

        return (x1, x2)
    
    except:
        print("The solutions are not real")

# part b)
def quadratic2(a, b, c):
    try:
        numerator1 = (-b - math.sqrt(b**2 - 4*a*c))
        numerator2 = (-b + math.sqrt(b**2 - 4*a*c))
        denominator = 2*a
        x1 = ((-b - math.sqrt(b**2 - 4*a*c))*(-b + math.sqrt(b**2 - 4*a*c))) / (2*a*(-b + math.sqrt(b** - 4*a*c)))
        x2 = ((-b + math.sqrt(b**2 - 4*a*c))*(-b - math.sqrt(b**2 - 4*a*c))) / (2*a*(-b - math.sqrt(b**2 - 4*a*c)))

        x1 = (numerator1*numerator2) / (denominator*numerator2)
        x2 = (numerator2*numerator1) / (denominator*numerator1)
        
        return (x1, x2)

    except:
        print("The solutions are not real")

def quadratic3(a, b, c):
    try:
        if b >= 0:
            x1 = (-b - math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a) 
            x2 = c / (a * ((-b - math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)))
            return(x1, x2)
        else:
            x1 = (-b + math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a) 
            x2 = c / (a * ((-b - math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)))
            return(x1, x2)
    except:
        print("The solutions are not real")
    
# reuslts
a = 0.001
b = 1000
c = 0.001
print("a) Using quadratic1:", quadratic1(a,b,c))
print("b) Using quadratic2:", quadratic2(a,b,c))
print("c) Accurately in all cases:", quadratic3(a, b, c), "\n")

# testing
print("Solve quadratic ax^2+bx+c=0")
try:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    print("a) Your solution using quadratic1:", quadratic1(a,b,c))
    print("b) Your solution using quadratic2:", quadratic2(a,b,c))
    print("c) Your solution accurately in all cases:", quadratic3(a, b, c), "\n")
except:
    print("Please, enter valid numbers")


# part b)
#
# we can notice that x2 has the same value for both
# the computations, instead x1 changes and becomes 
# a litte more accurate. this is due to errors in 
# operations with floats, since Python’s floats are 
# stored internally as binary numbers, converting a 
# float to or from a decimal string usually involves
# a small rounding error.
# in particular in our case, values variations are 
# so small that the precision of the computer is 
# not enough.



input("\npress enter to go on...")




################## EXERCISE 6 ##################
print("\n\n##### EXERCISE 6 #####")

# f(x) = x(x-1)
def f(x):
    return x*(x-1)

# first derivate of f(x)
def df(x, delta):
    return (f(x+delta) - f(x)) / delta

# exponent
e = [2, 4, 6, 8, 10, 12, 14, 16]
x = 1

# results
print("Analitically f(x=1)' =", 2*x -1)
min_err = 1
min_err_index = -1
for i in e:
    curr_df = df(x,10**-i)
    if i < 9:
        print("For delta = 10^-" + str(i)," :", curr_df)
    else:
        print("For delta = 10^-" + str(i),":", curr_df)
    if abs(curr_df - 1) < min_err:
        min_err = abs(curr_df - 1)
        min_err_index = i

if min_err_index != -1:
    print("The best accury result is obtained using delta = 10^-" + str(min_err_index), "with an error of", min_err)

# part a)
#
# the reason for which  we donnot obtain the correct result, when delta = 10^-2,
# is beacuse Python does not correctly compute the value of f(x+delta)
# in particual the error occurs when we try to do: 1.01 - 1
# this happens because computers represent floating point numbers as binary, 
# and it turns out that storing a precise decimal fraction as binary is not 
# possible
#
#
# part b)
#
# the accuracy grows increasing the value of the exponent, until reaching an
# apparently maximum for 10^-8, after that it decreases a little bit and then 
# for index bigger than 16 the value degenerates to 0, due to the fact that
# floats can only have a limited number of meaningful decimal places


input("\npress enter to go on...")




################## EXERCISE 7 ##################
print("\n\n##### EXERCISE 7 #####")

# semi-circle funtion
def semCircle(x):
    return math.sqrt(1-pow(x,2))

# Riemann definition of the integral:
def riemann(N):
    h = 2 / N
    sum = 0
    step = 2 / (N - 1)
    interval = [-1.0 + i * step for i in range(N)]
    for k in interval:
        sum += h * semCircle(k)
    return sum


# reuslts

N = 100
print("Analitic result:", math.pi / 2)
print("Computed result:", riemann(N), "using N =", N)
# The computed result is quite close to real one, but not equal

code = """
import math
def semCircle(x):
    return math.sqrt(1-pow(x,2))
def riemann(N):
    h = 2 / N
    sum = 0
    step = 2 / (N - 1)
    interval = [-1.0 + i * step for i in range(N)]
    for k in interval:
        sum += h * semCircle(k)
    return sum
N = 7150000
print("Computed result:", riemann(N), "using N =", N)
"""
# making some test on my working hardware I discovered that using
# N = 7150000 the running time is almost close to 1 sec, but of course
# this parameter can change depending on the working space.
print("Computation time:", timeit.timeit(code, number = 1))
# using a larger sliding window we can achieve a more precise reuslt
# than the one obtained using N = 100.
# instead, even if we try to run the code for 1 min, we will not
# obtain significat upgrades to justify the so huge computational 
# time.


