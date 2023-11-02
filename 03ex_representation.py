import math
import timeit

print ("\n")
## ESERCIZIO 1
print("La soluzione del primo esercizio")
def converti_numero(numero,type1):
    if type1 == hex:
        numero = hex(numero)
    elif type1 == int:
        numero = int(numero)
    elif type1 == bin:
        numero = bin(numero)
    return numero
        
       
a = converti_numero(23,bin)
print("Per esempio, il binario del numero 23 è: ", a)



print ("\n")
## ESERCIZIO 2
print("La soluzione del secondo esercizio")
def converti(stringa):
    
    segno = int(stringa[0])
    
    esponente_bias = int(stringa[1:9],2)
    
    esponente_nonbias = esponente_bias - 127
    
    mantissa = stringa[10:]
     
    potenza = -1
    mantissa_int = 0
    
    for i in mantissa:

        mantissa_int += (int(i) * pow(2, potenza))
        potenza -= 1      
    
    
    mantissa_int = mantissa_int + 1

    
    numero = pow(-1, segno) * mantissa_int * pow(2, esponente_nonbias)
    
    return numero
    
  
numero = converti('11000000000100000000000000000000')

print("Il numero float che si riferisce alla stringa è: ", numero)



print ("\n")
## ESERCIZIO 3
print("La soluzione del terzo esercizio")
underflow = 1.0
overflow= 1.0


while underflow / 2 != 0.0:
    underflow /= 2


while overflow * 2 != float('inf'):
    overflow *= 2

print(f"Il limite per l'underflow è : {underflow}")
print(f"Il limite per l'overflow: {overflow}")





print ("\n")
## ESERCIZIO 4
print("La soluzione del quarto esercizio")
precisione = 1.0
delta = 1.0

while (1.0 + delta) != 1.0:
    machine_precision = delta
    delta /= 2.0

print(f"La precisione del computer è di: {machine_precision}")


print ("\n")
## ESERCIZIO 5
print("La soluzione del quinto esercizio")

def quadratic(a,b,c):
    discriminante = b**2 - 4 * a * c
    if discriminante < 0:
        print("Non ci sono soluzioni reali")
    else:
    
        x1 = (-1 * b + math.sqrt(discriminante))/ (2 * a)
          
        x2 = (-1 * b - math.sqrt(discriminante)) / (2 * a)
    
    print("Formula Standard - x1:", x1)
    print("Formula Standard - x2:", x2)
    
    return x1,x2

def quadratic2(a,b,c):
    discriminante = b**2 - 4 * a * c
    if discriminante < 0:
        print("Non ci sono soluzioni reali")
    else:

        
        x1 = (-b + math.sqrt(discriminante))* ( -b - math.sqrt(discriminante) )/ ((2 * a)*( -b - math.sqrt(discriminante) ))
        x2 = (-b - math.sqrt(discriminante))* ( -b + math.sqrt(discriminante) )/ ((2 * a)*( -b + math.sqrt(discriminante) ))
        
    
    print("Formula Accurata - x1:", x1)
    print("Formula Accurata - x2:", x2)
    
    return x1,x2

def quadratic3(a,b,c):
    discriminante = b**2 - 4 * a * c
    if discriminante < 0:
        print("Non ci sono soluzioni reali")
    else:
        x1 = (-1 * b + math.sqrt(discriminante))/ (2 * a)
          
        x2 = (-1 * b - math.sqrt(discriminante)) / (2 * a)

        num1 = x1.as_integer_ratio()[0]
        den1 = x1.as_integer_ratio()[1]
        
        num2 = x2.as_integer_ratio()[0]
        den2 = x2.as_integer_ratio()[1]

        x1 = num1/den1
        x2 = num2/den2

    print("Formula più Accurata - x1:", x1)
    print("Formula più Accurata - x2:", x2)
    
    return x1,x2

quadratic(0.001,1000,0.001)
                                                                                              
quadratic2(0.001,1000,0.001)

quadratic3(0.001,1000,0.001)


