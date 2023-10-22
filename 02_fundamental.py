#1.Global variables

#Convert the function  𝑓  into a function that doesn't use 
#global variables and that does not modify the original list

def f(a_list):
    x=5 #converting to local variable
    new_list=[]
    for i in range(x):
        new_list.append(i)
    return new_list

a_list = [1, 2, 3]
answer = f(a_list)
print(answer)
print(blist)

#2\. **List comprehension**

ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(ans)

#3\. **Filter list**
def short_word(words,number):
    return list(filter(lambda word:len(word)< number, words))


names=["jeff","betty","homophobis","hey"]
n=5
short=short_word(names,n)
print(short)


#4\. **Map dictionary**
lang = {"Python": 3, "Java": '', "Cplusplus": 'test', "Php": 0.7}

def length_keys(key):
    return len(key)

l_keys = list(map(length_keys, lang.keys()))

print(l_keys)

#5\. **Lambda functions**
language_scores = {"Python": 3, "Java": '', "Cplusplus": 'test', "Php": 0.7}

sorted_lang_scores=sorted(language_scores.items(), key=lambda lang: lang[0])

print(sorted_lang_scores)

#6\. **Nested functions**

square = lambda x: x * x
cube = lambda x: square(x) * x
power_6 = lambda x: square(x) * cube(x) * x

# Calculate the square of a number
print("Square:", square(2))  

# Calculate the cube of a number
print("Cube:", cube(2))  

# Calculate the sixth power of a number
print("Power 6:", power_6(2)) 

#7\. **Decorators**
def hello(func):
    def wrapper(x):
        print("Hello World")
        result = func(x)
        return result
    return wrapper

@hello
def square(x):
    return x * x

result = square(2)
print("Result:", result)

#8\. **The Fibonacci sequence (part 2)**
def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

for i in range(20):
    result = fib(i)
    print(f"Fib({i}) = {result}")

#9\. **The Fibonacci sequence (part 3)**
# Recursive Fibonacci function
#9\. **The Fibonacci sequence (part 3)**
# Recursive Fibonacci function
def recursiveFibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2)
    
for num in range(20):
    print("The fibonacci of ", num, "is",recursiveFibonacci(num))
    
    
    
    
import timeit

n = 20

# Measure the execution time for the recursive Fibonacci function
recursive_time = timeit.timeit('recursiveFibonacci(n)', globals=globals(), number=10000)

print(f"Recursive Fibonacci Execution Time: {recursive_time:.6f} seconds")

#Fibonacci with for loop
def ForFibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

for num in range (20):
    print ("Fibonnacci for", num, "is",ForFibonacci(num))
    
    
    
# while Loop Fibonacci function

def whileFibonacci(n):
    a, b = 0, 1
    i = 0
    while i < n:
        a, b = b, a + b
        i += 1
    return a    

#calculating the execution time for while and for loops 
import timeit
n=20
for_loop_time = timeit.timeit('ForFibonacci(n)', globals=globals(), number=10000)

While_loop_time = timeit.timeit('whileFibonacci(n)', globals=globals(), number=10000)
print(f"for-based Fibonacci Execution Time: {for_loop_time:.6f} seconds")
print(f"while-based Fibonacci Execution Time: {While_loop_time:.6f} seconds")

## The execution time of for and while loops is nearly the same but for recusive function it take more time, therefore for and while loops performs better