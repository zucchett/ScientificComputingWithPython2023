#These are the solutions of the tasks presented in the second set of exercises, described in the file 02ex_fundamentals.ipynb

#Exercise 1
#The following code creates a copy of a given list so that the original list is not modified. We make sure of this statement by printing both of them.

import copy
x = 5

def f(alist):
    c_list = alist.copy()
    for i in range(x):
        c_list.append(i)
    return c_list

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist)

#Exercise 2
#Little exercise where we had to express list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))) using list comprehension.
print("\n \n \n ")

ans_comp = [x**2 for x in range(10) if x%2==1]
print(ans_comp)

#Exercise 3
#This exercise makes use of the function filter() to return a list containing all the words shorter than n from a given list of words.
print("\n \n \n ")

def counter(list_in, n):
    return list(filter(lambda list_in: len(list_in) < n, list_in))
in_list = ["Python", "Java", "Cplusplus", "test", "Php"]
#Example with n=7, this can be modified to a desired integer.
n = 7
print(counter(in_list, n))

#Exercise 4
#This exercise returns a list containing the length of the keys from a given dictionary.
print("\n \n \n ")

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
def mapper(dictionary):
    key_d = list(dictionary)
    return list(map(lambda x: len(key_d[x]), range(len(key_d))))
key_l = mapper(lang)
print(key_l)

#Exercise 5
#This code sorts the list of tuples according to the first element in the tuple.
print("\n \n \n ")

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key=lambda fs: fs[0])
print(language_scores)

#Exercise 6
#Exercise on nested function to return the 6th power of a number.
print("\n \n \n ")

def squared(int1):
    return int1**2
def cubic(int2):
    return int2**3
def power6(int3):
    return cubic(squared(int3))

#Exercise 7
#This code prints "Hello World!" each time the function is called, while also returning the result of the original function
print("\n \n \n ")

def hello(func):
    def wrapper(x):
        print("Hello World!")
        func(x)
        return func(x)
    return wrapper

@hello
def square(x):
        return x*x

#The following code is written just to prove the effect of the decorator described above.
#square(5)
#for i in range(0,20):
#    print(square(i))

#Exercise 8
#The following code obtaines the Fibonacci sequence in a recursive way. It is applied to obtain the first 20 numbers of the sequence.
print("\n \n \n ")

def rec_Fib(num):
    if (num == 0):
        return 0
    if (num==1):
        return 1
    else:
        return rec_Fib(num-1)+rec_Fib(num-2)
Fib_seq = []
for i in range(0, 20):
    Fib_seq.append(rec_Fib(i))
print(Fib_seq)

#Exercise 9
#In this exercise we are comparing the recursive and iterative way to obtain the Fibonacci sequence. As we can see from the timings
#the iterative method is much faster, so it represents a better implementation. This is because there are many instances that are 
#repeated when looking for the Fibonacci sequence: this slows down the implementation of the recursive method, which has to always
#calculate the instances.
print("\n \n \n ")

import timeit

start1 = timeit.timeit()
def iter_Fib(num):
    Fib = {}
    for i in range(0,num):
        if (i==0):
            Fib[i] = 0
        if (i==1):
            Fib[i] = 1
        elif ((i!=0)and(i!=1)):
            Fib[i] = Fib[i-1] + Fib[i-2]
    return Fib
def rec_Fib(num):
    if (num == 0):
        return 0
    if (num==1):
        return 1
    else:
        return rec_Fib(num-1)+rec_Fib(num-2)
    
def measure_exec_time_rec(N):
    return timeit.timeit(lambda: rec_Fib(N), number=1)
def measure_exec_time_iter(N):
    return timeit.timeit(lambda: iter_Fib(N), number=1)
print("Time taken for computing the first 20 numbers with the iterative method: ", measure_exec_time_iter(20)*(10**3), " ms")
print("Time taken for computing the first 20 numbers with the recursive method: ", measure_exec_time_rec(20)*(10**3), " ms")
#The % method doesn't work when giving the file by command line.
#x = %timeit iter_Fib(20)
#y = %timeit rec_Fib(20)

#Exercise 10
#Exercise on the class polygon. Comments are added inside of the class.
print("\n \n \n ")

class polygon:
    '''This class creates a polygon from a given tuple. The minimum number of sides given for the creation of a polygon should be 3.
    	There is a constructor which returns an element of the class and some useful methods regarding a polygon are described in the class'''
    x = []
    
    def __init__(self, tup_comp):
        if len(tup_comp)<3:
            print("The values inserted do not compose a polygon")
        else:
            self.x = tup_comp
            
    #This returns the length of the specified side if possible (it was not explicitly asked to show how to deal with the input if the side is out of bounds -> In this case it returns an error)
    #In order to not get the error we could use an if/else statement or a try/except construct.
    def getLength(self, n):
        return self.x[n]
    
    #This method returns the value of the perimeter of the polygon
    def perimeter(self):
        if len(self.x)<3:
            print("It is impossible to calculate the perimeter as the input inserted do not compose a polygon")
            return ''
        else:
            perim = 0
            for i in range(len(self.x)):
                perim += self.x[i]
            return perim
    
    def getOrderedSides(self, increasing):
        if len(self.x)<3:
            print("Input inserted cannot be converted to a polygon")
            return ''
        else:
            y = []
            for i in range(len(self.x)):
                y.append(self.x[i])
            if (increasing == True):
                return tuple(sorted(y))
            else:
                return tuple(sorted(y, reverse = True))
    

a = polygon((4, 5, 6))
print(a.perimeter())
print(a.getLength(0))
print(a.getOrderedSides(increasing=True))

#Exercise 11
#This class inherits methods from the polygon class described in the exercise before. The constructor is redefined and one method is added.
#Comments are added inside of the class
print("\n \n \n ")

class rectangle(polygon):
    '''The constructor is redefined: as the class is dealing with a rectangle we can have two cases: we pass just two sides for the rectangle
    	which will represent the width and height, or we pass 4 sides where the first has the same length as the third and the second has the same
    	length as the fourth side. The second case is a special case of a polygon whereas the first case represent a case which would be discarded
    	by the polygon class.'''
    x = []
    
    def __init__(self, tup_comp):
        if (len(tup_comp)==2)or((len(tup_comp)==4)and(tup_comp[0]==tup_comp[2])and(tup_comp[1]==tup_comp[3])):
            y=[]
            if len(tup_comp)==4:
                y.append(tup_comp[0])
                y.append(tup_comp[1])
                self.x = y
            else:
                self.x = tup_comp
        else:
            print("The input inserted does not represent a rectangle")
    
    #This method returns the area of a rectangle. In this case there is also a check for possible problems by using an if statement.
    def area(self):
        if len(self.x)==0:
            print("The input inserted does not represent a rectangle: area method valid only for rectangles")
            return ''
        else:
            return self.x[0]*self.x[1]
            
b = rectangle((4,5,4))
print(b.area())


#End of the exercises: I add an extra input in order to keep the code running for the last exercises.
input('Press ENTER to close the second set of exercises')