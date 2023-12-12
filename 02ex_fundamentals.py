<<<<<<< HEAD
#pre
import copy
import timeit
#decider = 8
decider = "ALL"
######################################################################################################################
# Exercise 1 

if decider == 1 or decider == "ALL":
	def function(alist,x=5):
		alist_copy = copy.copy(alist)
		for i in range(x):
			alist_copy.append(i)
		return alist_copy
	
	if decider == "ALL":
		print("--------------------------------EXERCISE 1-------------------------------------------")

	alist = [1, 2, 3]
	print("Original list BEFORE function-call is:",alist,"\n")

	ans = function(alist)

	print("Function returns:",ans,"\n")
	print("Original list AFTER function-call is:",alist,"\n")

#######################################################################################################################
#Exercise 2 

if decider == 2 or decider == "ALL":
	ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
	perm = [x*x for x in range(10) if x % 2 == 1]
	if decider == "ALL":
		print("--------------------------------EXERCISE 2-------------------------------------------")
       
	print("Original expression:",ans,"\n")
	print("Expression using list comprehension:", perm,"\n")

######################################################################################################################
#Exercise 3 

if decider == 3 or decider == "ALL":
	fruit = ["plum","apple","resberry","banana","strawbery","pear","apple","kiwi"]
	def function(a_fruit,n):
		if len(a_fruit) <= n:
			return True
		else:
			return False
		
	n = 4 # shorter than - paramater

	small_fruit = list(filter(lambda word: function(word,n),fruit))
       
	if decider == "ALL":
		print("--------------------------------EXERCISE 3-------------------------------------------")

	print("List of fruit that are shorter than",n,"is:", small_fruit,"\n")
#######################################################################################################################
#Exercise 4 

if decider == 4 or decider == "ALL":
	
	lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

	def function(part_of_dict):
		temp = len(part_of_dict)
		return temp    
	
	if decider == "ALL":
		print("--------------------------------EXERCISE 4-------------------------------------------")

	print("The lengths of the keys of the dictionary are:",list(map(function, lang)),"\n")
        
######################################################################################################################
#Exercise 5 

if decider == 5 or decider == "ALL":
	
	l_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

	l_scores.sort(key=lambda x: x[0])
       
	if decider == "ALL":
		print("--------------------------------EXERCISE 5-------------------------------------------")

	print("Sorted list of tuples:",l_scores,"\n")
	
######################################################################################################################
#Exercise 6 

if decider == 6 or decider == "ALL":
	def square(i):
		return i*i
	def cube(j):
		return j*j*j
	def sixth(k):
		return square(cube(k))
	n = 3
       
	if decider == "ALL":
		print("--------------------------------EXERCISE 6-------------------------------------------")
              
	#n = int(input("Enter a number you want to raise to the 6th power:"))
	print(n,"raised to the 6th power is:",sixth(n),"\n")

#######################################################################################################################
#Exercise 7 

if decider == 7 or decider == "ALL":
	def hello(func):
		def wrapper(*args, **kwargs):
			print("Hello World!")
			temp = func(*args,**kwargs)
			return temp
		return wrapper

	@hello
	def square(x):
		return x * x

	n = 4
       
	if decider == "ALL":
		print("--------------------------------EXERCISE 7-------------------------------------------")
              
	print(square(n))
######################################################################################################################
#Exercise 8 and 9
if decider == 8 or decider == "ALL" or decider == 9:
		
	if decider == "ALL":
		print("--------------------------------EXERCISE 8 and 9-------------------------------------")

    # Fibonacci sequence using recursive function
	def fibonacci_recursive(n):
			if n <= 0:
				return 0
			elif n == 1:
				return 1
			else:
				return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
	
	f_recursive = []
	for i in range(20):
		f_recursive.append(fibonacci_recursive(i))

	print("Fibonacci sequence (first 20 numbers) - Recursive: \n",f_recursive,"\n")

	recursive_time = timeit.timeit("fibonacci_recursive(20)",setup="from __main__ import fibonacci_recursive", number=1000)

	print("Time taken by the recursive Fibonacci function:",recursive_time,"seconds \n")

	# Fibonacci sequence from the previous exercise:
	def fibonacci_loop():
		fibonacci_sequence = [0, 1]
		for i in range(2, 20):
			next_fibonacci = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
			fibonacci_sequence.append(next_fibonacci)
		return fibonacci_sequence

	print("Fibonacci sequence (first 20 numbers) - Loop: \n",fibonacci_loop(),"\n")

	loop_time = timeit.timeit("fibonacci_loop()", setup="from __main__ import fibonacci_loop", number=1000)

	print("Time taken by the for loop Fibonacci:",loop_time,"seconds \n")

