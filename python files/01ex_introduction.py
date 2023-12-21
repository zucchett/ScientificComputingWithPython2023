# LECOCQ Arthur
from math import sqrt

def ex1a():
    for i in range(1,101):
        if(i//3*3==i and i//5*5==i):
            print(str(i)+" HelloWorld")
        else:
            if(i//3*3==i):
                print(str(i)+" Hello")
            elif(i//5*5==i):
                print(str(i)+" Wolrd")
            else:
                print(str(i))

def ex1b():
    tab=[]
    for i in range(1,101):
        if(i//3*3==i and i//5*5==i):
            tab.append(str(i)+" PythonWorks")
        else:
            if(i//3*3==i):
                tab.append(str(i)+" Python")
            elif(i//5*5==i):
                tab.append(str(i)+" Works")
            else:
                tab.append(str(i))
    for i in tab:
        print(i)
        
def ex2(object1, object2):
    print(object1)
    print(object2)

    object1,object2 = object2,object1

    print(object1)
    print(object2)

def ex3(point1,point2):
    if(len(point1)!=2 or len(point2)!=2):
        return 0
    else:
        return(sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2))
    
def ex4(string):
    tab=[[],[]]
    for letter in string:
        if(letter not in tab[0]):
            tab[0].append(letter)
            tab[1].append(1)
        else:
            tab[1][tab[0].index(letter)]+=1

    result=[]
    for i in range(len(tab[0])):
        result.append([tab[0][i],tab[1][i]])

    return(result)

def ex5(list):
    unique=[]
    for nb in list:
        if(nb not in unique):
            unique.append(nb)
        else:
            unique.remove(nb)
    return(unique)

def ex6(var1,var2):
    try:
        var1+var2
    except TypeError:
        print("Wrong types")
    else:
        print(var1+var2)

def ex7():
    list1 = [x**3 for x in range(10)]
    list2 = []
    for x in range(10):
        list2.append(x**3)
    print(list1)
    print(list2)

def ex8():
    list=[(i,j) for i in range(3) for j in range(4)]
    print(list)

def ex9():
    triples=[[x,y,z]  for z in range(5,101)  for y in range(4,z) for x in range(3,y) if(x**2+y**2==z**2 and x<y and y<z)]
    return(triples)

def ex10(vector):
    norm=0
    for i in vector:
        norm+=i**2
    norm=sqrt(norm)

    return([i/norm for i in vector])

def ex11(nlimit):
    fibo=[0,1]
    while(len(fibo)<=nlimit):
        fibo.append(fibo[-1]+fibo[-2])
    return(fibo)

if __name__ == '__main__':
    l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
    85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
    1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
    45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

    s1 = "Write a program that prints the numbers from 1 to 100. \
    But for multiples of three print Hello instead of the number and for the multiples of five print World. \
    For numbers which are multiples of both three and five print HelloWorld."

    s2 = "The quick brown fox jumps over the lazy dog"

    ex1a()
    ex1b()
    ex2(11,"pouet")
    print()
    ex2(10,11)
    print(ex3((3,0),(0,4)))
    print(ex4(s1))
    print()
    print(ex4(s2))
    print(ex5(l))
    ex6(1,2)
    print()
    ex6(1,"t")
    print()
    ex6([1],"t")
    print()
    ex6(1,1.0)
    ex7()
    ex8()
    print(ex9())
    print(ex10([1,2,3]))
    print(ex10([4,9,16,25]))
    print(ex11(20))