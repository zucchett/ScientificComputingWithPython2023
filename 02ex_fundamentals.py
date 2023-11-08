#-----------------------------------------------------------------------------------------------------
# exercise 2 part one.Global variables


def f(alist, x):
    # making a copy of the alist
    list2 = alist.copy()
    # we do it same as the question
    for i in range(x):
        list2.append(i)  # Add numbers to the new list.
    return list2

# Assigning to alist
alist = [1, 2, 3]
x = 5
ans = f(alist,x)
print(ans)    # we print the changed 'alist'
print(alist)  # We print the original 'alist'

#-----------------------------------------------------------------------------------------------------
# exercise 2 part two.List comprehension


ans = []  # Create an empty list to store the results.

# Loop through numbers from 0 to 9.
for x in range(10):
    # Check if the number is odd
    if x % 2 == 1:
        # Square the odd number and add it to the result list.
        ans.append(pow(x,x))

#-----------------------------------------------------------------------------------------------------
# exercise 2 part three.Filter list

word_list = []
count = int(input("Enter how many words you want to enter: "))

for i in range(count):
    word = input("Enter a word: ")
    word_list.append(word)
print("Word List:", word_list)

n = int(input("Enter the maximum word length: "))
filtered_words = list(filter(lambda word: len(word) < n, word_list))
print("Filtered Words:", filtered_words)

#-----------------------------------------------------------------------------------------------------
# exercise 2 part four.Map dictionary


# Define the dictionary
lang = {"Python": 3, "Java": '', "Cplusplus": 'test', "Php": 0.7}

# Create a function to get the lengths of the keys
def get_lengths(value):
    key_lengths = list(map(len, value.keys()))
    return key_lengths

# Print the list of key lengths
print("Key Lengths:", get_lengths(lang))

#-----------------------------------------------------------------------------------------------------
# exercise 2 part five.Lambda functions


# Create a list of language names with their numbers accourding to the question
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]


# let's think that the list is not sorted
is_sorted = False


# Keep sorting until the list is fully sorted
while not is_sorted:
    is_sorted = True  # we keep continue sorting until we find it completely sorted
    i = 0

    # here we check if two neighboring languages are in the correct order
    while i < len(language_scores) - 1:
        # Get the names of the current and next language to compare.
        current_lang = language_scores[i][0]    # Store the name of the current language.
        next_lang = language_scores[i + 1][0]   # Store the name of the next language for comparison.

        # If they're out of order, swap them
        if current_lang > next_lang:
            language_scores[i], language_scores[i + 1] = language_scores[i + 1], language_scores[i]
            is_sorted = False  # The list is not yet fully sorted
        i += 1

# Keep sorting until no more swaps are needed.

# Print the sorted list of languages
for language in language_scores:
    print(language)

#-----------------------------------------------------------------------------------------------------
# exercise2 part six.Nested functions


# This function calculates the square of a given number.
# It multiplies the number by itself to find the result.
# For example, if you pass 2 as the number, it will return 2 * 2 = 4.
def calculate_square(number):
    return number * number


# This function calculates the cube of a given number.
# It multiplies the number by itself twice to find the result.
# For example, if you pass 2 as the number, it will return 2 * 2 * 2 = 8.
def calculate_cube(number):
    return number * number * number


# This function calculates the 6th power of a given number by squaring it twice.
def calculate_sixth_power(number):
    square_result = calculate_square(number)
    sixth_power_result = calculate_cube(square_result)
    return sixth_power_result


# Test the functions with the number 2
number = 2
print("number is", number)
print(f"Square of {number}: {calculate_square(number)}")
print(f"Cube of {number}: {calculate_cube(number)}")
print(f"6th power of {number}: {calculate_sixth_power(number)}")

#-----------------------------------------------------------------------------------------------------
# exercise2 part seven.Decorators


# Define a decorator function named "hello"
def hello(function):
    # Define a new function "wrapper" to add "Hello World!" before calling the original function
    def wrapper(x):
        print("\nHello World!")  # Print "Hello World!"
        result = function(x)  # Call the original function with the argument 'x'
        return result  # Return the result of the original function

    return wrapper  # Return the wrapped function

# Decorate the "square" function with the "hello" decorator
@hello
def square(x):
    return x * x

# Call the decorated "square" function with the argument 5 and show the final result to the user
result = square(10)
print("we are calculating square of:  10")
print(f"Result: {result}")  # Print the result of the decorated function

#-----------------------------------------------------------------------------------------------------
# exercise2 part eight.The Fibonacci sequence (part 2)

# Function to calculate Fibonacci numbers
def fibonacci(n):
    if n <= 0:
        return 0  # If n is 0 or negative, return 0
    elif n == 1:
        return 1  # If n is 1, return 1
    else:
        # For n > 1, add the previous two Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

# Calculate and show the first 20 Fibonacci numbers
i = 0
while i < 20:
    result = fibonacci(i)  # Calculate the Fibonacci number at position i
    print("Fibonacci(", i, "):", result)  # Display the result
    i += 1

