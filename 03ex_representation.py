

# ################## exercise 1 ##################
# print("\n--- --- EXERCISE 1 --- ---")
# print("--- bin hex dec conversions ---\n")

# def convert (num, destination):
#     match num[1]:
#         case 'b':
#             print("the detected base is BIN")
#             num = int(num, 2)
#         case 'x': 
#             print("the detected base is HEX")
#             num = int(num, 16)
#         case _:
#             print("the detected base is DEC")
#             num = int(num)
        
#     match destination:
#         case 1:
#             return int(num)
#         case 2:
#             return bin(num)
#         case 3:
#             return hex(num)

# print("the number prefix is 0x for HEX, 0b for BIN and no prefix for DEC.")
# num = input("please insert a number in HEX, BIN or DEC: ")
# print("select the destination base")
# print("\t1 for DEC")
# print("\t2 for BIN")
# print("\t3 for HEX")
# try:
#     destination = int(input("please select 1, 2 or 3: "))
#     num = convert(num, destination)
#     print("the conversion yields", num)
# except:
#     print("not a valid number!")


# input("\npress ENTER to proceed to the next exercise...")

# ################## exercise 2 ##################
# print("\n--- --- EXERCISE 2 --- ---")
# print("--- single precision float ---\n")

# print("please enter a 32-bit binary string")
# theString = input()
# if(len(theString) != 32):
#     print("the string is not 32 bits long")
#     print("i will proceed to fill the remaining bits to zero")
#     theString = theString.ljust(32, '0')
#     print("the resulting string is")
#     print(theString)
# sign = 0
# if(theString[0] == '0'):
#     sign = +1
# else:
#     sign = -1
# print("sign=", sign)
# exp = int(theString[1:9], 2) - 127
# print("exponent=", exp)
# mantissa = 1
# for i in range(9, 32):
#     if(theString[i] == '1'):
#         mantissa += 1/(2**(i-8))
# print("mantissa=", mantissa)
# out = sign*mantissa*(2**exp)
# print("the float representation is", out)
# input("\npress ENTER to proceed to the next exercise...")

################## exercise 3 ##################
print("\n--- --- EXERCISE 3 --- ---")
print("--- underflow and overflow ---\n")

overflow = float(1)
half = float()
underflow = float(1)
while abs(overflow*2) != float('inf'):
    overflow = overflow*2
print("overflow:", overflow)
print("if we further multiply by 2, we obtain", overflow*2)

while abs(underflow/2) != float(0):
    underflow = underflow/2
print("underflow:", underflow)
print("if we further divide by 2, we obtain", underflow/2)





input("\npress ENTER to proceed to the next exercise...")

# ################## exercise 4 ##################
# print("\n--- --- EXERCISE 4 --- ---")
# print("--- map dictionary ---\n")
# lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
# print("the input dictionary is:", lang)
# keysLength = list(map(lambda x: len(x), lang.keys()))
# print("the list with the length of the keys is:", keysLength)

# input("\npress ENTER to proceed to the next exercise...")

# ################## exercise 5 ##################
# print("\n--- --- EXERCISE 5 --- ---")
# print("--- lambda functions ---\n")

# language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
# print("the input list is:", language_scores)
# language_scores.sort(key = lambda x : x[0])
# print("the sorted one is:", language_scores)

# input("\npress ENTER to proceed to the next exercise...")

# ################## exercise 6 ##################
# print("\n--- --- EXERCISE 6 --- ---")
# print("--- nested functions ---\n")

# def square(x): return x**2
# def cube(x): return x**3
# def sixth(x): return square(cube(x))

# n = input("please insert a number: ")
# try:
#     n = int(n)
#     print(n,"^2=", square(n))
#     print(n,"^3=", cube(n))
#     print(n,"^6=", sixth(n))
# except:
#     print("this is not a valid number.")

# input("\npress ENTER to proceed to the next exercise...")

# ################## exercise 7 ##################
# print("\n--- --- EXERCISE 7 --- ---")
# print("--- decorators ---\n")

# def hello(function):
#     def wrapper(n):
#         print("Hello World!")
#         return function(n)
#     return wrapper

# @hello
# def square(x):
#     return x**2
# @hello
# def cube(x):
#     return x**3
# @hello
# def sixth(x):
#     return square(cube(x))

