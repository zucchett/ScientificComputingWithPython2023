import math

# Exercise 1
def exercise1():
    # a)
    result = ["HelloWorld" if x % 3 == 0 and x % 5 == 0
              else "Hello" if x % 3 == 0
              else "World" if x % 5 == 0
              else x for x in range(1,101)]

    print(result)

    # b)
    tuple_result = tuple(["Python" if str == 'Hello'
                     else "Works" if str == 'World'
                     else str for str in result])

    print(tuple_result)


# Exercise 2
def exercise2():
    x = input("Set the value of x: ")
    y = input("Set the value of y: ")

    x, y = y, x

    print("x = ",x)
    print("y = ",y)


# Exercise 3
def exercise3():
    u = (3,0)
    v = (0,4)

    dist = math.sqrt((u[0]-v[0])**2 + (u[1]-v[1])**2)

    print(f"The Euclidean distance between {u} and {v} is {dist}")


# Exercise 4
def exercise4():
    s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
    s2 = "The quick brown fox jumps over the lazy dog"

    s1 = s1.lower()
    s2 = s2.lower()

    count1 = {}
    for char in s1:
        count1[char] = s1.count(char)

    count2 = {}
    for char in s2:
        count2[char] = s2.count(char)

    print("Counter for s1:\n",count1)
    print("Counter for s2:\n",count2)


# Exercise 5
def exercise5():
    l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
     85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
     1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
     45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

    unique_list = [x for x in l if l.count(x) == 1]

    print("The unique numbers in the list are:\n",unique_list)
    print(f"And there is {len(unique_list)} of them.")

    # Exploiting only python dictionaries
    unique_dict = {num: l.count(num) for num in l if l.count(num) == 1}

    print("Exployting only Python dictionaries")
    print("The unique numbers in the list are:\n",unique_dict.keys())
    print(f"And there is {len(unique_dict)} of them.")


# Exercise 6
def exercise6():
    var1 = input("Insert var1: ")
    var2 = input("Insert var2: ")

    try:
        result = float(var1) + float(var2)
        print(result)
    except:
        if type(var1) == str or type(var2) == str:
            result = var1 + var2
            print(result)
        else:
            print("Can't sum number with chars")


# Exercise 7
def exercise7():
    # a)
    for_cubes = []
    for i in range(0,11):
        for_cubes.append(i)

    print(for_cubes)

    # b)
    comp_cubes = [x for x in range(0,11)]
    print(comp_cubes)


# Exercise 8
def exercise8():
    a = [(i,j) for i in range(3) for j in range(4)]

    print(a)


# Exercise 9
def exercise9():
    p_triples = [(a,b,c)
                 for c in range(1,100) for b in range(1,c) for a in range(1,b)
                 if a**2 + b**2 == c**2]

    print(p_triples)


# Exercise 10
def exercise10():
    n_tuple = (10,20,30,40)

    norm2 = math.sqrt(sum(x**2 for x in n_tuple))
    norm_tuple = tuple(x / norm2 for x in n_tuple)

    print(norm_tuple)


# Exercise 11
def exercise11():
    fibo = [0,1]

    for i in range(2,20):
        fibo.append(fibo[i-1] + fibo[i-2])

    print(fibo)


exercise1()
exercise2()
exercise3()
exercise4()
exercise5()
exercise6()
exercise7()
exercise8()
exercise9()
exercise10()
exercise11()
