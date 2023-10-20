#author Federico Piloto 2107076

import sys
import math

#esercizio 1
print("Esercizio 1")

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
print("Esercizio 2")

print("x = ", sys.argv[2], "y = ", sys.argv[1])
print("")


#esercizio 3
print("Esercizio 3")

u = (3, 0)
v = (0, 4)

diff1 = v[0] - u[0]
diff2 = v[1] - u[1]
dist = math.sqrt(diff1**2 + diff2**2)

#oppure si può usare direttamente la funzione dist() della librearia math
#dist2 = math.dist(u,v)

print("Distanza euclidiana tra i punti : ", u, 'e ', v, '= ', dist)
print("")


#esercizio 4
print("Esercizio 4")

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
print("Occorrenze lettere prima stringa: ", freq)
print("")

freq = {}
for i in s2:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
        
print("Occorrenze lettere seconda stringa: ", freq)
print("")

#esercizio 5
print("Esercizio 5")

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
print('Lista con i valori da una sola occorrenza\n', listaUnici)
print('')

#esercizio 6
print("Esercizio 6")

a = sys.argv[3]
b = sys.argv[4]
try:
    a = float(a)
    b = float(b)

    print('La somma  di ', a, ' e ', b, ' è: ', a + b)
except:
    print('Impossibile eseguire la somma di ', a, ' e ', b)
print('')

#esercizio 7
print("Esercizio 7")

cubes = []
for i in range(11):
    cubes.append(pow(i, 3))
print('cubi dei numeri con for loop: ', cubes)

cubes = [x**3 for x in range(11)]
print('cubi dei numeri con list comprehensions: ', cubes)
print('')

#esercizio 8
print("Esercizio 8")

list = [(i,j) for i in range(3) for j in range(4)]
print(list)
print('')

#esercizio 9
print("Esercizio 9")
        
'''
list = []
limit = 100
for x in range(1, limit):
    for y in range(1, x):
        if (x-y) % 2 == 1 and math.gcd(x, y) == 1:
            a = x**2 - y**2
            b = 2*x*y
            c = x**2 + y**2
        if c < limit and (a, b, c) not in list:
            list.append((a, b, c))
'''

triples = [(a,b,c) for c in range(100) for a in range(c) for b in range(a) if a**2 + b**2 == c**2 and (a-b) % 2 == 1 and math.gcd(a,b) == 1]

print('Terne pitagoriche con c < 100')
print(triples)

print('')

#esercizio 10
print("Esercizio 10")
#l'algoritmo riceve da riga di comando i valori del vettore

vector = []
for i in range(5, len(sys.argv)):
    vector.append(int(sys.argv[i]))

print('vettore: ', vector)
somma = sum([x**2 for x in vector])
normalized = [x/somma for x in vector]
print('Vettore normalizzato:\n', normalized)
print('')

#esercizio 11
print("Esercizio 11")

fibo = [1, 1]
for i in range(2, 20):
     fibo.append(fibo[i-1] + fibo[i-2])

print('Sequenza Fibonacci dei primi 20 numeri')
print(fibo)


