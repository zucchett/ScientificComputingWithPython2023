import math

#Exercie1

def exercice1_a_b():
    tup = ()
    for i in range (1,101):
        
        if(i%3==0 and i%5==0):
            tup = tup+("PythonWork",)
            print("HelloWorkd")
        elif (i%3== 0):
            tup =tup+("Python",)
            print("Hello")
        elif(i%5==0):
            tup =tup+("World",)
            print("World")
        else : 
            tup =tup+(i,)
            print(i)
    print(tup)


#Exercice2

def exercice2():
    x = input("x = ")
    y = input("y = ")
    return y,x

#Exercice3
def exercice3(X1,X2):
    a,b=X1
    c,d=X2
    return math.sqrt((a-c)**2+(b-d)**2)
    
#Exercice4
def exercice4(S1,S2):

    S1 = S1.upper()
    S2 = S2.upper()
    D1 = {}
    D2 = {}
    for i in range (65,91):

        k = chr(i)
        
        D1[k] = S1.count(k)
        D2[k] = S2.count(k)
    return D1,D2

#Exercice5
def unique(L):
    L1 = []
    for i in L:
        if L.count(i) == 1:
            L1.append(i)
    return L1, len(L1)

def unique2(L):
    S = set(L)
    for i in S:
        L.remove(i) 
    S2 = set(L)
    S3 = S-S2
    return S3, len(S3)

#Exercice6
def tryExcept():
    i = int(input("i: "))
    f = input("f: ")
    s = float(i)
    try:
        print(i+f)
    except:
        print("i and f are incompatible \n")
    try:
        print(i+s)
    except:
        print("i and s are incompatible \n")
    try:
        print(f+s)
    except:
        print("f and s are incompatible \n")

#Exercice7
def  cube():
    return [i**3 for i in range(11)]
#Exercice8
def list_comprehension():
    return [(i,j) for i in range(3) for j in range(4)]

#Exercice9
def pythagore():
    return set([(a,b,c) for c in range(1,100) for b in range(1,c) for a in range(1,b+1) if a**2 + b**2 == c**2])
#Exercice10
def norm(v):
    n=0
    for x in v:
        n += x ** 2

    sq = math.sqrt(n)
    return tuple([x/sq for x in v])
#Exercice11
def fibunacci():
    fib= [0,1]
    for i in range(2,20):
        fib.append(fib[i-1] + fib[i-2])
    return 

