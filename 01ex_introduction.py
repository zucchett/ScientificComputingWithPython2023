# Exercise 1 (The HelloWorld Replacement)
def hello_world_replacement():
  hello_world_result = ()
  #goes through 1 to <101 which is 100
  for i in range(1, 101):
    #divisible by 15
    if i % 3 == 0 and i % 5 == 0:
      print("HelloWorld")
      hello_world_result += tuple(["HelloWorld"])
    #divisible by 3
    elif i % 3 == 0:
      print("Hello")
      hello_world_result += tuple(["Hello"])
    #divisible by 5
    elif i % 5 == 0:
      print("World")
      hello_world_result += tuple(["World"])
    else:
      print(i)
      hello_world_result += tuple([i])
  #replaces "Hello" with "Python" in our tuple
  python_works_result = tuple(item if item != "Hello" else "Python" 
                              for item in hello_world_result)
  #replaces "World" with "Works" in our tuple
  python_works_result = tuple(item if item != "World" else "Works" 
                              for item in python_works_result)
  #replaces "HelloWorld" with "PythonWorks" in our tuple
  python_works_result = tuple(item if item != "HelloWorld" else "PythonWorks" 
                              for item in python_works_result)
  print(python_works_result)

hello_world_replacement()

# Exercise 2 (The Swap)
import sys

def swap_variables(x, y):
  #swaps the variables without using a temp var
  return y, x;

# comment the following lines / had to comment them to satisfy:
# The exercises need to run without errors with `python3 01ex_introduction.py`

x = sys.argv[1]
y = sys.argv[2]

x, y = swap_variables(x, y)
print(x, y)

# Exercise 3 (Computing the distance)
import math

def euclidean_distance(u, v):
  # calculates the x difference
  dx = u[0] - v[0]
  # calculates the y difference
  dy = u[1] - v[1]

  print(math.sqrt(dx**2 + dy**2))

# u = (3,0)
# v = (0,4)
# euclidean_distance(u, v)

# Exercise 4 (Counting letters)
def count_characters(string):
  # declare an empty dictionary
  character_counts = {}
  # making all the chars lower for counting
  for character in string.lower():
    # if there's a key based on char increment the number (value of the key)
    if character in character_counts:
      character_counts[character] += 1
    # else create a key,value pair with initial value of 1
    else:
      character_counts[character] = 1
  # prints the character list and the number of occurance
  print("Characters and the number of their appearance in the text:")
  for character, count in character_counts.items():
    print(f"{character}: {count}")
  return character_counts

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

count_characters(s1)
count_characters(s2)

# Exercise 5 (Isolating the unique)
def count_unique_numbers(list):
  # we use dictionary just like the previous exercise
  # note that dictionary is a standard Python data structure
  numbers = {}
  # counts all the numbers repetitions
  for number in list:
    if number not in numbers:
      numbers[number] = 1
    else:
      numbers[number] += 1
  # checks to find all the unique occurances
  unique_numbers = []
  for number in numbers:
    if numbers[number] == 1:
      unique_numbers.append(number)

  return len(unique_numbers)

list = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

print(f"The number of unique numbers in the list is: {count_unique_numbers(list)}")

# Exercise 6 (Casting)
def add_variables(var1, var2):
  try:
    var1 = int(var1)
    var2 = int(var2)
    return var1 + var2
  except ValueError:
    try:
      var1 = float(var1)
      var2 = float(var2)
      return var1 + var2
    except ValueError:
      try:
        var1 = str(var1)
        var2 = str(var2)
        return var1 + var2
      except ValueError:
        # returns None if addition is not possible
        return None

# comment the following lines / had to comment them to satisfy:
# The exercises need to run without errors with `python3 01ex_introduction.py`

var1 = sys.argv[1]
var2 = sys.argv[2]

sum = add_variables(var1, var2)

if sum is not None:
  print(sum)
else:
  print("The addition of the two variables is not possible.")

# Exercise 7 (Cubes)
cubes = []
# Using for loop
for x in range(11):
  cubes.append(x**3)
# Using list comprehension
cubes = [x**3 for x in range(11)]

# Exercise 8 (List comprehension)
a = [(i, j) for i in range(3) for j in range(4)]

# Exercise 9 (Nested list comprehension)
pythagorean_triplets = []

for a in range(1, 100):
    for b in range(a, 100):
        c = math.sqrt(a**2 + b**2)
        if c.is_integer() and c < 100:
            pythagorean_triplets.append((a, b, int(c)))

# Remove duplicates from the array by casting to set
unique_pythagorean_triplets = set(pythagorean_triplets)

print(unique_pythagorean_triplets)

# Exercise 10 (Normalization of a N-dimensional vector)
def vector_normalizer(vector):
  # The total squared sum of all the elements
  total_squared_sum = 0
  for element in vector:
    total_squared_sum += element**2

  # In this case the vector is already normalized
  if total_squared_sum == 1:
    return vector

  # Normalize the vector and using tuple constructor
  normalized_vector = tuple(element / math.sqrt(total_squared_sum) for element in vector)

  return normalized_vector
"""
vector = (1, 2, 3)
normalized_vector = vector_normalizer(vector)
sum = 0
for element in normalized_vector:
    sum += element**2
    print(sum)
print(normalized_vector)
"""
# Exercise 11 (The Fibonacci sequence)
n0 = 0
n1 = 1
i = 0
while i < 20:
  print(n0)

  # Calculate the next Fibonacci number
  n2 = n0 + n1
  # Update n0 and n1
  n0 = n1
  n1 = n2

  i += 1