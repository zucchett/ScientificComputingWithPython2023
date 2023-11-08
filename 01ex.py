#esercizio 1
print("Esercizio 1\n")
tot=()
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("HelloWorld")
        tot=tot+("HelloWorld",)
    elif i%3==0:
        print("Hello")
        tot=tot+("Hello",)
    elif i%5==0:
        print("World")
        tot=tot+("World",)
    else:
        print(i)
        tot=tot+(i,)
temp=list(tot)
for j in range(len(temp)):
    if temp[j]=="Hello":
        temp[j]="Python"
    elif temp[j]=="World":
        temp[j]="Works"
tot=tuple(temp)
print("\n", tot)

#esercizio 2
print("\nEsercizio 2\n")
x = input("X value: ")
y = input("Y value: ")
x, y = y, x
print("After swap: X =", x, "Y =", y)

#esercizio 3
print("\nEsercizio 3\n")
import math
u = (0, 3)
v = (-3, 5)
dist = math.sqrt(math.pow(u[0]-v[0], 2)+math.pow(u[1]-v[1], 2))
print("%6.3f" %(dist))

#esercizio 4
print("\nEsercizio 4\n")
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
c=0
for i in range(65, 91):
    for j in range (0, len(s1)):
        if ord(s1.upper()[j])==i:
            c+=1
    if c!=0:
        print(chr(i), "risulta", c, "volte.")
        c=0
c=0
print("")
for i in range(65, 91):
    for j in range (0, len(s2)):
        if ord(s2.upper()[j])==i:
            c+=1
    if c!=0:
        print(chr(i), "risulta", c, "volte.")
        c=0

#esercizio 5
print("\nEsercizio 5\n")
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
rep1=[]
for i in range(0,len(l)):
    if l.count(l[i])==1:
        rep1.append(l[i])
print(len(rep1), "unique elements, which are: ", rep1)

#esercizio 6
print("\nEsercizio 6\n")
x = input("Insert X: ")
y = input("Insert Y: ")
try:
    x=float(x)
    y=float(y)
except:
    print("Almeno uno dei due non e' un float...")
try:
    x=int(x)
    y=int(y)
except:
    print("Almeno uno dei due non e' un int...")
try:
    if not(isinstance(x, str)):
        x=str(x)
    if not(isinstance(y, str)):
        y=str(y)
    print("Somma:", x+y)
except:
    print("Sembra che la somma non sia possibile!")

#esercizio 7
print("\nEsercizio 7\n")
cubi=[]
for x in range(0, 10):
    cubi.append(x**3)
print(cubi)

#esercizio 8
print("\nEsercizio 8\n")
print([(x, y) for x in range(3) for y in range(4)])

#esercizio 9
print("\nEsercizio 9\n")
import math
pyth = []
for a in range(1, 100):
    for b in range(a, 100):
        c = math.sqrt(a**2 + b**2)
        if c.is_integer() and c < 100:
            pyth.append((a, b, int(c)))
print(pyth)

#esercizio 10
print("\nEsercizio 10\n")
import math
vettore = (10, 6, 34, 7, 89)
somma_quad = sum(x**2 for x in vettore)
normalized = tuple(x/math.sqrt(somma_quad) for x in vettore)
print(normalized)

#esercizio 11
print("\nEsercizio 11\n")
fib=[1, 1]
for i in range(2, 21):
    fib.append(fib[i-1]+fib[i-2])
print(fib)
