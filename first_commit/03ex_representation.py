##Number representation
x = input('Insert an integer number: ')
ty = input('Insert the output representation type (e.g. hex, bin, dec): ')

def isBin(x):
    try:
        int(x, 2)
        return True
    except:
        return False
    
def isHex(x):
    if 'x' in x:
        return True
    else:
        return False

def numtype(x, ty):
    if isBin(x):
        if ty == 'dec':
            return print(int(x, 2))
        elif ty == 'hex':
            y = int(x,2)
            return print(hex(y))
    elif isHex(x):
        if ty == 'dec':
            return print(int(x, 16))
        elif ty == 'bin':
            y = int(x,16)
            return print(bin(y))
    else:
        if ty == 'hex':
            return print(hex(int(x)))
        elif ty == 'bin':
            return print(bin(int(x)))
     
numtype(x, ty)


##32-bit floating point number
print("\n")
import math

y = input('Insert a 32 bit binary string: ')


def singlePrec(y):
    temp = ''
    
    #zero padding 
    for i in range(len(y), 32):
        temp += '0'
    x = temp + y
    print('32 bits sequence (after the padding):', x)
    
    #sign
    if x[0] == '0':
        sign = '+'
    elif x[0] == '1':
        sign = '-'

    #exponent
    exp = int(x[1:9], 2)    

    #mantissa
    mantissa = x[9:]
    fmantissa = 1.0 + sum([int(mantissa[i-1])*(2**(-i)) for i in range(1,len(mantissa))])
    
    #final floating point number
    number = fmantissa*(2**(exp-127))

    #dealing with special values
    if sign == '0' and exp == 255 and (fmantissa - 1) == 0:
        sign = '+'
        number = 'inf'

    if sign == '1' and exp == 255 and (fmantissa - 1) == 0:
        sign = '-'
        number = 'inf'

    if exp == 255 and (fmantissa - 1) > 0:
        sign = ''
        number = 'NaN'
    return sign + str(number)

r = singlePrec(y)
print('Single precision floating point in decimal representation: ', r)


##Underflow and overflow
print("\n")
x = 1.0
y = 1.0
index1 = 0
index2 = 0
xlist = []
ylist = []

while x < float('inf'):
    x = x*2
    xlist.append(x)
    index1 += 1
    
print('Overflow limit:', xlist[index1-2])

while y > 0.0:
    y = y/2
    ylist.append(y)
    index2 += 1

print('Underflow limit:', ylist[index2-2])


##Machine precision
print("\n")
x = float(4)

for i in range(1,17):
    print(f'For i = {i}: ', x + 1.0 * 10**-i)
#The machine precision for floating point numbers is 15 decimal places


##Quadratic solution
print("\n")
import math
import cmath

def quadraticEq(a, b, c):
    solutions = []
    solutions.append((-b+math.sqrt(b**2 - 4*a*c))/(2*a))
    solutions.append((-b-math.sqrt(b**2 - 4*a*c))/(2*a))
    return solutions

def requadraticEq(a, b, c):
    solutions = []
    solutions.append((2*c)/(-b-math.sqrt(b**2 - 4*a*c)))
    solutions.append((-2*c)/(-b+math.sqrt(b**2 - 4*a*c)))
    return solutions


a = 0.001
b = 1000
c = 0.001
s1 = quadraticEq(a,b,c)
print('Solutions given by quadraticEq:', s1)
s2 = requadraticEq(a,b,c)
print('Solutions given by requadraticEq:', s2)
#The values that have been yielded by quadraticEq(a,b,c) and requadraticEq(a,b,c) are comparable with each other, still they are different values. This is due to the different approximations made by Python.


a = float(input('Insert the value of a:'))
b = float(input('Insert the value of b:'))
c = float(input('Insert the value of c:'))

def roots(a, b, c):
    solutions = []
    solutions.append((-b+cmath.sqrt(b**2 - 4*a*c))/(2*a))
    solutions.append((-b-cmath.sqrt(b**2 - 4*a*c))/(2*a))
    return solutions
    
s3 = roots(a,b,c)
print('Solutions given by roots:', s3)


##The derivative
print("\n")
import math

