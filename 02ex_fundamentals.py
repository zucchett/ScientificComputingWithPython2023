import math
#1. Global variables
def f(alist,x):
    f=alist.copy()
    for i in range(x):
        f.append(i)
    return f
x=5
a = [1, 2, 3]
ans = f(a,x)
print(ans)
print(a) # alist has been changed

#2. List comprehension
ans=[x*x for x in range(10) if x%2==1]
print(ans)

#3.Filter list


def leng(a,n):
    return list(filter(lambda s: len(s) < n,a))

s=['nanna','casa','tre','re']
y=4
print(leng(s,y))

#4. Map dictionary
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
def f(n):
    return len(n)



d=list(map(f,(lang.keys())))
print(d)

#5 Lambda functions
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

l=lambda x: x.sort()
l(language_scores)

print(language_scores)

#6 Nested functions
def squ (n):
    return n**(1/2)

def c (n):
    return n**3

def s (n):
    d=c(n)
    d=c(d)
    print(d)
    print(squ(c(n)))
    return squ(d)*squ(c(n))
n=2
print(s(n))

#7. Decorators

def Hello(func):
    def wrapper(n):
        print("Hello Word!")
        print(func(n))
    return wrapper
@Hello
def square(x):

    return x*x
n=3

square(n)

#8 The Fibonacci sequence (part 2)
def Fibonacci(x):
    if x<20:
        if x==0:
            f=[]
            return 1
        elif x==1 or x==2:
            return 1
        else:
            return Fibonacci(x-2)+Fibonacci(x-1)
for i in range(20):           
    print(Fibonacci(i))

#9 The Fibonacci sequence (part 3)
import timeit 
def Fib(n):
   if n < 2 : # in realtà basterebbe n < 1
      return n 
   f0 = 0
   f1 = 1

   for i in range(2, n+1) :
      f = f0 + f1
      f0 = f1
      f1 = f
   return f

def Fibonacci(x):
    if x<2:
        return x
    else:
        return Fibonacci(x-2)+Fibonacci(x-1)
i=20
tempo_di_esecuzione = timeit.timeit('Fib(i)',globals=globals(),number=1)
tempo_di_esecuzione1 = timeit.timeit('Fibonacci(i)',globals=globals(),number=1)
print(tempo_di_esecuzione)
print(tempo_di_esecuzione1)


#10 Class definition
class polygon():
    def __init__(self, comp):
        if len(comp)==2:
            self.x=comp[0]
            self.y=comp[1]
    
    def perimeter(self):
        return self.x*2+self.y*2

    def getOrderedSides(self,increasing):
        f=[self.x,self.y]
        if increasing==True:
            f.sort(reverse=True)
            return tuple(f)
        else:
            f.sort(reverse=False)
            return tuple(f)

a=polygon((6,5))
print(a.perimeter())
print(a.getOrderedSides(increasing = True))


#11. Class inheritance 
class Rectangle(polygon):

    def area(self):
        return (self.x*self.y)

a=Rectangle([5,6])

print(a.area())
