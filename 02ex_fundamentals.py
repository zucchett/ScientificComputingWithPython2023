import copy
import timeit

print ("\n")
## ESERCIZIO 1
print("La soluzione del primo esercizio")
x = 5

def f(alist):    
    x = 5
    l= copy.deepcopy(alist)
    for i in range(x):
        l.append(i)
    return l

alist = [1, 2, 3]
ans = f(alist)
print("La lista iniziale è : ", ans)
print("La nuovalista è: ", alist)

print ("\n")
## ESERCIZIO 2
print("La soluzione del secondo esercizio")
ans = [pow(x,2) for x in range(10)  if x %2 ==1]
print("La lista scritta con list comprehension è :", ans)

print ("\n")
## ESERCIZIO 3
print("La soluzione del terzo esercizio")
lista = ["ciao","lunapiena", "p","s", "esami2023"]
print("La lista di parole è: ", lista)
n = int(input("inserisci un numero: "))

def parole_piccole(parola):
    if len(parola) < n:           
        return parola
ans = list(filter(parole_piccole, lista))
print("La lista con le parole più corte del numero che hai dato è: ", ans)



print ("\n")
## ESERCIZIO 4
print("La soluzione del quarto esercizio")
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def conta_lunghezza(parola):
    return len(parola)

lunghezza = list(map(conta_lunghezza, lang.keys()))

print("La lunghezza delle chievi del dizionario è: ", lunghezza)

print ("\n")
## ESERCIZIO 5
print("La soluzione del quinto esercizio")
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key = lambda x : x[0])
print("La lista ordinata è: ", language_scores)


print ("\n")
## ESERCIZIO 6
print("La soluzione del sesto esercizio")

numero = 3

def f1(x):
    return pow(x,2)

def f2(x):
    return pow(x,3)

def f3(x):
    return f1(f2(x))

print(f"Il numero che ho scelto è {numero} e la sua potenza alla sesta è {f3(numero)}")

print ("\n")
## ESERCIZIO 7
print("La soluzione del settimo esercizio")
def hello(func):
    def wrapper(x):
        print("Hello World")
        func(x)
    return wrapper


@hello
def square(x):
    return x*x

square(3)



print ("\n")
## ESERCIZIO 8
print("La soluzione dell'ottavo esercizio")
def fibonacci2(x):    
    if x > 1:
        return fibonacci2(x - 1) + fibonacci2(x - 2)
    return x
        
print("la sequenza di fibonacci dei primi 20 numeri è: ")
for i in range(0,20):
    print(fibonacci2(i))




print ("\n")
## ESERCIZIO 9
print("La soluzione del nono esercizio")


codice1 = """
def Loopfibonacci(x):
    i = 2
    fibonacci = [0, 1]
    while i <  x:        
        next_num = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(next_num)
        i += 1
    return fibonacci
"""
 

tempo_trascorso1 = timeit.timeit ( codice1, setup="pass", number=1000)

codice2 ="""
def Recursivefibonacci(x):    
    if x > 1:
        return Recursivefibonacci(x - 1) + Recursivefibonacci(x - 2)
    return x

"""
tempo_trascorso2 = timeit.timeit ( codice2, setup="pass", number=1000)

print("Il tempo usando il ciclo while è: ", tempo_trascorso1, "secondi")  
print("Il tempo usando la funzione ricorsiva è: ", tempo_trascorso2, "secondi")
print("""
Le funzioni ricorsive possono richiedere più tempo dei loop in Python a causa dell'overhead associato alle chiamate ricorsive e alla gestione dello stack di chiamate.
associato alle chiamate ricorsive e alla gestione dello stack di chiamate,
rendendo i loop spesso più efficienti in termini di tempo di esecuzione.

""")
print ("\n")
## ESERCIZIO 10
print("La soluzione del decimo esercizio")
# Ho presupposto che l'utente scriva i lati in ordine 
# per esempio scrivere (3,4,5) singifica dire che il primo lato vale 3,
#il secondo 4 e il terzo 5


class polygon:
    def __init__(self, lati):
        self.x = lati
        
        if len(self.x)<3 :
            raise ValueError("I lati devono essere minimo 3.  Try again...")
        
    def get_length(self):
        return self.x
    
    def set_length(self,lato, valore):
        temp = list (self.x)
        temp[lato-1] = valore
        self.x = tuple(temp)
        return self.x
            
    def perimetro(self):
        somma = sum(list(self.x))
        return somma
    
    def getOrderedSides(self, increasing = True):
        temp = list(self.x)
        temp.sort(reverse = increasing)
        self.x = tuple(temp)
        return self.x
        #true = decrescente
        #false = crescente

lati = (9,9,7)
triangolo = polygon(lati)

print("Le lunghezze dei lati sono: ", triangolo.get_length())

print("Cambio la lunghezza del secondo lato con un altro valore ", triangolo.set_length(2,8))
        
print("il perimetro del poligono è: " , triangolo.perimetro())

print(triangolo.getOrderedSides(False))


print ("\n")
## ESERCIZIO 11
print("La soluzione dell'undicesimo esercizio")
class rectangle(polygon):
    
    def __init__(self, lati):
        self.x = lati
        if len(self.x) != 4 and self.x[0] != self.x [2]:
            raise ValueError("non è un rettangolo.  Try again...")
        
    def area(self):
        area = self.x[0]*self.x[1]
        return area
    

lati = (2,3,2,3)   
rettangolo = rectangle(lati)
print("I lati del rettangolo sono: ", lati , " e l'area del rettangolo è: ", rettangolo.area())





