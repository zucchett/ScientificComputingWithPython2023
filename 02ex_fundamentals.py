# 1. Global variables
def f(x, myList=None):

    import copy

    tempList = list(myList)
    # or even:
    # tempList = copy.copy(myList)

    for i in range(x):
        tempList.append(i)
    return tempList

# myList = [1, 2, 3]
# newList = f(5, myList)
# print(newList)
# print(myList)

# 2. List comprehension


def Ans():
    ans = [x * x for x in range(10) if x % 2 == 1]
    print(ans)
    return ans

# Ans()


# 3. Filter list
def Filter(words, n):

    newList = list(filter(lambda w: len(w) < n, words))

    print(newList)

    return newList

# Filter(["123", "1234567889", "12", "12345", "1234567", "6"], 3)


# 4.Map dictionary
def MapDictionary():

    lang = {"Python": 3, "Java": '', "Cplusplus": 'test', "Php": 0.7}

    keysLenght = list(map(lambda x: len(x), lang))

    print(keysLenght)

    return keysLenght

# MapDictionary()


# 5. Lambda functions
def LambdaSort():

    language_scores = [('Python', 97), ('Cplusplus', 81),
                       ('Php', 45), ('Java', 32)]

    language_scores.sort()

    # or
    # sort by key
    # language_scores.sort(key=lambda x: x[0])
    # sort by value
    # language_scores.sort(key=lambda x: x[1])

    for language, score in language_scores:
        print(f'{language}: {score}')

# LambdaSort()


# 6. Nested function
def Square(x):
    return x ** 2


def Cube(x):
    return x ** 3


def PowSix(x):

    result = Cube(Square(x))
    print(result)

    return result


# 7. Decorators
# Decorator definition
def hello(func):
    def wrapper(x):
        print("Hello World!")
        return func(x)
    return wrapper


@hello
def square(x):
    return x * x

# print(square(5))


# 8. Fibonacci
def FibonacciRecursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return FibonacciRecursive(n - 1) + FibonacciRecursive(n - 2)


# 9. Fibonacci efficiency
def Fibonacci(limit):
    fib = [0, 1]
    for i in range(2, limit):
        fib.append(fib[i - 1] + fib[i - 2])


def MeasureEfficiency():

    import timeit

    n = 20
    loop = 1

    recursiveTime = timeit.timeit(lambda: FibonacciRecursive(n), number=loop)

    loopTime = timeit.timeit(lambda: Fibonacci(n), number=loop)

    print(f"Recursive execution time: {recursiveTime/loop} seconds")
    print(f"Loop-based execution time: {loopTime/loop} seconds")

# MeasureEfficiency()


# 10. Class defintion
class Polygon:

    sides = tuple()

    def __init__(self, sides) -> None:

        if len(sides) < 3:
            raise Exception("Tuple should contain at least 3 sides")

        self.sides = tuple(sides)

    def SetSides(self, sides):
        if len(sides) < 3:
            raise Exception("At least 3 sides are needed")
        self.sides = list(sides)

    def GetSides(self):
        return self.sides

    def Perimeter(self):
        return sum(self.sides)

    def getOrderedSides(self, increasing=True):
        return tuple(sorted(self.sides, reverse=not increasing))


# 11. Class inheritance
class Rectangle(Polygon):

    width = 0
    length = 0

    def __init__(self, sides):

        if len(sides) < 4:
            raise Exception("Rectanlge has at least four sides")

        temp = list(set(sides))

        self.width = temp[0]
        self.length = temp[1]

        if len(temp) != 2:
            raise Exception("it is not a rectangle")

        super().__init__(sides)

    def Area(self):

        return self.width * self.length
        # print(temp)


# polygonTest = Polygon((3, 4, 5))
# print(polygonTest.Perimeter())
# print(polygonTest.getOrderedSides(True))
# rectTest = Rectangle((8, 4, 8, 4))
# print(rectTest.Area())
