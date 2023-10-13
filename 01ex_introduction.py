import math

################## exercise 1 ##################
print("\n--- --- EXERCISE 1 --- ---")
print("--- helloworld replacement ---\n")

theList = []
for x in range(1, 101):
    if(((x%3)==0) and ((x%5)==0)):
        theList.append("HelloWorld")
    elif((x%3)==0):
        theList.append("Hello")
    elif((x%5)==0):
        theList.append("World")
    else:
        theList.append(x)
print("printing as a list")
print(theList, "\n")

# tuples are not mutable so we need to first modify the list then we can generate the tuple
for i in range(len(theList)):
    if(theList[i]=="Hello"):
        theList[i]="Python"
    elif(theList[i]=="World"):
        theList[i]="Works"

theTuple = tuple(theList)
print("substitute and printing as a tuple")
print(theTuple)
input("\npress ENTER to proceed to the next exercise...")


################## exercise 2 ##################
print("\n--- --- EXERCISE 2 --- ---")
print("--- swap ---\n")

x = input('enter value of x: ')
y = input('enter value of y: ')

print("x = ", x)
print("y = ", y)
print("... swapping ...")
x, y = y, x
print("x = ", x)
print("y = ", y)
input("\npress ENTER to proceed to the next exercise...")


################## exercise 3 ##################
print("\n--- --- EXERCISE 3 --- ---")
print("--- euclidean distance ---\n")
try:
    x1 = float(input("enter value for x1: "))
    y1 = float(input("enter value for y1: "))
    x2 = float(input("enter value for x2: "))
    y2 = float(input("enter value for y2: "))

    P = (x1, y1)
    Q = (x2, y2)

    print("the euclidean distance is ", math.sqrt((Q[0]-P[0])**2 + (Q[1]-P[1])**2))
except:
    print("this is not a valid number format")

input("\npress ENTER to proceed to the next exercise...")


################## exercise 4 ##################

print("\n--- --- EXERCISE 4 --- ---")
print("--- string char counter ---\n")
userString = input("insert the string to evaluate: ")
# s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."
# s2 = "The quick brown fox jumps over the lazy dog"
# s1 = s1.casefold()
# s2 = s2.casefold()

userString = userString.casefold()

letters = {}
for c in userString:
    if c in letters:
        letters[c] += 1
    else:
        letters[c] =1
print("the count of the letters in the provided string is:")
print(list(letters.items()))
input("\npress ENTER to proceed to the next exercise...")


################## exercise 5 ##################
print("\n--- --- EXERCISE 5 --- ---")
print("--- isolating unique numbers ---\n")

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

print("the input vector is: ")
print(l)
occurrences = {}
for n in l:
    if n in occurrences:
        occurrences[n] += 1
    else:
        occurrences[n] =1

print("\nthe unique numbers are the following: ")
count = 0
for key in occurrences:
    if occurrences[key] == 1:
        print(key, end=', ')
        count+=1
print("\nfor a total of ", count, " unique numbers.")
input("\npress ENTER to proceed to the next exercise...")


################## exercise 6 ##################
print("\n--- --- EXERCISE 6 --- ---")
print("--- casting ---\n")
x1 = input("please insert the first addend: ")
x2 = input("please insert the second addend: ")

try:
    sum = float(x1) + float(x2)
    print(float(x1), " + ", float(x2), " = ", sum)
except:
    print("we can't sum strings, the best I can do is their concatenation: ")
    print(x1 + x2)
input("\npress ENTER to proceed to the next exercise...")


################## exercise 7 ##################
print("\n--- --- EXERCISE 7 --- ---")
print("--- list of cubes ---\n")

for_list = []
for i in range(11):
    for_list.append(i**3)

compr_list = [x**3 for x in range(11)]
print("for-generated list of cubes:")
print(for_list)
print("list-comprehension generated:")
print(compr_list)
input("\npress ENTER to proceed to the next exercise...")


################## exercise 8 ##################
print("\n--- --- EXERCISE 8 --- ---")
print("--- list comprehensions ---\n")

print("the result we want is the following (from the exercise assignment):")
a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

print("the result using a list comprehension is: ")
a = [(i,j) for i in range(3) for j in range(4)]
print(a)
input("\npress ENTER to proceed to the next exercise...")


################## exercise 9 ##################
print("\n--- --- EXERCISE 9 --- ---")
print("--- nested list comprehensions ---\n")

print("the list with the pythagorean triplets (a, b, c) whose c<100 is: ")

triplets = [(a, b, int(math.sqrt(a**2+b**2))) for a in range(1,100) for b in range(a,100) if(math.sqrt(a**2+b**2)<100 and math.sqrt(a**2+b**2)%1 == 0)]

print(triplets)
print("\nthe count of triplets is ", len(triplets))
input("\npress ENTER to proceed to the next exercise...")


################## exercise 10 ##################
print("\n--- --- EXERCISE 10 --- ---")
print("--- vector normalization ---\n")

str_vector = input("please insert the vector as comma separated values: ")
str_vector = str_vector.replace(" ", "")
try:
    int_vector = [int(x) for x in str_vector.split(",")]
    abs = 0
    for elem in int_vector : abs = abs+elem**2
    abs = math.sqrt(abs)
    print("the modulus of the input vector is ", abs)
    normalized = [x/abs for x in int_vector]
    print("the normalized vector is ", normalized)
    abs = 0
    for elem in normalized : abs = abs+elem**2
    abs = math.sqrt(abs)
    print("the modulus of the normalized vector is ", abs)
except:
    print("there are some non numerical characters in the input vector")
input("\npress ENTER to proceed to the next exercise...")


################## exercise 11  ##################

print("\n--- --- EXERCISE 11 --- ---")
print("--- fibonacci up to 20 ---\n")

count = 2
prev = 0
last = 1
print("fib( 0 ) = ", prev)
print("fib( 1 ) = ", last)
while count <= 20:
    curr = prev + last
    print("fib(",count,") = ", curr)
    prev = last
    last = curr
    count += 1
input("\npress ENTER to exit...")
