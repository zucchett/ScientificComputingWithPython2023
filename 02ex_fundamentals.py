######################################Global variables ##################
print("1. Global variables")
def f(alist,x):
    new_list = list(alist)  # Here I created a copy of the list alist
    for i in range(x):
        new_list.append(i)
    return new_list

alist = [1, 2, 3]
ans = f(alist,x=5)
print(ans)
print(alist)  # The list remains the same
######################################LIST COMPREHENSION##################
print("2. LIST COMPREHENSION")
ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(ans)
ans1 = [x**2 for x in range(10) if x%2==1]
print(ans1)
#############################################FILTER LIST###################
print("3. FILTER LIST")
def filter_list(l, n):
    filtered_list = list(filter(lambda word: len(word) < n, l))
    return filtered_list

if __name__ == "__main__":
    l = ["ICT", "python", "variables", "Padova", "master", "degree"]
    n = 4
    result = filter_list(l, n)
    print(result)
################################MAP DICTIONARY####################
print("4.MAP DICTIONARY")
def key_lengths(dicti):
    len_key = list(map(len, dicti.keys()))
    return len_key
if __name__ == "__main__":
    lang = {"Python": 3, "Java": '', "Cplusplus": 'test', "Php": 0.7}
    result = key_lengths(lang)
    print(result)
################################## Lambda functions#########################
print("5. Lambda function")
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
sorted_list = sorted(language_scores, key=lambda k: k[0])
for i, j in sorted_list:
    print(f"{i}: {j}")
##################################### NESTED FUNCTIONS #############################
print("6. Nested functions")
def square(x):
    return x ** 2
def cube(x):
    return x ** 3
def power_six(x):
    return square(cube(x))
########################## DECORATORS ###################################
print("7. DECORATORS")
def hello(func):
    def wrapper(*args, **kwargs):
        print("Hello World!")
        return func(*args, **kwargs)
    return wrapper
@hello
def square(x):
    return x * x
if __name__ == "__main__":
    result = square(5)
    print(f"Result: {result}")

###########################FIBONACCI PART2################################
print("8. FIBONACCI PART2")
def fib_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_l = fib_recursive(n - 1)
        fib_l.append(fib_l[-1] + fib_l[-2])
        return fib_l
if __name__ == "__main__":
    fib_seq = fib_recursive(20)
    print(fib_seq)
#########################################The Fibonacci sequence (part 3)###################################
print("9. The Fibonacci sequence (part 3)")
import timeit

def fib_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_l = fib_recursive(n - 1)
        fib_l.append(fib_l[-1] + fib_l[-2])
        return fib_l

# Iterative Fibonacci function
def iter_fib(nm):
    fib_seq = [0, 1]
    for i in range(2, nm):
        fib2 = fib_seq[i - 1] + fib_seq[i - 2]
        fib_seq.append(fib2)
    print(fib_seq)
if __name__ == "__main__":
    rec_time = timeit.timeit("fib_recursive(20)", globals=globals(), number=1000)
    it_time = timeit.timeit("iter_fib(20)", globals=globals(), number=1000)

    print("Execution time for recursive Fibonacci:", rec_time)
    print("Execution time for iterative (loop) Fibonacci:", it_time)
#The most efficient is the function that has less execution time which is the recursive Fibonacci

##########################################Class definition################################
print("10. class definition")
class Polygon:
    def __init__(self, sides):
        if len(sides) < 3:
            raise ValueError("A polygon must have at least 3 sides.")
        self.sides = list(sides)

    def set_side_length(self, side_index, length):
        if 0 <= side_index < len(self.sides):
            self.sides[side_index] = length

    def get_side_length(self, side_index):
            return self.sides[side_index]

    def perimeter(self):
        return sum(self.sides)

    def get_ordered_sides(self, increasing=True):
        ordered_sides = sorted(self.sides) if increasing else sorted(self.sides, reverse=True)
        return tuple(ordered_sides)
if __name__ == "__main__":
    polygon = Polygon((5, 4, 7, 3))
    print("Perimeter:", polygon.perimeter())
    print("Ordered Sides (increasing):", polygon.get_ordered_sides(increasing=True))
    print("Ordered Sides (decreasing):", polygon.get_ordered_sides(increasing=False))

################################ Class inheritance####################################
print("11. class inheritance")
class Polygon:
    def __init__(self, sides):
        self.sides = list(sides)

    def set_side_length(self, side_index, length):
        if 0 <= side_index < len(self.sides):
            self.sides[side_index] = length
        else:
            raise ValueError("Side index out of range.")

    def get_side_length(self, side_index):
         return self.sides[side_index]

    def perimeter(self):
        return sum(self.sides)

    def get_ordered_sides(self, increasing=True):
        ordered_sides = sorted(self.sides) if increasing else sorted(self.sides, reverse=True)
        return tuple(ordered_sides)

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width])

    def area(self):
        return self.sides[0] * self.sides[1]

rectangle = Rectangle(5, 4)
print("Perimeter:", rectangle.perimeter())
print("Ordered Sides (increasing):", rectangle.get_ordered_sides(increasing=True))
print("Ordered Sides (decreasing):", rectangle.get_ordered_sides(increasing=False))
print("Area:", rectangle.area())