######################################################################################################################
#Exercise 10 and 11 
if decider == 10 or decider == "ALL" or decider == 11:
	class Polygon:
		def __init__(self, sides):
			self.sides = list(sides)

		def get_sides(self):
			return self.sides

		def set_sides(self, sides):
			self.sides = list(sides)

		def perimeter(self):
			return sum(self.sides)

		def get_ordered_sides(self, increasing=True):
			if increasing is True:
				ordered_sides = sorted(self.sides, reverse = False) 
			else:
				ordered_sides = sorted(self.sides, reverse = True)
			return tuple(ordered_sides)

	class Rectangle(Polygon):
		def __init__(self, sides):
			super().__init__(sides)

		def area(self):
			return self.sides[0] * self.sides[1]

	R1 = Rectangle((4, 6))
	P1 = Polygon((2,2,2,2))

	if decider == "ALL":
		print("--------------------------------EXERCISE 10 and 11-----------------------------------")

	P1.set_sides((2,5,7,6))
	print("Sides of the polygon:", P1.get_sides(),"\n")
	print("Perimeter of the polygon:", P1.perimeter(),"\n")
	print("Ordered polygon sides in decreasing order:", P1.get_ordered_sides(False),"\n")
	print("Ordered polygon sides in increasing order:", P1.get_ordered_sides(True),"\n")

	print("Sides of the rectangle:", R1.get_sides(),"\n")
	print("Perimeter of the rectangle:", R1.perimeter(),"\n")
	print("Area of the rectangle:", R1.area(),"\n")



=======
#pre
import copy
import timeit
#decider = 8
decider = "ALL"
######################################################################################################################
# Exercise 1 

if decider == 1 or decider == "ALL":
	def function(alist,x=5):
		alist_copy = copy.copy(alist)
		for i in range(x):
			alist_copy.append(i)
		return alist_copy
	
	if decider == "ALL":
		print("--------------------------------EXERCISE 1-------------------------------------------")

	alist = [1, 2, 3]
	print("Original list BEFORE function-call is:",alist,"\n")

	ans = function(alist)

	print("Function returns:",ans,"\n")
	print("Original list AFTER function-call is:",alist,"\n")

#######################################################################################################################
#Exercise 2 

if decider == 2 or decider == "ALL":
	ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
	perm = [x*x for x in range(10) if x % 2 == 1]
	if decider == "ALL":
		print("--------------------------------EXERCISE 2-------------------------------------------")
       
	print("Original expression:",ans,"\n")
	print("Expression using list comprehension:", perm,"\n")

######################################################################################################################
#Exercise 3 

if decider == 3 or decider == "ALL":
	fruit = ["plum","apple","resberry","banana","strawbery","pear","apple","kiwi"]
	def function(a_fruit,n):
		if len(a_fruit) <= n:
			return True
		else:
			return False
		
	n = 4 # shorter than - paramater

	small_fruit = list(filter(lambda word: function(word,n),fruit))
       
	if decider == "ALL":
		print("--------------------------------EXERCISE 3-------------------------------------------")

	print("List of fruit that are shorter than",n,"is:", small_fruit,"\n")
#######################################################################################################################
#Exercise 4 

if decider == 4 or decider == "ALL":
	
	lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

	def function(part_of_dict):
		temp = len(part_of_dict)
		return temp    
	
	if decider == "ALL":
		print("--------------------------------EXERCISE 4-------------------------------------------")

	print("The lengths of the keys of the dictionary are:",list(map(function, lang)),"\n")
        
######################################################################################################################
#Exercise 5 

