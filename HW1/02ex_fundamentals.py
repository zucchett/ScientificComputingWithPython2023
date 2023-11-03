def f(alist):
    x = 5
    ans = [1, 2, 3]
    for i in range(x):
        ans.append(i)
    return ans

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist)
#-----------------------------------------------------------------------------------------------------------------------
ans = [i ** 2 for i in range(0,11) if i % 2 == 1]
print(ans)
#-----------------------------------------------------------------------------------------------------------------------
#user should enter the value of n
word_list =['ali','mohammad','sina']
result = list(filter(lambda n : len(n)<5 ,word_list))
print(result)
#--------------------------------------------------------------------------------------------------------------------------
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
lang_keys = lang.keys()
result_list = list(map(lambda n : len(n),lang_keys))
print(result_list)
#-----------------------------------------------------------------------------------------------------------------------
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key=lambda x : x[0])
print(language_scores)
#----------------------------------------------------------------------------------------------------------------------------
number_list = [1,2,3,4,5]
def square():
    square_list = [i ** 2 for i in number_list]
    return square_list
def cube():
    cube_list = [i **3 for i in number_list]    
    return cube_list
def sixth_power():
    first_list = [i ** 6 for i in square()]
    second_list = [j ** 6 for j in cube()]
    return first_list, second_list

print(sixth_power())
#-----------------------------------------------------------------------------------------------------------------------------------
def hello(func):
    def inner(*args, **kwargs):
        print('hello')
        returned_value = func(*args, **kwargs)
        return returned_value
    return inner

@hello
def square(x):
    return x*x        
print(square(4))
#------------------------------------------------------------------------------------------------------------------------------------
# Python program to display the Fibonacci sequence
recur_fibo_list = []
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

for i in range(19):
    recur_fibo_list.append(recur_fibo(i))
print(recur_fibo_list)
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
import timeit
fibo_list = [0,1,1]
def fiboloop():
    for i in range (3,19):
        next_fibo_value = fibo_list[i-2] + fibo_list[i-1]
        fibo_list.append(next_fibo_value)
#-----------------------------------------------------------------------------
recur_fibo_list = []
def recur_fibo_func() :
    def recur_fibo(n):
        if n <= 1:
            return n
        else:
            return(recur_fibo(n-1) + recur_fibo(n-2))
    for i in range(19):
        recur_fibo_list.append(recur_fibo(i))
#---------------------------------------------------------------------------------
time_1 = timeit.Timer(lambda:fiboloop())
time_2 = timeit.Timer(lambda:recur_fibo_func())
print(f'the proceed time for first solution is : {time_1.timeit(1)}')
print(f'the proceed time for second solution is : {time_2.timeit(1)}')
#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
class polygon :
    def __init__(self,sides_tuple) :
        self.sides_tuple = sides_tuple
    def demonstrat(self):
        print(f' the length of size are : {self.sides_tuple}')
    def perimeter(self):
        print(f'the perimeter of this polygon is : {sum(self.sides_tuple)}')
    def getOrderedSides(self):
        print(f'the sorted tuple of sides is : {tuple(sorted(self.sides_tuple))}')
a = polygon((4,3,2,1))
a.demonstrat()
a.perimeter()
a.getOrderedSides()
#------------------------------------------------------------------------------------------------------------------------------------------------
class polygon :
    def __init__(self,sides_tuple) :
        self.sides_tuple = sides_tuple
    def demonstrat(self):
        print(f' the length of size are : {self.sides_tuple}')
    def perimeter(self):
        print(f'the perimeter of this polygon is : {sum(self.sides_tuple)}')
    def getOrderedSides(self):
        print(f'the sorted tuple of sides is : {tuple(sorted(self.sides_tuple))}')

class rectangle(polygon):
    def __init__(self, sides_tuple):
        self.sides_tuple = sides_tuple
    def area(self):
        sorted_sides = sorted(self.sides_tuple)
        print(f'the area of rectangle is {sorted_sides[0] * sorted_sides[2]}')

example = rectangle((3,1,3,1))
print(example.area())
#------------------------------------------------------------------------------------------------------------------------------------------------------