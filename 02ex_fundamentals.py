import copy
import timeit

#Exercise 1
def exercise1():
    x = 5

    def f(alist,x):
        newlist = copy.copy(alist)

        for i in range(x):
            newlist.append(i)

        return newlist
    
    alist = [1, 2, 3]
    ans = f(alist,x)

    print("New list: ",ans)
    print("Original list: ",alist)


#Exercise 2
def exercise2():
    ans = [x*x for x in range(10) if x % 2 == 1]

    print(ans)


#Exercise 3
def wordsFilter(words,n):
    ans = list(filter(lambda w: len(w) < n, words))

    return ans

def exercise3():
    words = ["My", "name", "is", "Giovanni", "Giorgio"]
    n = 3
    ans = wordsFilter(words,n)
    print("List of words", words)
    print("Integer n:",n)
    print("Words shoter than n: ",ans)


#Exercise 4
def lenDict(lang):
    ans = list(map(len,lang.keys()))

    return ans

def exercise4():
    lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
    ans = lenDict(lang)
    print("Dictionary: ",lang)
    print("Length of the keys: ",ans)


#Exercise 5
def exercise5():
    language_scores = [('Python', 97), ('Cplusplus', 81), 
                       ('Php', 45), ('Java', 32)]

    language_scores.sort(key=lambda score: score[0])

    print(language_scores)


#Exercise 6
def nestedFunc(x):
    def square(x):
        return x**2

    def cube(x):
        return x**3

    return square(cube(x))

def exercise6():
    x = 2
    ans = nestedFunc(x)

    print(f"{x}^6 = {ans}")


#Exercise 7
def hello(func):
    def wrapper(x):
        print("Hello World!")
        func(x)

    return wrapper

@hello
def square(x):
    return x**2

def exercise7():
    x = 5
    square(x)


#Exercise 8
def recursiveFibonacci(n):
    if n <= 2:
        if n == 0:
            return []
        elif n == 1:
            return [0] 

        return [0,1]

    fibo = recursiveFibonacci(n-1)
    fibo.append(fibo[-1] + fibo[-2])

    return fibo

def exercise8():
    n = 20
    print(recursiveFibonacci(n))


#Exercise 9
def loopFibonacci(n):
    fibo = [0,1]

    for i in range(2,n):
        fibo.append(fibo[i-1] + fibo[i-2])

def exercise9():
    time_loop = timeit.timeit(
            'loopFibonacci(20)','from __main__ import loopFibonacci',number=1)
    time_recursive = timeit.timeit(
            'recursiveFibonacci(20)','from __main__ import recursiveFibonacci',
            number=1)

    print("Loop fibonacci: ",time_loop)
    print("Recursive fibonacci: ",time_recursive)
    # The execution time varies at every run but is very similar


#Exercise 10
class Polygon:

    sides = ()

    def __init__(self, sides):
        if len(sides) >= 3:
            if any(side <= 0 for side in sides):
                print("Error: All sides must be greater than zero")
            else:
                self.sides = sides
        else:
            print("Error: at least 3 sides required")

    def getSide(self,n):
        return self.sides[n]

    def setSide(self,n,side):
        if n < len(self.sides):
            if side <= 0:
                print("Error: All sides must be greater than zero")
            else:
                list_sides = list(self.sides)
                list_sides[n] = side

                self.sides = list_sides

    def perimeter(self):
        return sum(self.sides)

    def getOrderedSides(self, increasing = True):
        list_sides = list(self.sides)

        if not increasing:
            list_sides.sort(reverse=True)
        else:
            list_sides.sort()

        return tuple(list_sides)


def exercise10():
    poly = Polygon((35,5,10))

    print("The perimeter of a polygon is: ",poly.perimeter())
    print("The ordered sides of a polygon are: ",poly.getOrderedSides(increasing=True))


#Exercise 11
class Rectangle(Polygon):

    def __init__(self, length, width):
        super().__init__((length, width, length, width))

    def area(self):
        return super().getSide(0)*super().getSide(1)

def exercise11():
    rectangle = Rectangle(5,4)

    print("The perimeter of the rectangle is: ",rectangle.perimeter())
    print("The area of the rectangle is: ", rectangle.area())


exercise1()
exercise2()
exercise3()
exercise4()
exercise5()
exercise6()
exercise7()
exercise8()
exercise9()
exercise10()
exercise11()
