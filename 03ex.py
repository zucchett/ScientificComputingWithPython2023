#esercizio 1
print("Esercizio 1\n")

def convert_num(n, tipo):
    if isinstance(n, int):
        if tipo=="dec":
            print("The number", n, "in decimal is:", n)
        elif tipo=="hex":
            print("The number", n, "in hexadecimal is:", hex(n))
        elif tipo=="bin":
            print("The number", n, "in binary is:", bin(n))
        else:
            print("Invalid input!")
    elif isinstance(n, str):
        if n[1]=="b":
            x=int(n, 2)
        elif n[1]=="x":
            x=int(n, 16)
        else:
            "Invalid input!"    
        if isinstance(x, int):
            if tipo=="dec":
                print("The number", n, "in decimal is:", x)
            elif tipo=="hex":
                print("The number", n, "in hexadecimal is:", hex(x))
            elif tipo=="bin":
                print("The number", n, "in binary is:", bin(x))
            else:
                print("Invalid input!")
        else:
            print("Conversion error!")
convert_num("0b1011", "hex")

#esercizio 2
print("\nEsercizio 2\n")
Nbin="01000101010110000000000000000000"
segno=int(Nbin[0], 2)
espo=int(Nbin[1:9], 2)
mant=int(Nbin[9:], 2)
den=1
while den<=mant:
    den=den*10
mant=mant/den
Ndec=((-1)**segno)*(1+mant)*(2**(espo-127))
print(Ndec)

#esercizio 3
print("\nEsercizio 3\n")
upper=1.0
lower=1.0
while upper*2!=float('inf'):
    upper=upper*2
while lower/2!=0.0:
    lower=lower/2
print("Highest number:", upper,"\nSmallest fraction:", lower)

#esercizio 4
print("\nEsercizio 4\n")
test=1.0
while 1.0+test!=1.0:
    test=test/2
print("Smallest precision:", test)

#esercizio 5
import math as m
a, b, c = 4, 16, 1
print("\nEsercizio 5\n")
def AsolveEq(a, b, c):
    deter=b**2 - 4*a*c
    sol=[]
    if deter>=0:
        x1=((-b)+m.sqrt(deter))/(2*a)
        x2=((-b)-m.sqrt(deter))/(2*a)
        sol.append(x1)
        sol.append(x2)
    return sol
x=AsolveEq(a, b, c)
if len(x)==0:
    print("a)\nThis equation doesn't have real solutions!")
else:
    print("a)\nRoots 1:", x[0], "\nRoots 2:", x[1])

def BsolveEq(a, b, c):
    deter=b**2 - 4*a*c
    sol=[]
    if deter>=0:
        x1=((-b)+m.sqrt(deter))*((-b)-m.sqrt(deter))/(2*a)*((-b)-m.sqrt(deter))
        x2=((-b)-m.sqrt(deter))*((-b)+m.sqrt(deter))/(2*a)*((-b)+m.sqrt(deter))
        sol.append(x1)
        sol.append(x2)
    return sol
x=BsolveEq(a, b, c)
if len(x)==0:
    print("b)\nThis equation doesn't have real solutions!")
else:
    print("b)\nRoots 1:", x[0], "\nRoots 2:", x[1])

'''
The method in the B section is less accurate i think because by multiplying by the numerator we are increasing the value of the number used to find the roots, which means we are less precise since we are limited by the discrete precision of the computer.
'''

def CsolveEq(a, b, c):
    deter=b**2 - 4*a*c
    sol=[]
    if deter>=0:
        x1=((-b)+m.sqrt(deter))/(2*a)
        x2=((-b)-m.sqrt(deter))/(2*a)
        sol.append(x1)
        sol.append(x2)
    return sol
x=CsolveEq(a, b, c)
if len(x)==0:
    print("a)\nThis equation doesn't have real solutions!")
else:
    print("a)\nRoots 1:", x[0], "\nRoots 2:", x[1])

#esercizio 6
print("\nEsercizio 6\n")
def f(x):
    return x*(x-1)
def der_f(x, delta):
    return (f(x+delta)-f(x))/(delta)
n=8
delta=0.01
print(f(n))
for i in range(5):
    delta=delta/100
    print(der_f(n, delta))
'''
The solution does not match the analitical one both because of the approximation done in the function der_f and because of the limit in the granular precision of the rappresentation of numbers; this is visible by the fact the accuracy is not linear in the delta factor.
'''

#esercizio 7
import math as m
import timeit
print("\nEsercizio 7\n")
def measure_time(func):
    def wrapper(*args, **kwargs):
        Tstart = timeit.default_timer()
        result = func(*args, **kwargs)
        Tend = timeit.default_timer()
        Texec = Tend - Tstart
        print("This function took {:.6f} seconds to run.".format(Texec))
        return result
    return wrapper

@measure_time
def riemann(N):
    result=[]
    for i in range(N):
        result.append((2/N)*m.sqrt(1-(1-i*2/N)**2))
    print(sum(result))

N=100
riemann(N)
print((1.5707963267945069-1.5691342555492505)/100)
'''
With N=100 there is an error of 0.1% on the result (1.5691342555492505)
To stay under 1 second of computation time I need to use N<=1300000 (i5 8350u)
1.5707963267945069 is the result after a computation of 63 seconds (N=170000000)
The difference is negliegeble, in the order of 10^-5, not worth the extra time of wait.
'''
