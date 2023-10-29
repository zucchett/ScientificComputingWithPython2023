import math

###### EXERCISE 1 ######
# a)
print("### EXERCISE 1 ### \n")
print("part a)\n")

# create an empty list
mylist = []

# apply the substitutions 
for i in range(1,101):
    if i % 3 == 0 and i % 5 ==0:
        print("HelloWorld")
        mylist.append("HelloWorld")
    elif i % 3 == 0:
        print("Hello")
        mylist.append("Hello")
    elif i % 5 == 0:
        print("World")
        mylist.append("World")
    else:
        print(i)
        mylist.append(i)
#b) 
print("\npart b)\n")

# apply the substitutions 
for i in range(100):
    if mylist[i] == "Hello":
        mylist[i] = "Python"
    elif mylist[i] == "World":
        mylist[i] = "Works"
        
# convert the list into a tuple
mytuple = tuple(mylist)
print(mytuple)

print("\n\n")
input("... press enter to go to the next exercise ...")
print("\n\n")





###### EXERCISE 2 ######

print("### EXERCISE 2 ###\n")

# input sources 
x = input("Insert x value: ")
y = input("Insert y value: ")

# swap the values
x,y = y,x

# print the results
print("x value:", x,"\ny value:", y)

print("\n\n")
input("... press enter to go to the next exercise ...")
print("\n\n")






###### EXERCISE 3 ######

print("### EXERCISE 3 ###\n")

# delcaration of the points
x1 = float(input("enter value of x1: "))
y1 = float(input("enter value of y1: "))
x2 = float(input("enter value of x2: "))
y2 = float(input("enter value of y2: "))
u = (x1, y1)
v = (x2, y2)

# euclidean distance computation
output = math.sqrt((u[0]-v[0])**2+(u[1]-v[1])**2)

# print the result
print("The euclidean distance is:", output)

print("\n\n")
input("... press enter to go to the next exercise ...")
print("\n\n")






###### EXERCISE 4 ######

print("### EXERCISE 4 ###\n")

# testing strings
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

#input source
s1 = input("Please enter your string: ")

# define an empty set
myset1 = set()

# make the computations 
s1= s1.lower()
for elem in s1:
    myset1.add((elem, s1.count(elem)))

    
# print the results    
count = 0
print("In your string:")
for i in myset1:
    print("\"", i[0],"\" occurs", i[1])



print("\n\n")
input("... press enter to go to the next exercise ...")
print("\n\n")






###### EXERCISE 5 ######

print("### EXERCISE 5 ###\n")

# testing list
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

# define an empty dictionary
my_dict = {}

# make the computation
for i in l:
    if my_dict.get(i):
        for key in my_dict:
            if key == i:
                my_dict[key] += 1
    else:
        my_dict[i] = 1
count = 0
unique_number = []
for key in my_dict:
    if my_dict[key] == 1:
        unique_number.append(key)
        count += 1

# print the results
print("The unique numbers are:", count)
print("\nThey are:", unique_number)

            

print("\n\n")
input("... press enter to go to the next exercise ...")
print("\n\n")






###### EXERCISE 6 ######

print("### EXERCISE 6 ###\n")

# input sources
x1 = input("Please insert the first value: ")
x2 = input("Please insert the second value: ")

# computation
try:
    x3 = float(x1)
    x4 = float(x2)
    print("The sum is:", x3+x4)
except:
    print("The two inputs cannot be summed togheter, but I can concatenate them:", x1+x2)

print("\n\n")
input("... press enter to go to the next exercise ...")
print("\n\n")





###### EXERCISE 7 ######

print("### EXERCISE 7 ###\n")

# create an empty list
mylist_1 = []

# loop method
print("Loop method: ")
for i in range(11):
    mylist_1.append(i**3)
print(mylist_1)

# list comprehension method
print("\nList comprehension method: ")
mylist_2 = [i**3 for i in range(11)]
print(mylist_2)

print("\n\n")
input("... press enter to go to the next exercise ...")
print("\n\n")





###### EXERCISE 8 ######

print("### EXERCISE 8 ###\n")

# given code
a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

# single-line expression
mylist = [(i, j) for i in range(3) for j in range(4)]
print("\n",mylist)

print("\n\n")
input("... press enter to go to the next exercise ...")
print("\n\n")





###### EXERCISE 9 ######

print("### EXERCISE 9 ###\n")

# define an empty set
myset = set()

# find all possible couples
for a in range(101):
    for b in range(101):
        c_2 = a*a + b*b
        c = math.sqrt(c_2)
        c_int = int(c)
        if (c%1 == 0.0) and (c < 100):
            c_int = int(c)
            myset.add((a,b,c_int))
            
# create a copy of the previous set,
# otherwise is not possible to both iterate 
# over it and remove elements (change its size)
myset_copy = myset.copy()

#remove the repetitions
for i in myset_copy:
    if i[0] == 0 or i[1] == 0:
        myset.remove(i)
        
# convert the set into tuple
mytuple = tuple(myset)

# count the total number of couples
count = 0
for i in mytuple:
    count += 1

# print the results
print("There are", count, "couples, but if we don't want to consider the order,\ni.e., (12, 5, 13) is equal to (5, 12, 13), there are", int(count/2), "couples.\n")
print("The list of", count, "couples is the following:")
for i in range(0, count):
    print(mytuple[i])

print("\n\n")
input("... press enter to go to the next exercise ...")
print("\n\n")






###### EXERCISE 10 ######


print("### EXERCISE 10 ###\n")

try:
    # take the dimension as input
    dim = input("Which is the dimension of your vector? ")
    dim = int(dim)
    
    # take the coordinates as input
    myset = []
    print("Write the", dim, "coordinates: ")
    for i in range(dim):
        elem = input()
        elem = int(elem)
        myset.append(elem)
    mytuple = tuple(myset)

    # compute the normalization factor
    summation = 0
    for i in mytuple:
        summation += i**2
    result = math.sqrt(summation)
    print("The normalization factor is:", result)

    # compute the normalized tuple
    myset = []
    for i in mytuple:
        myset.append(i/result)
    norm_tuple = tuple(myset)
    print("The normalize tuple is:", norm_tuple)

    # check the correctness of the result
    result = 0
    for i in norm_tuple:
        result += i**2
    print("The result is correct if the following value is 1:", result)

    # other possible way to show the result
    if abs(1 - result) < 0.000000000001:
        print("The vecotr is correctly normalized")
    else:
        print("There are some errors")
    
except:
    print("Unexpected input value, please try again")

print("\n\n")
input("... press enter to go to the next exercise ...")
print("\n\n")








###### EXERCISE 11 ######

print("### EXERCISE 11 ###\n")

# create an empty list
mylist = []

# numbers computation 
for i in range(21):
    if i == 0:
        mylist.append(0)
    elif i == 1:
        mylist.append(1)
    else:
        mylist.append(mylist[i-1] + mylist[i-2])
        
#print the result
print("The first 20 numbers of the Fibonacci sequence are:\n",mylist)
