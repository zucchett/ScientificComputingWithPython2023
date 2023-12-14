# LAB 1
#ex1:
print("1 ------ The HelloWorld replacement")

result = [] #did a list because tuple can't be modified
for i in range(1, 101):
    if i % 3 == 0 :
        if i % 5 == 0 :
            print ("Helloworld")
            result.append("Helloworld")
        else : 
            print ("Hello")
            result.append("Hello")
    elif i % 5 == 0 :
        print ("World")
        result.append("World")
    else : 
        print(i)
        result.append(i)
print (result)
for j in range (len(result)) :
    if result[j] == "Hello" :
        result[j] = "Python"
    elif result[j] == "World" :
        result[j] = "Works"
print (result)
        
#ex2:
print("2 ------ The swap")

x = input("Set the value of x :")
y = input("Set the value of y :")
x,y = y,x
print("x :", x, ", y :", y)

#ex3:
print("3 ------ Computing the distance")

import math
u = [3,0]
v = [0,4]

distance = math.sqrt(pow((u[0]+v[0]), 2) + pow((u[1]+v[1]), 2))
print(distance)

#ex4:
print("4 ------ Counting letters")


def count_char (s) :
    all_freq = {}

    for i in s:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    return all_freq

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
print(count_char(s1))
print(count_char(s2))

#ex5:
print("5 ------ Isolating the unique")


def count_unique_numbers (lis) :
    l = set(lis)
    print(len(l))
    return l
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20,36]
print(len(l))
print(count_unique_numbers(l))

#ex6:
print("6 ------ Casting")


def add_variables(var1, var2):
    try:
        result = var1 + var2
        return result
    except TypeError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

x = input("Enter the first variable: ")
y = input("Enter the second variable: ")

try:
    x2 = int(x)
except ValueError:
    try:
        x2 = float(x)
    except ValueError:
        x2 = x

try:
    y2 = int(y)
except ValueError:
    try:
        y2 = float(y)
    except ValueError:
        y2 = y

result = add_variables(x2, y2)
print("Addition:", result)


#ex7:
print("7 ------ Cubes")


cubes_list_for = []
for x in range(11):
    cubes_list_for.append(x ** 3)

print(cubes_list_for)
cube_list_comprehension = [x ** 3 for x in range(11)]
print(cube_list_comprehension)

#ex8:
print("8 ------ List comprehension")


a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)
a_list_comprehension = [(i,j) for i in range(3) for j in range (4)]

print(a_list_comprehension)

#ex9:
print("9 ------ Nested list comprehension")


pythagorean_triples = [(a, b, c) for c in range(1, 100)
                        for b in range(1, c)
                        for a in range(1, b)
                        if a**2 + b**2 == c**2]

unique_pythagorean_triples = list(set(pythagorean_triples))
unique_pythagorean_triples.sort(key=lambda triple: triple[2])

for triple in unique_pythagorean_triples:
    print(triple)


#ex10:
print("10 ------ Normalization of a N-dimensional vector")


input_vector = [1,5,9,3]

vector_len = math.sqrt(sum(x**2 for x in input_vector))
output_vector = input_vector
for i in range(len(output_vector)) :
    output_vector[i] = output_vector[i] / vector_len

print(output_vector)
print(math.sqrt(sum(x**2 for x in output_vector)))

#ex11:
print("11 ------ The Fibonacci sequence")


fibonacci_list = [0,1]

for i in range(18):
    fibonacci_list.append(fibonacci_list[i]+fibonacci_list[i+1])

print(fibonacci_list)

