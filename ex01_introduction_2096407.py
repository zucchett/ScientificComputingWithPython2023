# Riccardo Principe 2096407 Homework1
# EXERCISE 1A
print('Exercise 1A')
for i in range(1,100,1):
    if i%3 == 0 and i%5 == 0:
        print('Hello World')
    elif i%5 == 0:
        print('World')
    elif i%3 == 0:
        print('Hello')
    else:
        print(i)
	
print('\n'+'Exercise 1B')
# EXERCISE 1B
l = []
for i in range(1,101,1):
    if i%3 == 0 and i%5 == 0:
        l.append('Hello World')
    elif i%5 == 0:
        l.append('World')
    elif i%3 == 0:
        l.append('Hello')
    else:
        l.append(i)

#print(l)
for i in range(len(l)):
    if l[i] == 'Hello':
        l[i] = 'Python'
    elif l[i] == 'World':
        l[i] = 'Works'
    elif l[i] == 'Hello World':
        l[i] = 'Python Works'

t = tuple(l)
print(t)
print('-------------------------------' + '\n')

# EXERCISE 2
print('Exercise 2')
#x = input('x: ')
x = 5
#y = input('y: ')
y = 7
x, y = y, x
print("x =", x)
print("y =", y)
print('-------------------------------' + '\n')

# EXERCISE 3
print('Exercise 3')
import math
u = (3,0)
v = (0,4)
d = math.sqrt((v[1]-u[1])**2 + (v[0]-u[0])**2 )
print(d)
print('-------------------------------' + '\n')

# EXERCISE 4
print('Exercise 4')
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

l4 = [0]*26
for i in range(len(s1)):
    n = ord(s1[i])
    if n > 64 and n < 91:
        l4[n-65] += 1
    elif n > 96 and n < 123:
        l4[n-97] += 1

for i in range(len(s2)):
    n = ord(s2[i])
    if n > 64 and n < 91:
        l4[n-65] += 1
    elif n > 96 and n < 123:
        l4[n-97] += 1
print(l4)
print('-------------------------------' + '\n')

# EXERCISE 5
print('Exercise 5')
l5 = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

unique = 0
for i in range(len(l5)):
    if l5.count(l[i]) == 1:
        unique+=1
print(unique)
print('-------------------------------' + '\n')

# EXERCISE 6
print('Exercise 6')
a = input('Insert a: ')
b = input('Insert b: ')
# a = 5
# b = 'stringa'

try:
    n1 = float(a)
    n2 = float(b)
    s = n1 + n2
    print(s)
except:
    print("It is not possible")
print('-------------------------------' + '\n')

# EXERCISE 7A
print('Exercise 7A')
x1 = []
for i in range(0,11,1):
    x1.append(i**3)
print(x1)

# EXERCISE 7B
print('\n'+'Exercise 7B')
cube_numbers = [x**3 for x in range(11)]
print(cube_numbers)
print('-------------------------------' + '\n')

# EXERCISE 8
print('Exercise 8')
l8 = [(a,b,c) for a in range(1,100) for b in range(1,100) for c in range(1,100) if (a**2 + b**2) == c**2]
print(l8)

print('-------------------------------' + '\n')

# EXERCISE 9
print('Exercise 9')
l9 = []
for a9 in range(1,100):
    for b9 in range(1,100):
        for c9 in range(1,100):
            if (a9**2 + b9**2) == c9**2:
                l9.append((a9,b9,c9))
print(l9)
print('-------------------------------' + '\n')

# EXERCISE 10
print('Exercise 10')
size = int(input('Give me the size of the list: '))
# size = 8
l_10 = []
for i in range(size):
    l_10.append(int(input('num: ')))
    
norm = [float(i)/sum(l_10) for i in l_10]
print(norm)
print(sum(norm))
print('-------------------------------' + '\n')

# EXERCISE 11
print('Exercise 11')
a = 0
b = 1
l = []
l.append(a)
l.append(b)
for i in range(20):
    l.append(a+b)
    a,b = b, (a+b)
print(l)