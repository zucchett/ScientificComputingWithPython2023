# 03ex_representation.py

# 1. Number representation
print("1. Number representation \n")

def converter(num : int, output : str):
    if type(num) == int : 
        if output == 'bin':
            return bin(num)
        elif output == 'hex' :
            return hex(num)
        elif output == 'dec' : 
            return num
        else :
            print("representation not recognized")
    else :
        print("Num is not an int")

#testing 
print(converter(50, "hex"))

# 2. 32-bit floating point number
print("\n 2. 32-bit floating point number \n")

def bin_to_decimal(stringa : str):
    s = int(stringa[0])
    sign = (-1)**s
    e = stringa[1:9]
    exp = int(e, 2)
    f = stringa[9:]
    mantissa = 1
    for i in range(len(f)) :
        mantissa += int(f[i])/(2**(i+1))
    x = sign*mantissa*(2**(exp-127)) # bias = 127 for single precision 
    return x

print(bin_to_decimal("110000101011000000000000"))

# 3. Underflow and overflow
print("\n 3. Underflow and overflow \n")

a, b = 1, 1 
N = 2000

for n in range(N): 
    try :
        a = a*2
        print(n, "%.e" % a)
    except OverflowError :
        print("Reached overflow ") 
        break

for n in range(N):
    b = b/2
    print(n, b)
    if b == 0.0 :
        print("Reached underflow") 
        break

# 4. Machine precision
print("\n 4. Machine precision \n")

c = 1 

for n in range(30) :
    c = 1+  10**(-n)
    print(n,"|", c)  

# 5. Quadratic solution
print("\n 5. Quadratic solution \n")

from math import sqrt

# a)
def quadratic_eq(a,b,c):
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    
    zero1 = a*x1**2 + b*x1+c #checking
    zero2 = a*x2**2 + b*x2+c #checking

    print("x_1,2 =", x1,"and", x2, "\n", zero1, zero2)
    
#testing 
a = 0.001
b = 1000
c = 0.001

print(quadratic_eq(a,b,c))

#b)
def quadratic_eq_2(a,b,c):
    x3 = 2*c/(-b - sqrt(b**2 - 4*a*c))
    x4 = 2*c/(-b + sqrt(b**2 - 4*a*c)) 

    zero3 = a*x3**2 + b*x3+c
    zero4 = a*x4**2 + b*x4+c

    print("x_3,4 =", x3,"and", x4, "\n", zero3, zero4)

print(quadratic_eq_2(a,b,c))

# the problem resides in the determinant term because it is subtracting a 10^-6 number from a 10^6 one, resulting close to the b value. Then this value is subtracted from b, creating cancellation error.
# however, the determinant is computed correctly, as seen by printing its value. Instead, when doing the square root, it results in some rounding errors due to floating point precision  

# c)
# one way to solve the problem is to avoid cancellation errors, and so computing only one root (the one with the minus sign because b is positive). The other one is obtained as c/a.

def quadratic_eq_3(a,b,c):
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a) # to avoid cancellation error I chose to compute the solution with minus sign
    x1 = c / (a*x2) # this computes the other solution directly from the first one, therefore avoiding subtracting two close numbers
    
    zero2 = a*x2**2 + b*x2+c #check if x2 is a solution
    zero1 = (a*x1**2 + b*x1+c)
    
    #print("x2 precise =", x2,"\n x1 precise", x1, "\n zero1 =", zero1, "\n zero2=",zero2)
    print("x2=",x2)
   
#testing
a = 0.001
b = 1000
c = 0.001

print(quadratic_eq_3(a,b,c))
   

# 6. The derivative
print("\n 6. The derivative \n")

def f(x):
    return x*(x-1)

# a)
def derivative(x, delta): 
    return (f(x+delta)-f(x))/delta

def analytical_derivative(x):
    return 2*x-1

print("The result of the analytical derivative ", analytical_derivative(1), "is different from the one obtained by definition", derivative(1, 10**-2)) # Catastrophic cancellation occurs when subtracting two numbers that are very close to one another

# b)
delta = [10**-4, 10**-6, 10**-8, 10**-10, 10**-12, 10**-14]
for i in range(len(delta)):
    print(delta[i],"->", derivative(1, delta[i])) # The accuracy is better for delta ~ 10^-8 and worsen for lower values (because one gets close to overflow ) and for higher values (because of subtraction of very close numbers) 

# 7. Integral of a semicircle
print("\n 7. Integral of a semicircle \n")

# a)
N = 100
a = -1
b = 1

from math import sqrt, pi

def f(x):
    return sqrt(1-x**2)
    
def R_integral(N):
    sum = 0
    for k in range(1,N+1):
        y = a + k * 2/N 
        sum += 2/N * f(y) 
    return sum

# a) 
print("The Riemann integral", R_integral(100), "is different from pi/2 =" , pi/2, "with difference =" , abs(pi/2-R_integral(100)))

# b)
import time 

N = 10000000
a = -1
b = 1

from math import sqrt, pi

def f(x):
    return sqrt(1-x**2)
    
def R_integral(N):
    start = time.time()
    sum = 0
    for k in range(1,N+1):
        y = a + k * 2/N 
        sum += 2/N * f(y) 
    end = time.time()
    if (end-start) > 1 : # for 1 minute one should only increase the value of N and change the if condition to 60
        print(N, sum)
        return True
    return False

for i in range(0, N, 100000):
    if R_integral(i) : break 
