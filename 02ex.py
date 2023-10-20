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

