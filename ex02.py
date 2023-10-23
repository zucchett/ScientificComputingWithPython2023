## Exercise 1
x = 5

def f(alist):
    new_list = alist.copy()  # I've created a copy to keep that original list unmodified
    for i in range(x):
        new_list.append(i)
    return new_list

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has not been changed

## Exercise 2
ans = [x * x for x in range(10) if x % 2 == 1]

## Exercise 3
def filter_words(words, n):
    shorter_words = list(filter(lambda word: len(word) < n, words))
    return shorter_words

## Exercise 4
def get_key_lengths(lang):
    key_lengths = list(map(lambda key: len(key), lang.keys()))
    return key_lengths

## Exercise 5
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key=lambda x: x[0])

print(language_scores)

## Exercise 6
def square(number):
    return number ** 2

def cube(number):
    return number ** 3

def sixth_power(number):
    cubed = cube(number)
    return square(cubed)

## Exercise 7
def hello(func):
    def wrapper(*args, **kwargs):
        print("Hello World!")
        return func(*args, **kwargs)
    return wrapper

## Exercise 8
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(20):
    result = fibonacci(i)
    print(result)

## Exercise 9
Execution time of recursiveFibonacci:  10.663453238999864
Execution time of loopFibonacci:  0.012449977000869694

## Exercise 10
class Polygon:
    def __init__(self, sides):
        self.sides = list(sides)

    def get_sides(self):
        return self.sides

    def set_sides(self, sides):
        self.sides = list(sides)

    def perimeter(self):
        return sum(self.sides)

    def get_ordered_sides(self, increasing=True):
        ordered_sides = sorted(self.sides)
        if not increasing:
            ordered_sides.reverse()
        return tuple(ordered_sides)

# Create an instance of the Polygon class
p = Polygon((5, 3, 8, 2, 4))

# Test the perimeter method
perimeter = p.perimeter()
print("The perimeter of the polygon is: {}".format(perimeter))

# Test the getOrderedSides method
ordered_sides = p.get_ordered_sides(increasing=True)
print("The sides of the polygon in increasing order are: {}".format(ordered_sides))

## Exercise 11
class Rectangle(Polygon):
    def __init__(self, sides):
        if len(sides) != 2:
            raise ValueError("A rectangle should have exactly 2 sides provided!")
        super().__init__(sides * 2)

    def area(self):
        return self.sides[0] * self.sides[1]

# Create an instance of the Rectangle class
r = Rectangle((5, 8))

# Test the perimeter method inherited from Polygon
perimeter = r.perimeter()
print("The perimeter of the rectangle is: {}".format(perimeter))

# Test the area method specific to Rectangle
area = r.area()
print("The area of the rectangle is: {}".format(area))