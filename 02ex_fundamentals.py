import copy
import timeit
# ------------------ EX 1 ------------------
# 1)  Convert the function  𝑓 into a function that doesn't use global variables and that does not modify the original list
print("1)  No use of global variables \n")
x = 5

#alist is passed by assignment 
def f(alist):
    alist2 = alist.copy()
    for i in range(x):
        alist2.append(i)
    return alist2

alist = [1, 2, 3]
ans = f(alist)
print("id ans", id(ans), "ans:", ans)
print("id alist", id(alist), "alist:", alist) # now alist hasn't been changed
print("\n")

# ------------------ EX 2 ------------------
# 2) Write the following expression using a list comprehension:
print("2)  Convert expression using a list comprehension \n")
ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print("ans without list comprehension", ans)
ansc = [x**2 for x in range(10) if x % 2 == 1 ]
print("ans by using list comprehension", ansc)
print("\n")

# ------------------ EX 3 ------------------
#3) Using the filter() hof, define a function that takes a list of words and 
#   an integer n as arguments, and returns a list of words that are shorter than n.
print("3)  Using filter \n")

def funct(l, n):
    ret = list(filter(lambda w: len(w) < n, l))
    return ret

words = ["Using", "the", "filter()", "hof", "define", "a", "function", "that", "takes", "a", "list", "of", "words"]
print("words:", words)
num = 0
try:
    num = int(input("insert an integer n = "))
    print("funct(words,n)", funct(words,num))
except:
    print("n isn't an integer")

print("\n")

# ------------------ EX 4 ------------------
print("4)  Map dictionary \n")
# by using a map, compute the length of each key
def key_length(dict):    
    lengths = list(map(len, dict.keys()))
    return lengths
    
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
print("keys:", lang.keys())
print("key_lengths:", key_length(lang))
print("\n")

# ------------------ EX 5 ------------------
print("5)  Lambda functions \n")
#sorts the following list of tuples using a lambda function, according to 
#the alphabetical order of the first element of the tuple:
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
print("language_scores: ", language_scores)

#define a lambda to use as a sorting criteria
language_scores.sort(key = lambda tup: tup[0])
print("language_scores sorted: ", language_scores)
print("\n")

# ------------------ EX 6 ------------------
print("6)  Nested functions \n")
def square(n):
    return n**2

def cube(n):
    return n**3

def sixth_pow(n):
    return square(cube(n))

try:
    num = int(input("insert an integer n = "))
    print("n^6 = ", sixth_pow(num))
except:
    print("n isn't an integer")
print("\n")

# ------------------ EX 7 ------------------
# 7) create a decorator that makes every wrapped function print
# “Hello World!” each time the function is called.
print("7) Decorators \n")
def hello(f):
    def wrapper(y):
        print("Hello World!")
        return f(y)
    
    return wrapper
#simplest way to use decorator
@hello
def square(x):
    return x*x

#call the function
try:
    print("Function square(n) called with decorator")
    n = int(input("Insert n = "))
    print("square(n) = ", square(n))
except:
    print("n isn't an integer")
print("\n")

# ------------------ EX 8 ------------------
# 8) Calculate the first 20 numbers of the Fibonacci sequence using a recursive function.
print("8) Recursive - Fibonacci_sequence \n")
def recursiveFibonacci(n):
    f = []
    if(n <= 1):
        f.append(0)
        f.append(1)
        return f
    f = recursiveFibonacci(n-1)
    f.append(f[n-1]+f[n-2])
    return f


#first element of Fibonacci sequence is zero
seq = recursiveFibonacci(20)
# 20 = number of elements in the sequence
print("Fibonacci sequence with 20 elements:", seq)
print("\n")

# ------------------ EX 9 ------------------
# 9) Calculate the first 20 numbers of the Fibonacci sequence using a recursive function.
def loopFibonacci(k):
    f = [0,1]
    i = 2
    while(len(f) <= k):
        f.append(f[i-2] + f[i-1])
        i += 1
    return f

