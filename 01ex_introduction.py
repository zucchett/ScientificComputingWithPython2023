import math
# ------------------ EX 1 ------------------
# 1.a)  prints the numbers from 1 to 100
print("1.a)  prints the numbers from 1 to 100, with some values modified\n")
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        # for numbers which are multiples of both three and five prints "HelloWorld"
        print("HelloWorld")
    elif i % 3 == 0:
        # for multiples of three prints "Hello" 
        print("Hello")
    elif i % 5 == 0:
        #for the multiples of five prints "World"
        print("World")
    else:
        print(i)
print("\n")  

# b) puts the result in a tuple
#since tuple are immutable objects, it uses a list and then it converts the list to a tuple
print("1.b)  puts the result in a tuple, substituting Hello with Python, World with Works\n")
output = [] #at the beginning I use a list, since tuple are immutable
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        output.append("HelloWorld")
    elif i % 3 == 0:
        output.append("Hello")
    elif i % 5 == 0:
        output.append("World")
    else:
        output.append(i)
#substitutes Hello with Python, World with Works
output = [x if (x != "Hello" and x != "World") else "Python" if x == "Hello" else "Works" for x in output]
output_tuple = tuple(output)
print(output_tuple)
print("\n")  

# ------------------ EX 2 ------------------
# Swap values without using a temporary variable
print("2)  Swap values without using a temporary variable\n")
[x,y] = (input("First value x: "), input("Second value y: "))
y, x = x, y
print("SWAP...\nx =",x, "\ny =", y)
print("\n") 

# ------------------ EX 3 ------------------
print("3)  euclidean distance\n")
# receives coordinates of 2 points in a 2D space
(ux, uy) = (float(input("x_P1 = ")), float(input("y_P1 = ")))
(vx, vy) = (float(input("x_P2 = ")), float(input("y_P2 = ")))
# computes the euclidean distance
dist = math.sqrt((ux-vx)**2+(uy-vy)**2)
print("Euclidean distance", dist)
print("\n") 

# ------------------ EX 4 ------------------
print("4)  occurances of letters in strings\n")
# strings
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

# set with pair (letter, letter's number of occurances in the string), for each string
s1_occ = {}
s2_occ = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    n_s1 = s1.lower().count(letter)
    n_s2 = s2.lower().count(letter)
    s1_occ.update({letter: n_s1})
    s2_occ.update({letter: n_s2})
    
print("String s1\n", s1_occ)
print("\nString s2\n", s2_occ)
print("\n") 

# ------------------ EX 5 ------------------
print("5)  unique numbers in list\n")
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

#with cycle
unique = []
for i in range(len(l)):
    if(l.count(l[i]) == 1):
        unique.append(l[i])
print(f"Computation with cycle: Unique numbers in the list are %d\n" % len(unique),sorted(unique))
#determines and counts the unique numbers exploiting only the Python data structures
unique_num = [n for n in l if l.count(n) == 1]
print(f"Computation with only Python data structures: Unique numbers in the list are %d\n" % len(unique_num),sorted(unique_num))
print("\n") 

# ------------------ EX 6 ------------------
print("6)  addition between input-variables\n")
# reads from command line 2 variables --> int, float or str
(v1, v2) = input("First variable:"), input("Second variable:")
# it must try to perform the addition of these two variables
# 1. Values are read as str -> they  must be convert into float or int, if it's possible
try:
    s = int(v1) + int(v2) 
    print("sum between 2 integers: ", s)
except:
    # one of them, or both of them, can't be converted into int --> a)they aren't integers b)they're float
    try:
        s = float(v1) + float(v2)
        print("sum between 2 floats: ", s)
    except:
        # if cast into int or float isn't possible -> concatenation between strings
       s = v1 + v2
       print("Addition between strings corresponds to their concatenation: ", s)
print("\n") 

# ------------------ EX 7 ------------------
print("7)  cubes computation\n")
# list of cubes in [0,10]
cubes = []
#a) for loop
for x in range(11):
   cubes.append(math.pow(x,3))
print("By using a for loop:", cubes)

#b) list comprehension -> generates a new list called cubes
cubes = [math.pow(x,3) for x in range(11)]
print("By using a list comprehension:", cubes)
print("\n") 

# ------------------ EX 8 ------------------
print("8) using only a single expression\n")
'''
a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)
'''
#single-line expression
print([(i,j) for i in range(3) for j in range(4)])
print("\n") 

# ------------------ EX 9 ------------------
print("9) Pythagorean triples\n")
# tuple for  Pythagorean triples. NB -> tuples are immutable
t = [(a2,b2,c2) for a2 in range(1,100) for b2 in range(a2,100) for c2 in range(1,100) if c2**2 == a2**2 + b2**2]
#IN ADDITION if I have to remove tuples which are built by multiples of others
l = len(t)
for i in range(0,l):
    j = i + 1
    while j < l:
        if((t[j][0]  /  t[i][0]) == (t[j][1] /  t[i][1])  == (t[j][2] / t[i][2])):
            t.remove(t[j])
            l -= 1
        else: 
            j += 1
print(t)
print("\n") 
# ------------------ EX 10 ------------------
#Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers, 
#and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1).
print("10) Normalization\n")
v = (4,2,5,12,3)
print("v:", v)
v_2 = [t**2 for t in v]
length = math.sqrt(sum(v_2))
v_normalized = [i/length for i in v]
print("v_normalized:", v_normalized)
#checks that the squared sum of all the entries is = 1
vn_2 = [t**2 for t in v_normalized]
length_n = math.sqrt(sum(vn_2))
print("length v_normalized:", length_n)

print("\n") 
# ------------------ EX 11 ------------------
print("11) Fibonacci sequence\n")
fib = [0,1]
i = 2
while(len(fib) < 20+1):
    fib.append(fib[i-2] + fib[i-1])
    i += 1
print("20 values of Fibonacci sequence starting from 0:\n", fib[:20])
print("20 values of Fibonacci sequence starting from 1:\n", fib[1:])
print("\n") 