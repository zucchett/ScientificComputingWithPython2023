# QUESTION 1
# SOLUTION

# 1. Global Variables
# Convert the function  into a function that doesn't use global variables and that does not modify the original list
"""
x = 5
def f(alist):
    for i in range(x):
        alist.append(i)
    return alist
alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed
"""

x = 5


def f(alist, n):
    x = n
    print("x (local) = ", x)
    newlist = [item for item in alist]
    for i in range(x):
        newlist.append(i)
    return newlist


alist = [1, 2, 3]
ansWER = f(alist=alist, n=4)
print("x (global) = ", x)
print("ANSWER = ", ansWER)
print("alist = ", alist)
####################################END OF QUESTION 1

#QUESTION NUMBER 2
#SOLUTION
#2 **List comprehension**

#Write the following expression using a list comprehension:

#ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))

ans = [x * x for x in range(10) if x % 2 == 1]
print(ans)
print()
###############################END OF QUESTION 2

#QUESTION NUMBER 3
#SOLUTION
"""
3. Filter list
Using the filter() hof, define a function that takes a list of words and an integer n as arguments, and returns a
list of words that are shorter than n.
"""
def shtr_wrd(words, n):
    return list(filter(lambda word: len(word) < n, words))
words = ["Works", "PythonWorks", "python", "SCP", "Assignment", "hello", "world"]
print(str(shtr_wrd(words, 6)))
print()
#######################END OF QUESTION 3

#QUESTION 4
#SOLUTION
"""
4. **Map dictionary**
Consider the following dictionary:
`lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}`

Write a function that takes the above dictionary and uses the `map()` higher order function to return a list
that contains the length of the keys of the dictionary.
"""
mark = {"Python": 3, "Java": '', "Cplusplus": 'test', "Php": 0.7}
def f(mark):
    return list(map(len, mark.keys()))
print(f(mark))
print()
############################END OF QUESTION 4

#QUESTION NUMBER 5
#SOLUTION
"""
5. Lambda functions
Write a Python program that sorts the following list of tuples using a lambda function, according to the alphabetical
order of the first element of the tuple:
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
Hint: use the method sort() and its argument key of the list data structure.
"""
def sort_in_order(mark):
    mark.sort(key=lambda t: t[0])
    return mark
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
print(sort_in_order(language_scores))
print()
################################END OF QUESTION 5

# QUESTION NUMBER 6
# SOLUTION

# 6\. **Nested functions**

# Write two functions: one that returns the square of a number, and one that returns its cube.

# Then, write a third function that returns the number raised to the 6th power, using only the two previous functions.
def square(M):
    return M * M


def cube(M):
    return M * M * M


def sixth_pwr(M):
    return square(M) * cube(M) * int(cube(M) / square(M))


m = 4
print("function result: " + str(sixth_pwr(m)))
print("Calculation: " + str(m ** 6))
print()
#############################END OF QUESTION 6

#QUESTION NUMBER 7
#SOLUTION
"""
7. Decorators
Write a decorator named hello that makes every wrapped function print “Hello World!” each time the function is called.
The wrapped function should look like:
@hello
def square(x):
    return x*x
"""
def hello(function):
    def wrapper(X):
        print("Hello World!")
        return function(X)
    return wrapper

@hello
def square(X):
    return X * X
x = 2
equal = square(x)
print("Square of " + str(x), "= " + str(equal))
print()
###############################END OF QUESTION 7

# QUESTION NUMBER 8
# SOLUTION

"""
8. The Fibonacci sequence (part 2)
Calculate the first 20 numbers of the Fibonacci sequence using a recursive function.
"""


def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


fiblist = []
for M in range(20):
    fiblist.append(fib(M))

print(fiblist)
print()
################################END OF QUESTION 8

# QUESTION NUMBER 9
# SOLUTION
"""
9.The Fibonacci sequence (part 3)
Run both the Fibonacci recursive function from the previous exercise, and the Fibonacci function from 01ex that use
only for and while loops.
Measure the execution code of the two functions with timeit (link to the doc), for example:
%timeit loopFibonacci(20)
%timeit recursiveFibonacci(20)
which one is the most efficient implementation? By how much?
"""

import timeit


