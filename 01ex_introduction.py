import math

# 1 The HelloWorld replacement
def task_1():
    results = []
    for i in range(1, 100):
        if(i%3==0):
            if(i%5==0):
                results.append('Hello World')
                
            else: results.append('Hello')
        elif(i%5==0):
            results.append('World')
        else:
            results.append(i)
    print("Results for part a:")
    print(results)
        
    for element in results:
        if(element=='Hello'): element = 'Python'
        elif(element == 'World'): element = 'Works'
    results_b = tuple(results)
    print("Results for part b:")
    for res in results_b:
        print(res)


print('Task 1')
task_1()

# 2 The swap
def task_2():
    x = input('Enter x value: ')
    y = input('Enter y value: ')
    x, y = y, x
    print('x value: ' + str(x))
    print('y value: ' + str(y))

print('Task 2')
task_2()

# 3 Computing the distance
def task3(u, v):
   d = math.sqrt((v[0] - u[0])**2 + (v[1] - u[1])**2)
   print(d)

print('Task 3')
task3((3,0), (0,4))

# 4 Counting letters
def task4(input_string):
    input_string = input_string.lower()
    input_string = input_string.replace(' ', '')
    num_of_times_each_character_occurs = {}
    for letter in set(input_string):
        num_of_times_each_character_occurs[letter] = input_string.count(letter)
        print(letter + ' occurs ' + str(input_string.count(letter)) + ' times in the given string.')

#test strings 
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
print('Task 4')
task4(s2)

# 5 Isolating the unique
def task5(list_w_numbers):
   set_of_unique_numbers = set(list_w_numbers)
   num_of_unique_numbers = len(set_of_unique_numbers)
   print('Number of uniqe numbers in list: ' + str(num_of_unique_numbers))
   print('Uniqe numbers: ')
   print(set_of_unique_numbers)

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

print('Task 5')
task5(l)

# 6 Casting
def task6():
    var1 = input('Enter variable: ')
    var2 = input('Enter next variable: ')
    try:
        var1 = int(var1)
    except ValueError:
        try:
            var1 = float(var1)
        except ValueError:
            var1 = var1

    try:
        var2 = int(var2)
    except ValueError:
        try:
            var2 = float(var2)
        except ValueError:
            var2 = var2

    try:
        result = var1 + var2
        print(result)
    except:
        print('Addition not possible')
        return f"Error: {TypeError}"

print('Task 6')
task6()

# 7 Cubes
#a
def task7a():
    cubes = []
    for x in range(0,11):
        cube = x ** 3
        cubes.append(cube)
    print(cubes)

print('Task 7a')
task7a()

#b
def task7b():
    cubes = [x ** 3 for x in range(0,11)]
    print(cubes)

print('Task 7b')
task7b()


# 8 List comprehension
def task8():
    a = [(i, j) for i in range(3) for j in range(4)]
    print(a)

print('Task 8')
task8()

# 9 Nested list comprehension
def task9():
    pythagorean_triples = [(a, b, c) for a in range(1, 100) for b in range(a, 100) for c in range(b, 100) if a**2 + b**2 == c**2]
    print(pythagorean_triples)

print('Task 9')
task9()

# 10 Normalization of a N-dimensional vector
def task10(vector):
    magnitude = math.sqrt(sum(x**2 for x in vector))
    normalized_vector = tuple(x/magnitude for x in vector)
    return normalized_vector

test_vector = [3, 6, 9]
print('Task 10')
print(task10(test_vector))

# 11 The Fibonacci sequence
def task11():
    Fibonacci_sequence = []
    while len(Fibonacci_sequence) < 20:
        if(len(Fibonacci_sequence) < 2):
            Fibonacci_sequence.append(1)
        else:
            Fibonacci_sequence.append(sum(Fibonacci_sequence[len(Fibonacci_sequence)-2:]))
    print(Fibonacci_sequence)

print('Task 11')
task11()

