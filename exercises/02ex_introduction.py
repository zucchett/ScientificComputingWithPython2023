import timeit

# 1. Global variables
print('1. GLOBAL VARIABLES')


def f(alist, x):
    new_list_alist = alist + list(range(x))
    return new_list_alist


alist = [1, 2, 3]
x = 5
ans = f(alist, x)
print(ans)
print(alist)

# 2. List comprehension
print('2. LIST COMPREHENSION')

ans = [x * x for x in range(10) if x % 2 == 1]

print(ans)

# 3.  Filter list
print('3. FILTER LIST')


def filter_words_by_length(word_list, n):
    filtered_words = list(filter(lambda word: len(word) < n, word_list))
    return filtered_words


words_list = ["python", "university", "cappuccino", "tea", "pizza"]
n = 6
result = filter_words_by_length(words_list, n)
print(result)

# 4. Map dictionary
print('4. MAP DICTIONARY')


def map_lengths_of_keys(dictionary):
    key_lengths = list(map(lambda key: len(key), dictionary.keys()))
    return key_lengths


lang = {"Python": 3, "Java": '', "Cplusplus": 'test', "Php": 0.7}
result = map_lengths_of_keys(lang)
print(result)

# 5. Lambda functions
print('5. LAMBDA FUNCTIONS')

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key=lambda x: x[0])

for language, score in language_scores:
    print(language, score)

# 6. Nested functions
print('6. NESTED FUNCTIONS')


def square(square_number):
    return square_number ** 2


# Function to calculate the cube of a number
def cube(cube_number):
    return cube_number ** 3


# Function to calculate the 6th power using square and cube functions
def sixth_power(cub_num):
    # Calculate the square of the number
    squared = square(cub_num)

    # Calculate the cube of the squared result
    cube_result = cube(squared)

    return cube_result


# Example usage:
cub_num = 2
cube_result = sixth_power(cub_num)
print(f"{cub_num} raised to the 6th power is {cube_result}")

# 7. Decorators
print('7. DECORATORS')


def hello(func):
    def wrapper(*args, **kwargs):
        print("Hello World!")
        return func(*args, **kwargs)

    return wrapper


# Apply the 'hello' decorator to a function
@hello
def square(x):
    return x * x


# Call the decorated function
result = square(5)

# 8. The Fibonacci sequence (part 2)
print('8. THE FIBONACCI SEQUENCE (PART 2)')


def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursive(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence


# Calculate the first 20 numbers of the Fibonacci sequence
n = 20
fib_sequence = fibonacci_recursive(n)

# Print the Fibonacci sequence
print(f"The first {n} numbers of the Fibonacci sequence are: {fib_sequence}")

# 9. The Fibonacci sequence (part 3)
print('9. THE FIBONACCI SEQUENCE (PART 3)')


def recursiveFibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = recursiveFibonacci(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence


# Iterative Fibonacci function
def loopFibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence


# Measure the execution time of both functions for n = 20
recursive_time = timeit.timeit("recursiveFibonacci(20)", globals=globals(), number=1000)
iterative_time = timeit.timeit("loopFibonacci(20)", globals=globals(), number=1000)

print(f"Recursive Fibonacci execution time: {recursive_time:.6f} seconds")
print(f"Iterative Fibonacci execution time: {iterative_time:.6f} seconds")

# 10. Class definition
print('10. CLASS DEFINITION')


class Polygon:
    def __init__(self, sides):
        if len(sides) < 3:
            raise ValueError("A polygon must have at least 3 sides")
        self.sides = list(sides)

    def get_sides(self):
        return self.sides

    def set_sides(self, sides):
        if len(sides) < 3:
            raise ValueError("A polygon must have at least 3 sides")
        self.sides = list(sides)

    def perimeter(self):
        return sum(self.sides)

    def getOrderedSides(self, increasing=True):
        ordered_sides = sorted(self.sides) if increasing else sorted(self.sides, reverse=True)
        return tuple(ordered_sides)


# Test the Polygon class
polygon = Polygon((3, 4, 5, 6))
print("Sides of the polygon:", polygon.get_sides())
print("Perimeter of the polygon:", polygon.perimeter())
print("Ordered sides (increasing):", polygon.getOrderedSides(increasing=True))
print("Ordered sides (decreasing):", polygon.getOrderedSides(increasing=False))

# 11. Class inheritance
print('11. CLASS INHERITANCE')


class Rectangle(Polygon):
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive values for a rectangle")
        super().__init__([length, width, length, width])  # Ensure that the input forms a rectangle

    def area(self):
        return self.sides[0] * self.sides[1]


# Test the Rectangle class
rectangle = Rectangle(4, 6)  # Create a rectangle with length 4 and width 6
print("Sides of the rectangle:", rectangle.get_sides())
print("Perimeter of the rectangle:", rectangle.perimeter())
print("Area of the rectangle:", rectangle.area())
