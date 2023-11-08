import math
#1. The HelloWorld replacement

#a
a=range(1,100)
for i in a:
    if i%3==0 and i%5==0:
        print("Hello Word")
    elif i%3==0:
        print("Hello")
    elif i%5==0:
        print("Word")
    else:
        print(i)
#b
t=[]
for i in range(1,100):
    if i%3==0 and i%5==0:
        print("Hello Word")
        t.append("Python Works")
    elif i%3==0:
        print("Hello")
        t.append("Python")
    elif i%5==0:
        print("Word")
        t.append("Works")
    else:
        print(i)
t=tuple(t)
print(t)
##es2 The swap
a=input('Enter the first value ')
b=input('Enter the first value ')
a,b=b,a
print(a)
print(b)
##3. Computing the distance

u=(3,0)
v=(0,4)
c=u[0]+v[0]
c2=u[1]+v[1]
i=(c**2+c2**2)**(1/2)
print(i)

#4. Counting letters

from collections import Counter
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
s2=s2.lower()
s1=s1.lower()
d=Counter(s1)
f=Counter(s2)
print(f)
print(d)




#5. Isolating the unique
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
c=[]
for i in l:
    if l.count(i)==1:
        c.append(i)

#6. Casting
a=input("Enter a variable")
b=input("Enter a variable")
try:
    a=int(a)
except:
    try:
        a=float(a)
    except:
        a=str(a)
try:
    b=int(b)
except:
    try:
        b=float(b)
    except: 
        b=str(b)
        
try:
    print(a+b)

except:
    print('it was no possible to perform the addition')
        
#7. Cubes
#a
cubi=[]
for i in range(11):
    cubi.append(i**3)
print(cubi)
#b
c=[x**3 for x in range(11)]
print(c)

#8. List comprehension
a=[(i,j) for i in range(3) for j in range(4)]
print(a)

#9. Nested list comprehension
z=[]
d=[ (a,b,c) for a in range(1,101) for b in range(1,101) for c in range(1,101)]
for i in d:
    if i[0]**2+i[1]**2==i[2]**2:
        j=sorted(i)
        j=tuple(j)
        if j not in z:
            MCD=math.gcd(i[0],i[1],i[2])
            if MCD==1:
                z.append(j)

print(z)



#10 Normalization of a N-dimensional vector
import math
v=(2,5,6)
z=0
for i in v:
    z=z+i**2
z=math.sqrt(z)
n=[i/z for i in v]
s=[(i/z)**2 for i in v]
n=tuple(n)
print('Vector: ',v)
print('Normalized vector: ',n)
print('Sum of all th entries of the normalized vector is: ',sum(s))

#11 The Fibonacci sequence
Fib=[]
for i in range (1,21):
    if i==1 or i==2:
        Fib.append(1)
    else:
        print(i)
        d=Fib[i-2]+Fib[i-3]
        Fib.append(d)

print(Fib)
