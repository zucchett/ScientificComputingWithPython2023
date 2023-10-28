#author Federico Pilotto 2107076

import sys
import math

#esercizio 1
print("Excercise 1")

i = 1
lista = []
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print("HelloWorld")
        lista.append("PythonWorks")
    elif i % 3 == 0:
        print("Hello")
        lista.append("Python")
    elif i % 5 == 0:
        print("World")
        lista.append("Works")
    else:
        print(i)
        lista.append(i)
    i += 1
tupla = tuple(lista)
print(tupla)
print("")

#esercizio 2
print("Exercise 2")

print("x = ", sys.argv[2], "y = ", sys.argv[1])
print("")


#esercizio 3
print("Exercise 3")

u = (3, 0)
v = (0, 4)

diff1 = v[0] - u[0]
diff2 = v[1] - u[1]
dist = math.sqrt(diff1**2 + diff2**2)

#you can use directly the function dist() of the math library
#dist2 = math.dist(u,v)

print("Euclidean distance between the two point : ", u, 'and ', v, '= ', dist)
print("")


#esercizio 4
print("Exercise 4")

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

s1 = s1.lower()
s2 = s2.lower()

freq = {}
for i in s1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("Letters frequency of the first string: ", freq)
print("")

freq = {}
for i in s2:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
        
print("Letters frequency of the secondo string: ", freq)
print("")

#esercizio 5
print("Exercise 5")

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
 
freq = {}
listaUnici = []

for i in l:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for i in freq:
    if freq[i] == 1:
        listaUnici.append(i)
print('List of item with frequence = 1\n', listaUnici)
print('')

#esercizio 6
print("Exercise 6")

a = sys.argv[3]
b = sys.argv[4]
try:
    a = float(a)
    b = float(b)

    print('The sum of ', a, ' and ', b, ' is: ', a + b)
except:
    print('Impossible to do the sum of these items ', a, ' and ', b)
print('')

#esercizio 7
print("Exercise 7")

cubes = []
for i in range(11):
    cubes.append(pow(i, 3))
print('Cubes done with for cycle: ', cubes)

cubes = [x**3 for x in range(11)]
print('Cubes done with list comprehensions: ', cubes)
print('')

#esercizio 8
print("Exercise 8")

list = [(i,j) for i in range(3) for j in range(4)]
print(list)
print('')

#esercizio 9
print("Exercise 9")

triples = [(a,b,c) for c in range(100) for a in range(c) for b in range(a) if a**2 + b**2 == c**2 and (a-b) % 2 == 1 and math.gcd(a,b) == 1]

print('Pythagorean triple with c < 100')
print(triples)

print('')

#esercizio 10
print("Exercise 10")

vector = [1, 23, 4, 5, 12]
for i in range(5, len(sys.argv)):
    vector.append(int(sys.argv[i]))

print('Vector: ', vector)
somma = sum([x**2 for x in vector])
normalized = [x/somma for x in vector]
print('Normalized Vector:', normalized)
print('')

#esercizio 11
print("Exercise 11")

fibo = [1, 1]
for i in range(2, 20):
     fibo.append(fibo[i-1] + fibo[i-2])

print('Fibonacci sequence of the first 20 numbers')
print(fibo)




