import sys
import math
import collections

#exercise 1
print('Exercise 1')

print('Exercise 1.a')
i=1
while i<=100:
    if i % 3 ==0 & i % 5 ==0:
        print('HelloWorld,', end=' ')
    elif i % 3 == 0:
        print('Hello,', end=' ')
    elif i % 5 == 0:
        print('World,', end=' ')
    else:
        print(i,',', end=' ')
    i=i+1

print('Exercise 1.b')
i=2
tupla = ('1')
while i<=100:
    if i % 3 ==0 & i % 5 ==0:
        tupla = tupla + (', PythonWorks')
    elif i % 3 == 0:
        tupla = tupla + (', Python')
    elif i % 5 == 0:
        tupla = tupla + (', Works')

    else:
        numero = str(i)
        tupla = tupla + (', ') + (numero)
    i=i+1
    
print(tupla)

print('')

#exercise 2
print('Exercise 2')

print('x=' , sys.argv[2], 'y=', sys.argv[1])

print('')

#exercise 3
print('Exercise 3')

tuple1 = (3, 0)
tuple2 = (0, 4)

x = tuple1[0] - tuple2[0]
y = tuple1[1] - tuple2[1]

result = math.sqrt(x*x + y*y)
print('the euclidean distance between the points is: ', result)

print('')

#exercise 4
print('Exercise 4')
'''
More efficient way:
string = input('write a string:' ).lower()
occurrences = collections.Counter(string)
print(occurrences)
'''
#Metodo con dizionari:
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

diz1 = {}
diz2 = {}
for keys in s1.lower():
    diz1[keys] = diz1.get(keys, 0) + 1
for keys in s2.lower():
    diz2[keys] = diz2.get(keys, 0) + 1

print("Count of all characters in s1 is : \n" + str(diz1))
print("Count of all characters in s2 is : \n" + str(diz2))

print('')
#exercise 5
print('Exercise 5')

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

unique_numbers = []
dictionary = {}

for item in l:
    dictionary[item] = dictionary.get(item, 0) + 1

for value, key in dictionary.items():  
    if key == 1:
        unique_numbers.append(value)
    
print(unique_numbers)
print('')
#exercise 6
print('Exercise 6')

n1 = sys.argv[3]
n2 = sys.argv[4]

try:
    n1 = float(n1)
    n2 = float(n2)

    print('sum between', n1, 'and', n2, 'is: ', n1 + n1)
except:
    print('It is not possible to compute ', n1, ' + ', n2)
    
print('')
#exercise 7
print('Exercise 7')

print('Exercise 7.a')
list1 = []
for i in range(11):
     list1.append(i**3)
print('list with for loop: ',list1)

print('Exercise 7.b')
list2 = [x**3 for x in range(11)]
print('list with list comprehension: ',list2)

print('')

print('Exercise 8')
a = [(i,j) for i in range(3) for j in range(4)]
print(a)
print('')

print('Exercise 9')

triplet = [(a,b,c) for c in range(100) for b in range(c) for a in range(b) if c*c == a*a + b*b]

print('Pythagorean triple with c < 100:', triplet)

print('')

print('Exercise 10')

vector = [3, 4, 5, 9, 3, 11]

norm = [x/(sum([x**2 for x in vector])) for x in vector]

print('Vector: ', vector)
print('Normalized vector:', norm)
print('')

print("Exercise 11")

loopFib = [1, 1]
for i in range(2, 20):
     loopFib.append(loopFib[i-1] + loopFib[i-2])

print('The first 20 numbers of the Fibonacci sequence: ', loopFib)

