#EXERCISES WEEK No 2
#Suly Vannesa Cifuentes Bohorquez
#Student ID: 2080663

import timeit # ex 9

#-------------------------------------- EX. #1 Global Variables-------------------------------------

print("\nEXERCISE # 1 \n")

x = 5

def f(alist):
    n_list = alist[:]  # Create a copy of the original list
    for i in range(x):
        n_list.append(i)
    return n_list

alist = [1, 2, 3]
ans = f(alist)
print("Modified List:",ans)  
print("Original List:", alist)  

#-------------------------------------- EX. #2 List of Comprehension-------------------------------------

print("\nEXERCISE # 2 \n")

ans = [x * x for x in range(10) if x % 2 == 1]
print("Result list of comprehension: ",ans)

#-------------------------------------- EX. #3 Filter List-------------------------------------

print("\nEXERCISE # 3 \n")

def filter_by_length(word_list, n):
    filtered_w = filter(lambda word: len(word) < n, word_list)
    return list(filtered_w)

# Input from the user for n and word_list
n = int(input("Enter N the maximum length for words: "))
word_list = input("Enter a list of words separeted by , : ").split(",")

short_words = filter_by_length(word_list, n)
print("Words shorter than", n, "characters:", short_words)

#-------------------------------------- EX. #4 Map Dictionary -------------------------------------

print("\nEXERCISE # 4 \n")

def get_lengths(dictionary):
    key_lengths = list(map(len, dictionary.keys()))
    return key_lengths

lang = {"Python": 3, "Java": '', "Cplusplus": 'test', "Php": 0.7}

key_lengths_list = get_lengths(lang)
print("Lengths:",lang, key_lengths_list)

#-------------------------------------- EX. #5 Lambda functions --------------------------------------
print("\nEXERCISE # 5 \n")

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key=lambda x: x[0])

print("Result by scores:",language_scores)

#-------------------------------------- EX. #6 Nested functions --------------------------------------

print("\nEXERCISE # 6 \n")

def square(x):
    return x ** 2 ##square

def cube(x):
    return x ** 3 ##cube

def sixth_power(x):
    squared = square(x)
    cubed = cube(x)
    return squared * cubed

number = int(input("Enter number you want to raise to the 6th power: "))
result = sixth_power(number)
print(f"{number} raised to the 6th power is: {result}")

#-------------------------------------- EX. #7 Decorators --------------------------------------

print("\nEXERCISE # 7 \n")

def hello(func):
    def wrapper(*args, **kwargs):
        print("Hello World!")
        return func(*args, **kwargs)
    return wrapper

@hello
def square(x):
    return x * x

# Call the decorated function
result = square(5)
print("Result:", result)

#-------------------------------------- EX. #8 The Fibonacci sequence (part 2) -------------------------------------------
print("\nEXERCISE # 8 \n")

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Calculate the first 20 Fibonacci numbers
n = 20
fib_numbers = fibonacci(n)

# Print the Fibonacci sequence
print("Fibonacci part.2 = ",fib_numbers)

#-------------------------------------- EX. #9 The Fibonacci sequence (part 3) -------------------------------------------

print("\nEXERCISE # 9 \n")

# Recursive Fibonacci function
def recursiveFib(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = recursiveFib(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Iterative Fibonacci function (from the previous exercise)
def loopFib(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

n = 20

recursive_time = timeit.timeit("recursiveFib(n)", globals=globals(), number=1000)
print("Time taken for recursiveFib(20):", recursive_time)

iterative_time = timeit.timeit("loopFib(n)", globals=globals(), number=1000)
print("Time taken for loopFib(20):", iterative_time)

#-------------------------------------- EX. #10 Class definition  -------------------------------------------

print("\nEXERCISE # 10 \n")

class Polygon:
    def __init__(self, sides):
        if len(sides) < 3:
            raise ValueError("A polygon must have at least 3 sides.")
        self.sides = list(sides)

    def set_sides(self, sides):
        if len(sides) < 3:
            raise ValueError("A polygon must have at least 3 sides.")
        self.sides = list(sides)

    def get_sides(self):
        return self.sides

    def perimeter(self):
        return sum(self.sides)

    def getOrderedSides(self, increasing=True):
        sorted_sides = sorted(self.sides) if increasing else sorted(self.sides, reverse=True)
        return tuple(sorted_sides)

# Test the Polygon class
polygon = Polygon((5, 3, 7, 2, 4))  # Create an instance with an unordered list of sides
print("Perimeter:", polygon.perimeter())  # Calculate and print the perimeter
print("Ordered Sides (incr):", polygon.getOrderedSides())  # Get and print sides in increasing order
print("Ordered Sides (decr):", polygon.getOrderedSides(increasing=False))  # Get and print sides in decreasing order


#-------------------------------------- EX. #11 Class inheritance  -------------------------------------------

print("\nEXERCISE # 11 \n")

class Rectangle(Polygon):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive values.")
        super().__init__([width, height, width, height])  

    def area(self):
        return self.sides[0] * self.sides[1]


rectangle = Rectangle(5, 3)  # Create a rectangle with width 5 and height 3
print("Perimeter:", rectangle.perimeter())  
print("Area:", rectangle.area()) 
