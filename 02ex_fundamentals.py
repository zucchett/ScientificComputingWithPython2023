#Ex1
x = 5

def f(alist):
    L = alist.copy()
    for i in range(5):
        L.append(i)
    return L

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist)  # alist didn't change

#Ex2
ans = [x * x for x in range(10) if x % 2 == 1]
print(ans)

#Ex3
def filter_list(L, n):
    ans = list(filter(lambda w: len(w) < n, L))
    return ans

L = ["yasminemasmoudi", "hello", "hi"]
n = 6
result = filter_list(L, n)
print(result)

#Ex4
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
ans = list(map(lambda x : len(x) , lang.keys() ))
print(ans)

#Ex5
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key= lambda x : x[0].upper())
ans = language_scores
print(ans)

#Ex6
def square(x):
    return x * x
def cube(x):
    return x * x * x
def third_f(x):
    return cube(square(x))
third_f(2)

#Ex7
def hello(func): 
    def wrapper(x):
        print("Before")
        print( func(x) )
        print("After")
    return wrapper 

@hello
def square(x):
    return x*x

square(4)

#Ex8
def fib(x):
    if x <= 1:
        return x
    else:
        return fib (x-1) + fib(x-2)
fib(4)

#Ex9
import timeit

def loopFibonacci(n):
    fib = [0,1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]
def recursiveFibonacci(x):
    if x<=1:
        return x
    else:
        return recursiveFibonacci(x-1) + recursiveFibonacci(x-2)
    
if __name__ == "__main__":
    print(timeit.timeit("loopFibonacci(20)", globals=globals(), number=10000))
    print(timeit.timeit("recursiveFibonacci(20)", globals=globals(), number=10000))

#For the iterative Fibonacci function (loopFibonacci(20)), the time per loop is approximately 0.0172 ms.
#For the recursive Fibonacci function (recursiveFibonacci(20)), the time per loop is approximately 9.7913 ms.

#Conclusion: The iterative Fibonacci function is 570 times faster than the recursive Fibonacci function 
#for the input value `n = 20`.

#Ex10
class Polygon:
    x = []

    def __init__(self, t):
        if len(t)< 3 :
            print("A polygon must have at least 3 sides")
        else:
            self.t = list(t)
    
    def getSideLengths(self): 
        return self.t
    
    def setSideLengths(self, t): 
        if len(t)< 3 :
                print("A polygon must have at least 3 sides")
        else:
            self.t = list(t)
    
    def perimeter(self): 
        return sum(self.t)
    
    def getOrderedSides(self, increasing = True):
        if increasing:
            sides = sorted(self.t) #the output is a list 
        else: 
            sides = sorted(self.t, reverse=True) #the output is a list 
        return tuple(sides) 
#testing the class 
polygon = Polygon((4, 5, 6))
print("Polygon's side lengths:", polygon.getSideLengths())
print("Perimeter:", polygon.perimeter())
print("Ordered Sides (Increasing):", polygon.getOrderedSides(increasing=True))
print("Ordered Sides (Decreasing):", polygon.getOrderedSides(increasing=False))

#Ex11
class Rectangle (Polygon):
    def __init__(self, length, width):
        super().__init__([length, width, length, width])
    def area(self):
        return self.t[0]*self.t[1] 
    
#testing the class
rectangle = Rectangle(4, 5) 
print("Side lengths of the Rectangle:", rectangle.getSideLengths())
print("Perimeter of the Rectangle:", rectangle.perimeter())
print("Area of the Rectangle:", rectangle.area())