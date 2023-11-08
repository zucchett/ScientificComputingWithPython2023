import math as m 
import numpy as np
from sklearn import preprocessing

#------------TASK 1a------------#

def hello_world_replace():
    for i in range(1, 101):
        if ((i%3 == 0) and (i%5 == 0)):
            print('HelloWorld')
        elif (i%3 == 0): 
            print('Hello')
        elif (i%5 == 0):
            print('World')
        else:
            print(i)

print('Task 1a: \n')            
hello_world_replace()
print('\n')

#------------TASK 1b------------#

def hello_world_list():
    list = []
    for i in range(1, 101):
        if ((i%3 == 0) and (i%5 == 0)):
            list.append('HelloWorld')
        elif (i%3 == 0): 
            list.append('Hello')
        elif (i%5 == 0):
            list.append('World')
        else:
            list.append(i)
    return list

def make_tuple():    
    #convert list to a tuple       
    res = tuple(hello_world_list())

    #convert back to list to change
    res = list(res)
    
    for i in range(0, len(res)):
        if (res[i] == 'Hello'):
            res[i] = 'Python'
        if (res[i] == 'World'):
            res[i] = 'Works'

    #change back to tuple
    res = tuple(res)
    return res

print(f'Task 1b: \n {make_tuple()} \n')

#------------TASK 2------------#
def swap_values():

    x_input = input('Enter x value: ')
    y_input = input('Enter y value: ')
    print('X and Y before swap: ', 'x =', x_input, ',', 'y =', y_input)

    x_input, y_input = y_input, x_input
    print('X and Y after swap: ','x =', x_input,',','y =', y_input, '\n')

print('Task 2: \n')
swap_values()
print('\n')

#------------TASK 3------------#
def euclidian_distance(x_1, y_1, x_2, y_2):
    u = (x_1, y_1)
    v = (x_2, y_2)
    euc_dist = m.sqrt((v[0] - u[0])**2 + (v[1] - u[1])**2)
    return euc_dist

print(f'Task 3: \n The euclidian distance between two vectors is: \n {euclidian_distance(3,0,0,4)} \n')

#------------TASK 4------------#

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

def count_characters(test_string):
    all_freq = {}

    for c in test_string:
        if c != ' ':
            if c in all_freq:
                all_freq[c] += 1
            else:
                all_freq[c] = 1

    return all_freq

print(f'Task 4: \n Count of all characters in string is: \n {str(count_characters(s2))} \n')

#------------TASK 5------------#
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

def count_unique_nr(number_array):
    unique = {}

    for n in number_array:
        if n not in unique:
            unique[n] = 1
    
    return unique

print(f'Task 5: \n Unique numbers in number array are: \n {str(count_unique_nr(l))} \n')

#------------TASK 6------------#

def convert_int_float(input):
    try:
        var = int(input)
    except ValueError:
        try:
            var = float(input)
        except ValueError:
            var = input
    return var

def casting():
    input_1 = input('Enter an int, float, or string: ')
    input_2 = input('Enter an int, float, or string: ')
    
    # Have to convert var to int or float if possible, 
    # not possible if user input is a string
    var_1 = convert_int_float(input_1)
    var_2 = convert_int_float(input_2)

    try:
        res = var_1 + var_2
        print(f"The result of adding {var_1} and {var_2} is: {res}")
    except (TypeError, ValueError) as e:
        print(f'Error: {e}')
    else:
        # Continue with the program here
        return res

print('Task 6: \n')
casting()
print('\n')

#------------TASK 7a------------#
#cubes: 1**3 = 1, 2**3 = 8
x = list(range(0,11,1))

def cubes_a(list):
    cube_list = []
    for n in range(0,len(list)):
        n_3 = n**3
        if (n_3 < list[-1]) and (n != 0):
            cube_list.append(n**3)
    return cube_list

print(f'Task 7a: \n The cubes of the given list are: \n {cubes_a(x)} \n')

#------------TASK 7b------------#
def cubes_b(list):
    cube_list = []
    for n in list:
        n_3 = n**3
        if (n_3 < list[-1]) and (n != 0):
            cube_list.append(n**3)
    return cube_list

print(f'Task 7b: \n The cubes of the given list are: \n {cubes_b(x)} \n')

#------------TASK 8------------#

#Function 
def function_to_replace():
    a = []
    for i in range(3):
        for j in range(4):
            a.append((i, j))
    print(a)

def list_comprehension(l_range_1, l_range_2):
    list = [(i,j) for i in range(l_range_1) for j in range(l_range_2)]
    return list

print(f'Task 8: \n {list_comprehension(3,4)} \n')  

#------------TASK 9------------#

def pythagorean_triplet(upper_lim):
    pythag_triplet = [(a, b, c) for a in range(1, upper_lim) \
    for b in range(a, upper_lim) for c in range(b, upper_lim) \
    if a**2 + b**2 == c**2]

    pythag_tuple = tuple(pythag_triplet)

    return pythag_tuple

N = 100
print(f'Task 9: \n The unique pythagoran triples are: \n {pythagorean_triplet(N)} \n')

#------------TASK 10------------#

int_array = np.array([1,2,3,4,5,6,7,8,9])

def normalize_N_dim_vec(vec):
    normalized_arr = preprocessing.normalize([vec])
    sum = np.sum(normalized_arr ** 2)
    return normalized_arr, sum

norm_arr, sum = normalize_N_dim_vec(int_array)
print(f'Task 10: \n The normalized array: {norm_arr} \n The sum of all the elements in the normalized array: {sum} \n')

#------------TASK 11------------#

def fibonacci_sequence(lower_lim, upper_lim):
    #add seed values first
    fibonacci_seq = np.array([0,1])
    for i in range(lower_lim, upper_lim):
        f_n = fibonacci_seq[i-1] + fibonacci_seq[i-2]
        fibonacci_seq = np.append(fibonacci_seq, f_n)
    return fibonacci_seq

print(f'Task 11: \n The first 20 numbers in the fibonacci sequence are: \n {fibonacci_sequence(2, 20)}')
