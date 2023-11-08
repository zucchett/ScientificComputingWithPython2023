#1. Global variables
from timeit import timeit


def f(alist, x):
    y = list(alist)
    for i in range(x):
        y.append(i)
    return y
alist = [1, 2, 3]
x = 5
ans = f(alist,x)
print(ans)
print(alist) # alist has been changed

#2
alist = [x**2 for x in range(10) if x%2 == 1]
print(alist)

#3
def wordsAnalys(wList, n):
    print(list(filter(lambda x: len(x) <n, wList)))
wList = ["ENGINEER", "PYTHON", "UNIPD", "ITALY", "CIAO"]
n = 6
wordsAnalys(wList,  n)

#4
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
print(list(map(lambda l: len(l),lang.keys())))

#5Lambda functions
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key = lambda y: y[0])
print(language_scores)

#6 Nested functions
def sixth_power(n):
    def square(n):
        return n*n
    def cube(n):
        return n*n*n
    return square(cube(n))
print(sixth_power(2))
print(sixth_power(3))

#Decorators
def hello(f):
    def helloWrapper(x):
        print("Hello World!")
        result = f(x)
        return result
    return helloWrapper
#-----------
@hello
def square(x):
    return x * x
#---------
print(square(3))
print(square(7))
print(square(1))
print(square(2))

#8The Fibonacci sequence (part 2)
def recursive_fibo(num):
    flist = []
    def fibo(num):
        if (num <= 2):
            res = num - 1
        else:
            res = fibo(num - 2) + fibo(num - 1)
        if (len(flist) == num - 1):
            flist.append(res)
        return res

    fibo(num)
    return flist
print(recursive_fibo(20))

#9. The Fibonacci sequence (part 3)
#loop
def loopFibo (num):
    flist = []
    for i in range(num):
        if (len(flist) < 2):
            flist.append(i)
        else:
            (flist.append(flist[i-1] + flist[i-2]))
    return flist
#Recursive
def recursiveFibo(num):
    flist = []
    def fibo(num):
        if (num <= 2):
            result = num-1
        else:
            result = fibo(num-2)+fibo(num-1)
        if (len(flist) == num-1):
            flist.append(result)
        return result
    fibo(n)
    return flist
#-----
print("loop's execution time:")
%timeit loop_fibo(20)
print("recursive function execution tim:")
%timeit rec_fibo(20)

#------
#10. Class definition
class polygon:
    sides = ()

    def __init__(self, sides):
        if (len(sides) < 3):
            print("a polygon ob should have at least 3 sides")
            return
        else:
            self.sides = sides

    def getLengths(self):
        return self.sides

    def setLengths(self, lengths):
        if (len(lengths) != len(self.sides)):
            print("you should enter", len(self.sides), "number")
            return
        else:
            self.sides = lengths

    def perimeter(self):
        return sum(self.sides)

    def getOrderedSides(self, increasing=True):
        self.sides = tuple(sorted(self.sides, reverse=not increasing))
        return self.sides
#----
s1 = (1, 2)
po = polygon(s1)
#----
s2 = (3, 4, 5, 6)
po = polygon(s2)
#------
print(po.perimeter())
print(po.getOrderedSides(False))
lengths= (34,4, 12, 10)
po.setLengths(lengths)
print(po.getLengths())


#-----------11
class polygon:
    sides = ()
    def __init__(self, sides):
        if (len(sides) < 3):
            print("a polygon ob should have at least 3 sides")
            return
        else:
            self.sides = sides

    def getLengths(self):
        return self.sides

    def setLengths(self, lengths):
        if (len(lengths) != len(self.sides)):
            print("you should enter", len(self.sides), "number")
            return
        else:
            self.sides = lengths
    def perimeter(self):
        return sum(self.sides)

    def getOrderedSides(self, increasing=True):
        self.sides = tuple(sorted(self.sides, reverse=not increasing))
        return self.sides
#---rectangle class
class rectangle(polygon):
    def __init__(self, length, width):
        x = (length, width, length, width)
        polygon.__init__(self, x)

    def area(self):
        return self.sides[0] * self.sides[1]


a = rectangle(5, 4)
print(a.area())
print(a.getLengths())
print(a.getOrderedSides(True))