if decider == 5 or decider == "ALL":
	
	l_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

	l_scores.sort(key=lambda x: x[0])
       
	if decider == "ALL":
		print("--------------------------------EXERCISE 5-------------------------------------------")

	print("Sorted list of tuples:",l_scores,"\n")
	
######################################################################################################################
#Exercise 6 

if decider == 6 or decider == "ALL":
	def square(i):
		return i*i
	def cube(j):
		return j*j*j
	def sixth(k):
		return square(cube(k))
	n = 3
       
	if decider == "ALL":
		print("--------------------------------EXERCISE 6-------------------------------------------")
              
	#n = int(input("Enter a number you want to raise to the 6th power:"))
	print(n,"raised to the 6th power is:",sixth(n),"\n")

#######################################################################################################################
#Exercise 7 

if decider == 7 or decider == "ALL":
	def hello(func):
		def wrapper(*args, **kwargs):
			print("Hello World!")
			temp = func(*args,**kwargs)
			return temp
		return wrapper

	@hello
	def square(x):
		return x * x

	n = 4
       
	if decider == "ALL":
		print("--------------------------------EXERCISE 7-------------------------------------------")
              
	print(square(n))
######################################################################################################################
#Exercise 8 and 9
if decider == 8 or decider == "ALL" or decider == 9:
		
	if decider == "ALL":
		print("--------------------------------EXERCISE 8 and 9-------------------------------------")

    # Fibonacci sequence using recursive function
	def fibonacci_recursive(n):
			if n <= 0:
				return 0
			elif n == 1:
				return 1
			else:
				return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
	
	f_recursive = []
	for i in range(20):
		f_recursive.append(fibonacci_recursive(i))

	print("Fibonacci sequence (first 20 numbers) - Recursive: \n",f_recursive,"\n")

	recursive_time = timeit.timeit("fibonacci_recursive(20)",setup="from __main__ import fibonacci_recursive", number=1000)

	print("Time taken by the recursive Fibonacci function:",recursive_time,"seconds \n")

	# Fibonacci sequence from the previous exercise:
	def fibonacci_loop():
		fibonacci_sequence = [0, 1]
		for i in range(2, 20):
			next_fibonacci = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
			fibonacci_sequence.append(next_fibonacci)
		return fibonacci_sequence

	print("Fibonacci sequence (first 20 numbers) - Loop: \n",fibonacci_loop(),"\n")

	loop_time = timeit.timeit("fibonacci_loop()", setup="from __main__ import fibonacci_loop", number=1000)

	print("Time taken by the for loop Fibonacci:",loop_time,"seconds \n")

######################################################################################################################
#Exercise 10 and 11 
if decider == 10 or decider == "ALL" or decider == 11:
	class Polygon:
		def __init__(self, sides):
			self.sides = list(sides)

		def get_sides(self):
			return self.sides

		def set_sides(self, sides):
			self.sides = list(sides)

		def perimeter(self):
			return sum(self.sides)

		def get_ordered_sides(self, increasing=True):
			if increasing is True:
				ordered_sides = sorted(self.sides, reverse = False) 
			else:
				ordered_sides = sorted(self.sides, reverse = True)
			return tuple(ordered_sides)

	class Rectangle(Polygon):
		def __init__(self, sides):
			super().__init__(sides)

		def area(self):
			return self.sides[0] * self.sides[1]

	R1 = Rectangle((4, 6))
	P1 = Polygon((2,2,2,2))

	if decider == "ALL":
		print("--------------------------------EXERCISE 10 and 11-----------------------------------")

	P1.set_sides((2,5,7,6))
	print("Sides of the polygon:", P1.get_sides(),"\n")
	print("Perimeter of the polygon:", P1.perimeter(),"\n")
	print("Ordered polygon sides in decreasing order:", P1.get_ordered_sides(False),"\n")
	print("Ordered polygon sides in increasing order:", P1.get_ordered_sides(True),"\n")

	print("Sides of the rectangle:", R1.get_sides(),"\n")
	print("Perimeter of the rectangle:", R1.perimeter(),"\n")
	print("Area of the rectangle:", R1.area(),"\n")


>>>>>>> 1f59f72b98c0d9e3c9ec74e57fb0c289ef2352b4
