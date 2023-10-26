#1)Global Variables
print("Program 1")
def f(alist, x):
    new_list = alist.copy()
    for i in range(x):
        new_list.append(i)
    return new_list

alist = [1, 2, 3]
ans = f(alist, 5)
print(ans)
print(alist)  # Original alist is not changed
print("Program 1 ends\n")

#2)list comprehension
print("Program 2 begins")
ans = [x * x for x in range(10) if x % 2 == 1]
print(ans)
print("Program 2 ends\n")

#3)Filter list
print("Program 3 begins")
def filter_words_by_length(word_list, n):
    filtered_words = list(filter(lambda word: len(word) < n, word_list))
    return filtered_words

# Example usage:
word_list = ["apple", "banana", "cherry", "date", "elderberry"]
n = 6
result = filter_words_by_length(word_list, n)
print(result)  # Output: ['apple', 'date']
print("Program 3 ends\n")

#4)Map dictionary
print("Program 4 begins")
def get_key_lengths(dictionary):
    key_lengths = list(map(len, dictionary.keys()))
    return key_lengths

lang = {"Python": 3, "Java": '', "Cplusplus": 'test', "Php": 0.7}
key_lengths = get_key_lengths(lang)
print(key_lengths)
print("Program 4 ends\n")

#5)Lambda functions
print("Program 5 begins")
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

# Sort the list based on the first element of each tuple (alphabetical order)
language_scores.sort(key=lambda x: x[0])

# Print the sorted list
for item in language_scores:
    print(item)

print("Program 5 ends\n")
#6)Nested Functions
print("Program 6 begins")
# Function to return the square of a number
def square(number):
    return number ** 2

# Function to return the cube of a number
def cube(number):
    return number ** 3

# Function to return the number raised to the 6th power
def power_of_six(number):
    # To get the 6th power, you can call the cube function twice
    return cube(cube(number))

# Example usage:
num = 2
square_result = square(num)
cube_result = cube(num)
power_of_six_result = power_of_six(num)

print(f"Square of {num}: {square_result}")
print(f"Cube of {num}: {cube_result}")
print(f"{num} raised to the 6th power: {power_of_six_result}")
print("Program 6 ends\n")

#7)Decorators
print("Program 7 begins")
def hello(func):
    def wrapper(*args, **kwargs):
        print("Hello World!")
        return func(*args, **kwargs)
    return wrapper

@hello
def square(x):
    return x * x

result = square(5)

print("Program 7 ends\n")
#8)The fibonacci sequence(part 2)
print("Program 8 begins")
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = fibonacci_recursive(n - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

n = 20
fibonacci_sequence = fibonacci_recursive(n)
print(fibonacci_sequence)
print("Program 8 ends\n")

#9)The fibonacci sequence(part 3)
print("Program 9 begins")
import timeit

# Recursive Fibonacci function
def recursiveFibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = recursiveFibonacci(n - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

# Loop-based Fibonacci function
def loopFibonacci(n):
    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

# Measure the execution time of both functions
recursive_time = timeit.timeit("recursiveFibonacci(20)", globals=globals(), number=1000)
loop_time = timeit.timeit("loopFibonacci(20)", globals=globals(), number=1000)

print(f"Time taken by recursiveFibonacci(20): {recursive_time:.6f} seconds")
print(f"Time taken by loopFibonacci(20): {loop_time:.6f} seconds")

if recursive_time < loop_time:
    print("recursiveFibonacci is more efficient.")
    print(f"It's {loop_time / recursive_time:.2f} times faster.")
else:
    print("loopFibonacci is more efficient.")
    print(f"It's {recursive_time / loop_time:.2f} times faster.")

print("Program 9 ends\n")
#10)Class definition
print("Program 10 begins")
class Polygon:
    def __init__(self, sides):
        if len(sides) < 3:
            raise ValueError("A polygon must have at least 3 sides.")
        self.sides = list(sides)

    def get_sides(self):
        return self.sides

    def set_sides(self, sides):
        if len(sides) < 3:
            raise ValueError("A polygon must have at least 3 sides.")
        self.sides = list(sides)

    def perimeter(self):
        return sum(self.sides)

    def getOrderedSides(self, increasing=True):
        ordered_sides = sorted(self.sides) if increasing else sorted(self.sides, reverse=True)
        return tuple(ordered_sides)

# Test the Polygon class
sides = (5, 3, 7, 2)
polygon = Polygon(sides)

print("Original sides:", polygon.get_sides())
print("Perimeter:", polygon.perimeter())
print("Ordered sides in increasing order:", polygon.getOrderedSides())
print("Ordered sides in decreasing order:", polygon.getOrderedSides(increasing=False))


print("Program 10 ends\n")


#11)class inheritance
print("Program 11 begins")
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

class Rectangle(Polygon):
    def __init__(self, length, width):
        # Ensure that the input data is consistent with a rectangle
        if length <= 0 or width <= 0:
            raise ValueError("Both length and width must be positive values.")
        super().__init__([length, width, length, width])

    def area(self):
        return self.sides[0] * self.sides[1]

# Testing the Rectangle class
if __name__ == "__main__":
    length = 4
    width = 3
    rectangle = Rectangle(length, width)

    print(f"Rectangle with length {length} and width {width}:")
    print(f"Perimeter: {rectangle.perimeter()}")
    print(f"Area: {rectangle.area()}")

print("Program 11 ends\n")
