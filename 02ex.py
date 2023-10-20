#esercizio 1
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
ans = [x * x for x in range(10) if x % 2 == 1]
print(ans)

#esercizio 3
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
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
def lenkey(chiave):
    return len(chiave)
lunghezze=map(lenkey, lang.keys())
for x in lunghezze:
    print(x)

#esercizio 5
scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
x = lambda a : a[0]
chiavi=[]
for y in scores:
    chiavi.append(x(y))
chiavi.sort()
print(chiavi)

#esercizio 6
