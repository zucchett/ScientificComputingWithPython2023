# 1. Convert the function  𝑓
  into a function that doesn't use global variables and that does not modify the original list
x = 5

def f(alist):
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) 

#2.Write the following expression using a list comprehension
ans=[x * x for x in range(10) if x % 2 == 1]
print (ans)

#3.Using the filter() hof, define a function that takes a list of words and an integer n as arguments, and returns a list of words that are shorter than n.
def filter_shortwords(word_list, n):
    
    short_words = filter(lambda word: len(word) < n, word_list)
    return list(short_words)  
# Example 
words = ["Nai", "Bungoma", "Nyeri", "Mombasa", "Baringo"]
n = 6
short_words = filter_short_words(words, n)
print(short_words)

#4.Write a function that takes the above dictionary and uses the map() higher order function to return a list that contains the length of the keys of the dictionary.
 def get_key_lengths(lang):
    key_lengths = list(map(len, lang.keys()))
    return key_lengths

lang = {"Python": 3, "Java": '', "Cplusplus": 'test', "Php": 0.7}

key_lengths = get_key_lengths(lang)
print(key_lengths)

#5. Write a Python program that sorts the following list of tuples using a lambda function, according to the alphabetical order of the first element of the tuple
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

# Sort the list of tuples base the language name
language_scores.sort(key=lambda x: x[0])

# Print the sorted list
for language, score in language_scores:
    print(f'{language}: {score}')
#6. Write two functions: one that returns the square of a number, and one that returns its cube.
#Then, write a third function that returns the number raised to the 6th power, using only the two previous functions
def square(x):
   return x**2
def cube(x):
    return x**3
def sixth_power(x):
    return square(cube(x))

# Example usage
x = 3
square_result = square(x)
cube_result = cube(x)
sixth_power_result = sixth_power(x)

print(f"Square: {square_result}")
print(f"Cube: {cube_result}")
print(f"6th Power: {sixth_power_result}")

#7.Write a decorator named `hello` that makes every wrapped function print “Hello World!” each time the function is called
def hello(func):
    def wrapper(*args, **kwargs):
        print("Hello World!")
        result = func(*args, **kwargs)
        return result
    return wrapper

@hello
def square(x):
    return x * x

result = square(5)
print(result)

#8. Calculate the first 20 numbers of the Fibonacci sequence using a recursive function
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

n = 20
fibonacci_sequence = fibonacci_recursive(n)
print(fibonacci_sequence)

#9. Run both the Fibonacci recursive function from the previous exercise, and the Fibonacci function from 01ex that use only for and while loops.
#Measure the execution code of the two functions with timeit
import timeit

def fibonacci_recursive(num):
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    elif num == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursive(num - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

num = 20
fibonacci_sequence = fibonacci_recursive(num)


#Calculate the first 20 numbers of the Fibonacci sequence using only for or while loops
fib_sequence = [0, 1]
for x in range(2, 20):
    next_number = fib_sequence[x - 1] + fib_sequence[x - 2]
    fib_sequence.append(next_number)
#measure the execution
recursive_time = timeit.timeit()
loop_time = timeit.timeit()
print(recursive_time)
print(loop_time)
#10. Define a class polygon. The constructor has to take a tuple as input that contains the length of each side. 
#The (unordered) input list does not have to have a fixed length, but should contain at least 3 items
class Polygon:
    def __init__(self, sides_lengths):
        if len(sides_lengths) < 3:
            raise ValueError("A polygon must have at least 3 sides.")
        self.sides_lengths = list(sides_lengths)


    def perimeter(self):
        return sum(self.sides_lengths)

    def get_ordered_sides(self, increasing=True):
        sorted_sides = sorted(self.sides_lengths)
        if not increasing:
            sorted_sides = sorted_sides[::-1]
        return tuple(sorted_sides)

# Testing the Polygon class
polygon = Polygon((3, 4, 5, 6))
print("Perimeter:", polygon.perimeter())
print("Ordered Sides (Increasing):", polygon.get_ordered_sides(increasing=True))
print("Ordered Sides (Decreasing):", polygon.get_ordered_sides(increasing=False))

#11. Define a class `rectangle` that inherits from `polygon`. Modify the constructor, if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle

class Rectangle(Polygon):
    def __init__(self, length, width):
        # Check if input is valid for a rectangle (positive lengths)
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive for a rectangle.")
        super().__init__((length, width, length, width))  # Pass sides to the parent class constructor

    def area(self):
        return self.sides_lengths[0] * self.sides_lengths[1]

# Testing the Rectangle class
rectangle = Rectangle(4, 5)
print("Perimeter:", rectangle.perimeter())
print("Area:", rectangle.area())
