import math

# Exercise 1
# a
def exercise1():
    result = ["HelloWorld" if x % 3 == 0 and x % 5 == 0
              else "Hello" if x % 3 == 0
              else "World" if x % 5 == 0 
              else x for x in range(1,101)]
    
    print(result)

    # b TODO
    tuple_result = tuple(result)
    print(tuple_result)
    

# Exercise 2
def exercise2():
    x = input("Set the value of x: ")
    y = input("Set the value of y: ")
    x, y = y, x

    print("x = ",x)
    print("y = ",y)

# Exercise 3
def exercise3():
    u = (3,0)
    v = (0,4)
    
    print(math.sqrt((u[0]-v[0])**2 + (u[1]-v[1])**2))

# Exercise 4
def exercise4():
    s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
    s2 = "The quick brown fox jumps over the lazy dog"

    s1 = s1.lower()
    s2 = s2.lower()

    for char in s1:
        print(char, " ", s1.count(char))

    for char in s2:
        print(char, " ", s2.count(char))


#exercise1()
#exercise2()
#exercise3()
#exercise4()