def recursiveFibo(n):
    if n == 0 or n == 1:
        return n
    return recursiveFibo(n - 1) + recursiveFibo(n - 2)


def loopFibo(n):
    f = [1, 1]
    i = 2
    while i <= n:
        f.append(f[i - 1] + f[i - 2])
        i = i + 1
    return f


starttime_loop = timeit.default_timer()
loopFibo(20)
TimeEnd_loop = timeit.default_timer() - starttime_loop
print("Execution time for loopFibonacci :", TimeEnd_loop)
starttime_rec = timeit.default_timer()
recursiveFibo(20)
TimeEnd_rec = timeit.default_timer() - starttime_rec
print("Execution time for recursiveFibonacci :", TimeEnd_rec)
print("loopFibonacci is more efficient By, ", (TimeEnd_rec / TimeEnd_loop), )
print()
####################################END OF QUESTION 9

#QUESTION NUMBER 10
#SOLUTION
"""
10.Class definition
Define a class polygon. The constructor has to take a tuple as input that contains the length of each side.
The (unordered) input list does not have to have a fixed length, but should contain at least 3 items.
Create appropriate methods to get and set the length of each side
Create a method perimeter() that returns the perimeter of the polygon
Create a method getOrderedSides(increasing = True) that returns a tuple containing the length of the sides arranged in
increasing or decreasing order, depending on the argument of the method
Test the class by creating an instance and calling the perimeter() and getOrderedSides(increasing = True) methods.
"""
class Polygon:
    lengths = []

    def __init__(self, lengths):
        if len(lengths) > 2:
            self.lengths = lengths

    def getLengths(self):
        return self.lengths

    def getElement(self, index):
        if index < len(self.lengths):
            return self.lengths[index]

    def setLengths(self, index, element):
        if index < len(self.lengths):
            self.lengths[element] = element

    def perimeter(self):
        perimeter = 0
        for i in self.lengths:
            perimeter = perimeter + i
        return perimeter

    def getOrderedSides(self, increasing=True):
        O_List = self.lengths
        if increasing:
            O_List.sort()
        else:
            O_List.sort(reverse=True)
        return O_List

polygon = Polygon([5, 7, 1, 2, 0, 4, 3])
print("Polygon = ", polygon.lengths)
print("Perimeter of polygon = ", polygon.perimeter())
O_list = polygon.getOrderedSides()
print("Ordered list(increasing) = " + str(O_list))
O_list = polygon.getOrderedSides(increasing=False)
print("Ordered list(decreasing) = " + str(O_list))
print()
##############################END OF QUESTION 10

#QUESTION NUMBER 11
#SOLUTION

"""
11.Class inheritance
Define a class rectangle that inherits from polygon. Modify the constructor, if necessary, to make sure that the
input data is consistent with the geometrical properties of a rectangle.
Create a method area() that returns the area of the rectangle.
Test the rectangle class by creating an instance and passing an appropriate input to the constructor.
"""


class Polygon:
    lengths = []

    def __init__(self, lengths):
        if len(lengths) > 2:
            self.lengths = lengths
        else:
            print("Component size should be greater than 2!")

    def getLengths(self):
        return self.lengths

    def getElement(self, index):
        if index < len(self.lengths):
            return self.lengths[index]

    def setLengths(self, index, element):
        if index < len(self.lengths):
            self.lengths[element] = element

    def perimeter(self):
        perimeter = 0
        for i in self.lengths:
            perimeter = perimeter + i
        return perimeter

    def getOrderedSides(self, increasing=True):
        ordered_list = self.lengths
        if increasing:
            ordered_list.sort()
        else:
            ordered_list.sort(reverse=True)
        return ordered_list


class Rectangle(Polygon):
    def __init__(self, lengths):
        super().__init__(lengths)
        if len(lengths) == 4:
            lengths.sort()
            if (lengths[0] == lengths[1]) and (lengths[2] == lengths[3]):
                self.lengths = lengths
            else:
                print("Dimesions are not correct!")
        else:
            print("Component size should be 4!")

    def area(self):
        return self.lengths[0] * self.lengths[2]
        # in init function, the list is assigned sorted


rectangle = Rectangle([3, 1, 3, 1])
print("Area is equal to , ", rectangle.area())
#####################################END OF QUESTION 11

