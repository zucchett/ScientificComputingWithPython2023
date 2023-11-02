#********* 'Global variables' ********* 
print('\n\n____________ Global variables ____________\n')


x = 5
def f(the_list):
    newlist = the_list.copy()
    for i in range(x):
        newlist.append(i)
    return newlist

alist = [1, 2, 3]
ans = f(alist)
print("The modified list:", ans)
print("The original list:", alist)


#********* 'List comprehension' *********
print('\n\n____________ List comprehension ____________\n')


ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print('Using list, map and filter: ', ans)

ans2 = [x*x for x in range(10) if x % 2 == 1]
print('Using list comprehension: ', ans2)


#********* 'Filter list' *********
print('\n\n____________ Filter list ____________\n')


my_word = ['casa', 'moto', 'albero', 'antenna', 'astronauta', 'gru', 'costituzione', 'voto', 'esame', 'laurea', 'lavoro']
my_integer = 5

print('The list of words is: ', my_word)
print('The integer is: ', my_integer)

def myfunction(the_word, the_integer):
    try:
        final_word = list(filter(lambda x: len(x) < the_integer, the_word));
        return final_word
    except:
        print('Attention! Some of the arguments may be wrong!')
result = myfunction(my_word, my_integer)
print('The new list of words whose length is less than', my_integer, 'is: ', result)


#********* 'Map dictionary' *********
print('\n\n____________ Map dictionary ____________\n')


lang = {"Python": 3, "Java": '', "Cplusplus": 'test', "Php": 0.7}

def keyslength(dic):
    try:
        lengths_list = []
        list(map(lambda x: lengths_list.append(len(x)), dic.keys()))
        return lengths_list
    except:
        print('Attention! The argument of the function may be wrong!')

result = keyslength(lang)
print('The lengths of the keys , ', lang.keys(), ' are: ', result)


#********* Lambda functions' *********
print('\n\n____________ Lambda functions ____________\n')


language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

def lookfirst(x):
    try:
        return x[0]
    except:
        print('Attention! Some of the argument may be wrong!')

language_scores.sort(key = lookfirst);
print('Here is the list sorted according to the first element of each tuple: \n', language_scores)


#********* 'Nested functions' *********
print('\n\n____________ Nested functions ____________\n')


def thesquare(x):
    try:
        y = x*x
        return y;
    except:
        print('Attention! The argument may be wrong!')

def thecube(x):
    try:
        y = x*x*x;
        return y;
    except:
        print('Attention! The argument may be wrong!')
        
def thesixth(x):
    try:
        y = thecube(thesquare(x));
        return y;
    except:
        print('Attention! The argument may be wrong!')

n = 10
print('The square of ', n, ' is ', thesquare(n))
print('The cube of ', n, ' is ', thecube(n))
print('The sixth power of ', n, ' is ', thesixth(n))


#********* 'Decorators' *********
print('\n\n____________ Decorators ____________\n')


def hello(func):
    
    def wrapper(x):
        print("Hello World!")
        result = func(x)
        return result
        
    return wrapper

@hello
def square(x):
    return x*x

n = 10
print('The square of ', n, ' is ', square(n))


#********* 'The Fibonacci sequence (part 2)' *********
print('\n\n____________ The Fibonacci sequence (part 2) ____________\n')


def recursiveFibonacci(x):
    if x == 1:
        return [0]
    elif x == 2:
        return [0, 1]
    else:
        sequence = recursiveFibonacci(x - 1)
        result = sequence[-1] + sequence[-2]
        sequence.append(result)
        return sequence

fibonacci_sequence = recursiveFibonacci(20)
print(f"Fibonacci sequence for n=20: {fibonacci_sequence}")


#********* 'The Fibonacci sequence (part 3)' *********
print('\n\n____________ The Fibonacci sequence (part 3) ____________\n')


import timeit

def recursiveFibonacci(x):
    if x == 1:
        return [0]
    elif x == 2:
        return [0, 1]
    else:
        previous_sequence = recursiveFibonacci(x - 1)
        result = previous_sequence[-1] + previous_sequence[-2]
        new_sequence = previous_sequence
        new_sequence.append(result)
        return new_sequence

def loopFibonacci(n):
    list = [0, 1];

    j = 0;
    k = 1;

    while len(list) < n:
        z = list[j] + list[k];
        list.append(z);

        j = j + 1
        k = k + 1

   
    return list

timer_loop = timeit.Timer(lambda: loopFibonacci(20))


timer_recursive = timeit.Timer(lambda: recursiveFibonacci(20))

repeat = 1000  
execution_time_loop = timer_loop.timeit(number=repeat)
execution_time_recursive = timer_recursive.timeit(number=repeat)


print('The average execution time of the function with the while loop is ', execution_time_loop/repeat, ' seconds')
print('The average execution time of the recursive function is ', execution_time_recursive/repeat, ' seconds')

print('The recursive function takes more time because there are many calls of the same function')


#********* 'Class definition' *********
print('\n\n____________ Class definition ____________\n')


class Polygon:

    def __init__(self, sides):
        if len(sides) < 3:
            print('Error! The number of sides is not sufficient to create a polygon')
        elif any(x <= 0 for x in sides):
            print('Error! All the sides must be longer than zero')
        else:
            self.sides = sides

    def getLength(self, n):
        if n < 0 or n > len(self.sides) - 1:
                print('Error! The index is not valid for the polygon')
        else:
            return self.sides[n]

    def setLength(self, n, length):
        if length < 0:
            print('Error! The length cannot be less than zero')
        elif n < 0 or n > len(self.sides) - 1:
                print('Error! The index is not valid for the polygon')
        else:
            self.sides[n] = length

    def perimeter(self):
        return sum(self.sides)
        
    def getOrderedSides(self, increasing):
        if increasing == True:
            return sorted(self.sides)
        else:
            return sorted(self.sides, reverse = True)
        
     
the_polygon = Polygon([1, 3, 2, 5, 4])
#the_polygon = Polygon([1,1,-3])  this istance is useful to test the error message during inizialization

print('This is the starting Polygon: 1, 3, 2, 5, 4')
print('The perimeter of the polygon is ', the_polygon.perimeter())
print('The ascending sorted sequence of the polygon is ', the_polygon.getOrderedSides(increasing = True))
print('The descending sorted sequence of the polygon is ', the_polygon.getOrderedSides(increasing = False))
print('The value of the third side (the count starts from zero) is ', the_polygon.getLength(3))
the_polygon.setLength(0, 100)
print('The value of the first side (the count starts from zero) has just been modified to 100 (if there is not any error message from the previous step)')
print('The value of the first side (the count starts for zero) is ', the_polygon.getLength(0))



#********* 'Class inheritance' *********
print('\n\n____________ Class inheritance ____________\n')


class Rectangle(Polygon):
    
    def __init__(self, sides):
        if len(sides) != 4:
            print("Error: number of components is not 4")
        elif sides[0] != sides[2] or sides[1] != sides[3]:
            print("Error: opposite sides are not equal")
        else:
            self.sides = sides
    
    def area(self):
        return self.sides[0]*self.sides[1]
    
the_rectangle = Rectangle([2,8,2,8])
print('This is the starting rectangle: 2, 8, 2, 8')
print("The rectangle has sides equal to ", the_rectangle.getOrderedSides(increasing = True))
print("The area of the rectangle is ", the_rectangle.area())
