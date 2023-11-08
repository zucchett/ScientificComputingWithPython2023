import math as m 
import numpy as np
import timeit as t
import pandas as pd
#------------TASK 1------------#

def f(lst, upper_lim):
    list = []
    for i in range(upper_lim):
        list.append(i)
    return list

lst = [1,2,3]
new_list = f(lst, 5) 
print(f'Task 1: \n The original list: \n {lst} \n And the new list: \n {new_list} \n')

#------------TASK 2------------#

list_2 = [x**2 for x in range(10) if x % 2 == 1]
print(f'Task 2: \n The list made with list comprehension: \n {list_2} \n')

#------------TASK 3------------#
def filter_words_by_len(wordlist, n):
    def condition(word):
        return len(word) <= n
    return list(filter(condition, wordlist))

wordlist_1 = ['Hello', 'I', 'You', 'Music', 'Guitar', 'Bye', 'Impossible'] 
filtered_words = filter_words_by_len(wordlist_1, 5)
print(f'Task 3: \n Original list: \n {wordlist_1} \n List with filtered words by length: \n {filtered_words} \n')

#------------TASK 4------------#
lang = {"Python": 3, "Java": '', "Cplusplus": 'test', "Php": 0.7}

def key_lengths(dict):
    return list(map(len, dict.keys()))

key_len_list = key_lengths(lang)
print(f'Task 4: \n The lenght of the keys in the dictionary: \n {lang} \n is placed in this list: \n {key_len_list} \n')

#------------TASK 5------------#
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key = lambda x: x[1])
print(f'Task 5: \n The sorted list of tuples: \n {language_scores} \n')


#------------TASK 6------------#
def squared(number):
    squared_n = number**2
    return squared_n

def cube(number):
    cubed_n = number**3
    return cubed_n

def sixed_power(number):
    sixed_power_n = (squared(number) * cube(number)) * m.sqrt(squared(number))
    return sixed_power_n

x = 2

print(f'Task 6: \n The squared number of {x} is {squared(x)} \
      \n The cube of the number {x} is {cube(x)} \
      \n The 6th power of the number {x} is {sixed_power(x)} \n')

#------------TASK 7------------#
def hello(func):
    def wrapper(*args, **kwargs): #we don´t know what parameters the func will have, but we know it will have some
        val = func(*args, **kwargs)
        print("Hello World")
        return val
    return wrapper
    
@hello
def square(x):
    return x*x

x = 2
print('Task 7: \n Test of wrapper function: \n')
print(square(x))
print('\n')

#------------TASK 8------------#

def fibonacci_recur(n):
    if n <= 1:
        return n
    else:
        return(fibonacci_recur(n-1) + fibonacci_recur(n-2))

n = 20
print(f'Task 8: \n The 20 first numbers of the fibonacci sequence: \n')
for i in range(n):
    print(fibonacci_recur(i))

print('\n')

#------------TASK 9------------#

#fibonacci sequence from ex1
def fibonacci_sequence(lower_lim, upper_lim):
    #add seed values first
    fibonacci_seq = np.array([0,1])
    for i in range(lower_lim, upper_lim):
        f_n = fibonacci_seq[i-1] + fibonacci_seq[i-2]
        fibonacci_seq = np.append(fibonacci_seq, f_n)
    return fibonacci_seq


time_recur = t.timeit("fibonacci_recur(20)", globals=globals(), number=1)
time_for_loop = t.timeit("fibonacci_sequence(2,20)", globals=globals(), number=1)
time_diff = time_recur - time_for_loop

print(f'Task 9: \n Time to run recursive fibonacci sequence: \n {time_recur} \
       \n Time to run the one with for loops: \n {time_for_loop} \n')

print(f"The implementation with for loops is more efficient by {time_diff:.5f} seconds. \n")

#------------TASK 10------------#
class Polygon:
    def __init__(self, sides_len):
        if len(sides_len) < 3:
            raise ValueError("A polygon must have at least 3 sides.")
        self.sides_len = list(sides_len)

    def set_lenght(self, side_index, lenght):
        if side_index < 0 or side_index >= len(self.sides_len):
            raise ValueError("Invalid side index")
        self.sides_len[side_index] = lenght

    def get_lenght(self, side_index):
        return self.sides_len[side_index]
    
    def perimeter(self):
        return sum(self.sides_len)
    
    def getOrderedSides(self, increasing=True):
        ordered_sides = sorted(self.sides_len) if increasing else sorted(self.sides_len, reverse=True)
        return tuple(ordered_sides)

#test class
triangle = Polygon((4,4,4))
sum = triangle.perimeter()
print(f'Task 10: \n The sum of the lenghts of all sides: {sum}')
triangle.set_lenght(1,2)
num_order = triangle.getOrderedSides(increasing=True)
print(f'List of ordered sides lenghts: {num_order}')
side_lenght = triangle.get_lenght(0)
print(f'Side lenght of side 0: {side_lenght} \n')


#------------TASK 11------------#

class Rectangle(Polygon):
    def __init__(self, sides_len):
        if len(sides_len) != 4:
            raise ValueError("A rectangle has only 4 sides.")
        if ((pd.Series(sides_len).value_counts()).count() != 2):
            raise ValueError("A rectangle has 2 and 2 sides that are similar.")

        self.sides_len = list(sides_len)

    def area(self):
        return min(self.sides_len) * max(self.sides_len)
    

rectangle_1 = Rectangle((2,4,2,4))

print(f'Task 11: \n The area of your rectangle: {rectangle_1.area()}')
