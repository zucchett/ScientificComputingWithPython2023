#AGGIONRAMENTO DI SABATO PER CAPIRE
#******* 'The HelloWorld Replacement' *********
print('\n ___________The HelloWorld Replacement___________ \n')

i = 1
my_list = []

while i <= 100:
   
    if (i % 3 == 0) and (i % 5 == 0):
        print('Hello World')
        my_list.append('PythonWorks')
   
    elif (i % 3 == 0):
        print('Hello')
        my_list.append('Python')
    
    elif (i % 5 == 0):
        print('World')
        my_list.append('Works')
    
    else:
        print(i)
        my_list.append(i)

    i = i + 1;
    
my_tuple = tuple(my_list)
print('\n', my_tuple)


#**********'The Swap'***********
print('\n ___________The Swap___________\n')

a = []
x = input('Write the value of x: ')
y = input('Write the value of y: ')

x , y = y , x;

print('the new value of x is ', x)
print('and the new value of y is ', y)


#**********'Computing the Distance'***********
print('\n___________Computing the Distance___________\n')

import math

x1 = input('Insert the x-value of the first point: ')
x1 = float(x1)

y1 = input('Insert the y-value of the first point: ')
y1 = float(y1)

first_point = (x1, y1)

x2 = input('Insert the x-value of the second point: ')
x2 = float(x2)

y2 = input('Insert the y-value of the second point: ')
y2 = float(y2)

second_point = (x2, y2)

distance = math.sqrt((first_point[0]-second_point[0])**2+(first_point[1]-second_point[1])**2)
print('The distance is ', distance)


#**********'Counting letters'***********
print('\n___________Counting letters___________\n')

from collections import Counter

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
string1 = s1.lower()

s2 = "The quick brown fox jumps over the lazy dog"
string2 = s2.lower()

print('The FIRST STRING is ', string1)
print('The SECOND STRING is ', string2)

print('\n\n******** FIRST STRING **********')
counter1 = Counter(string1)
for i in counter1:
    print(i ,'appears ', counter1[i], ' times')

print('\n******** SECOND STRING **********')
counter2 = Counter(string2)
for i in counter2:
    print(i ,'appears ', counter2[i], ' times')


#**********'Isolating the unique'***********
print('\n___________Isolating the unique___________\n')

from collections import Counter

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

counter = Counter(l)

unique_elements = [x for x in l if counter[x] == 1]
print(unique_elements)
print('The number of unique elements of the list is: ', len(unique_elements))


#**********'Casting'***********
print('\n___________Casting___________\n')

a = input('Write the first number')
b = input('Write the second number')

try:
    c = float(a) + float(b);
    print(c)
except:
    print( "Please, insert numbers")


#**********'Cubes'***********
print('\n___________Cubes___________\n')

cubes1 = [pow(x,3) for x in range(11)]
print(cubes1)

cubes2 = []
for i in range(11):
    cubes2.append(i**3)

print(cubes2)


#**********'List Comprehension'***********
print('\n___________List Comprehension___________\n');

print([(i, j) for i in range(3) for j in range(4)]);


#**********'Nested list comprehension'***********
print('\n___________-Nested list comprehension___________\n');

the_list = []

for a in range(1, 100):
    for b in range(a, 100):
        for c in range(b, 100):
            if a**2+b**2 == c**2:
                temp = (a,b,c)
                the_list.append(temp)


the_tuple = tuple(the_list)    
for triples in the_tuple:
    print(triples)



#**********'Normalization of a N-dimensional vector'***********
print('\n___________Normalization of a N-dimensional vector___________\n');


import math

the_list = (3, 1, 1, 2);

modulo = math.sqrt(sum(x**2 for x in the_list));
normalized_list = [i/modulo for i in the_list];

print('The vector is ', the_list)
print('The magnitude is ', modulo);

tuple_norm = tuple(normalized_list);
print('The normalized vector is ', tuple_norm);


#**********'The Fibonacci sequence'***********
print('\n___________The Fibonacci sequence___________\n');

list = [0, 1];

j = 0;
k = 1;

while len(list) < 20:
    z = list[j] + list[k];
    list.append(z);

    j = j + 1;
    k = k + 1;

print(list);