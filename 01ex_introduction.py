#pre

import math
import random

#decider = 11		# Wich exercise to perform
decider = "ALL"	# Perform all exrcises

###############################################################################################################################
# Exercise 1 

if decider == 1 or decider == "ALL":
	# First assignemnt
	numbers_1_100=[x+1 for x in range(100)]
	for i in range(100):
		if numbers_1_100[i] % 3 == 0 and numbers_1_100[i] % 5 == 0:
			numbers_1_100[i] = "HelloWorld"
		elif numbers_1_100[i] % 5 == 0:
			numbers_1_100[i] = "World"
		elif numbers_1_100[i] % 3 == 0:
			numbers_1_100[i] = "Hello"
		else:
			numbers_1_100[i]=numbers_1_100[i]

	numbers_1_100_tuple = tuple(numbers_1_100)
	print("First assignment:",numbers_1_100_tuple,"\n")
	# replace "Hello" to "Python" & "World" to "Works"
	try:
		for j in range(len(numbers_1_100_tuple)):
			if numbers_1_100_tuple[j] == "Hello":
				numbers_1_100_tuple[j] = "Python"
			elif numbers_1_100_tuple[j] == "World":
				numbers_1_100_tuple[j] = "Works"
		print("Replace assignment:",numbers_1_100_tuple)
	except:
		print("Tuple type cannot be changed \n")
		for j in range(len(numbers_1_100_tuple)):
			if numbers_1_100[j] == "Hello":
				numbers_1_100[j] = "Python"
			elif numbers_1_100[j] == "World":
				numbers_1_100[j] = "Works"
		changed_numbers_1_100_tuple = tuple(numbers_1_100)

		print("Replace assignment:",changed_numbers_1_100_tuple,"\n")


###############################################################################################################################
# Exercise 2

if decider == 2 or decider == "ALL":
	x = input('Enter value of x: ')
	y = input('Enter value of y: ')

	print("Original values: x =", x, "y =", y, "\n")

	x, y = y, x
	print("Swapped values: x =", x, "y =", y,"\n")

#################################################################################################################################
# Exercise 3
if decider == 3 or decider == "ALL":
	u = (3,4)
	v = (52,84)

	distance = math.sqrt((u[0]-v[0])*(u[0]-v[0])+(u[1]-v[1])*(u[1]-v[1]))

	print("Point u =",u,"Point v =",v, "\n")

	print("Distance between two given points in Euclidean space is:",distance,"\n")
#################################################################################################################################
# Exercise 4

if decider == 4 or decider == "ALL":
	alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	occurance_s1 = []
	occurance_s2 = []
	s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World.For numbers which are multiples of both three and five print HelloWorld."
	s2 = "The quick brown fox jumps over the lazy dog"
	s1_temp = s1.lower()
	s2_temp = s2.lower()

	for i in range(len(alphabet)):	#26 letters of the english alphabet
		x = s1_temp.count(alphabet[i])
		y = s2_temp.count(alphabet[i])
		occurance_s1.append(x)
		occurance_s2.append(y)

	print("Number of times each character occurs in the first string","\n")

	for j in range(len(alphabet)):
		print(alphabet[j],"is in first string",occurance_s1[j],"times.")
	print("Number of times each character occurs in the second string","\n")

	for k in range(len(alphabet)):
		print(alphabet[k]," is in the second string ",occurance_s2[k]," times.")


##################################################################################################################################
# Exercise 5

if decider == 5 or decider == "ALL":
	l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85, 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91, 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41, 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

	temp = 0
	A =[]

	# Without python data structures
	for j in range(len(l)):
		for k in range(len(l)):
			if l[j] == l[k]:
				temp += 1
		if temp == 1:
			A.append(l[j])
		temp = 0

	print("Numbers with only one occurance (without PDS): \n",A,"\n Number of numbers with only one occurance: ",len(A),"\n")

	# Using python data sctructures
	B = []

	for i in l:
		C = l.count(i)
		if C == 1:
			B.append(i)

	print("Numbers with only one occurance (with PDS): \n",B,"\n Number of numbers with only one occurance:",len(B),"\n")
##################################################################################################################################
# Exercise 6

if decider == 6 or decider == "ALL":
	var_1 = input('Enter value of x (str,int or float): ')
	var_2 = input('Enter value of y (str,int or float): ')

	try:
		result = var_1 + var_2
		print("Result of an addition:",result,"\n")
	except:
		print("Operation is not possible \n")
####################################################################################################################################
# Exercise 7

if decider == 7 or decider == "ALL":
	cubes_loop = []
	for x in range(11):
	    cube_loop = x ** 3
	    cubes_loop.append(cube_loop)
	print("Cubes by loop =",cubes_loop,"\n")

	cubes_list_cop = [x ** 3 for x in range(11)]
	print("Cubes by list coprehension = ",cubes_list_cop,"\n")
######################################################################################################################################
# Exercise 8

if decider == 8 or decider == "ALL":
	a = []
	for i in range(3):
	    for j in range(4):
	        a.append((i, j))
	print("List created without using list comprehension:",a,"\n")

	A = [(i, j) for i in range(3) for j in range(4)]

	print("List created with list comprehension:",A,"\n")

######################################################################################################################################
# Exercise 9

if decider == 9 or decider == "ALL":
	triples = [(a, b, c) for a in range(1, 100 + 1) for b in range(a, 100 + 1) for c in range(b, 100 + 1) if a**2 + b**2 == c**2]
	triples_tuple = tuple(triples)
	print("Unique Pythagorean triples for the positive integers a, b and c < 100: \n",triples_tuple,"\n Number of those triples is:",len(triples_tuple),"\n")

####################################################################################################################################
# Exercise 10

if decider == 10 or decider == "ALL":
	x  = 0
	check = 0
	n_vector = []
	length_of_vector = int(input("Enter the lenght of a vector: "))

	vector = tuple([random.uniform(0, 10) for k in range(length_of_vector)])	#random vector of entered lenght, each element in a range of (0,10)

	for i in range(len(vector)):
		x += vector[i]*vector[i]

	for j in vector:
		n_vector.append(j/math.sqrt(x))

	for h in range(len(vector)):
                check += n_vector[h]*n_vector[h]

	print("Original vector =", vector,"\n")
	print("Normalized vector =",n_vector,"\n")
	print("Was the normalization correct? 1 = ",check,"? \n")


######################################################################################################################################
#Exercise 11

if decider == 11 or decider == "ALL":

	fibonacci_sequence = [0, 1]

	decider_2 = input("Decide if you want to calculate Fibbonacci sequence whit while or for("'while'","'for'"):") 

	if decider_2 == "for":
		for i in range(2, 20):
			next_fibonacci = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
			fibonacci_sequence.append(next_fibonacci)
		print("Fibonacci sequence (first 20 numbers): \n",fibonacci_sequence)

	if decider_2 == "while":
		fibonacci_sequence_while = []
		while len(fibonacci_sequence_while) < 20:
			fibonacci_sequence_while.append(fibonacci_sequence[0])
			fibonacci_sequence[0],fibonacci_sequence[1]=fibonacci_sequence[1],fibonacci_sequence[0]+fibonacci_sequence[1]
		print("Fibonacci sequence (first 20 numbers): \n",fibonacci_sequence_while)

