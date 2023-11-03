#These are the solutions of the tasks presented in the first set of exercises, described in the file 01ex_introduction.ipynb

#Exercise 1
#The following code solves both point a) and b) of the task presented. For b) point, I added an extra print which was not asked but
#could be of use to see the tuple printed.

results = []
for i in range(1,101):
    if((i%3==0)and(i%5!=0)):
        print("Hello")
        results.append("Python")
    elif (i%5==0)and(i%3!=0):
        print("World")
        results.append("Works")
    elif (i%5==0)and(i%3==0):
        print("HelloWorld")
        results.append("PythonWorks")
    else:
        print(i)
        results.append(i)
results_tuple=tuple(results)
print(results_tuple)


#Exercise 2
#The exercise asked to swap two values passed by command line (input). Again I put an extra print function to show that the two
#values have changed

print("\n \n \n ")

x=input("Define the value of x, no restriction on the type of input: ")
print("Value of x: ", x)
y=input("Define the value of y, no restriction on the type of input: ")
print("Value of y: ", y)
x, y= y, x
print("Final value of x: ", x)
print("Final value of y: ", y)

#Exercise 3
#This code does not know how to behave if the arguments passed by command line are not int or float. Were I to deal also with these
#kind of inputs I should have used the try/except approach, but this was not explicitly asked in the exercise

print("\n \n \n ")

import math
print("In this exercise we want to compute the euclidean distance, so the input shall be integers or floats")
u_1, u_2 = input("Insert the value for u_1: "), input("Insert the value of u_2: ")
u_1, u_2 = float(u_1), float(u_2)
u = (u_1, u_2)
v_1, v_2 = input("Insert the value for v_1: "), input("Insert the value of v_2: ")
v_1, v_2 = float(v_1), float(v_2)
v = (v_1, v_2)
euclidean_distance = math.sqrt((u_1-v_1)**2+(u_2-v_2)**2)
print("The euclidean distance is: ", euclidean_distance)


#Exercise 4
#There are two print functions that are not necessary or asked, but they show that the program works.

print("\n \n \n ")

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

string1 = s1.lower()
string2 = s2.lower()
alphabet="abcdefghijklmnopqrstuvxyz"
s1_occ = {}
s2_occ = {}
for j in alphabet:
    s1_occ[j] = string1.count(j)
    s2_occ[j] = string2.count(j)
print(s1_occ.keys(), s1_occ.values())
print(s2_occ.keys(), s2_occ.values())


#Exercise 5 
#The task did not include the last print function, which I added to show also the unique numbers that are present in the given list.

print("\n \n \n ")

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85, 
85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91, 
1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41, 
45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

occ = []
temp_occ = 0
for i in range(0,len(l)):
    temp_occ = l.count(l[i])
    if (temp_occ > 1):
        temp_occ = 0
    elif (temp_occ == 1):
        occ.append(l[i])
        temp_occ = 0
print("The length of the list containing only unique number is: ", len(occ))
print("The list itself containing only unique numbers is: ", occ)


#Exercise 6 
#The task asked only to print without errors: this code, given certain inputs, prints 3 different outputs. However, they can be reduced
#to only one if the types given as input are different from each other, including one of the two or both to be different than a number.

print("\n \n \n ")

print("The type of the inputs can be the same or different and based on this condition the output may vary.")
in1, in2 = input("Write the value of the first variable: "), input("Write the value of the second variable: ")
try:
    num1, num2 = int(in1), int(in2)
    print(num1 + num2)
except:
    ''
try:
    fl1, fl2 = float(in1), float(in2)
    print(fl1 + fl2)
except:
    ''
try:
    st1, st2 = str(in1), str(in2)
    print(st1 + st2)
except:
    ''


#Exercise 7 
#The print function was not asked but it is useful in seeing directly that the two ways to create the list return the same result.

print("\n \n \n ")

acub = []
for i in range(0,11):
    acub.append(i**3)
print(acub)
bcub = [x**3 for x in range(11)]
print(bcub)


#Exercise 8 
#Same comment as exercise 7

print("\n \n \n ")

a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

a_com = [(i, j) for i in range(3) for j in range(4)]
print(a_com)


#Exercise 9
#This code prints the unique Pythagorean triplets (a, b, c) with c<100

print("\n \n \n ")

in_100 = [x for x in range(0,100)]
li_tri = [(a, b, c) for a in range(1,100) for b in range(1,100) for c in range(0,100) if ((a**2)+(b**2)==(c**2))]
i = 0
while i<len(li_tri):
    for j in range(0, len(li_tri)):
        if ((li_tri[i][0]==li_tri[j][1])and(li_tri[i][2]==li_tri[j][2])):
            li_tri.remove(li_tri[i])
            i = i-1
            break
    i +=1
i=0
print(li_tri)
while i<len(li_tri):
    for j in range(0, len(li_tri)):
        if ((i!=j)and(li_tri[j][0]%li_tri[i][0]==0)and(li_tri[j][1]%li_tri[i][1]==0)and(li_tri[j][2]%li_tri[i][2]==0)and((li_tri[j][0]/li_tri[i][0])==(li_tri[j][1]/li_tri[i][1]))):
            li_tri.remove(li_tri[j])
            i = i-1
            break
    i +=1

print(len(li_tri))
li_tri = tuple(li_tri)
print(li_tri)


#Exercise 10
#This code takes in a vector expressed with a list and return the normalised vector. The sum is almost one (can be easily rounded to one 
#using the round() method.)

print("\n \n \n ")

import math
xin = [x for x in range(0,25)]
N = len(xin)
sm = 0
for i in range(0, N):
    sm += xin[i]**2
sm = math.sqrt(sm)
for i in range(0, N):
    xin[i] = round(xin[i]/sm, 2)
print(xin)
sm_tot = 0
for i in range(0, N):
    sm_tot += xin[i]**2
print("Sum: ", sm_tot)


#Exercise 11
#First 20 numbers of the Fibonacci sequence obtained through an iterative way.

print("\n \n \n ")

Fib = {}
for i in range(0,20):
    if (i==0):
        Fib[i] = 0
    if (i==1):
        Fib[i] = 1
    elif ((i!=0)and(i!=1)):
        Fib[i] = Fib[i-1] + Fib[i-2]
print(Fib)

#End of the exercises: I add an extra input in order to keep the code running for the last exercises, was I to not do this the
#program would close as soon as I put the last input in exercise 6
input('Press ENTER to close the first set of exercises')