#-----------------------------------------------------------------------------------------------------
# exercise2 part nine.The Fibonacci sequence (part 3)


import timeit

# Define the recursive Fibonacci function
# This function calculates the nth Fibonacci number using a recursive approach.
# It checks if n is 0 or 1 and returns 0 or 1.
# For n > 1, it calls itself recursively to find the Fibonacci number by adding
# the previous two Fibonacci numbers.
def recursiveFibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2)


# Define the Fibonacci with a for loop
# It makes a list 'fibonacci_numbers' with the first two Fibonacci numbers.
# then it uses a 'for' loop to calculate and store the next Fibonacci numbers.
# The loop runs from 2 to n-1, and adding the previous two numbers
# in 'fibonacci_numbers' to compute the next Fibonacci number.
# The calculated Fibonacci sequence will return as a list
def loopFibonacci(n):
    fibonacci_numbers = [0, 1]
    for i in range(2, n):
        next_fib = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_fib)
    return fibonacci_numbers

# Measure the execution time of the recursive Fibonacci function
# Run 'recursiveFibonacci(20)' 1000 times and record the time taken
recursive_time = timeit.timeit("recursiveFibonacci(20)", globals=globals(), number=1000)

# Measure execution time of the loop-based Fibonacci function
loop_time = timeit.timeit("loopFibonacci(20)", globals=globals(), number=1000)

# Display execution times for comparison
print("\nRecursive Fibonacci time:", recursive_time, "seconds")
print("Loop-based Fibonacci time:", loop_time, "seconds")

# Compare the efficiency of the two implementations
if recursive_time < loop_time:
    print("\nThe recursive implementation is more efficient.")
else:
    print("\nThe loop-based implementation is more efficient.")

#-----------------------------------------------------------------------------------------------------
# exercise2 part ten.class definition


# Class definition for Polygon
class Polygon:
    # Creating a polygon with a list of side lengths
    def create_polygon(n, sides):
        # Check if there are at least 3 sides
        if len(sides) < 3:
            print("Polygon should have minimum 3 sides.")
        else:
            n.sides = list(sides)

    # Method to change the side lengths of the polygon
    def setSidesLength(n, sides):
        # Check if there are at least 3 sides
        if len(sides) < 3:
            print("A polygon must have a minimum of 3 sides.")
        else:
            n.sides = list(sides)   # Update the side lengths

    # Method to get the current side lengths
    def getSides(n):
        return n.sides

    # Method to calculate the polygon's perimeter by summing the side lengths
    def perimeter(n):
        total_length = 0  # Set the total length to zero at first.
        for side_length in n.sides:
            total_length += side_length  # Add each side's length to the total
        return total_length  # Return the calculated perimeter

    # Method to get the side lengths in increasing or decreasing order
    def getOrderedSides(n, increasing=True):
        sorted_sides = sorted(n.sides)
        if not increasing:
            sorted_sides.reverse()
        # Return the sorted sides
        return sorted_sides

# Testing the class with different side lengths
polygon = Polygon()
polygon.create_polygon([5, 8, 12, 6, 10])
print("Perimeter:", polygon.perimeter())
print("increasing:")
print("Ordered Sides:", polygon.getOrderedSides(increasing=True))
print("decreasing:")
print("Ordered Sides:", polygon.getOrderedSides(increasing=False))

#-----------------------------------------------------------------------------------------------------
# exercise2 part eleven.class inheritance


# Class definition for Polygon
class Polygon:
    # Creating a polygon with a list of side lengths
    def create_polygon(n, sides):
        # Check if there are at least 3 sides for any polygon
        if len(sides) < 3:
            print("Polygon should have minimum 3 sides.")
        n.sides = list(sides)

    # Method to calculate the polygon's perimeter by summing the side lengths
    def perimeter(n):
        total_length = 0  # Set the total length to zero at first.
        for side_length in n.sides:
            total_length += side_length  # Add each side's length to the total
        return total_length  # Return the calculated perimeter

# Rectangle class definition that inherits from Polygon
class Rectangle(Polygon):
    # Taking width and height as input
    def create_polygon(n, width, height):
        if width <= 0 or height <= 0:
            print("Invalid input!! Both width and height must be greater than zero.")
        else:
            # Verify that the input data depicts a four-sided rectangle.
            Polygon.create_polygon(n, [width] * 2 + [height] * 2)

    # function to calculate and return the area of the rectangle
    def area(n):
        width, height = n.sides[0], n.sides[2]
        return width * height

# Testing the Rectangle class
rectangle = Rectangle()
rectangle.create_polygon(5, 8)  # Create a rectangle with width 5 and height 8
print("\nCreated a rectangle with width 5 and height 8")
print("Perimeter of Rectangle:", rectangle.perimeter())
print("Area of Rectangle:", rectangle.area())

#-----------------------------------------------------------------------------------------------------
