# ################## exercise 1
# print("Point A")
# theList = []
# for x in range(1, 101):
#     if(((x%3)==0) and ((x%5)==0)):
#         theList.append("HelloWorld")
#     elif((x%3)==0):
#         theList.append("Hello")
#     elif((x%5)==0):
#         theList.append("World")
#     else:
#         theList.append(x)
# #print(theList) # but I don't like the formatting
# for x in theList: print(x)

# print("\nPoint B")
# #tuples are not mutable so we need to first modify the list
# for i in range(len(theList)):
#     if(theList[i]=="Hello"):
#         theList[i]="Python"
#     elif(theList[i]=="World"):
#         theList[i]="Works"

# theTuple = tuple(theList)
# for x in theTuple: print(x)

# ################## exercise 2

# x = input('enter value of x: ')
# y = input('enter value of y: ')
# x, y = y, x
# print("x = ", x)
# print("y = ", y)

################## exercise 3
# import math

# x1 = float(input("enter value for x1: "))
# y1 = float(input("enter value for y1: "))
# x2 = float(input("enter value for x2: "))
# y2 = float(input("enter value for y2: "))

# P = (x1, y1)
# Q = (x2, y2)

# print("the euclidean distance is ", math.sqrt((Q[0]-P[0])**2 + (Q[1]-P[1])**2))


# ################## exercise 4

# print("--- --- EXERCISE 4 --- ---")
# print("-- string char counter --")
# userString = input("insert the string to evaluate: ")
# # s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."
# # s2 = "The quick brown fox jumps over the lazy dog"

# # s1 = s1.casefold()
# # s2 = s2.casefold()

# userString = userString.casefold()

# letters = {}
# for c in userString:
#     if c in letters:
#         letters[c] += 1
#     else:
#         letters[c] =1
# print("the count of the letters in the provided string is:")
# print(list(letters.items()))

# letters = {}
# for c in s1:
#     if c in letters:
#         letters[c] += 1
#     else:
#         letters[c] =1
# print("the frequency of the letters in the string s1 is:")
# print(list(letters.items()))


# letters = {}
# for c in s2:
#     if c in letters:
#         letters[c] += 1
#     else:
#         letters[c] =1
# print("the frequency of the letters in the string s2 is:")
# print(list(letters.items()))


################## exercise 5
# print("--- --- EXERCISE 5 --- ---")

# l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
#  85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
#  1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
#  45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

# occurrences = {}
# for n in l:
#     if n in occurrences:
#         occurrences[n] += 1
#     else:
#         occurrences[n] =1


# print("The unique numbers are the following: ")
# count = 0
# for key in occurrences:
#     if occurrences[key] == 1:
#         print(key)
#         count+=1
# print("For a total of ", count, " unique numbers.")


################## exercise 6

# print("--- --- EXERCISE 6 --- ---")
# print("--- casting ---")
# x1 = input("please insert the first variable: ")
# x2 = input("please insert the second variable: ")

# try:
#     sum = float(x1) + float(x2)
#     print(float(x1), " + ", float(x2), " = ", sum)
# except:
#     print("we can't sum two strings, so here's their concatenations :-)")
#     print(x1 + x2)


################## exercise 7

# print("--- --- EXERCISE 7 --- ---")
# print("--- cubes ---")
# for_list = []
# for i in range(11):
#     for_list.append(i**3)

# compr_list = [x**3 for x in range(11)]
# print("for-generated list of cubes:")
# print(for_list)
# print("list-comprehension generated:")
# print(compr_list)

################## exercise 8

# print("--- --- EXERCISE 8 --- ---")
# print("--- list comprehensions ---")

# print("the result we want is the following:")
# a = []
# for i in range(3):
#     for j in range(4):
#         a.append((i, j))
# print(a)
# print("the result using a list comprehension is: ")
# a = [(i,j) for i in range(3) for j in range(4)]
# print(a)

################## exercise 9
# import math

# print("--- --- EXERCISE 9 --- ---")
# print("--- nested list comprehensions ---")
# print("the list with the pythagorean triplets (a, b, c) whose c<100 is: ")

# triplets = [(a, b, int(math.sqrt(a**2+b**2))) for a in range(1,100) for b in range(1,100) if(math.sqrt(a**2+b**2)<100 and math.sqrt(a**2+b**2)%1 == 0)]

# print(triplets)
# print("the count of triplets is ", len(triplets))

################## exercise 10
import numpy

print("--- --- EXERCISE 10 --- ---")
print("--- list normalization ---\n")

str_vector = input("please insert the vector of comma separated values: ")
str_vector = str_vector.replace(" ", "")
try:
    int_vector = [int(x) for x in str_vector.split(",")]
    sum = numpy.sum(int_vector)
except:
    print("there are some non numerical characters in the input vector")


