#QUESTION NUMBER 1
#SOLUTION

"""
1. Number representation

Write a function that converts numbers among the bin, dec, and hex representations (bin<->dec<->hex).
Determine the input type in the function, and pass another argument to choose the output representation.
"""

def converter(a):
    string = str(a)

    if string[1] == "x":
        print("a is hex, converting to int and bin")
        return int(a, 16), bin(int(a, 16))
    elif string[1] == "b":
        print("a is bin, converting to int and hex")
        return int(a, 2), hex(int(a, 2))
    else:
        try:
            print("a is int, converting to bin and hex")
            return bin(a), hex(a)
        except:
            print("a is not either an int, bin or hex number")
    return


for a in ["0b1010", "10", "0xa", "test"]:
    for type_n in ["bin", "hex", "dec", "test"]:
        print("converting ", a, " into ", type_n)
        print((a, type_n), "\n")
        print()
/////////////////////////////END OF QUESTION 1

#QUESTION NUMBER 2
#SOLUTION
"""
2. 32-bit floating point number

Write a function that converts a 32 bit binary string (for example, `110000101011000000000000`) into a single precision
floating point in decimal representation. Interpret the various bits as sign, fractional part of the mantissa and
exponent, according to the IEEE 754 recommendations.
"""
a = "110000101011000000000000"

def tofloat(w):
    e = int(w[1:9], 2)
    rang = [i for i in range(1, 24)]
    f = list(map(lambda x: x[0] * 2 ** (-x[1]), list(zip([int(x) for x in w[9:32]], rang))))
    print("f: ", f)
    n = (-1) ** int(w[0]) * 2 ** (e - 127) * (sum(f) + 1)
    print("mantissa: ", sum(f) + 1)
    print("exponent: ", e - 127)
    print("sign: ", (-1) ** int(w[0]))
    return n


print("Computing over a:", a, "which correspond to -88 in floating point representation with 32 bits\n")
print("\n Result: ", tofloat(a))
print()

////////////////////////////////END OF QUESTION 2

#QUESTION NUMBER 3
#SOLUTION

"""
3. Underflow and overflow

Write a program to determine the underflow and overflow limits (within a factor of 2) for floating point numbers on your
computer.

*Hint*: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed
the under/over-flow limits.
"""

import math

Min = 1
for i in range(1500):
    Tmp = Min / 2
    if Tmp == 0:
        print("Underflow limit found: ", Min, "Iteration number: ", i)
        break
    else:
        Min = Tmp

Max = 1.0
for i in range(10000):
    Tmp = Max * 2
    if Tmp == math.inf:
        print("Overflow limit found: ", Max, "Iteration number: ", i)
        break
    else:
        Max = Tmp
///////////////////////////////////END OF QUESTION 3

#QUESTION NUMBER 4
#SOLUTION
"""
4. Machine precision

Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.

Hint*: define a new variable by adding an increasingly smaller value and check when the addition starts to have 
no effect on the number.
"""

a = 1
for i in range(10000):
    tmp = a / 10
    if tmp != a:
        a = tmp
    else:
        print("Number of decimal of precision = ", i)
        break
///////////////////////////////////END OF QUESTION 4

#QUESTION NUMBER 5
#SOLUTION

"""
5. Write a function that takes in input three parameters $a$, $b$ and $c$ and prints out the two solutions to the
quadratic equation $ax^2+bx+c=0$ using the standard formula:
$$
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
$$

(a) use the program to compute the solution for $a=0.001$, $b=1000$ and $c=0.001$

(b) re-express the standard solution formula by multiplying the numerator and the denominator by
$-b\mp\sqrt{b^2-4ac}$ and again find the solution for $a=0.001$, $b=1000$ and $c=0.001$.
How does it compare with what has been previously obtained, and why?

(c) write a function that computes the roots of a quadratic equation accurately in all cases
"""

import math

a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))

