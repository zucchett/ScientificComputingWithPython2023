
#*****************************************Global variables *****************************************
print('\n \n# ------------ Global variables  ------------ # \n \n')
def f(alist,x):
    new_l = list(alist)
    for i in range(x):
        new_l.append(i)
    return new_l

alist = [18, 20, 43]
ans = f(alist,x=5)
print(" Global variables " , ans)
print(alist)


#*****************************************LIST COMPREHENSION *****************************************
print('\n \n# ------------ LIST COMPREHENSION  ------------ # \n \n')

ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(" The LIST COMPREHENSION  " , ans)

#*****************************************Filter list *****************************************
print('\n \n# ------------ Filter list  ------------ # \n \n')

def filter_words_by_length(word_list, n):
    filtered_words = list(filter(lambda word: len(word) < n, word_list))
    return filtered_words

word_list = ["Naoures", "Ahmed", "Salim", "Yesmin", "Firas"]
n = 6
short_words = filter_words_by_length(word_list, n)
print("Filtered words:", short_words)


#*****************************************MAP DICTIONARY *****************************************
print('\n \n# ------------ MAP DICTIONARY  ------------ # \n \n')

def lang_dict(dict):
    key = list(map(len, dict.keys()))
    return key

dict = {"Python": 3, "Java": '', "Cplusplus": 'test', "Php": 0.7}
MAP_DICTIONARY  = lang_dict(dict)
print(" The MAP DICTIONARY  :", MAP_DICTIONARY )


#*****************************************Lambda functions *****************************************
print('\n \n# ------------ Lambda functions  ------------ # \n \n')

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key=lambda x: x[0])
print(language_scores)




#*****************************************NESTED FUNCTIONS *****************************************
print('\n \n# ------------ NESTED FUNCTIONS ------------ # \n \n')


def square(x):
    return x ** 2
def cube(x):
    return x ** 3
def power_six(x):
    return square(cube(x))

# test

x = 2
print("The square of 2 is " , square(2))
print("The cube of 2 is " , cube(2))
print("2 raised 6 is " , power_six(2))



#*****************************************DECORATORS*****************************************
print('\n \n# ------------ DECORATORS ------------ # \n \n')

def hello(func):
    def wrapper(*args, **kwargs):
        print("Hello World!")
        return func(*args, **kwargs)
    return wrapper

#here the @hello decorator will modify the behavior of the square function
@hello
def square(x):
    return x * x

#test
print("Let's test the decorator :",square(100))


#*****************************************FIBONACCI PART2*****************************************
print('\n \n# ------------ FIBONACCI PART2------------ # \n \n')
#i answerd this is ex 1 :
#Recursive Fibonacci
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence
fibonacci = fibonacci(20)
print("The Fibonacci Sequence with recurrence or by indexing : ",fibonacci )

#*****************************************FIBONACCI PART3*****************************************
print('\n \n# ------------ FIBONACCI PART3------------ # \n \n')

import timeit
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

# The Fibonacci sequence from exercise 1
fibonacci_sequence = fibonacci(20)
print("The Fibonacci Sequence using loops for / while:", fibonacci_sequence)
fibonacci_time = timeit.timeit("fibonacci(20)", globals=globals(), number=1000)
print("The time for the fibonacci function:", fibonacci_time)



#*****************************************Class definition*****************************************
print('\n \n# ------------ Class definition------------ # \n \n')
class Polygon:
    # Constructor of the class
    def __init__(self, sides):
        if len(sides) < 3:
            print("The Polygon must have at least 3 sides")
        self.side = list(sides)

    def set_side(self, side_i, l):
        if 0 <= side_i < len(self.side):
            self.side[side_i] = l
        else:
            raise ValueError("Out of range")

    def get_side(self, side_i):
        if 0 <= side_i < len(self.side):
            return self.side[side_i]
        else:
            raise ValueError("Out of range")

    def perimeter_polygon(self):
        return sum(self.side)

    def get_ordered_sides(self, increasing=True):
        sides = sorted(self.side) if increasing else sorted(self.side, reverse=True)
        return tuple(sides)

polygon1 = Polygon((5, 8, 7, 7))
polygon2 = Polygon((5, 8, 1))
print("Decreasing the side order is :", polygon1.get_ordered_sides(increasing=False))
print("Increasing the side order is:", polygon1.get_ordered_sides(increasing=True))
print("The Perimeter of the polygon is :", polygon1.perimeter_polygon())
print("Decreasing the side order is :", polygon2.get_ordered_sides(increasing=False))
print("Increasing the side order is:", polygon2.get_ordered_sides(increasing=True))
print("The Perimeter of the polygon is :", polygon2.perimeter_polygon())


#*****************************************Class inheritance*****************************************
print('\n \n# ------------ Class inheritance------------ # \n \n')


class Rectangle(Polygon):
    def __init__(self, width, height):
        if len([width, height]) != 2:
            raise ValueError("A Rectangle  have exactly 2 sides: width and height")
        super().__init__([width, width, height, height])  # Rectangle has 4 equal-length sides
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

#test
#rectangle1 = Rectangle(1, 1)
rectangle1 = Rectangle(5, 1)
print("The height of the rectangle:", rectangle1.height)
print(" The width of the rectangle:", rectangle1.width)
print("The area of the rectangle:", rectangle1.area())
#rectangle2 = Rectangle(1, 1,5,6)

