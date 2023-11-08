user_number = input('please insert the value : ')
try :
    print(f'the binary type of inserted number is {bin(int(user_number))} and the decimal type is {hex(int(user_number))}')
except :
    if user_number[1] == 'x' :
        print(f'the binary type of inserted number is {bin(int(user_number,16))} and the decimal type is {int(user_number,16)}')
    elif user_number[1] == 'b' :
        print(f'the hexadecimal type of inserted number is {hex(int(user_number,2))} and the decimal type is {int(user_number,2)}')    
#----------------------------------------------------------------------------------------------------------------------------------------------
user_number = input('please insert your number : ')
# for example : 110000101011000000000000
def b_to_f(user_number):
    sign = int(user_number[0])
    exponent = int(user_number[1:9],2)
    fraction = int('1' + user_number[9:],2)
    return ((-1) ** sign * fraction) / (1<<(len(user_number)-9-(exponent-127)))
print(f'the result is {b_to_f(user_number)}')
#---------------------------------------------------------------------------------------------------------------------------------------------
undflow = 1
ovflow = 1
for i in range(1023):
    undflow = undflow / 2
    ovflow  = ovflow  * 2
scientific_underflow="{:e}".format(undflow)
scientific_overflow="{:e}".format(ovflow)
print(f'\nThe over flow is: {scientific_overflow}')
print(f'The under flow is: {scientific_underflow}')
#-------------------------------------------------------------------------------------------------------------------------------------------------
var = 2
add = 1e-1
for i in range(20):
    var = var + add
    add = add * 1e-1
    print(f'Step {i}')
    print(var)
#----------------------------------------------------------------------------------------------------------------------------------------------------
import math

a = 0.001
b = 1000
c = 0.001

x1_1 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
x1_2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)


x2_1 = (2*c) / (-b - math.sqrt(b*b - 4*a*c))
x2_2 = (2*c) / (-b + math.sqrt(b*b - 4*a*c))

print("First approach,  x1 :",x1_1)
print("First approach,  x2 :",x1_2)
print("---------------------------")
print("Second approach, x1 :",x2_1)
print("Second approach, x2 :",x2_2)
print("---------------------------")

x3_1 = -b/(2*a) + math.sqrt((b/(2*a))**2 - c/a)
x3_2 = -b/(2*a) - math.sqrt((b/(2*a))**2 - c/a)
print("Third approach,  x1 :",x3_1)
print("Third approach,  x2 :",x3_2)
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------
import sympy
from sympy import *
def limit(z):
    x = 1
    zi = symbols('zi')
    expretion = (((x + zi)*(x + zi + 1 )) - (x*(x-1)))
    limit_expretion = sympy.limit(expretion,zi,0)
    return limit_expretion
print(limit(0.01))
#------------------------------------------------------------------------------------------------------
zigma_list = [10**-4,10**-6,10**-8,10**-10,10**-12,10**-14]
for i in zigma_list :
    print(f'the derivative of function with zigma = {i} is equal to :  {limit(i)}')
#according to the result that is calculated by python with different zigma we have the same answer 
#--------------------------------------------------------------------------------------------------------    
#--------------------------------------------------------------------------------------------------------    
import math
import timeit
def integ(N):
    a = 0
    for i in range(-int(N/2),int(N/2)):
        x = i*2/N + 1/N
        a = a + 2/N * math.sqrt(1-x*x)
    return a

N1 = 100
result = integ(N1)
dev = result - math.pi/2
print("%.30f" % result, " -----  deviation from true value for N = ",N1,"is :",dev)

N2 = 5500000  # This number resluts in 1 minute execution time.
result = integ(N2)
dev = result - math.pi/2
print("%.30f" % result, " -----  deviation from true value for N = ",N2,"is :",dev)

N3 = 60*N2  # This number resluts in 1 minute execution time.


print("execution time per loop for ( N=",N2,")")
time = timeit.timeit(lambda: integ(N2), number = 5) / 5
print(time)

# As N gets bigger, deviation is smaller and result has better accuracy, but it takes more time to execute.
#-------------------------------------------------------------------------------------------------------------------------------------
