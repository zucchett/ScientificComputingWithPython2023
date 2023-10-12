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

# print("the euclidean distance is ", math.sqrt((x2-x1)**2 + (y2-y1)**2))
### SISTEMA METTENDO LA TUPLA, SCEMO


# ################## exercise 4
# s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."
# s2 = "The quick brown fox jumps over the lazy dog"

# s1 = s1.casefold()
# s2 = s2.casefold()

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
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

occurrences = {}
for n in l:
    if n in occurrences:
        occurrences[n] += 1
    else:
        occurrences[n] =1
print("the unique number is")


print(occurrences.items())