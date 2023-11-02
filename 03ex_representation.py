
#-------------

def changeRepresentation(number, outputType):
    try:
        if number.startswith('0b'):
            n_dec = int(number, 2)
        elif number.startswith('0x'):
            n_dec = int(number, 16)
        else:
            n_dec = int(number)
    except ValueError:
        print("Input is not a valid number in the specified format.")
        return

    n_bin = bin(n_dec)
    n_hex = hex(n_dec)

    print("input number in",outputType,"will be :")
    if outputType.lower() == "d":
        print(n_dec)
    elif outputType.lower() == "b":
        print(n_bin)
    elif outputType.lower() == "h":
        print(n_hex)
    else:
        print("Invalid type. enter 'd' for decimal, 'b' for binary, or 'h' for hexadecimal.")

number = input("Enter the number: ")
outputType = input("Enter output type ('d: dec', 'b: bin', or 'h: hex'): ")
changeRepresentation(number, outputType)

#------2
def convert(n):
    sign_bit = n[0]
    exponent_bits = n[1:9]
    mantissa_bits = n[9:32]

    exponent = int(exponent_bits, 2) - 127
    mantissa = sum(int(bit) * 2**(-i - 1) for i, bit in enumerate(mantissa_bits))

    result = (1.0 + mantissa) * 2**exponent

    sign = '' if sign_bit == '0' else '-'
    return float(sign + str(result))

n1 = '01100001010110001110000000'
n2 = '10000010101100010011000000110000'
n3 = '0101111111100000101101001110000'
print(convert(n1))
print(convert(n2))
print(convert(n3))

#-----3
x = 1.0
for i in range(0, 1030):
    x = x * 2
    if (i > 1000):
        print("i :", i, " |||  x :", x)

# "x : (i:1022)" overflow.
print("***************")
y = 1.0
for i in range(0, 1080):
    y = y / 2
    if (i > 1050):
        print("i :", i, " |||  y :", y)

# "y : (i:1073)" : underflow.
#-----------4
x = 1.0
for i in range(0,20):
    y = x + 1.0 * 10**-i
    print("i :",i,"*** %.30f:"%x,"*** b :",y,"*** x == y :",x==y)


#---------5
import math

a = 0.001
b = 1000
c = 0.001
#*****a******
x11 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
x12 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
#*****b******
x21 = (2*c) / (-b - math.sqrt(b*b - 4*a*c))
x22 = (2*c) / (-b + math.sqrt(b*b - 4*a*c))
print("1th approach,  x1 :",x11)
print("1th approach,  x2 :",x12)
print("***")
print("2th approach, x1 :",x21)
print("2th approach, x2 :",x22)
print("****")
#The results turn out differently because each method is better at approximating one of the roots.Why is this happening?
#It all boils down to a tricky calculation involving a big number and a small one.
#When we calculate 'b*b', we're dealing with a big number, while '4a*c' is a small one. The math between them gets tricky due to how computers store floating-point numbers.
#In the first approach, we're approximating x = 0 / 2*a, whi;le in the second in  x ~= 2*c / 0
# # limitations of floating point numbers leads to different results.
#In each approach one of the roots is zero, so the calculated result for that root isn't entirely accurate.
#*******c********
x31 = -b/(2*a) + math.sqrt((b/(2*a))**2 - c/a)
x32 = -b/(2*a) - math.sqrt((b/(2*a))**2 - c/a)
print("approach 3,  x1 :",x31)
print("approach 3,  x2 :",x32)
# due to dangerous calculation I want to sidestep the calculation of (b^2 - 4ac) I reconfigured the shape
# I split it into two parts '-b/2a' and 'sqrt(b^2-4ac)/2a' and then factured out 2a
# it would be as : sqrt{(b/2a)^2 - c/a}


#*******6********
def df(delta):
    def f(x):
        return x * (x - 1)

    d = (f(1 + delta) - f(1)) / delta
    return d

dl = 1e-2
result = df(dl)
error = result - 1
print(dl, "\t Numerical Derivative", result, "\t --- error =", error)
dl = 1e-4
print(dl, "\t Numerical Derivative ", result, "\t --- error =", error)
dl = 1e-6
print(dl, "\t Numerical Derivative ", result, "\t --- error =", error)
dl = 1e-8
print(dl, "\t Numerical Derivative ", result, "\t --- error =", error)
dl = 1e-10
print(dl, "\t Numerical Derivative ", result, "\t --- error =", error)
dl = 1e-12
print(dl, "\t Numerical Derivative ", result, "\t --- error =", error)
dl = 1e-14
print(dl, "\t Numerical Derivative ", result, "\t --- error =", error)
# initially, reducing the 'delta' value improves accuracy, brings the function output closer to its true value = 1.
#However, at  certain point (around 1e-10), further reducing delta results in larger errors and reduced accuracy.
# around (1e-10) by decreasing delta,  makes bigger error and decreases accuracy.
# If we rewrite the derivative equation for x=1, it can be expressed as df = (1 + delta) (1 + delta -1) / delta
# When delta is not extremely small, the second parentheses (1 + delta - 1) simplifies to 'delta,' resulting in df = (1 + delta). It's evident that (1 + delta) is closer to 1 when delta is smaller.
# but when delta is extremely smalll, (1+ delta -1) != delta.
# In this case (1 + delta -1) ~= (1-1), and also (1 + delta)~= 1,
# so it would be df = (1 * 0) / delta. and its entierlry different.
# in this new formula when delta decreases, result gets larger,because its denominator.

#*************-----7-----******
import math
import timeit

def integrate(N):
    result = 0
    for i in range(-int(N/2), int(N/2)):
        x = i*2/N + 1/N
        result += 2/N * math.sqrt(1 - x*x)
    return result
#*-----
N1 = 100
result1 = integrate(N1)
deviation1 = result1 - math.pi/2
print(f"Approximation for N = {N1}: {result1:.30f}, Deviation from true value: {deviation1}")
#***
N2 = 5800000
result2 = integrate(N2)
deviation2 = result2 - math.pi/2
print(f"Approximation for N = {N2}: {result2:.30f}, Deviation from true value: {deviation2}")
#*****
N3 = 60 * N2
# Uncomment the following lines to calculate for N3
# result3 = integrate(N3)
# deviation3 = result3 - math.pi/2
# print(f"Approximation for N = {N3}: {result3:.30f}, Deviation from true value: {deviation3}")
print(f"Execution time per loop for N = {N2}: (please wait a moment)")
execution_time = timeit.timeit(lambda: integrate(N2), number=5) / 5
print(execution_time)
# As N increases, the deviation from the true value decreases, resulting in better accuracy, but the execution time also increases.
