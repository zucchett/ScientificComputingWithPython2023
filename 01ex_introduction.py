import math

def ex1_a_1():
    print('1.A program that prints the numbers from 1 to 100')
    x = 1
    while x != 101:
        print(x)
        x += 1

    print("\n################################################\n")

def ex1_a_2():
    print("""1.a.A program that prints the numbers from 1 to 100 but for multiples of
three print "Hello" instead of the number and for the multiples of five print "World".""")
    x = 1
    while x != 101:
        if x % 3 == 0:
            print('Hello')
        elif x % 5 == 0:
            print('World')
        else:
            print(x)
        x += 1

    print("\n################################################\n")
	
def ex1_a_3():
    print("""1.a.A program that prints the numbers from 1 to 100 but for multiples of
three print "Hello" instead of the number and for the multiples of five print "World"
for numbers which are multiples of both three and five print "HelloWorld".""")
    x = 1
    while x != 101:
        if x % 3 == 0 and x % 5 == 0:
            print('HelloWorld')
        elif x % 3 == 0:
            print('Hello')
        elif x % 5 == 0:
            print('World')
        else:
            print(x)
        x += 1	

    print("\n################################################\n")

def ex1_b_1():
    print("""1.b. Write a program that:
prints the numbers from 1 to 100
but for multiples of three print "Hello" instead of the number and for the multiples of five print "World"
for numbers which are multiples of both three and five print "HelloWorld".
b) Put the result in a tuple and substitute "Hello" with "Python" and "World" with "Works".""")
    x = 1
    result_tuple = tuple()
    print(type(result_tuple))
    y = list(result_tuple)
    while x != 101:
        if x % 3 == 0 and x % 5 == 0:
            print('HelloWorld')
            y.append('HelloWorld')
        elif x % 3 == 0:
            print('Hello')
            y.append('Python')
        elif x % 5 == 0:
            print('World')
            y.append('Works')
        else:
            print(x)
            y.append(x)
        x += 1
    
    result_tuple = tuple(y)
    print(type(result_tuple))
    print(result_tuple)
    print("\n################################################\n")

def ex1_b_2():
    print("""1.b. Write a program that:
prints the numbers from 1 to 100
but for multiples of three print "Hello" instead of the number and for the multiples of five print "World"
for numbers which are multiples of both three and five print "HelloWorld".
b) Put the result in a tuple and substitute "Hello" with "Python" and "World" with "Works".""")
    x = 1
    result_tuple = tuple()
    print(type(result_tuple))
    y = list(result_tuple)
    while x != 101:
        if x % 3 == 0 and x % 5 == 0:
            print('HelloWorld')
            y.append('PythonWorks')
        elif x % 3 == 0:
            print('Hello')
            y.append('Python')
        elif x % 5 == 0:
            print('World')
            y.append('Works')
        else:
            print(x)
            y.append(x)
        x += 1
    
    result_tuple = tuple(y)
    print(type(result_tuple))
    print(result_tuple)
    print("\n################################################\n")

def ex2():
    print("""2.Write a program that swaps the values of two input variables x and y from command line (whatever the type).
Try to do that without using a temporary variable, exploiting the Python syntax.""")
    x = input("Enter first value: ")    
    y = input("Enter second value: ")

    print("First value is " + str(x))
    print("Second value is " + str(y))

    x, y = y, x

    print("After swapping ")
    print("First value is " + str(x))
    print("Second value is " + str(y))
    print("\n################################################\n")

def ex3():
    print("""3.Write a program that calculates and prints the euclidean distance between two given points 
and in a 2D space, where and are both 2-tuples.""")
    x = (3, 0)
    y = (0, 4)
    print(type(x), type(y))
    print("Distace equal to " + str(math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)))
    print("\n################################################\n")

