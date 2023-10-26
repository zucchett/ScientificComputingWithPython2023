'''

Exercise 1 
\. **The HelloWorld replacement**

a) Write a program that:
- prints the numbers from 1 to 100
- but for multiples of three print "`Hello`" instead of the number and for the multiples of five print "`World`"
- for numbers which are multiples of both three and five print "`HelloWorld`".

b) Put the result in a tuple and substitute "`Hello`" with "`Python`" and "`World`" with "`Works`".

'''
print("\n### Exercise 1")
hundred_num = [x for x in range(1,101)]
print("-- Prints the numbers from 1 to 100\n\n",hundred_num) 

changed_hundred_num = []
for x in hundred_num:
	if (x %3 ==0 and x%5==0):
		changed_hundred_num.append("HelloWorld")
	elif (x % 3==0):
		changed_hundred_num.append("Hello") 
	elif (x %5==0):
		changed_hundred_num.append("World")
	else:
		changed_hundred_num.append(x)

print("\n-- 3->'Hello', 5->'World', 15->'HelloWorld'\n\n",changed_hundred_num)  
iter = 0
for x in changed_hundred_num:
	if (x == "Hello"):
		changed_hundred_num[iter] = "Python"
	elif (x == "World"):
		changed_hundred_num[iter] = "Works"
	iter +=1
	
tuple_num = tuple(changed_hundred_num)
print("\n-- Hello->Python, World->Works\n\n",tuple_num)
# tuple_num[1] = 1 we cannot change tuple values, therefore  first changed the value and converted to tuple

'''
#Exercise 2

2\. **The swap**

Write a program that swaps the values of two input variables `x` and `y` from command line (whatever the type).

Try to do that without using a temporary variable, exploiting the Python syntax.
'''
print("\n### Exercise 2")
x , y = 10,23

print("x = ", x, ", y = ", y)

x,y = y,x

print("x = ", x, ", y = ", y)


'''


#Exercise 3
**Computing the distance**

Write a program that calculates and prints the euclidean distance between two given points $u$ and $v$ in a 2D space, where $u$ and $v$ are both 2-tuples $(x,y)$.

Example: if $u=(3,0)$ and $v=(0,4)$, the function should return $5$.

*Hint:* in order to compute the square root, import the `math` library with `import math` and use `math.sqrt()`.
'''
print("\n### Exercise 3")
import math 
u=(3,0)
v=(0,4)

x = (v[0] - u[0], v[1] - u[1])
print("u =",u,"\nv =", v)

distance = math.sqrt(x[0]**2 + x[1]**2)

print("Distance:",distance)

'''
#Exercise 4
4\. **Counting letters**

Write a program that calculates the number of times each character occurs in a given string. Ignore differences in capitalization.

The test strings are:

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

'''
print("\n### Exercise 4")
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"


s1_lower = s1.lower()
s2_lower = s2.lower()

out_s1 = {x : s1_lower.count(x) for x in set(s1_lower )} 
out_s2 = {x : s2_lower.count(x) for x in set(s2_lower )} 

print(out_s1)
print(out_s2)


'''

#Exercise 5 
5\. **Isolating the unique**

Write a program that determines and counts the unique numbers (numbers with only one occurrence) in the list:

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

Do the same exploiting only the Python data structures.

'''
print("\n### Exercise 5")
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

count_l = {x : l.count(x) for x in set(l )} 
unique_l = []
for key,value in count_l.items():
	
	if value ==1:
		unique_l.append(key)
print(unique_l)
print("Number of unique elements:",len(unique_l))

'''

#Exercise 6
6\. **Casting**

Write a program that:
* reads from command line two variables, that can be either `int`, `float`, or `str`.
* use the `try`/`except` expressions to perform the addition of these two variables, only if possible
* print the result without making the code crash for all the `int`/`float`/`str` input combinations.
'''
print("\n### Exercise 6")
x = "Py"
y = 5.3
print("x =", x, " y = ", y)
error_list = []
try:
    c = int(x) + int(y)
   
    print(c)
except:
    error= ["Operation failed: x is",type(x), " and y is",type(y)]
    error_list.append(error)
try:
    c = float(x) + float(y)
   
    print(c)
except:
    error= ["Operation failed: x is",type(x), " and y is",type(y)]
    error_list.append(error)

try:
    c = x + y
   
    print(c)
except:
    error= ["Operation failed: x is",type(x), " and y is",type(y)]
    error_list.append(error)
error_lists = []
[error_lists.append(n) for n in error_list if n not in error_lists]
string = ''.join(map(str,error_lists))
print(string)



'''
#Exercise 7
7\. **Cubes**

Create a list of the cubes of *x* for *x* in *[0, 10]* using:

a) a for loop

b) a list comprehension
'''
print("\n### Exercise 7")
cube_loop = []
for i in range(0,10,1):
	cube_loop.append(pow(i,3))
    
cube_lst_compr = [pow(x,3) for x in range(10)]

print("a for loop:          ",cube_loop)
print("a list comprehension:",cube_lst_compr)


'''
#Exercise 8
8\. **List comprehension**

Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.

a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

'''
print("\n### Exercise 8")
a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print("A basic 'a' = ", a)

list_comp_a = [(x, y) for x in range(3) for y in range(4)]
print("L.compr 'a' = ",list_comp_a)

'''

#Exercise 9

9. Nested list comprehension

A Pythagorean triple is an integer solution to the Pythagorean theorem. 
a^2 + b^2 = c^2. The first Pythagorean triple is (3, 4, 5).

Find and put in a tuple all unique Pythagorean triples for the positive integers 
a,b and c with c<100.

'''
print("\n### Exercise 9")

import math

list_triple = []
for a in range(1,100):
    for b in range(1,100):
        c = math.sqrt(a**2 + b**2)
        if c <100:
            if (int(c) == c):
                list_triple.append(sorted([a,b,int(c)]))
        else:
            break
list_triple_rem_dub = []
[list_triple_rem_dub.append(n) for n in list_triple if n not in list_triple_rem_dub]

print("The number of unique Pythagorean triples is:",len(list_triple_rem_dub),"\n\n",list_triple_rem_dub)



'''
#Exercise 10
10. Normalization of a N-dimensional vector

Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers, and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1).
'''
print("\n### Exercise 10")
sum_vec = 0
vector_n = [5, 7, 2.3, 12, 1.7]
for x in range(len(vector_n)):
    vector_n[x] = vector_n[x]**2
    sum_vec += vector_n[x]
for x in range(len(vector_n)):
    vector_n[x] = vector_n[x]/sum_vec
print(vector_n)

 
'''
#Exercise 11
11. The Fibonacci sequence

Calculate the first 20 numbers of the Fibonacci sequence using only for or while loops.

'''

print("\n### Exercise 11")
fibo_num = [1,1]
for x in range(2,20,1):
    fibo_num.append(fibo_num[-1] + fibo_num [-2])
    
print("The",len(fibo_num), "first Fibonacci numbers are \n", fibo_num)