print("9) Comparison of Fibonacci sequences \n")
start = timeit.default_timer()
output = loopFibonacci(20)
end = timeit.default_timer()
print("loopFibonacci sequence:", output)
print("loopFibonacci time:", end-start)

output.clear()
start = timeit.default_timer()
output = recursiveFibonacci(20)
end = timeit.default_timer()
print("recursiveFibonacci sequence:", output)
print("recursiveFibonacci time:", end-start)
# NB: I've used also this different method to measure the execution code of the 2 functions
tloop = timeit.timeit(lambda: loopFibonacci(20),number=1)
trec = timeit.timeit(lambda: recursiveFibonacci(20),number=1)
print("tloop", tloop, "\ntrec", trec, "\nchange in time 100.0*(trec-tloop)/trec = ", 100.0*(trec-tloop)/trec, '%')
print("\n")

# OBS: the most efficient implementation is the loopFibonacci 
# the difference in time changes depending on the execution, but most of the time
#doesn't exceed 40%

# ------------------ EX 10 ------------------
# 10) Define a class polygon. The constructor has to take a tuple as input
# that contains the length of each side. The (unordered) input list does
# not have to have a fixed length, but should contain at least 3 items.
print("class definition - polygon")
class polygon:
    sides = ()
    # Definition of the Constructor
    def __init__(self, lengths):
        if(len(lengths) < 3):
            print("Error: the tuple should contain at least 3 items\n")
        else:
            self.sides = lengths # a tuple is expected as input

    # This method allows to get individial elements of the 'x' attribute 
    def getSideN(self, n): # n is the n-th side
        if n < len(self.sides):
            return self.sides[n]
        else:
            print(f"Error: the polygon has only {len(self.sides)} sides")

    # This method allows to set individial elements of the 'x' attribute 
    def setSideN(self, n, newl): # n is the component index, and newl is the value
        if n < len(self.sides):
            self.sides[n] = newl
        else:
            print(f"Error: the polygon has only {len(self.sides)} sides")
    def perimeter(self):
        return sum(self.sides)

    def getOrderedSides(self, increasing = True):
        s = copy.copy(self.sides) #it's better not to modify the original list
        if(increasing):  
            s.sort()
            return s
        else:
            self.sides.sort(reverse=True)
            return s

p = polygon([3,4]) #tries to create a polygon with less than 3 sides
p = polygon([15,20,3,1,7])
print("polygon sides:", p.getSideN(0), p.getSideN(1), p.getSideN(2), p.getSideN(3), p.getSideN(4))
print("getSide(6)")
n = p.getSideN(6) #tries to get a side that doesn't exist
print("perimeter()", p.perimeter())
print("getOrderedSides()", p.getOrderedSides())
print("getOrderedSides(increasing = False)",p.getOrderedSides(False))
print("\n")
# ------------------ EX 11 ------------------
# 11) Define a class rectangle that inherits from polygon
print("class inheritance - polygon")
class rectangle(polygon):
    # The constructor here is optional, and can be inherited from the parent class if omitted
    def __init__(self, lengths):
        l = copy.copy(lengths)
        if len(l) != 4:
            print("Error: number of rectangle_sides is not 4")
            #first-second must be equal, as well as third-fourth (if all sides are equal it's a special case of rectangle)
        else: 
            list(l).sort() #it's better not to modify the original list, so I uses l   
            if (l.count(l[0]) != 2 or l.count(l[2]) != 2):
                print("Error: this is not a rectangle since there aren't 2 couples of equal sides")
            else:
                self.sides = lengths

    def area(self):
        lengths = self.sides #it's better not to modify the original list
        list(lengths).sort()
        return (self.sides[0]*self.sides[2])

print("rectangle((2,4,4,5)")
wrong = rectangle((2,4,4,5))
print("rectangle((5,4,4,5))")
r = rectangle((5,4,4,5))
print("area(r)", r.area())
print("\n")

