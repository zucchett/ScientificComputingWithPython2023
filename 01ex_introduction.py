import math as m

## ESERCIZIO 1
numeri = []
for x in range(1,100):
    if x % 5 == 0 and x % 3 == 0:
        numeri.append("HelloWorld")
    elif x % 3 == 0 :
        numeri.append("Hello")
    elif x % 5 == 0 :
        numeri.append("World")    
    else:
        numeri.append(x)


for i in range(len(numeri)):
    if numeri[i] == "Hello":
        numeri[i] = "Python"
    elif numeri[i] == "World":
        numeri[i] = "Works"
numeri_tuple = tuple(numeri)

print("Soluzioni del primo esercizio")        
print(f"la soluzione dell'punto a) è: {numeri}")
print(f"la soluzione dell'punto b) è: {numeri_tuple}")

print(" \n")
## ESERCIZIO 2
print("Soluzione del secondo esercizio") 
x = input("write an input: ")
x1 = input("write another input: ")
lista = [x,x1]

x = lista[1]
x1 = lista[0]
print("i valori invertiti sono: " ,x,x1 )

print(" \n")
## ESERCIZIO 3
u = (3,0)
v = (0,4)

distance = m.sqrt( pow((u[0] + v[0]), 2) + pow((u[1] + v[1]),2))

print("Soluzioni del terzo esercizio")  
print(f"I vettori sono : {u} e {v} e la distanza è: {distance}")


print(" \n")
## ESERCIZIO 4
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

s1 = s1.lower()
s2 = s2.lower()

diz = {}
i = 0

j = 0
diz2 = {}

for i in range(0, len(s1)):
    if s1[i] == ' ':
        continue
    
    elif  s1[i] not in diz:
        diz[s1[i]] = 1
        
    elif s1[i] in diz:
        diz[s1[i]]+=1
        

for j in range(0, len(s2)):
    if s2[j] == ' ':
        continue
    
    elif  s2[j] not in diz2:
        diz2[s2[j]] = 1
        
    elif s2[j] in diz2:
        diz2[s2[j]]+=1

print("Soluzioni del quarto esercizio") 
print("Ripetizioni nella prima stringa")
print(diz)      
print ( "Ripetizioni nella seconda stringa")       
print(diz2)


print(" \n")
## ESERCIZIO 5
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

i = 0
j = 0 
be = False
ripetuti =[]
for i in range(0 , len(l)-1):
    if i == len(l)-1:
        break
    for j in range(i+1, len(l)):
        if l[i] == l[j]:
            ripetuti.append(l[j])

#così ho trovato quelli che si ripetono
    
i = 0
j = 0 
while i < len(l):
    for j in range(0, len(ripetuti)):
        if l[i] == ripetuti[j]:
            l.remove(l[i])
    i+=1
print("Soluzione del quinto esercizio")     
print("i numeri non ripetuti mai sono: ", l, " e sono ", len(l))


print(" \n")
## ESERCIZIO 6
print("Soluzione del sesto esercizio")
x = input("write an input: ")
x1 = input("write another input: ")
try:
    somma = float(x) + float(x1)
except:
    somma = x +x1  
print("la somma tra le due variabili è: ", somma)


print(" \n")
## ESERCIZIO 7
cubi_cicli_for = []
for x in range(11):
    cubi_cicli_for.append(x**3)


print("Soluzione del settimo esercizio")
print(f"Lista dei cubi con il ciclo for: {cubi_cicli_for}")

cubi_list_comprehension = [x**3 for x in range(11)]
print(f"Lista dei cubi con la list comprehension: {cubi_list_comprehension}")


print(" \n")
## ESERCIZIO 8
lista = [(i,j) for i in range(3) for j in range(4)]
print("Soluzione dell'ottavo esercizio")
print("La lista è: ", lista)


print(" \n")
## ESERCIZIO 9

terna = [[a,b,c] for a in range (1, 100) for b in range (a,100)
         for c in range (b,100) if a**2 + b**2 == c**2]

terne_non_duplicate = [tuple(triple) for triple in terna]
terne_non_duplicate = sorted(terne_non_duplicate)

# terne primitive 


terne_primitive =[]

for t1 in terne_non_duplicate:
    is_primitiva = False
    MCD = m.gcd(t1[0],t1[1],t1[2])
    if MCD == 1:
        is_primitiva = True

    if is_primitiva:
        terne_primitive.append(t1)



print("Soluzione del nono esercizio")
print(f" Le terne sono: {len(terne_primitive)} e sono {terne_primitive}")


print(" \n")
## ESERCIZIO 10
print("Soluzione del decimo esercizio")

vettore = (6,3,4)
somma = 0 
for i in range(len(vettore)):
    somma += pow(vettore[i],2)    

norma = m.sqrt(somma)

somma1 = 0 
for i in range(len(vettore)):
    somma1 += pow(vettore[i]/norma,2)

vettore_normalizzato = m.sqrt(somma1)

print(f"Il vettore è: {vettore} e la sua norma è: {norma}")
print("Il vettore normalizzato è: ",vettore_normalizzato)
    


print(" \n")
## ESERCIZIO 11
print("Soluzione dell'undicesimo esercizio")

fibonacci = [0, 1]

i = 2
while i < 20:
    next_num = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(next_num)
    i += 1

print("La sequenza di Fibonacci dei primi 20 numeri è: ", fibonacci)



