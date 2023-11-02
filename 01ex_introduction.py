#EXERCISES WEEK No 1 
#Suly Vannesa Cifuentes Bohorquez
#Student ID: 2080663
#-------------------------------------- EX. #1 The HelloWorld replacement-------------------------------------
print("\nEXERCISE # 1 \n")
#Part A Replacing multiples of 3 and 5 to Hello World
  
listReplacement = [] # List for the Hello World Replaceement  

for x in range(1, 101):
  if x % 3 == 0 and x % 5== 0:
      listReplacement.append("HelloWorld")
  elif x % 5 == 0:
      listReplacement.append("World") 
  elif x % 3 == 0:
      listReplacement.append("Hello") 
  else: 
        listReplacement.append(str(x))

print("\nResult List:\n")
for item in listReplacement:
    print(item)

#PartB from Hello World to Python Works 

resultT= tuple(listReplacement)
resultT = tuple(item.replace("Hello", "Python").replace("World", "Works") if isinstance(item, str) else item for item in resultT)

print("\nResult list in a Tuple: \n")
for item in resultT:
    print(item)

#--------------------------------------------------EX. #2 The Swap---------------------------------------------

print("\nEXERCISE # 2 \n")

#Command line to take the inputs 

x = input(" Value of x: ")
y = input(" Value of y: ")

x, y = str(y), str(x)

print("\nNew Value of x:", x)
print("New Value of y:", y)

#------------------------------------ Ex. # 3 Euclidean distance--------------------------------------------
## For this we import the math library at the begining 

# Euclidean distance: It's a way to quantify the straight-line distance between
# two points in a two-dimensional or multi-dimensional space.


print("\nEXERCISE # 3 \n")

input_a = input("Enter the values of A (x,y): ")
p_a = tuple(map(int, input_a.split(',')))

input_b = input("Enter the values of B (x,y): ")
p_b = tuple(map(int, input_b.split(',')))

print("Point A =", p_a)
print("Point B =", p_b)

x1, y1 = p_a
x2, y2 = p_b

# Euclidean Distance
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f"The Euclidean distance between {p_a} and {p_b} is {distance:.2f}\n")

#------------------------------------ Ex. # 4 Counting letters--------------------------------------------

print ("\nEXERCISE # 4\n")

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

s1 = s1.lower()  # Convert to lowercase to ignore capitalization
s2 = s2.lower()

# Create a list to store the caracters

counts_s1 = [0] * 256  # -> 256 to cover all possible ASCII
counts_s2 = [0] * 256

#  s1
for char in s1:
    if char.isascii(): #this ensures that is going to count all the ASCII characteres
        counts_s1[ord(char)] += 1 #counter 

# s2
for char in s2:
    if char.isascii():
        counts_s2[ord(char)] += 1


print("Character counts in s1:")
for char_code, count in enumerate(counts_s1):
    if count > 0:
        print(f"Character '{chr(char_code)}': {count}")

# Print for s2
print("\nCharacter counts in s2:")
for char_code, count in enumerate(counts_s2):
    if count > 0:
        print(f"Character '{chr(char_code)}': {count}")
        
#------------------------------------ Ex. # 5 Issolating the unique --------------------------------------------

print ("\nEXERCISE # 5\n")

# List of numbers
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
     85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
     1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
     45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

unique = [] 
duplicates = []

for number in l:
    if l.count(number) == 1:
        unique.append(number) ## add it to unique if count =1
    elif number not in duplicates:
        duplicates.append(number) #if not then add it to duplicates

print("Unique numbers in the list:")
print(unique)
print(f"Count of unique numbers: {len(unique)}")

## ahora con datastructure set

# Defining the list
print("\n Now using datastructures SET \n")
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
     85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
     1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
     45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

# Using sets to find unique numbers
unique = set()
duplicate_numbers = set()

for number in l:
    if number in unique:
        unique.remove(number)
        duplicate_numbers.add(number)
    elif number not in duplicate_numbers:
        unique.add(number)

# Count the number of unique numbers
count_of_unique_numbers = len(unique)

print("Unique numbers in the list:")
print(unique)
print(f"Count of unique numbers: {count_of_unique_numbers}") 

#------------------------------------ Ex. # 6 Casting --------------------------------------------

print("\nEXERCISE # 6 \n")

try:
    v1 = input("Enter the variable #1: ")
    v2 = input("Enter the variable #2: ")

    # Try to convert the variables to numbers
    v1 = float(v1)
    v2 = float(v2)

    result = v1 + v2

 
    print(f"Addition result: {result}")

except (ValueError, TypeError):
    # Error if the conversion  wasn't possible
    print("Error: Please provide valid values for addition.")
except Exception as e:
    print(f"An error occurred: {e}")


#------------------------------------ Ex. # 7 Cubes --------------------------------------------

print ("\nEXERCISE # 7 \n")  

cubes = [] 

for x in range(11):  # Loop through numbers from 0 to 10
    cube = x ** 3     
    cubes.append(cube)  

print("Cubes using a for:", cubes)

##Part B Using list of comprehension

cubes_list = [x ** 3 for x in range(11)]

print("Cubes list comprehension:", cubes_list)

#------------------------------------ Ex. # 8 List of Comprehension --------------------------------------------

print ("\nEXERCISE # 8 \n") 

a = [(i, j) for i in range(3) for j in range(4)]
print(a)

#----------------------------------- Ex. # 9 Nested List --------------------------------------------

print ("\nEXERCISE # 9 \n") 

pythagorean_t = []


for a in range(1, 100):
    for b in range(a, 100):
        c = (a**2 + b**2) ** 0.5  # Pythagorean theorem

        # Check if c is an integer and less than 100
        if c.is_integer() and c < 100:
            pythagorean_t.append((int(a), int(b), int(c)))

py_tuple = tuple(pythagorean_t)

print("Unique Pythagorean triples: ",py_tuple)

#----------------------------------- Ex. # 10 Normalization of a N-dimensional vector --------------------------------------------

 
print ("\nEXERCISE # 10 \n") 

n_dimensional_vector = (7, 8, 9)

# Calculate the squared sum of all entries
squared_sum = sum(entry ** 2 for entry in n_dimensional_vector)

magnitude = squared_sum ** 0.5

# Normalization
normalized_vector = tuple(entry / magnitude for entry in n_dimensional_vector)


print("Original Vector:", n_dimensional_vector)
print("Normalized Vector:", normalized_vector)


#----------------------------------- Ex. # 11 Fibonacci Sequence  --------------------------------------------

print ("\nEXERCISE # 11 \n") 

fibonacci = [0, 1] # Two first fibonacci

for i in range(2, 20):
    next_fibonacci = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(next_fibonacci)
print("Fibonacci sequence:",fibonacci)
