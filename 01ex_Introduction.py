#############01EX_INTRODUCTION####################################
##########################THE HELLOWORLD REPLACEMENT###############
print("1. the hello world replacement")
# a
def program(i):
    if i%3==0:
       print("Hello")
    elif i%5==0:
       print("World")
    elif i%3==0 and i%5==0 :
       print("Hello World")
    else:
        print(i)
if __name__ == "__main__":
    #for i in range(1,101):
    print(program(50))
# b
tuple = ()

# if __name__ == "__main__":
#     for i in range(1,100):
#         result = program(i)
#         if(result == "Hello"):
#             tuple = tuple + "Python"
#         elif(result == "World"):
#             tuple = tuple + "Works"
#         else:
#             tuple = tuple + str(result)
#     print(tuple)
#############################The SWAP################################
print("2. the swap")
def permutation(x,y):
    x , y = y , x
    return x, y
if __name__ == "__main__":
    x = input("Enter the first variable!: ")
    y = input("Enter the second variable!: ")
    print(permutation(x, y))
#############################COMPUTING THE DISTANCE###################
print("3. computing the distance")
import math
def distance(u,v):
    return math.sqrt((u[0]**2+v[0]**2) + (u[1]**2+v[1]**2))
if __name__ == "__main__":
    u = (0,3)
    v = (0,4)
    print("The Euclidean distance between u and v is = ", distance(u,v))
##########################COMPUTING LETTERS###########################
print("4. computing letters")
import string
def compute_letters(sentence, letter):
    nb = 0
    for car in sentence.upper():
        if car == letter.upper():
            nb = nb + 1
    return nb
if __name__ == "__main__":

    s1 = "Write a program that prints the numbers from 1 to 100. \
    But for multiples of three print Hello instead of the number and for the multiples of five print World. \
    For numbers which are multiples of both three and five print HelloWorld."
    s2 = "The quick brown fox jumps over the lazy dog"
    list = string.printable # This the list of all tthe ASCII characters accessible using the string module.
    # print (list)
    sentences=[s1,s2]
    d1 = dict()
    d2 = dict()

    for char in list:
        count = compute_letters(s1, char)
        d1[char] = count
    print("The number of occurence of a letter in the sentence s1",d1)
    for char in list:
        count = compute_letters(s2, char)
        d2[char] = count
    print("The number of occurence of a letter in the sentence s1",d2)

##################################ISOLATING THE UNIQUE#############################################
print("5. isolating the unique")
import numpy as np
def isolating_unique(l):
    a = np.unique(l)
    return l, len(a)

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
     85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
     1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
     45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
print(isolating_unique(l))
#################################CASTING###################################
print("6. casting")
# Read two variables from the command line
input1 = input("Give an input 1")
input2 = input("Give an input 2")

try:
# Try to convert the inputs to float
    num1 = float(input1)
    num2 = float(input2)

    result = num1 + num2
    print("Result:", result)

except ValueError:
    # If the two variables cannot be converted to float so we convert them to strings and concatane them
    result = str(input1) + str(input2)
    print("Result (concatenation):", result)
except IndexError:
    print("Error")

###################################CUBES########################################
print("7. cubes")
# a: with for loop
cube=[]
for i in range(0,11):
    cube.append(i**3)
print("a = ", cube)
# b: with list comprehension
cube = [x**3 for x in range(11)]
print("b = ",cube)

##############################LIST COMPREHENSION##################################
print("8. List comprehension")
a = [(i,j) for i in range(3) for j in range(4)]
print("The final list with list comprehension = ",a)

############################## Nested list comprehension #############################
print("9. Nested list comprehension")
import math
triples = []
c = 100
for a in range(1, 101):
    for b in range(a, 101):
        c = math.sqrt(a**2 + b**2)
        if c.is_integer():
            triples.append((a, b, int(c)))
triples= set(triples)
uni_triples = list(triples)
t = tuple(uni_triples)
print("The nested list comprehension=", t)
##############################Normalization of a N-dimensional vector#########################
print("10. Normalization of a N-dimensional vector")
import math

def normalize_vector(v):
    squared_sum = sum(x ** 2 for x in v)
    square_root = math.sqrt(squared_sum)
    normalized_vector = tuple(x / square_root for x in v)

    return normalized_vector

if __name__ == "__main__":
    vector = (3, 4, 5)
    result = normalize_vector(vector)
    print("Normalized Vector:", result)


###############################FIBONACCI NUMBERS########################################3
print("11. FIBONACCI NUMBERS")
fib_seq = [0, 1]
for i in range(2, 20):
    fib2 = fib_seq[i - 1] + fib_seq[i - 2]
    fib_seq.append(fib2)
print("The Fibonacci numbers : " , fib_seq)






