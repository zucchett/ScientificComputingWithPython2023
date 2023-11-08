import numpy as np
import sys
import math
import struct
from timeit import Timer
import decimal

print("*****************************************")
print("Number representation")
print("*****************************************")

#function that converts integer numbers
def convertitor(n,output):
    if(n[1]=="b"):
        print("Input type: bin")
    elif(n[1]=="x"):
        print("Input type: hex")
    else:
        print("Input type: dec")
    n_dec = int(n,2)
    if (output=="dec"):
        return n_dec
    elif (output=="bin"):
        n_bin = bin(n_dec)
        return n_bin
    elif(output=="hex"):
        n_hex = hex(n_dec)
        return n_hex

#test of the function with different convertions
#binary numbers are the type 0b.....
#hex numbers are the type 0x......
print(convertitor("0b10","dec"))
print(convertitor("0b10","hex"))
print(convertitor("0b10","bin"))
print("\n")

print("*****************************************")
print("32-bit floating point number")
print("*****************************************")
bin = int('110000101011000000000000', 2)
def binaryToFloat(value):  
    return struct.unpack('f', struct.pack('I', value))[0]
fl1 = binaryToFloat(bin)

print(f'Decimal equivalent of 110000101011000000000000: {fl1}')

def conversion(N): 
    if (len(N)<32):
        l = 32 - len(N)
        temp = ""
        for i in range (0,l):
            temp = temp + "0"
        N = temp + N
    a = int(N[0])       
    b = int(N[1:9],2)    
    c = int("1"+N[9:], 2)

    return (-1)**a * c /( 1<<( len(N)-9 - (b-127) ))
bin = '110000101011000000000000' 
print(conversion(bin)) 


print("\n")

print("*****************************************")
print("Underflow and overflow")
print("*****************************************")
#variable that contains the number of times the cycle will be executed
N = 2000
#two variables initialized to 1
i = 1
j = 1
while((j/2)!=0):
    i=i*2
    j=j/2

print("Overflow: ",format(decimal.Decimal(i), '2.5e'))
print("Underflow: ",j)
print("\n")


print("*****************************************")
print("Machine precision")
print("*****************************************")
#initial value of epsilon, as suggested in the text of the exercise
eps=1
#at each iteration, the value of epsilon has a smaller value
#the cycle ends when the addition of "eps" has no effect on the number
while eps+1 != 1:
   eps = eps/2
print(2*eps) #epsilon is multiplied by 2 because in the last iteration of the while cycle
             #it is divided by two

print("\n")

print("*****************************************")
print("Quadratic solution")
print("*****************************************")

#first version of the function (standard formula to find the solutions of a quadratic equation)
def sol(a,b,c):
    x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
    print("First solution, classic formula:\n",x1)
    print("Second solution, classic formula:\n",x2)

#second version of the function
def second_sol(a,b,c):
    x1 = ((-b+math.sqrt(b**2-4*a*c))*(-b+math.sqrt(b**2-4*a*c)))/((2*a)*(-b+math.sqrt(b**2-4*a*c)))
    x2 = ((-b-math.sqrt(b**2-4*a*c))*(-b-math.sqrt(b**2-4*a*c)))/((2*a)*(-b-math.sqrt(b**2-4*a*c)))
    print("First solution, with multiplication:\n",x1)
    print("Second solution, with multiplication:\n",x2)

sol(0.001,1000,0.001)
second_sol(0.001,1000,0.001)
#the 2 solutions are the same for both functions

def third_sol(a,b,c):
    x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2 = c/(a*x1)
    print("First solution, third option formula:\n",x1)
    print("Second solution, third option formula:\n",x2)
third_sol(0.001,1000,0.001)

def fourth_sol(a,b,c):
    x1 = (2*c)/(-b+math.sqrt(b**2-4*a*c))
    x2 = c/(a*x1)
    print("First solution, fourth option formula:\n",x1)
    print("Second solution, fourth option formula:\n",x2)
fourth_sol(0.001,1000,0.001)

print("\n")


print("*****************************************")
print("The derivative")
print("*****************************************")

def f(x):
    return x*(x-1)

def derivative(x,delta):
    d = delta
    return (f(x+d)-f(x))/d

print("Derivate of the function in the point x=1 :", derivative(1,0.01))
#the analytical result is 1, the result given by the program is a bit different due to number representation

#second part of the exercise
deltas = [10**-4,10**-6,10**-8,10**-10,10**-12,10**-14]
for d in deltas:
    print("Delta %.14f:"%d,derivative(1,d))
#decreasing the value of delta, the result is more accurate. From a certain point underflow occurs so the result
#is not properly accurate

print("\n")

print("*****************************************")
print("Integral of a semicircle")
print("*****************************************")


print("Exact solution: ",np.pi/2) #to compare the obtained retults with the implemented function


def integral(N):
    I = 0
    x = -1
    n = 0
    for n in range(0,N+1):
        I = I + ((2/N)*math.sqrt(1-x**2))
        x = x + 1/N
    return I

temp = 100 #variable to store the number of splits
res = integral(temp)
print("Value returned by the function = ", res)
#the two values are different, in particular the one returned by the function is slightly bigger


t = Timer(lambda: integral(temp))
print("Time for execution (in seconds, for N=100) = ",t.timeit(number = 1))

ok = False
total = 0 #variable to store the time for each execution

#the cycle developed allows you to find what value
#of N allows you to perform the calculation close to the time specified by the exercise
while(not(ok)):
    t = Timer(lambda: integral(temp))
    total = t.timeit(number = 1)
    if (total>=1.0):
        ok = True
    temp = temp + 1000000 #arbitrarily chosen increase

print("Time for execution (in seconds) = ", total, ", N =",temp)
#Sperimental result from testing the above function: is given also the number of splits for the integral

#res = integral(70000000)
#t = Timer(lambda: integral(70000000))
#print(t.timeit(number = 1))
#print("Value returned by the function: ", res)

ok = False
total = 0 #variable to store the time for each execution
while(not(ok)):
    t = Timer(lambda: integral(temp))
    total = t.timeit(number = 1)
    if (total>=60.0):
        ok = True
    temp = temp + 50000000 #arbitrarily chosen increase

print("Time for execution (in seconds) = ", total, ", N =",temp)
res = integral(temp)
print("Value returned by the final function = ", res)
#running the function for approximately 1 minute, is returned a more accurate result of the integral
#the cycle developed allows you to find what value
#of N allows you to perform the calculation close to the time specified by the exercise
#The gain in running it for 1 minute is the fact that the obtained result is more accurate