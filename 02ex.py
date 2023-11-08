#esercizio 1
print("Esercizio 1\n")
x = 5

def f(alist, other=[]):
    other=alist.copy()
    for i in range(x):
        other.append(i)
    return other

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has NOT been changed

#esercizio 2
print("\nEsercizio 2\n")
ans = [x * x for x in range(10) if x % 2 == 1]
print(ans)

#esercizio 3
print("\nEsercizio 3\n")
words=["dog", "sidewalk", "universe", "summer", "peloponneso"]
print(words)
def countif(aword, n=7):
    if len(aword)<n:
        return True
    else:
        return False

short = filter(countif, words)
for x in short:
    print(x)

#esercizio 4
print("\nEsercizio 4\n")
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
def lenkey(chiave):
    return len(chiave)
lunghezze=map(lenkey, lang.keys())
for x in lunghezze:
    print(x)

#esercizio 5
print("\nEsercizio 5\n")
scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
x = lambda a : a[0]
chiavi=[]
for y in scores:
    chiavi.append(x(y))
chiavi.sort()
print(chiavi)

#esercizio 6
print("\nEsercizio 6\n")
def square(x):
    return x**2
def cube(y):
    return y**3
def atsix(z):
    return cube(square(z))
k=2
print(k)
print(square(k))
print(cube(k))
print(atsix(k))

#esercizio 7
print("\nEsercizio 7\n")
def hello(func):
    def say_hello():
        print("Hello World!")
        func()
    return say_hello
@hello    
def test():
    print("Decorators work!")
test()

#esercizio 8
print("\nEsercizio 8\n")
def ric_fib(x):
    if x==0 or x==1:
        return 1
    else:
        return (ric_fib(x-1)+ric_fib(x-2))
def fib20_ric():
    for i in range(21):
        print(ric_fib(i))
fib20_ric()

#esercizio 9
print("\nEsercizio 9\n")
import timeit
def measure_time(func):
    def wrapper(*args, **kwargs):
        Tstart = timeit.default_timer()
        result = func(*args, **kwargs)
        Tend = timeit.default_timer()
        Texec = Tend - Tstart
        print("This function took {:.6f} seconds to run.".format(Texec))
        return result
    return wrapper

@measure_time
def fib20_ric():
    for i in range(21):
        print(ric_fib(i))
@measure_time
def fib20_it():
    fib=[1, 1]
    for i in range(2, 21):
        fib.append(fib[i-1]+fib[i-2])
    print(fib)

fib20_ric()
fib20_it()
'''
The iterative one is way faster (around 500 times) due to the ricursive one wasting time calculating a lot of time the same istances.
'''

#esercizio 10
print("\nEsercizio 10\n")
class polygon:
    lati=()

    def __init__(self, parti):
        if len(parti)>2:
            self.lati = tuple(parti)
        else:
            print("Error! I need at least 3 sides for a polygon.")
    
    def perimeter(self):
        p=0
        for i in range(len(self.lati)):
            p=p+self.lati[i]
        return p

    def getOrderedSides(self, order):
        return sorted(self.lati, reverse=not(order))

prova=(6, 4, 8)
tri = polygon(prova)
print(tri.perimeter())
print(tri.getOrderedSides(False))

#esercizio 11
print("\nEsercizio 11\n")
class rectangle(polygon):

    def __init__(self, sides):
        if len(sides)==2:
            self.lati = (sides[0], sides[1], sides[0], sides[1])
        else:
            print("Error! I need height and width to make a rectangle.")

    def area(self):
        return (self.lati[0]*self.lati[1])

test = (2, 5)
rett = rectangle(test)
print(rett.perimeter())
print(rett.getOrderedSides(False))
print(rett.area())
