import timeit

#esercizio 1
print('Esericizio 1')
def f(alist):
    x = 5
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist)
print('')

#esercizio 2
print('Esericizo 2')
ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
lista = [x**2 for x in range(10) if x % 2 == 1]
print('Lista data\n', ans)
print('Lista con list comprehension\n', lista)
print('')

#esercizio 3
print('Esericizio 3')
n = 6
words = ['pippo', 'pluto', 'paperino', 'caprino', 'cagnolino', 'lettino', 'fiumicino', 'tapettino', 'scovolino', 'camino']

print('Risultato atteso')

print('Dopo aver chiamato filter: \n', list(filter(lambda words: len(words) < n, words)))
print('')

#esercizio 4
print('Esericizio 4')

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
print(list(map(lambda lang: len(lang), lang)))
print('')

#esercizio 5
print('Esericizio 5')

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
print('Lista ordinata\n', sorted(language_scores, key=lambda x: x[0]))
print('')

#esercizio 6
print('Esericizio 6')

def square(x):
    return x**2
def cube(x):
    return x**3
def power6(x):
    return x*square(x)*cube(x)

print(power6(2))
print('')

#esercizio 7
print('Esericizio 7')

#esercizio 8
print('Esericizio 8')

def rec_fibonacci(n):
    if n > 1:
        return rec_fibonacci(n-1) + rec_fibonacci(n-2)
    return n
print(rec_fibonacci(20))
print('')

#esercizio 9
print('Esericizio 9')
def iter_fibonacci(n):
    fibo = [1, 1]
    for i in range(2, n):
        fibo.append(fibo[i-1] + fibo[i-2])
    return fibo
#imposto numero di esecuzioni a 10000 perché con il valore di default
#rec_fibonacci(n) impegnava il computer per troppo tempo
loop = 10000

result = timeit.timeit(lambda: iter_fibonacci(20), number=loop)
result2 = timeit.timeit(lambda: rec_fibonacci(20), number=loop)
print('Tempo esecuzione fibonacci iterativo: ', result)
print('Tempo esecuzione fibonacci ricorsivo: ', result2)
print('')

#esercizio 10
print('Esericizio 10')

class Polygon:
    dimension = ()

    def __int__(self, components):
        self.dimension = components

    def getDimension(self):
        return len(self.dimension)

    def getLength(self, pos):
        return self.dimension[pos]

    def setLength(self, pos, length):
        self.dimension[pos] = length

    def perimeter(self):
        return sum(self.dimension)

    def getOrderedLength(self):
        return sorted(self.dimension)

print('Test classe Polygon')
tupla = (1, 2, 3, 4, 5)
poly = Polygon(tupla)

print('Perimetro: ', poly.perimeter())
print('lati ordinati: ', poly.getOrderedLength())
print('')

#esercizio 11
print('Esericizio 11')

class Rectangle(Polygon):

    def __int__(self, components):
        if len(components) == 2:
            self.dimension = components
        else:
            print('Bisogna inserire una base e una altezza')


    def area(self):
        return self.dimension[0]*self.dimension[1]


print('Test classe Rectangle')
rect = Rectangle((5,10))
print('Area: ', rect.area())