print("""
La risposta al quesito b) é: La formula accurata applica essenzialmente lo stesso calcolo,
ma riorganizza i termini per migliorare la stabilità numerica e siccome sono numeri molto piccoli python inizia ad arrotondarli
ed è per questo che esce un numero leggermente diverso.
""")


print ("\n")
## ESERCIZIO 6
print("La soluzione del sesto esercizio")

def derivat(f, a, h):
    numerical_derivative = (f(a + h) - f(a)) / h
    return numerical_derivative


def f(x):
    return x*(x-1)


a = 1.0  
h = pow(10,-2)
h1 = pow(10,-4)
h2 = pow(10,-6)
h3 = pow(10,-8)
h4 = pow(10,-10)
h5 = pow(10,-12)
h6 = pow(10,-14)

derivata = derivat(f, a, h)
derivata1 = derivat(f, a, h1)
derivata2 = derivat(f, a, h2)
derivata3 = derivat(f, a, h3)
derivata4 = derivat(f, a, h4)
derivata5 = derivat(f, a, h5)
derivata6 = derivat(f, a, h6)




print(f"La derivata di a = {a} con h = {h}: {derivata}")
print(f"La derivata di a = {a} con h = {h1}: {derivata1}")
print(f"La derivata di a = {a} con h = {h2}: {derivata2}")
print(f"La derivata di a = {a} con h = {h3}: {derivata3}")
print(f"La derivata di a = {a} con h = {h4}: {derivata4}")
print(f"La derivata di a = {a} con h = {h5}: {derivata5}")
print(f"La derivata di a = {a} con h = {h6}: {derivata6}")

print("""
La risposta al quesito a) è: Il motivo per cui i risultati analitici (1,00) e numerici (1,01) non concordano perfettamente è dovuto principalmente alla dimensione finita del passo (ℎ) utilizzato nell'approssimazione numerica. Man mano che 
h si riduce, il risultato numerico si avvicina alla derivata vera, ma non sarà esatto. Inoltre, gli errori di precisione numerica e di arrotondamento possono contribuire alle differenze tra i due valori.

La risposta al quesito b)è: si osserva che man mano che h diventa più piccolo, l'accuratezza del calcolo della derivata numerica migliora e l'errore assoluto tra la derivata analitica e quella numerica diventa più piccolo.
In altre parole, l'accuratezza cresce con h in modo tale che un h più piccolo produca un risultato più accurato.

""")
print ("\n")
## ESERCIZIO 7
print("La soluzione del settimo esercizio")

def semicerchio(x):
    # Function defining the semicircle
    return math.sqrt(1 - pow(x,2))

def riemann_integrale(a, b, n):
    integrale = 0
    fetta = (b - a) / n
    h = 2 / n
    for i in range(n):
        xi = a + i * fetta
        integrale += h * semicerchio(xi)
    return integrale


n = 100
risultato = riemann_integrale(-1, 1, n)
valore_vero = math.pi/2



print(f"Risulatato del computer: {risultato}")
print(f"Vero valore dell'integrale: {valore_vero}")

print("""
la risposta al quesito a) è: I due risultati sono simili ma non identici, perché la precisione dell'approssimazione dipende dalla scelta di N. 
Aumentando il valore di N, la somma di Riemann diventerà un'approssimazione più precisa del valore dell'integrale.
""")
# 
max_time = 1
tempo_esecuzione = timeit.timeit(lambda: riemann_integrale(0, 1, n), number=1)

while tempo_esecuzione < max_time:
    n *= 2
    tempo_esecuzione = timeit.timeit(lambda: riemann_integrale(0, 1, n), number=1)

# calcolo il guadagno se eseguo il programma per un minuto
n_minute = 1
m = 100
tempo_esecuzione1 = timeit.timeit(lambda: riemann_integrale(0, 1, m), number=1)
while tempo_esecuzione1 < 60:
    m *= 10000
    tempo_esecuzione1 = timeit.timeit(lambda: riemann_integrale(0, 1, m), number=1)



print(f"Numero di fette (n) per runnare in meno di 1 secondo: {n}")

print(f"N raggiunte dopo un minuto:  {m}")



