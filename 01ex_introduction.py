#EXERCISE 1
list1 = []
print("Before substitution:")
for i in range(1,101):
    if (((i % 3) == 0) and ((i % 5) == 0)):
        list1.append("HelloWorld")
    if ((i % 3) == 0):
        list1.append("Hello")
    elif  ((i % 5) == 0):
        list1.append("World")
    else:
        list1.append(i)
print(list1)

print("After substitution:")
for i in range(1,101):
    if list1[i] == 'Hello':
        list1[i] = 'Python'
    elif list1[i] == "World":
        list1[i] = 'Works'
tuple1 = tuple(list1)
print(tuple1)


#EXERCISE 2
x = input("Set the value of x: ")
y = input("Set the value of y: ")
x,y = y,x
print("The swapped inputs are: ", x,y)


#EXERCISE 3
import math
u = (3, 0)
v = (0, 4)
print(math.sqrt((v[0]-u[0])**2 + (v[1]-u[1])**2))


#EXERCISE 4
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

s1 = s1.lower()
s2 = s2.lower()

print("OCCURRENCE OF THE CHAR IN STRING 1")
for i in range(97,123):
    counter1 = s1.count(chr(i))
    print(chr(i),"/",chr(i-32),"=",counter1)

print("OCCURRENCE OF THE CHAR IN STRING 2")
for i in range(97,123):
    counter2 = s2.count(chr(i)) 
    print(chr(i),"/",chr(i-32),"=",counter2)


#EXERCISE 5
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

uniq = []
for i in range(len(l)):
    if (l.count(l[i])) == 1 :
        uniq.append(l[i])
print("Number of unique numbers: ", len(uniq))
print("Unique numbers: ",uniq)
print("I already used exploited only the Python data structures")

#EXERCISE 6
x,y = input("Set the value of x: "),input("Set the value of y: ")
try:
    z = float(x) + float(y)
    print("The sum is: ",z)
except:
    print(x,"  ",y," are not numbers")
    choice = input("Do you want to concatenate?[yes/no]")
    if(choice == "yes"):
        print("The result of the concatenation is: ",x + y)


#EXERCISE 7
#EXERCISE 7a
print("list of the cubes of x for x in [0, 10]: ")
for x in range(11):
    print(x**3)

#EXERCISE 7b
print("list of the cubes of x for x in [0, 10]: ")
cubes = [x**3 for x in range(11)]
print (cubes)


#EXERCISE 8
#without list comprehension
print("Without list comprehension: ")
a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

#with list comprehension
print("With list comprehension: ")
print ([(x, y) for x in range(3) for y in range(4)])


#EXERCISE 9
triples = tuple( [ (a,b,c) for a in range(1,100) for b in range(1,100) for c in range(1,100) if ( (c*c == a*a + b*b) and a<b)] )
print("Unique Pythagorean triples for c < 100: ")
print(triples)

#EXERCISE 10
import math

#in this code "vect" is the example
vect = [1.89 ,2 ,4, 9, 99]
print("The vector is: ", vect)
sumSq = 0
for i in range(len(vect)):
    sumSq = sumSq + vect[i]**2
#print(norm)
norm = math.sqrt(sumSq)
vectNorm = [ vect[i]/norm for i in range(len(vect)) ]
print("The normalized vector is", vectNorm)


#EXERCISE 11
fibSeq = [ i for i in range(0,20)]
for i in range(2,20):
    fibSeq[i] = fibSeq[i-1] + fibSeq[i-2]
print("Fibonacci Sequence: ",fibSeq)