# a with math.sqrt
print("\nResults with math.sqrt:")
print("\na)\nx1 = ", (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
print("x2 = ", (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))

# b with math.sqrt
print("\nb)\nx1 = ", ((-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)) * (-b + math.sqrt(b ** 2 - 4 * a * c)) / (
            -b + math.sqrt(b ** 2 - 4 * a * c)))
print("x2 = ", ((-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)) * (-b - math.sqrt(b ** 2 - 4 * a * c)) / (
            -b - math.sqrt(b ** 2 - 4 * a * c)))

# a with **.5
print("\n\nResults with **.5:")
print("\na)\nx1 = ", (((-b + (b ** 2 - 4 * a * c)) ** .5) / (2 * a)))
print("x2 = ", (((-b - (b ** 2 - 4 * a * c)) ** .5) / (2 * a)))
# b with **.5
print("\nb)\nx1 = ", (((-b + (b ** 2 - 4 * a * c)) ** .5) / (2 * a)) * ((-b + (b ** 2 - 4 * a * c)) ** .5) / (
            (-b + (b ** 2 - 4 * a * c)) ** .5))
print("x2 = ", (((-b - (b ** 2 - 4 * a * c)) ** .5) / (2 * a)) * ((-b - (b ** 2 - 4 * a * c)) ** .5) / (
            (-b - (b ** 2 - 4 * a * c)) ** .5))

# I couldn't find the difference of point b

# c
print("\nc)\nResults with math.sqrt() and math.fsum():")
print("\nx1 = ", (math.fsum([-b , math.sqrt(b ** 2 - 4 * a * c)]) / (2 * a)))
print("x2 = ", (math.fsum([-b, -math.sqrt(b ** 2 - 4 * a * c)]) / (2 * a)))
print()
///////////////////////////////////////END OF QUESTION 5

#QUESTION NUMBER 6
#SOLUTION
"""
6.The derivative

Write a program that implements the function $f(x)=x(x−1)$

(a) Calculate the derivative of the function at the point $x = 1$ using the derivative definition:

$$
\frac{{\rm d}f}{{\rm d}x} = \lim_{\delta\to0} \frac{f(x+\delta)-f(x)}{\delta}
$$

with $\delta = 10^{−2}$. Calculate the true value of the same derivative analytically and compare it with the answer
your program gives. The two will not agree perfectly. Why?

(b) Repeat the calculation for $\delta = 10^{−4}, 10^{−6}, 10^{−8}, 10^{−10}, 10^{−12}$ and $10^{−14}$. How does the
accuracy scale with $\delta$?
"""

f = lambda x: x * (x - 1)

d = (f(1 + 10 ** -2) - f(1)) / 10 ** -2

print("a) df/dx = ", d, "  The algorithm doesn't have enough numerical stability \n")

for b in [4, 6, 8, 10, 12, 14, 16]:
    print("Value of the derivative for delta = 10^-{} = ".format(b), (f(1 + 10 ** -b) - f(1)) / 10 ** -b)
    print()

# b) I would say that there is no precise correlation between delta and the result. The closest value is reached with 10^-8.
///////////////////////////////////////////END OF QUESTION 6

# QUESTION NUMBER 7
# SOLUTION
"""
7. **Integral of a semicircle**

Consider the integral of the semicircle of radius 1:
$$
I=\int_{-1}^{1} \sqrt(1-x^2) {\rm d}x
$$
which is known to be $I=\frac{\pi}{2}=1.57079632679...$.

Alternatively we can use the Riemann definition of the integral:
$$
I=\lim_{N\to\infty} \sum_{k=1}^{N} h y_k
$$

with $h=2/N$ the width of each of the $N$ slices the domain is divided into and where
$y_k$ is the value of the function at the $k-$th slice.

(a) Write a program to compute the integral with $N=100$. How does the result compare to the true value?

(b) How much can $N$ be increased if the computation needs to be run in less than a second? What is the gain in
running it for 1 minute? Use `timeit` to measure the time.
"""
from cmath import phase
from math import pi
import timeit


def semi_circle(x):
    return (1 - (x ** 2)) ** (1 / 2)


def integral(N, UpperLimit, LowerLimit, f):
    result = 0
    h = (UpperLimit - LowerLimit) / N  # 2/N
    for i in range(N):
        result = result + h * f(i)
    return phase(result)
# a)
N = 100
upper_limit = 1
lower_limit = -1
print("Result of integral: " + str(integral(N, upper_limit, lower_limit, semi_circle)))
print("pi / 2 = " + str(pi / 2))
# The difference between the true value and the result of the integral is 0.00020214747626989826

# b)
TimeStarts = timeit.default_timer()
integral(N * 12002, upper_limit, lower_limit, semi_circle)
TimeEnds = timeit.default_timer() - TimeStarts
print("Execution time for integral: " + str(TimeEnds) + " seconds")
# N can be multiplied approximately 12002 times for the computation needs
# to be run in less than a second.

TimeStarts = timeit.default_timer()
res = integral(N * 12002 * 60, upper_limit, lower_limit, semi_circle)
TimeEnds = timeit.default_timer() - TimeStarts
print("Execution time for integral: " + str(TimeEnds) + " seconds")
print("Result of (1 minute) integral: " + str(res))
print()
///////////////////////END OF QUESTION 7
