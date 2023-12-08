import timeit

def ex1(alist):
    print("1. Global variables")
    new_alist = alist[0:]
    x = 5
    for i in range(x):
        new_alist.append(i)
    return new_alist

def ex2():
    print("2. List comprehension")
    ans = [i*i for i in range(10) if i%2 == 1]
    print(ans)
    print("\n#################################\n")

def ex3(words, n):
    print("3. Filter list")
    print(list(filter(lambda i: len(i)<n,words)))
    print("\n#################################\n")

def ex4(dict):
    print("4. Map dictionary")
    print(list(map(len, dict.keys())))
    print("\n#################################\n")

def ex5():
    print("5. Lambda functions")
    language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
    language_scores.sort(key=lambda item: item[0])
    print(language_scores)
    print("\n#################################\n")

def ex6():
    def square(x):
        x **= 2
        return x

    def cube(x):
        x **= 3
        return x
        
    print("6. Nested functions")
    x = 2
    print(square(cube(x)))
    print("\n#################################\n")

def ex7():
    print("7. Decorators")
    def hello(func):
        def wrapper(x):
            print("Hello World!")
            return func(x)
        return wrapper

    @hello
    def square(x):
        return x * x

    print(square(3))
    print("\n#################################\n")


def ex8(n):
    if n <= 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib_list = ex8(n - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

def fib_loop(n):
    result = [0, 1]
    i = 0
    while i < n-1:
        result.append(result[i] + result[i+1])
        i += 1
    return result

def ex9():
    print("9. The Fibonacci sequence (part 3)\n")

    print("Loop time")
    time = timeit.timeit(lambda: fib_loop(20), number=1)
    print(str(time))

    print("\nRecursion time")
    time = timeit.timeit(lambda: ex8(20), number=1)
    print(str(time))

    print("""\nUsing a loop, stores the calculation results for each Fibonacci number in a sequence and uses them to calculate the next number. This avoids repeated calculations and makes the algorithm more efficient. The efficiency depends on the amount of Fibonacci, because of complexity. Recursion complexity is o(2^n), loop complexity is O(n)""")
    print("\n#################################\n")


class Polygon:
    x = ()
    def __init__(self, components):
        self.x = components       
   
    def perimeter(self):
        per = 0
        for i in range(len(self.x)):
            per += self.x[i]
        return per

    def getOrderedSides(self, value):
        self.x = list(self.x)
        if value == True:
            self.x.sort()
        else:
            self.x.sort(reverse = True)
        return(tuple(self.x))
        
class Rectangle(Polygon):
    def __init__(self, components):
        if len(components) == 2:
            super().__init__(components)
            print("The area is")
        else:
            print("Please, set only 2 components")
    
    def area(self):
        area = (self.x[0] * self.x[1])
        print(area)
        return area


            
def ex10():
    print("10. Class definition")
    a = Polygon((2, 4, 5, 3))
    print(a.perimeter())
    print(a.getOrderedSides(True))
    print(a.getOrderedSides(False))
    print("\n#################################\n")

def ex11():
    print("11.Class inheritance")
    b = Rectangle((5, 7))
    b.area()
  

alist = [1, 2, 3]
print(ex1(alist))
print(alist)
print("\n#################################\n")

ex2()

list_of_words = ['dffdf', 'ffffffffffff', 'ffffffff', 'ffffffff', 'fff', 'ffdfsf', 'sdfsfd', 'fd', 'fdfddddddddddddddddddd']
n = 5
ex3(list_of_words,n)

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
ex4(lang)

ex5()
ex6()
ex7()
print("8. The Fibonacci sequence (part 2)")
print(ex8(20))
print("\n#################################\n")

ex9()
ex10()
ex11()