# n = input("please insert a number: ")
# try:
#     n = int(n)
#     print(n,"^2=", square(n))
#     print(n,"^3=", cube(n))
#     print(n,"^6=", sixth(n))
# except:
#     print("this is not a valid number")

# input("\npress ENTER to proceed to the next exercise...")

# ################## exercise 8 ##################
# print("\n--- --- EXERCISE 8 --- ---")
# print("--- fibonacci recursive ---\n")

# def recFib(n):
#     if(n==0 or n==1):
#         return 1
#     return recFib(n-1) + recFib(n-2)

# fibTo20 = [recFib(x) for x in range(21)]
# print("the list of fibonacci form fib(0) to fib(20) is: ")
# print(fibTo20)
# input("\npress ENTER to proceed to the next exercise...")

# ################## exercise 9 ##################
# print("\n--- --- EXERCISE 9 --- ---")
# print("--- fibonacci comparison ---\n")

# def recFib(n):
#     if(n==0 or n==1):
#         return 1
#     return recFib(n-1) + recFib(n-2)
# def iterFib(n):
#     prev = 0
#     curr = 1
#     this = 1
#     count = 1
#     while count <= n:
#         prev, curr = curr, this
#         this = prev + curr
#         count+=1
#     return curr

# if __name__ == '__main__':
#     import timeit
#     time_rec = 0
#     time_iter = 0
#     print("calculating fibonacci of first 20 integers 100 for times, using the iterative and recursive algorithm...")
#     for x in range(21):
#         s1 = "iterFib("+str(x)+")"
#         s2 = "recFib("+str(x)+")"
#         time_iter += timeit.timeit(s1, setup="from __main__ import iterFib", number = 100)
#         time_rec += timeit.timeit(s2, setup="from __main__ import recFib", number = 100)
#     print("time for recursive algorithm: %.6fs" % time_rec)
#     print("time for iterative algorithm: %.6fs" % time_iter)

# input("\npress ENTER to proceed to the next exercise...")

# ################## exercise 10 ##################
# print("\n--- --- EXERCISE 10 --- ---")
# print("--- class definition ---\n")

# class Polygon:
#     sides = []
#     def __init__(self, sides):
#         if(type(sides) is tuple and len(sides)>=3):
#             self.sides = list(sides)
#         else:
#             raise ValueError("the Polygon class constructor is expected to receive a tuple as input")
#     def setSides(self, sides):
#         if(type(sides) is list and len(sides)>=3):
#             self.sides = sides
#         else:
#             raise ValueError("setSides is expected to receive a list")
    
#     def getSides(self):
#         return tuple(self.sides)
    
#     def perimeter(self):
#         return sum(self.sides)
    
#     def getOrderedSides(self, increasing = True):
#         return tuple(sorted(self.sides, reverse = not(increasing)))
    

# dim_vector = input("please insert the dimensions, comma separated, at least 3: ")
# dim_vector = dim_vector.replace(" ", "")
# try:
#     dim_list = tuple([float(x) for x in dim_vector.split(",")])
#     p = Polygon(dim_list)
#     print("output of getSides method:")
#     print(p.getSides())
#     print("output of getOrderedSides(True):")
#     print(p.getOrderedSides(increasing = True))
#     print("perimeter: ", p.perimeter())
# except:
#     print("the input format is not right.")

# input("\npress ENTER to proceed to the next exercise...")

# ################# exercise 11 ##################
# print("\n--- --- EXERCISE 10 --- ---")
# print("--- class inheritance ---\n")

# class Rectangle(Polygon):
#     def __init__(self, sides):
#         if(len(sides)==2):
#             sides = sides + sides
#             super().__init__(sides)
#         else: raise ValueError("the input is expected to have 2 values: base and height")
    
#     def area(self):
#         return self.sides[0]*self.sides[1]
    
# dim_vector = input("please insert the base and height, comma separated: ")
# dim_vector = dim_vector.replace(" ", "")
# try:
#     dim_list = tuple([float(x) for x in dim_vector.split(",")])
#     p = Rectangle(dim_list)
#     print("output of getSides method:")
#     print(p.getSides())
#     print("output of getOrderedSides(True):")
#     print(p.getOrderedSides(increasing = True))
#     print("perimeter:", p.perimeter())
#     print("area: ", p.area())
# except:
#     print("the input format is not right.")

# input("\npress ENTER to exit.")