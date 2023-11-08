
#*****************************************The HelloWorld replacement*****************************************
print('\n \n# ------------ The HelloWorld replacement ------------ # \n \n')

print('# ------------ Question a ------------ # \n \n')

result_ex1=tuple()
for i in range(1,101,1):
    if i%3 ==0  & i%5==0 :
        result_ex1=result_ex1+("`HelloWorld`",)

    elif i%3 == 0 :
        result_ex1=result_ex1+("`Hello`",)

    elif i%5 == 0 :
        result_ex1=result_ex1+("`World`",)
    else :
        result_ex1=result_ex1+(i,)


print(result_ex1)

print('\n \n # ------------ Question b ------------ # \n \n')
result_ex1_b = list(result_ex1)
for i in range(len(result_ex1_b)):
    if result_ex1_b[i] == "`Hello`" or result_ex1_b[i] == "`HelloWorld`" or result_ex1_b == "`World`":
        result_ex1_b[i] = result_ex1_b[i].replace('Hello', 'Python').replace("World", "Works")

print(result_ex1_b)
#*****************************************The swap*****************************************
print('\n \n# ------------ The swap ------------ # \n \n')

x = input("Enter x value: ")
y = input("Enter y value:")
print("x & y before swapping: x = " , x ," y = " ,y )
x, y = y, x
print("x & y before swapping: x = " , x ," y = " ,y )



#*****************************************Computing the distance*****************************************
print('\n \n# ------------ Computing the distance ------------ # \n \n')

import math
def distance_eucl(u,v):
     distance = math.sqrt((v[0] - u[0]) ** 2 + (v[1] - u[1]) ** 2)
     return distance

if __name__ == "__main__":
    u1 = float(input("Enter the 2D coordinate of U_1: "))
    u2 = float(input("Enter the 2D coordinate of U_2: "))
    u=(u1,u2)
    v1 = float(input("Enter the 2D coordinate of V_1 :"))
    v2 = float(input("Enter the 2D coordinate of V_2 :"))
    v=(v1,v2)


    print("The Euclidean distance between u and v is = ", distance_eucl(u,v))


#*****************************************Counting letters*****************************************
print('\n \n# ------------ Counting letters ------------ # \n \n')

def count(string):

    string_lower = string.lower()
    count = {}
    for i in string_lower:
        if i.isalpha():
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
    for i, j in count.items():
        print(f"'{i}': {j}")


s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
test_strings = [s1, s2]
for test_string in test_strings:
    print(f"The counting letter program for the string : '{test_string}':")
    count(test_string)

#*****************************************Isolating the unique*****************************************
print('\n \n# ------------ Isolating the unique ------------ # \n \n')

#My first idea is to put all the unique numbers in dict
def count_uniq(val ,list):
    sum=0
    for i in range(len(list)):
        if list[i]==val:
            sum+=1
    return sum

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]


dict = {}
for i in range(len(l)):
    count = count_uniq(l[i], l)
    if count == 1:
        dict[l[i]] = count

print(dict)
#while exploiting only the Python data structures i m gonna use a list
unique_numbers = [i for i in l if l.count(i) == 1]
print(unique_numbers)

#*****************************************Casting*****************************************
print('\n \n# ------------ casting ------------ # \n \n')

variable1 = (input("Enter first variable: "))
variable2 = (input("Enter second variable: "))

try:
    var1 = int(variable1)
    var2 = int(variable2)
except ValueError:
    try:
        var1 = float(variable1)
        var2 = float(variable2)
    except ValueError:
        var1 = str(variable1)
        var2 = str(variable2)

try:
    result = var1 + var2
    print(result)
except (TypeError, ValueError):
    print("Incompatible data types")
except Exception :
    print("There is an  error" )

#*****************************************Cubes*****************************************
print('\n \n# ------------ cubes ------------ # \n \n')

# Using a for loop
cube =[]
for i in range(0,11):
    cube_val=i**3
    cube.append((cube_val))

print("The cube values with a loop is ", cube)

# Using a list comprehension
cube_com = [i**3 for i in range(11)]
print("The cube values with a list comprehension ",cube_com)

#*******************************************List comprehension*******************************************
print('# ------------ List comprehension ------------ # \n \n')

a = [(i, j) for i in range(3) for j in range(4)]
print("The List comprehension of a " , a)
#*******************************************Nested list comprehension*******************************************
print('# ------------Nested List comprehension ------------ # \n \n')

# using a list comprehension
pythagor_triples2 = [(a, b, c) for c in range(1, 100) for b in range(1, c) for a in range(1, b) if a**2 + b**2 == c**2]

unique_triples = list(set(pythagor_triples2))
unique_triples.sort()
unique_triples_tuple = tuple(unique_triples)
print("The unique Pythagorean triples for the positive integers $a$, $b$ and $c$ with $c < 100$. " , unique_triples_tuple)


#*******************************************Normalization of a N-dimensional vector*******************************************
print('\n \n# ------------Normalization of a N-dimensional vector ------------ # \n \n')


def normalize(vector):
    normalize = math.sqrt(sum(x**2 for x in vector))
    if normalize == 0:
        return vector
    normalized_vector = tuple(x / normalize for x in vector)
    return normalized_vector

vector1 = (39, 8)
normalized_vector = normalize(vector1)
print(" The Normalization of a N-dimensional vector is  : " ,normalized_vector )


#*********************************************The Fibonacci sequence*********************************************
print('\n \n# ------------ **The Fibonacci sequence**------------ # \n \n')
#The Fibonacci numbers may be defined by the recurrence relation : F0=0  , F1=1 & Fn =Fn-1 +Fn-2
#using loops for / while
fibonaci= [0, 1]
for i in range(2, 20):
    numm = fibonaci[i-1] + fibonaci[i-2]
    fibonaci.append(numm)
print("The Fibonacci Sequence using loops for / while: ",fibonaci )
#with recurrence or by indexing
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence
fibonacci = fibonacci(20)
print("The Fibonacci Sequence with recurrence or by indexing : ",fibonacci )


