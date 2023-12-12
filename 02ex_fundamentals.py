# 1. Global variables
x = 5
def f(a_list):
    t_array = list(a_list)
    for p in range(x):
        t_array.append(p)
    return t_array


alist = [1, 2, 3]
n_ans = f(alist)
print(alist)
print(n_ans)


# 2 List comprehension
ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(ans)

ansNew = [x * x for x in range(10) if x % 2 == 1]
print(ansNew)


#3. Filter list
def is_shorter(li, n):
    shorter_list = filter(lambda i: i < n, li)
    return list(shorter_list)

tmp_list = is_shorter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
print(tmp_list)


#4. Map dictionary
lang = {"Python": 3, "Java": '', "Cplusplus": 'test', "Php": 0.7}

def is_keys(li):
    count_list = list(map(lambda x: len(x), li.keys()))
    return count_list

print(is_keys(lang))

#5. Lambda functions

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key =lambda first_ele: first_ele[0])

print(language_scores)


#  6Nested functions

def num_square(n):
    square = n ** 2
    return square


def num_cube(n):
    cube = n ** 3
    return cube


def power_num(n):
    power = num_cube(num_square(n))
    return power


print(power_num(2))

# 7. Decorators
def decorator(func):
    def wrapper( ):
        func()
        # print(f'{func}')
    return wrapper


@decorator
def hello():
    print("Hello World!")


hello()

#8. The Fibonacci sequence (part 2)
fibo_seq = []
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        b = fibo(n-2)+fibo(n-1)
        return b

for i in range(1,21):
    fibo_seq.append(fibo(i))

print(fibo_seq)

# 9.The Fibonacci sequence (part 3)
import timeit
def first_solve(n=20):
    i = 0
    a, b = 0, 1
    finona = []
    while i < n:
        i += 1
        finona.append(b)
        a, b = b, a + b
    return finona


def second_solve(n):
    if n == 1 or n == 2:
        return 1
    else:
        return second_solve(n-2)+second_solve(n-1)


first_time = timeit.Timer(lambda: first_solve(20))
second_time = timeit.Timer(lambda: second_solve(20))
#
print(first_time.timeit(1))
print(second_time.timeit(1))

# 10.Class definition
class polygon:
    def __init__(self, list):
        self.list = list
        self.lene = len(list)
        if self.lene < 3:
            print("enter more than 3")
            return

    def perimeter(self):
        perimeter = sum(self.list)
        # print("first solv: ",self.list[0] * self.lene)
        print("sum: ", perimeter)

    def getOrderedSides(self, increasing=True):
        print(sorted(self.list))


x = polygon((3, 6, 7, 1))
x.perimeter()
x.getOrderedSides()


# 11.Class inheritance
class rect_angle():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length


shape = rect_angle(5, 6)
print(shape.area())