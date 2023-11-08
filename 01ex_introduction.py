# 1. The HelloWorld replacement
def HelloWorld():

    resultList = list()

    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            resultList.append("HelloWorld")
        elif n % 3 == 0:
            resultList.append("Hello")
        elif n % 5 == 0:
            resultList.append("World")
        else:
            resultList.append(n)

    resultTuple = tuple()

    for i in resultList:
        if type(i) == str:
            if i.__contains__("Hello"):
                resultTuple += (i.replace("Hello", "Python"),)
            elif i.__contains__("World"):
                resultTuple += (i.replace("World", "Works"),)
        else:
            resultTuple += (i,)

    print(resultTuple)

# HelloWorld()


# 2. The swap
def TheSwap():
    x = input("x: ")
    y = input("y: ")

    x, y = y, x

    print(f"Old values: x = {y}, y = {x}")
    print(f"Swapped values: x = {x}, y = {y}")

# TheSwap()


# 3. Computing the distance
def ComputeDistance():
    import math

    u = (1, 2)
    v = (4, 6)

    distance = math.sqrt(pow((u[0] - v[0]), 2) + pow((u[1] - v[1]), 2))

    print(f"Distance: {distance}")

# ComputeDistance()


# 4. Counting letters
def CountingLetters(op):

    txt = str()

    s1 = "Write a program that prints the numbers from 1 to 100. \
    But for multiples of three print Hello instead of the number and for the multiples of five print World. \
    For numbers which are multiples of both three and five print HelloWorld."
    s2 = "The quick brown fox jumps over the lazy dog"

    if op == 1:
        txt = s1
    else:
        txt = s2

    txt = txt.lower()

    result = dict()

    for letter in txt:
        if letter.isalpha():
            if result.__contains__(letter):
                result[letter] += 1
            else:
                result.__setitem__(letter, 1)

    for letter, count in result.items():
        print(f"{letter}: {count}")

# CountingLetters(1)


# 5. Isolating the unique
def IsolateTheUnique():

    l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
         85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
         1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
         45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

    result = set(item for item in l)

    print(result)

# IsolateTheUnique()


# 6. Casting
def Cast():

    a = input("Input [int, float, string]: ")
    b = input("Input [int, float, string]: ")

    try:
        a = float(a)
        b = float(b)

        print(a + b)

    except Exception as error:
        print(
            f"You cannot perform addition with non-number value. error is: {error}")

# Cast()


# 7. Cubes
def Cube(limit):

    result = list(pow(i, 3) for i in range(1, limit + 1))

    print(result)

# Cube(10)


# 8. List comprehension
def ListComprehension():

    a = list((i, j) for i in range(3) for j in range(4))

    print(a)

# ListComprehension()


# 9. Nested list comprehension
def NestedListComprehension(limit):

    triples = tuple((a, b, c)
                    for c in range(1, limit+1)
                    for b in range(1, c)
                    for a in range(1, b)
                    if a**2 + b**2 == c**2)

    triples = tuple(set(triples))

    print(triples)

# NestedListComprehension(50)


# 10. Normalization of a N-dimensional vector
def Normalization(vector):
    import math

    magnitued = math.sqrt(sum(i**2 for i in vector))
    normalized = tuple(i/magnitued for i in vector)

    print(normalized)

    return normalized

# Normalization((3, 4, 5))


# 11. The Fibonacci sequence
def Fibonacci(limit):

    fib = [0, 1]

    for i in range(2, limit):
        fib.append(fib[i - 1] + fib[i - 2])

    print(fib)

# Fibonacci(20)
