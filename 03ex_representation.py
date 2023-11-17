# 1. Number representation
num = 10100
print(type(num))
def convert_num(num, opt):
    print(num, opt)
    type_num = type(num)
    print(type_num)
    if opt == "din_to_dec":
        din_dec = int(num, 2)  # 2-10
        print("Value in dec:", din_dec)
    elif opt == "bin_to_hex":
        bin_hex = hex(int(num, 2))  # 2-16
        print("Value in hex:", bin_hex)
    elif opt == "dec_to_hex":
        dec_hex = hex(num)[2:]  # 10-16
        print("Value in dec:", dec_hex)
    elif opt == "dec_to_bin":
        dec_bin = bin(num)[2:]  # 10-2
        print("Value in dec:", dec_bin)
    elif opt == "hex_to_dec":
        hex_bin = bin(int(num, 16))  # 16-2
        print("Value in dec:", hex_bin)
    elif opt == "hex_to_dec":
        hex_dec = int(num, 16)  # 16-10
        print("Value in dec:", hex_dec)
    return


input_num = input("write a number: ")
input_opt = input("write another argument to choose the output representation: ")

convert_num(input_num, input_opt)


# 2. 32-bit floating point number
a ="11000000101100000000"
def floating(x):
    x = str(x)
    s = list(x[0])
    e = list(x[1:9])
    m = list(x[10:])

    exp = 0b11000000
    print(bin(exp & 128))
    for i in e:
        exp = ((exp | 128) >> int(i))

    print(exp)
floating(a)


#3. Underflow and overflow
num = 999
un_flow = 1
ov_flow = 1

for i in range(num):
    un_flow = un_flow / 2
    ov_flow = ov_flow * 2
    print(i, "\t", ":%1.5e" % un_flow, "\t", ":%1.5e" % ov_flow)


#4. Machine precision
num = 20
var = 7
sam = 1/9

for i in range(num):
    var = var + sam
    sam = sam * (1/9)
    print(i, "\t\t", var)

print("After 14th step there is no effect on the number")

#5. Quadratic solution

import math
def qu_result():
    # a = float(input('input a: '))
    # b = float(input('input b: '))
    # c = float(input('input c: '))
    a = 0.001
    b = 1000
    c = 0.001

    # a)
    d = float((b ** 2) - (4 * a * c))
    sol1 = ((-b) - math.sqrt(d)) / (2 * a)
    sol2 = ((-b) + math.sqrt(d)) / (2 * a)
    print('a) THE SOLUTION ARE {0} AND {1}'.format(sol1, sol2))

    # b)
    d = float((b ** 2) - (4 * a * c))
    factor = ((-b) - math.sqrt(d))
    sol1 = (((-b) - math.sqrt(d)) * factor) / ((2 * a) * factor)
    sol2 = (((-b) + math.sqrt(d)) * factor) / ((2 * a) * factor)

    print('b) THE SOLUTION ARE {0} AND {1}'.format(sol1, sol2))
    ##a) THE SOLUTION ARE -999999.999999 AND -9.999894245993346e-07
    ##b) THE SOLUTION ARE -999999.999999 AND -9.999894245993346e-07

# c)
def qua_normal( a = 0.001, b = 1000,c = 0.001):
    # a = float(input('input a: '))
    # b = float(input('input b: '))
    # c = float(input('input c: '))
    d = float((b ** 2) - (4 * a * c))
    if d > 0 and a != 0:
        num_roots = 2
        d = float((b ** 2) - (4 * a * c))
        sol1 = ((-b) - math.sqrt(d)) / (2 * a)
        sol2 = ((-b) + math.sqrt(d)) / (2 * a)
        print("c) THE SOLUTION ARE {} AND {}" .format(sol1, sol2))
    elif d == 0 and a != 0:
        num_roots = 1
        x = (-b) / 2 * a
        print("ONE ROOT IS: ", x)
    else:
        num_roots = 0
        print("SORRY,NO ROOTS PLEASE ENTER AGAIN < 0.")
        exit()


qu_result()

qua_normal()

#6. The derivative

from sympy import *
# a)-2
x = Symbol("x")
f = x * (x - 1)
df = diff(f, x)
df = lambdify(x, df)
print("Result of the function : ", df(1))


# a)-2
def f(x):
    return x * (x - 1)


def true_value(fx, vx):
    b = 1e-2  # 等于10的-2次方
    df = fx(vx + b) - fx(vx)
    dx = b
    result = df / dx
    return float("%f" % result)


print("Result of the function with b=0.01: ", true_value(f, 1))


# b)
def f(x):
    return x * (x - 1)


def other_value(fx, vx, b):
    df = fx(vx + b) - fx(vx)
    dx = b
    result = df / dx
    return float("%f" % result)


b = 1e-2
for i in range(0, 6):
    b = b * 1e-2
    print("Result of the function with b ", "%.14f" % b, ":", other_value(f, 1, b))



#7. Integral of a semicircle