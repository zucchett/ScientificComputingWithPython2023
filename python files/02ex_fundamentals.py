#LECOCQ Arthur
from time import time

def ex1(list):
    for i in range(5):
        list.append(i)
    return(list)

def ex2():
    return([x*x for x in range(10) if x%2 == 1])

def ex3(words,n):
    return(list(filter(lambda word: (len(word)<=n),words)))

def ex4(dico):
    return(list(map(lambda x:len(x),dico)))

def ex5(list):
    list.sort(key=lambda x:x[0])
    return list

def ex6_1(nb):
    return(nb**2)

def ex6_2(nb):
    return(nb**3)

def ex6(nb):
    return(ex6_2(ex6_1(nb)))

def ex7_decorator(function):
    def wrapper():
        print("Hello World")
        function()
    return(wrapper)

@ex7_decorator
def ex7():
    print("Blop")

def ex8(nb):
    if(nb<=1):
        return(nb)
    else:
        return(ex8(nb-1)+ex8(nb-2))
    
def ex9_1(nb):
    fibo=[0,1]
    while(len(fibo)<=nb):
        fibo.append(fibo[-1]+fibo[-2])
    return(fibo[-1])

def ex9_2(nb):
    fibo=[0,1]
    for i in range(2,nb+1):
        fibo.append(fibo[i-1]+fibo[i-2])
    return(fibo[-1])

def ex9(nb):
    a=time()
    ex8(nb)
    b=time()
    print(str(b-a)+"s")

    a=time()
    ex9_1(nb)
    b=time()
    print(str(b-a)+"s")

    a=time()
    ex9_2(nb)
    b=time()
    print(str(b-a)+"s")

class polygon:
    sides = ()

    def __init__(self,tuple):
        if(len(tuple)<3):
            return(ValueError)
        self.sides = tuple

    def getSides(self):
        return(self.sides)

    def getPerimeter(self):
        return(sum(self.sides))
    
    def setSides(self,tuples):
        if(len(tuples)<3):
            return(ValueError)
        self.sides=tuples

    def setValueSide(self,index,value):
        if(index>len(self.sides)):
            return(ValueError)
        temp = list(self.sides)
        temp[index-1]=value
        self.sides = tuple(temp)

    def getOrderedSides(self,increasing = True):
        orderedSides = sorted(self.sides,reverse=not(increasing))
        return(tuple(orderedSides))
    
class rectangle(polygon):

    def __init__(self,tuple):
        if(len(tuple)!=2):
            return(ValueError)
        self.sides=tuple

    def setSides(self,tuples):
        if(len(tuples)!=2):
            return(ValueError)
        self.sides=tuples

    def getArea(self):
        temp = list(self.sides)
        return(temp[0]*temp[1])

    def getPerimeter(self):
        return(sum(self.sides)*2)

def ex10(tuple):
    object = polygon(tuple)
    print(object.getSides())
    print(object.getPerimeter())
    object.setValueSide(3,10)
    print(object.getPerimeter())
    print(object.getOrderedSides(True))
    print(object.getOrderedSides(False))

def ex11(tuple):
    object = rectangle(tuple)
    print(object.getArea())
    print(object.getPerimeter())
    print(object.getSides())

if __name__ == '__main__':
    alist = [1, 2, 3]
    words=["abc","abcd","abcde","xyz","xyzt","123","1234","12345"]
    lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
    language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
    print(ex1(alist))
    print(ex2())
    print(ex3(words,3))
    print(ex3(words,4))
    print(ex4(lang))
    print(ex5(language_scores))
    print(ex6(2))
    ex7()
    print(ex8(20))
    print(ex9_1(20))
    print(ex9_2(20))
    ex9(20)
    ex10((1,2,3,5,3))
    ex11((5,4))