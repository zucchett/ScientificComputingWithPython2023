import math

###################1. The HelloWorld replacement####################
print("###################START 1. The HelloWorld replacement###################")
hello_list = []
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("HelloWorld")
        hello_list.append("HelloWorld")
    elif i % 3 == 0:
        print("Hello")
        hello_list.append("Hello")
    elif i % 5 == 0:
        print("World")
        hello_list.append("World")
    else:
        print(i)
        hello_list.append(i)
    
hello_tuple = tuple(hello_list)
substitute_tuple = (['PythonWorks' if hello_tuple[i] == 'HelloWorld' else 'Python' if hello_tuple[i] == 'Hello' else 'Works' if hello_tuple[i] == 'World' else hello_tuple[i] for i in range(len(hello_tuple))])
print(substitute_tuple)

###################2. The swap####################
print("###################START 2. The swap###################")
x = 1
y = 2
x, y = y, x 
print("x:"+str(x)+" y:"+str(y))

###################3. Computing the distance####################
print("###################START 3. Computing the distance###################")
u = (3,0)
v = (0,4)
result = math.sqrt(((u[0]+v[0])**2)+((u[1]+v[1])**2))
print("The distance between the two points: "+str(u)+", "+str(v)+" is: "+str(result))

###################4. Counting letters####################
print("###################START 4. Counting lettersCL###################")
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

s1_lowercase = s1.lower()
s2_lowercase = s2.lower()
char_count_s1 = {}
char_count_s2 = {}

for i in range(len(s1_lowercase)):
    if s1_lowercase[i] in char_count_s1.keys():
        char_count_s1[s1_lowercase[i]] += 1
    else:
        char_count_s1[s1_lowercase[i]] = 1
print("Character count string 1: "+str(char_count_s1))

for i in range(len(s2_lowercase)):
    if s2_lowercase[i] in char_count_s2.keys():
        char_count_s2[s2_lowercase[i]] += 1
    else:
        char_count_s2[s2_lowercase[i]] = 1
print("Character count string 2: "+str(char_count_s2))

###################5. Isolating the unique####################
print("###################START 5. Isolating the unique###################")
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
unique_values = []
for i in range(len(l)):
    if l.count(l[i]) == 1:
        unique_values.append(l[i])
print("The unique values are: "+str(unique_values)+", and they are "+str(len(unique_values))+" in total.")

###################6. Casting####################
print("###################START 6. Casting###################")
var1_str = input("Type the value of variable 1: ")
var2_str = input("Type the value of variable 2: ")
try:
    var1 = float(var1_str)
    var2 = float(var2_str)
    try:
        result = var1 + var2
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")

###################7. Cubes####################
print("###################START 7. Cubes###################")
list_cubes_for = []
for i in range(11):
    list_cubes_for.append(i**3)
print(list_cubes_for)

list_cube_list_comprehension = [i**3 for i in range(11)]
print(list_cube_list_comprehension)

###################8. List comprehension####################
print("###################START 8. List comprehension###################")
a = []
a = [(i,j) for i in range(3) for j in range(4)]
print(a)

###################9. Nested list comprehension####################
print("###################START 9. Nested list comprehension###################")
solutions = []
for c in range(1,101):
    for a in range(1,100):
        for b in range(1,100):
            if a**2 + b**2 == c**2 and (b,a,c) not in solutions:
                solutions.append((a,b,c))
print(solutions)

###################10. Normalization of a N-dimensional vector####################
print("###################START 10. Normalization of a N-dimensional vector###################")
vector = (10,13,8)
sum_sqrt = 0
for i in range(len(vector)):
    sum_sqrt += vector[i]**2
den_normalize = 1/math.sqrt(sum_sqrt)
normalized_vector = [round(vector[i]*den_normalize,2) for i in range(len(vector))]
print("Normalized vector: "+str(normalized_vector))

###################11. The Fibonacci sequence####################
print("###################START 11. The Fibonacci sequence###################")
fib_old = 0
fib_new = 0
for i in range(20):
    if i == 0:
        print(0)
    elif i == 1 or i == 2: 
        print(1)
        fib_old = 1
        fib_new = 1
    else:
        print(fib_new+fib_old)
        fib_old, fib_new = fib_new, fib_new+fib_old