def ex4():
    print("4.Write a program that calculates the number of times each character occurs in a given string. Ignore differences in capitalization.")
    s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
    s2 = "The quick brown fox jumps over the lazy dog"

    s1 = s1.lower()
    s2 = s2.lower()
    my_dict = {}

    for i in s1:
        if i not in my_dict:
            my_dict.update({i: 1})
        else:
            my_dict[i] = my_dict[i] + 1
    
    print(my_dict)

    my_dict2 = {}

    for i in s2:
        if i not in my_dict2:
            my_dict2.update({i: 1})
        else:
            my_dict2[i] = my_dict2[i] + 1
    
    print(my_dict2)

    print("First string")
    for key, value in my_dict.items():
        print(f"Character: {key}, The number of times: {value}")
        
    print("Second string")
    for key, value in my_dict2.items():
        print(f"Character: {key}, The number of times: {value}")

    print("\n################################################\n")

def ex5():
    print('5.Write a program that determines and counts the unique numbers (numbers with only one occurrence) in the list:')
    l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
    
    my_dict = {}

    for i in l:
        if i not in my_dict:
            my_dict.update({i: 1})
        else:
            my_dict[i] = my_dict[i] + 1
    print(my_dict)
    print('')
    new_dict = {}
    for i in my_dict:
        if my_dict[i] == 1:
            new_dict[i] = my_dict[i]
            
    print(new_dict)
    print("The unique numbers: " + str(len(new_dict)))

    print("\n################################################\n")

def ex6():
    print("""6.Write a program that:
reads from command line two variables, that can be either int, float, or str.
use the try/except expressions to perform the addition of these two variables, only if possible
print the result without making the code crash for all the int/float/str input combinations.""")
    
    x = input("Enter first value: ")    
    y = input("Enter second value: ")

    print("Result of the sum of two values")

    try:
        print(int(x)+int(y))
    except ValueError:
        try:
            print(float(x)+ float(y))
        except:
            print(x+y)

    print("\n################################################\n")

def ex7():
    print('7.Create a list of the cubes of x for x in [0, 10] using a for loop')
    cubes_a = []
    i = 0
    while i != 11:
        cubes_a.append(i**3)
        i = i + 1
    print(cubes_a)


    print('Create a list of the cubes of x for x in [0, 10] using a list comprehension')
    cubes_b = [x**3 for x in range(11)]
    print(cubes_b)
    print("\n################################################\n")

def ex8():
    print("""8.Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.
        a = []
        for i in range(3):
            for j in range(4):
                a.append((i, j))
        print(a)""")
    x = [(i, j) for i in range(3) for j in range(4)]
    print(x)
    print("\n################################################\n")
    
def ex9():
    print("9.Find and put in a tuple all unique Pythagorean triples for the positive integers a, b, c, where c lower than 100 ")
    result = []
    a = 1
    b = 1
    for a in range(1, 100):
        for b in range(a, 100):
            c = math.sqrt(a**2 + b**2)
            if c < 100 and c.is_integer():
                result.append((a, b, int(c)))
    
    result = tuple(result)
    
    print('\n'.join([f"(Value a: {a}, Value b: {b}, Value c: {int(c)})" for a, b, c in result]))
    print("\n################################################\n")  
def ex10():
    print("""10.Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers,
and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1).""")
    
    vector = (2,2,2)
    sum = 0 
    for x in vector:
        sum += x**2

    norm_vector = math.sqrt(sum)

    new_vector = tuple(x/norm_vector for x in vector)

    print(new_vector)
    print("\n################################################\n")
    
def ex11():
    print("11.Calculate the first 20 numbers of the Fibonacci sequence using only for or while loops.")
    result = [0, 1]
    i = 0
    while i < 18:
        result.append(result[i] + result[i+1])
        i += 1
    
    print(result)



ex1_a_1()
ex1_a_2()
ex1_a_3()
ex1_b_1()
ex1_b_2()
ex2()
ex3()
ex4()
ex5()
ex6()
ex7()
ex8()
ex9()
ex10()
ex11()