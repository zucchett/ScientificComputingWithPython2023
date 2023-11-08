# 1. Global variables
print("\n\n---------- 1. Global variables ----------\n\n")
def f(alist, x):
    alist = []
    for i in range(x):
        alist.append(i)
    return alist


x = 5
alist = [1, 2, 3]
ans = f(alist,x)
print(ans)
print(alist) # alist has been changed

# 2. List comprehension
print("\n\n---------- 2. List comprehension ----------\n\n")
#Write the following expression using a list comprehension:
ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))

print(ans)

ans = [i**2 for i in range(10) if i%2==1 ]

print(ans)


# 3. Filter list
print("\n\n---------- 3. Filter list ----------\n\n")

def filterFunc(word, n=5):
    return len(word) <= n
words = ["prova","forzaromabhgwhjrbgks", "Francesco", "Totti", "FrancescoTotti"]
ris = list(filter(filterFunc,words))
print(ris)

# 4. Map dictionary
print("\n\n---------- 4. Map dictionary ----------\n\n")
#Consider the following dictionary:
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
#Write a function that takes the above dictionary and uses the map()
# higher order function to return a list that contains the length of the keys of the dictionary.
def func(elem):
    return len(elem)
ris = list(map(func, lang.keys()))

print(ris)


# 5. Lambda functions
print("\n\n---------- 5. Lambda functions ----------\n\n")
#Write a Python program that sorts the following list of tuples using a lambda function, according to the alphabetical order of the first element of the tuple:
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
#Hint: use the method sort() and its argument key of the list data structure.

lista = lambda x: x.sort()

lista(language_scores)
print(language_scores)


# 6. Nested functions
print("\n\n---------- 6. Nested functions ----------\n\n")
def square(x):
    return x**2

def cube(x):
    return x**3

def sixth(x):
    return cube(square(x))

print(sixth(2))


# 7. Decorators
print("\n\n---------- 7. Decorators ----------\n\n")
def hello(square):
    def wrapper(x):
        print("Hello World!")
        return square(x)
    return wrapper


@hello
def square(x):
    return x*x

print(square(5))


# 8. The Fibonacci sequence (part 2)
print("\n\n---------- 8. The Fibonacci sequence (part 2) ----------\n\n")
def recursive_fib(x):
    if x <= 1:
        return x
    else:
        return recursive_fib(x-1)+recursive_fib(x-2)


for i in range(20):
    print(recursive_fib(i))

# 9. The Fibonacci sequence (part 3)
print("\n\n---------- 9. The Fibonacci sequence (part 3) ----------\n\n")
import timeit
test_fib_recursive = '''
def recursive_fib(x):
    if x <= 1:
        return x
    else:
        return recursive_fib(x-1)+recursive_fib(x-2)
recursive_fib(20)
'''


test_fib_loop = '''
def fib_loop(x):
    a = 0
    b = 1
    for i in range(x-2):
        a,b = b, a+b
    return b
fib_loop(20)
'''

it_fib=timeit.timeit(stmt=test_fib_loop, number=100)
rec_fib=timeit.timeit(stmt=test_fib_recursive, number=100)
print("Iterative fib: ", it_fib)
print("Recursive fib: ", rec_fib)

diff = float(rec_fib/it_fib)

print('%s %d %s' % ('\nIterative fib is ',
diff, "times faster than recursive fib"))



# 10. Class definition
print("\n\n---------- 10. Class definition ----------\n\n")

class polygon:

    x = ()

    def __init__(self, l_sides):
        if len(l_sides)<3:
            print("The tuple must have at least 3 elements")
        else:
            self.x=l_sides

    def setSideLenght(self,side,lenght):
        if side < len(self.x):
            self.x[side]=lenght

    def getSideLenght(self, side):
        return self.x[side]

    def perimeter(self):
        perimeter = 0
        for i in list(self.x):
            perimeter += i
        return perimeter

    def getOrderedSides(self,increasing = True):
        if increasing == True:
            return tuple(sorted(self.x))
        else:
            return tuple(sorted(self.x, reverse=True))


p = polygon((4,3,5,1))
print(p.perimeter())
print(p.getOrderedSides())
print(p.getOrderedSides(False))


class rectangle(polygon):

    def __init__(self, components):
        if len(components) == 2:
            self.x = components
        else:
            print("Error: number of components is not 2")

    def area(self):
        return self.x[0] * self.x[1]


rect = rectangle((2, 6))
area = rect.area()
print("\nThe area of the rectangle is:", area)


# 11. Class inheritance
print("\n\n---------- 11. Class inheritance ----------\n\n")
class rectangle(polygon):

    def __init__(self, l_sides):
        if len(l_sides) == 2:
            self.x = l_sides
        else:
            print("# of sides must be 2")

    def area(self):
        return self.x[0] * self.x[1]


rec = rectangle((2, 4))
print("area is",rec.area())