def function(x):
    return x*(x-1)

x = 1
delta = 10**-2
deriv = (function(x+delta)-function(x))/delta
print('The value of the derivative for delta = 10e-2 is:', deriv)
print('The accuracy of the measure (compared with the analytical one) is ', 1-deriv)
#The analytical value of the derivative of function(1) is 1. The two do not perfectly agree since in the derivative calculation yielded by the problem we are not actually approximating delta perfectly to zero, but we are taking it equal to 0.1

delta1 = 10**-4
deriv = (function(x+delta1)-function(x))/delta1
print('The value of the derivative for delta = 10e-4 is:', deriv)
print('The accuracy of the measure (compared with the analytical one) is ', 1-deriv)

delta2 = 10**-6
deriv = (function(x+delta2)-function(x))/delta2
print('The value of the derivative for delta = 10e-6 is:', deriv)
print('The accuracy of the measure (compared with the analytical one) is ', 1-deriv)

delta3 = 10**-8
deriv = (function(x+delta3)-function(x))/delta3
print('The value of the derivative for delta = 10e-8 is:', deriv)
print('The accuracy of the measure (compared with the analytical one) is ', 1-deriv)

delta4 = 10**-10
deriv = (function(x+delta4)-function(x))/delta4
print('The value of the derivative for delta = 10e-10 is:', deriv)
print('The accuracy of the measure (compared with the analytical one) is ', 1-deriv)

delta5 = 10**-12
deriv = (function(x+delta5)-function(x))/delta5
print('The value of the derivative for delta = 10e-12 is:', deriv)
print('The accuracy of the measure (compared with the analytical one) is ', 1-deriv)

delta6 = 10**-14
deriv = (function(x+delta6)-function(x))/delta6
print('The value of the derivative for delta = 10e-14 is:', deriv)
print('The accuracy of the measure (compared with the analytical one) is ', 1-deriv)
#Theoretically the smaller the value of delta, the smaller the difference between the analytical value of the derivative and the computed one. Actually observeing the trend of the error, the more we approach the accuracy limit of the machine, the larger is the error yielded.


##Integral of a semicircle
print("\n")
import math
import timeit

def semiFunction(x):
    f = math.sqrt(1 - x**2)
    return f
    
def Riemann(N):
    arg = []
    for x in range(1,N):
        i = -1 + x*(2/N)
        arg.append((2/N)*semiFunction(i))
    I = math.fsum(arg)
    return I

I = Riemann(100)
print('The integral value calculated with Riemann function is', I)
#The value obtained with N=100 is sufficiently close to the true value, still one can check that for increasing values of N, the value of I is more precise.

code = """ 
import math

def semiFunction(x):
    f = math.sqrt(1 - x**2)
    return f
    
def Riemann(N):
    arg = []
    for x in range(1,N):
        i = -1 + x*(2/N)
        arg.append((2/N)*semiFunction(i))
    I = math.fsum(arg)
    return I
 
I = Riemann(100)
"""

def timeRiemann(N):
    code = f""" 
import math

def semiFunction(x):
    f = math.sqrt(1 - x**2)
    return f
    
def Riemann(N):
    arg = []
    for x in range(1,N):
        i = -1 + x*(2/N)
        arg.append((2/N)*semiFunction(i))
    I = math.fsum(arg)
    return I
 
I = Riemann({N})
"""
    time = timeit.timeit(code, number = 1)
    return time #[s]

#t = 0
#N = 800000
#while t < 1.0:
#    t = timeRiemann(N)
#    N = N + 100
#print('If the computation needs to be run in less than a second, N can be increased up to:', N)


#The following while gives the N for which the code gets runned for one minute. The value obtained is N = 45500000.
#t = []
#N = 100000000
#while t < 60.0:
#    time = timeRiemann(N)
#    t.append(time)
#    N = N + 1000000
#    Nlist.append(N)
#    print(N, time)
#print(N)
#print(Riemann(45500000)

print('The integral value calculated with the Riemann function for N = 45500000 is: 1.5707963267894778')
print('The accuracy obtained is in the order of ', (math.pi/2 - 1.5707963267894778))
#The more N gets increased, the similar it gets to the true value of the integral.
