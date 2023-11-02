#1. Number representation
print("\n\n---------- 1. Number representation ----------\n\n")
# Write a function that converts integer numbers among the bin, dec, and hex representations
# (bin<->dec<->hex). Determine the input type in the function, and pass another
# argument to choose the output representation.

def conversion (num, output_type):
    if output_type == bin:
        return bin(num)
    elif output_type == hex:
        return hex(num)
    elif output_type == int:
        return int(num)


print(conversion(0b01110,bin))

#2. 32-bit floating point number
print("\n\n---------- 2. 32-bit floating point number ----------\n\n")
# Write a function that converts a 32 bit binary string (for example, 110000101011000000000000)
# into a single precision floating point in decimal representation.
# Interpret the various bits as sign, fractional part of the mantissa and exponent,
# according to the IEEE 754 reccommendations.

def floating_to_decimal(x):
    x = str(x)
    s = list(x[0])
    e = list(x[1:9])
    m = list(x[10:])

    exp = 0b11000000
    print(bin(exp & 128))
    for i in e:
        exp = ((exp | 128) >> int(i))

    print(exp)
floating_to_decimal(110000101011000000000)

# 3. Underflow and overflow
print("\n\n---------- 3. Underflow and overflow ----------\n\n")
# Write a program to determine the approximate underflow and overflow limits
# (within a factor of 2) for floating point numbers on your computer.

# Hint: define two variables initialized to 1, and halve/double them for
# a sufficient amount of times to exceed the under/over-flow limits.

x = 1.0
y = x * 2.0
while ((x).hex() == (y/2).hex()):
     x = x * 2.0
     y = x * 2.0
print("The overflow limit is: ", x)

x = 1.0
y = x / 2.0
while ((x).hex() == (y*2).hex()):
     x = x / 2.0
     y = x / 2.0
print("The underflow limit is: ", x)

# 4. Machine precision
print("\n\n---------- 4. Machine precision ----------\n\n")
# Similarly to the previous exercise, write a program to determine the machine
# precision for floating point numbers.

# Hint: define a new variable by adding an increasingly smaller value and check when
# the addition starts to have no effect on the number.
import math
import timeit
x=1.0
precision=0.1
while (x + precision).hex() != x.hex():
    precision/=2

print("Machine precision is",precision)

# 5. Quadratic solution
print("\n\n---------- 5. Quadratic solution ----------\n\n")

def quadratic(a,b,c):
    delta = pow(b,2)-4*a*c
    return  (b*(-1)+math.sqrt(delta))/(2*a),(b*(-1)-math.sqrt(delta))/(2*a)

print("result for 𝑎=0.001 , 𝑏=1000 and 𝑐=0.001 is",quadratic(0.001,1000,0.001))

def quadraticB(a,b,c):
    delta = pow(b,2)-4*a*c
    factor1 = b*(-1)-math.sqrt(delta)
    factor2 = b*(-1)+math.sqrt(delta)
    print(factor1)
    print(factor2)
    return  (b*(-1)+math.sqrt(delta))*(factor1)/(2*a*factor1),(b*(-1)-math.sqrt(delta))*(factor2)/(2*a*factor2)

print("result for 𝑎=0.001 , 𝑏=1000 and 𝑐=0.001 is",quadraticB(0.001,1000,0.001))

def quadraticC(a,b,c):
    delta = pow(b,2)-4*a*c
    factor = 1e-30
    print(factor)
    return  (b*(-1)+math.sqrt(delta))*factor/(2*a*factor),(b*(-1)-math.sqrt(delta))*factor/(2*a*factor)

print(quadraticC(0.001,1000,0.001))

# 6. The derivative
print("\n\n---------- 6. The derivative ----------\n\n")
function_f = lambda x: x * (x - 1)

x = 1
delta = 1e-2
derivative = (function_f(x + delta) - function_f(x)) / delta
print("derivative with 1e-2", derivative)

# derivative of f(x)=x(x-1) is f'(x) = 2x-1
real_value = 2 * x - 1
print("real value:", real_value)

deltas = [1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]

for d in deltas:
    derivative = (function_f(x + d) - function_f(x)) / d
    print("delta", d, ":", derivative)

print("The accuracy increases when delta decreases, but at a certain point, whe "
      "delta reach 1e-10 the value starts to getting worst because of the "
      "floating point limitation")


# 7. Integral of a semicircle
print("\n\n---------- 7. Integral of a semicircle ----------\n\n")
import math
import timeit

def integral(N):
    sum = 0
    h = 2/N
    x = -1
    for k in range(1,N+1):
        sum += math.sqrt(1.0 - x**2)
        x+=h

    return sum*h


test_integral='''
def integral(N):
    sum = 0
    h = 2/N
    x = -1
    for k in range(1,N+1):
        sum += math.sqrt(1.0 - x**2)
        x+=h

    return sum*h
integral(5030000)
'''


print("integral with N=100 is",integral(100))

es1 = timeit.timeit(stmt=test_integral, setup="import math", number=1)

print("Time(in seconds) to run 10 times Integral function for N=5030000: ",es1)

true_value=math.pi/2
approx = integral(5030000)
diff = abs(true_value-approx)
print("true value:",true_value)
print("approx:",integral(5030000*60))
print("difference:",diff)

# Difference between true value and value calculated in 1 minute
# (with value N=5030000*60) is 2.1254864535080742e-10
