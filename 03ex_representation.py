import math
import timeit
#Es 1 Number representation
def conv (x, y):
    if type(x)==int:
        if y==bin:
            return bin(x)
        if y==hex:
            return hex(x)
        else:
            return x
    elif 'b' in list(x):
        if y==bin:
            return x
        if y==hex:
            x=int(x, 2)
            return hex(x)
        else:
            return int(x,2)
    elif 'x' in list(x):
        if y==bin:
            x=int(x,16)
            return bin(x)
        if y==hex:
            return x
        else:
            return int(x,16)
print('Conversion',conv(26,bin))

#Es 2 32-bit floating point number
def bintodec (x):
    x=str(x)
    s=x[0]
    e=x[1:9]
    m=x[9:]
    e_dec=int('0b'+e,2)

    man=1
    n=1
    for i in m:

        f=int(i)
        man+=f/2**n

        n=n+1
    r=man*2**(e_dec-127)
    if s=='0':
        print(r)
        return r
    elif s=='1':
        return -r

print('The float value is :',bintodec('10000011111000000000000000000000'))

#Es 3 Underflow and overflow
i=True
c=1
while i==True:
    f=c/2
    if f==0:
        i=False
    else:
        c=f
print('The overflow limit is: ',c)
i=True
c=0
f=1.0
while i==True:
     f= f * 2.0
     if (f).hex()==(f/2).hex():
         i=False
     else:
         c=f
print('The underflow limit is: ',c)

#Es4 Machine precision
i=True
c=0.0
f=1.0
p=0.1
while i==True:
     r=f+p
     if (r).hex()==(f).hex():
         i=False
     else:
         p=p/2
print('Machine precision for floating point is': p)

#Es5 Quadratic solution
def quadS1(a,b,c):
    d=b**2-4*a*c
    if d>=0:
        x1=(-b+math.sqrt(d))/(2*a)
        x2=(-b-math.sqrt(d))/(2*a)
        return x1, x2
    else:
        print('Error the result is not a part of real numbers ')
        
print('Standard solution formula results',quadS1(0.001,1000,0.001))

def quadS2(a,b,c):
    d=b**2-4*a*c
    if d>=0:
        x1=(-b+math.sqrt(d))/((2*a))
        x2=(-b-math.sqrt(d))/(2*a)
        x1=x1*(-b-math.sqrt(d))/(-b-math.sqrt(d))
        x2=x2*(-b+math.sqrt(d))/(-b+math.sqrt(d))

        return x1, x2
    else:
        print('Error the result is not a part of real numbers ')
        
print('Re-express standard solution formula results', quadS2(0.001,1000,0.001))

def quadS3(a,b,c):
    d=b**2-4*a*c
    if d>=0:
        x1=((-b+math.sqrt(d))*(-b-math.sqrt(d)))/((2*a)*(-b-math.sqrt(d)))
        x2=((-b-math.sqrt(d))*(-b+math.sqrt(d)))/((2*a)*(-b+math.sqrt(d)))
        y1=x1.hex()
        y2=x2.hex()
        y1=float.fromhex(y1)
        y2=float.fromhex(y2)
        return y1, y2
    else:
        print('Error the result is not a part of real numbers ')
        
print('Results ', quadS3(0.001,1000,0.001))
 


#Es6 The derivative
def f(x):
    return x*(x-1)

i=1
p=0.01
der=(f(i+p)-f(i))/p
print('The derivative of the function is ',der)
print('True value of the derivate analytically 2x-1 is ',1)

for j in [10**(-4),10**(-6),10**(-8),10**(-10),10**(-12)]:
    der=(f(i+j)-f(i))/j
    print('The derivative of the function is ',der, 'for 𝛿=', j )
    
#Es 7 Integral of a semicircle
def integ(N):
    s=[]
    h = 2.0 / N
    x = -1
    for i in range(1,N+1):
        #print(x)
        c=lambda x: math.sqrt(1.0-x**2)
        #print(c(x))
        s.append(c(x))
        x = x + h
    
    return (sum(s) * h)
    
print(s)
print("The integral with N=100 : ", integ(100))
test1 = '''
def integ(N):
    s=[]
    h = 2.0 / N
    x = -1
    for i in range(1,N+1):
        #print(x)
        c=lambda x: math.sqrt(1.0-x**2)
        #print(c(x))
        s.append(c(x))
        x = x + h
    
    return (sum(s) * h)
       
integ(100)
'''
print("Time(sec) to run integ(100): ", timeit.timeit(stmt=test1, setup="import math", number=1))

#Usinig the function timeit that shows that the function integ takes around 0.0003324999 sec
#we can  increased N by 7500.
test = '''
def integ(N):
    s=[]
    h = 2.0 / N
    x = -1
    for i in range(1,N+1):
        #print(x)
        c=lambda x: math.sqrt(1.0-x**2)
        #print(c(x))
        s.append(c(x))
        x = x + h
    
    return (sum(s) * h)
       
integ(100*7500)
'''

print("Computation time(sec) with N = 100*7547 is: ", timeit.timeit(stmt=test, setup="import math", number=1))
print("Integral after 1 min run: ", integ(100*7500*60))
