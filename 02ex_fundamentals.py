#author Federico Pilotto 2107076

import timeit

#esercizio 1
print('Exercise 1')

def f(alist, n):
    temp = alist.copy()
    for i in range(n):
        temp.append(i)
    return temp

alist = [1, 2, 3]
print('Modify list: ', f(alist, 5))
print('Original list: ', alist)
print('')

#esercizio 2
print('Exercise 2')
ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
lista = [x**2 for x in range(10) if x % 2 == 1]
print('Given list\n', ans)
print('List with list comprehension\n', lista)
print('')

#esercizio 3
print('Exercise 3')
n = 6
words = ['pippo', 'pluto', 'paperino', 'caprino', 'cagnolino', 'lettino', 'fiumicino', 'tapettino', 'camino']

print('Attended result: ',words[0], ' ', words[1])

print('After calling the HOF filter: ', list(filter(lambda words: len(words) < n, words)))
print('')

#esercizio 4
print('Exercise 4')

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
print(list(map(lambda lang: len(lang), lang)))
print('')

#esercizio 5
print('Exercise 5')

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
print('Sorted list\n', sorted(language_scores, key=lambda x: x[0]))
print('')

#esercizio 6
print('Exercise 6')

def square(x):
    return x**2
def cube(x):
    return x**3
def power6(x):
    return x*square(x)*cube(x)

print('2 power to 6: ', power6(2))
print('')

#esercizio 7
print('Exercise 7')

def hello(func):
    def wrapper(x):
        print("Hello World")
        print(func(x))
    return wrapper

@hello
def square(el):
     return el*el

square(5)
print('')

#esercizio 8
print('Exercise 8')
def rec_fib(n):
    if n <= 1:
        return n
    return rec_fib(n-1) + rec_fib(n-2)

fibo = [1,1]
for i in range(3, 21):
    fibo.append(rec_fib(i))
print(fibo)
print('')

#esercizio 9
print('Exercise 9')

def iter_fib(n):
    fibo = [1, 1]
    for i in range(2, n):
        fibo.append(fibo[i-1] + fibo[i-2])
    return fibo

#I set the number of execution to 10000 because the default number (1 milion) requires
#too much time to test rec_fib(n)
loop = 10000

result = timeit.timeit(lambda: iter_fib(20), number=loop)
result2 = timeit.timeit(lambda: rec_fib(20), number=loop)
print('Time for ', loop, ' eecution of iterative fibonacci: ', result)
print('Time for ', loop, ' execution of recursive fibonacci: ', result2)
print("The iterative algorithm is much more efficient then the recursive one! ->", int(result2/result), ' times faster')
print('')


#esercizio 10
print('Exercise 10')

class Polygon:
    lati = ()
    def __init__(self, iLati):
        if len(iLati) >= 3:
            self.lati = iLati
        else:
            print('The polygon must has at least 3 items')

    def getDimension(self):
        return len(self.lati)

    def getLength(self, pos):
        return self.lati[pos]

    def setLength(self, pos, length):
        newLati = []
        for i in range(len(self.lati)):
            newLati.append(self.lati[i])
            if i == pos:
                newLati[i] = length

        self.lati = tuple(newLati)

    def perimeter(self):
        return sum(self.lati)

    def getOrderedLength(self, increasing):
        if increasing:
            return sorted(self.lati)
        else:
            return sorted(self.lati, reverse = True)

print('Test class Polygon')

poly = Polygon((9, 3, 4, 5, 10))

print('Perimeter: ', poly.perimeter())
print('Sorted items: ', poly.getOrderedLength(False))
poly.setLength(2, 7)
print('We modified one item: ', poly.lati)
print('New perimeter: ', poly.perimeter())
print('')

#esercizio 11
print('Exercise 11')

class Rectangle(Polygon):

    def __int__(self, iLati):
        if len(iLati) == 4:
            self.lati = iLati
        else:
            print('You must follow the following format: a b a b')


    def area(self):
        return self.lati[0]*self.lati[1]


rect = Rectangle((5,10, 5, 10))
print('Test classe Rectangle: base: ', rect.lati[0], ' high: ', rect.lati[1])
print('Area: ', rect.area())
print('Perimeter: ', rect.perimeter())