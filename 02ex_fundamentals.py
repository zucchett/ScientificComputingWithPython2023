# Exercise 1 (Global variables)

def f(alist, x):
  # creates a new empty list to return in the end
  new_list = []
  # gets x as an input which can be local var (also global var but not necessarily)
  for i in range(x):
    # fills the new list based on alist (original input array will remain intact)
    new_list.append(alist[i])
  return new_list

# Exercise 2 (List comprehension)

# does x*x for every x from [0,10) and puts them in the list if they are not
# divisable by 2 (remainder of 1)
ans = [x * x for x in range(10) if x % 2 == 1]
# print(ans)

# Exercise 3 (Filter list)

def filter_list(words, n):
  # returns a list based on the filter()
  # the lambda function takes word as input, checks if it is shorter than n and
  # returns true or false based on that, then the filter will filter 'words'
  # with regards to the true values of the lambda function (filters the false ones)
  return list(filter(lambda word: len(word) < n, words))

# Exercise 4 (Map dictionary)

def map_dictionary(lang):
  # map takes lambda function that has a 'key' input and returns the size of it
  # and as the iterator, it takes the keys of our dict to feed the lambda func
  key_lengths = map(lambda key: len(key), lang.keys())
  return list(key_lengths)

# Exercise 5 (Lambda functions)

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
# sorts the list of tuples using a lambda function and setting its key as x[0]
# which will translate into the first element of the tuples
language_scores.sort(key=lambda x: x[0])

# Exercise 6 (Nested functions)

def square(x):
  # returns x^2
  return x * x

def cube(x):
  # returns x^3
  return x * x * x

def sixth_power(x):
  # returns (x^3)^2
  return square(cube(x))
  # can also return (x^2)^3
  # return cube(square(x))

# Exercise 7 (Decorators)

# a decorator to print Hello World! each time the wrapped function is called (@hello)
def hello(func):
  # sets the structure of the decorater and how it should act when it is called before a func
  def wrapper(*args, **kwargs):
    print("Hello World!")
    return func(*args, **kwargs)
  # returns the wrapper which is the main functionality of the decorator's behaviour
  return wrapper

# Exercise 8 (The Fibonacci sequence (part 2))

def recursiveFibonacci(n):
  if n <= 0:
    raise ValueError("n must be a non-negative integer.")

  if n == 1 or n == 2:
    return [0, 1][:n]
  else:
    fibonacci_numbers = recursiveFibonacci(n - 1)
    fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    # returns a list of the first n Fibonacci numbers ( [1,n] --> n numbers in the list)
    return fibonacci_numbers

# Exercise 9 (The Fibonacci sequence (part 3))
def loopFibonacci(n):
  if n < 0:
    raise ValueError("n must be a positive integer.")
  if n == 0:
    fibonacci_numbers = [0]
  if n == 1:
    fibonacci_numbers = [0, 1]
  else:  
    fibonacci_numbers = [0, 1]
    i = 2
    while i < n:
      fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
      i += 1
  # from [0, n) --> n numbers in the list
  return fibonacci_numbers

import timeit

print(timeit.timeit("recursiveFibonacci(20)", setup="from __main__ import recursiveFibonacci", number=1))
#7.79994297772646e-06
print(timeit.timeit("loopFibonacci(20)", setup="from __main__ import loopFibonacci", number=1))
#2.800021320581436e-06

# loopFibonacci is almost 66% faster than the recursive one

# Exercise 10 (Class definition)

class Polygon:
  # takes a tuple containing the length of each side of the polygon
  def __init__(self, sides):

    # if the input tuple does not contain at least 3 items
    if len(sides) < 3:
      raise ValueError("Polygon must have at least 3 sides.")

    self.sides = sides
  
  # getter to return a tuple containing the length of each side of the polygon
  def get_sides(self):
    return self.sides
  
  # setter to set the length of each side of the polygon
  def set_sides(self, sides):

    # if the input tuple does not contain at least 3 items
    if len(sides) < 3:
      raise ValueError("Polygon must have at least 3 sides.")

    self.sides = sides
  
  # returns the perimeter of the polygon
  def perimeter(self):
    perimeter = 0
    for side in self.sides:
      perimeter += side
    return perimeter

  # returns a tuple containing the length of the sides arranged in increasing or decreasing order
  # default parameter is True so by default it returns in increasing order
  def get_ordered_sides(self, increasing=True):
    ordered_sides = sorted(self.sides)
    if not increasing:
      ordered_sides.reverse()
    return ordered_sides

polygon = Polygon([4, 3, 5])

perimeter = polygon.perimeter()
print("Perimeter:", perimeter)

# Get the ordered sides (no need to pass increasing=True since it's true by default)
ordered_sides = polygon.get_ordered_sides()
print("Ordered sides:", ordered_sides)

# Exercise 11 (Class inheritance)

class Rectangle(Polygon):

  # takes only width and height of the rectangle
  def __init__(self, width, height):
    # if the input width and height are not positive
    if width <= 0 or height <= 0:
      raise ValueError("Width and height must be positive.")
    # we use super to pass our arguments to the parent constructor
    super().__init__((width, height, width, height))

    self.width = width
    self.height = height
  
  # returns the area of the rectangle
  def area(self):
    return self.width * self.height

rectangle = Rectangle(6, 8)

area = rectangle.area()
print("Area:", area)
# Get the ordered sides (decreasing)
ordered_sides = rectangle.get_ordered_sides(increasing=False)
print("Ordered sides:", ordered_sides)
