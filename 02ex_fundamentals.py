{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can solve these exercises in the room or at home. For this week, and the next 3 weeks, exercises have to be solved by creating a single dedicated `.py` file called `02ex_fundamentals.py`.\n",
    "\n",
    "You can divide the individual exercises in the source code with appropriate comments (`#`).\n",
    "\n",
    "The exercises need to run without errors with `python3 02ex_fundamentals.py`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1\\. **Global variables**\n",
    "\n",
    "Convert the function $f$ into a function that doesn't use global variables and that does not modify the original list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = 5\n",
    "\n",
    "def f(alist):\n",
    "    for i in range(x):\n",
    "        alist.append(i)\n",
    "    return alist\n",
    "\n",
    "alist = [1, 2, 3]\n",
    "ans = f(alist)\n",
    "print(ans)\n",
    "print(alist) # alist has been changed"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2\\. **List comprehension**\n",
    "\n",
    "Write the following expression using a list comprehension:\n",
    "\n",
    "`ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print([i**2 for i in range(10) if i % 2 != 0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3\\. **Filter list**\n",
    "\n",
    "Using the `filter()` hof, define a function that takes a list of words and an integer `n` as arguments, and returns a list of words that are shorter than `n`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "i=0\n",
    "def func(word):\n",
    "    global i\n",
    "    n = 3\n",
    "    if(i<n):\n",
    "        i+=1\n",
    "        return True\n",
    "    return False    \n",
    "r = filter(func, ['php', 'javascript', 'java', 'c++', 'c', 'python', 'go', 'rust', 'dart', 'swift'])\n",
    "print(list(r))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4\\. **Map dictionary**\n",
    "\n",
    "\n",
    "Consider the following dictionary:\n",
    "\n",
    "`lang = {\"Python\" : 3, \"Java\" : '', \"Cplusplus\" : 'test', \"Php\" : 0.7}`\n",
    "\n",
    "Write a function that takes the above dictionary and uses the `map()` higher order function to return a list that contains the length of the keys of the dictionary."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def f(string):\n",
    "    return len(string)\n",
    " \n",
    "print(list(map(f, {\"Python\" : 3, \"Java\" : '', \"Cplusplus\" : 'test', \"Php\" : 0.7})))       "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5\\. **Lambda functions**\n",
    "\n",
    "Write a Python program that sorts the following list of tuples using a lambda function, according to the alphabetical order of the first element of the tuple:\n",
    "\n",
    "`language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]`\n",
    "\n",
    "*Hint*: use the method `sort()` and its argument `key` of the `list` data structure."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(sorted([('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)], key = lambda x : x[0],reverse=False))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "6\\. **Nested functions**\n",
    "\n",
    "Write two functions: one that returns the square of a number, and one that returns its cube.\n",
    "\n",
    "Then, write a third function that returns the number raised to the 6th power, using only the two previous functions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def square(number):\n",
    "    return number**2\n",
    "\n",
    "def cube(number):\n",
    "    return number**3    \n",
    "\n",
    "def six_power(number):\n",
    "    return number * square(number) * cube(number)\n",
    "\n",
    "print(six_power(2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "7\\. **Decorators**\n",
    "\n",
    "Write a decorator named `hello` that makes every wrapped function print “Hello World!” each time the function is called.\n",
    "\n",
    "The wrapped function should look like:\n",
    "\n",
    "```python\n",
    "@hello\n",
    "def square(x):\n",
    "    return x*x\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World!\n",
      "25\n"
     ]
    }
   ],
   "source": [
    "def hello(func):\n",
    "    def wrapper(x):\n",
    "        print('Hello World!')\n",
    "        func(x)\n",
    "    return wrapper\n",
    "\n",
    "\n",
    "@hello \n",
    "def square(x):\n",
    "    print(x*x)\n",
    "\n",
    "square(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "8\\. **The Fibonacci sequence (part 2)**\n",
    "\n",
    "Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using a recursive function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 "
     ]
    }
   ],
   "source": [
    "def fibonacci(n):\n",
    "    if n <= 1:\n",
    "        return n\n",
    "    return fibonacci(n - 1) + fibonacci(n - 2)\n",
    "\n",
    "n = 1\n",
    "while (n <= 20):\n",
    "    print(fibonacci(n), end=' ')\n",
    "    n += 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "9\\. **The Fibonacci sequence (part 3)**\n",
    "\n",
    "Run both the Fibonacci recursive function from the previous exercise, and the Fibonacci function from 01ex that use only `for` and `while` loops.\n",
    "\n",
    "Measure the execution code of the two functions with `timeit` ([link to the doc](https://docs.python.org/3/library/timeit.html)), for example:\n",
    "\n",
    "`%timeit loopFibonacci(20)`\n",
    "\n",
    "`%timeit recursiveFibonacci(20)`\n",
    "\n",
    "which one is the most efficient implementation? By how much?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Time taken for normal fibonacci -> 5.369999996673869e-05\n",
      "Time taken for recursive fibonacci -> 39.23033659999999\n"
     ]
    }
   ],
   "source": [
    "import timeit\n",
    "\n",
    "def fibonacci(n):\n",
    "    fibonacci = [1, 1]\n",
    "    for i in range(1, n - 1):\n",
    "        fibonacci.append(fibonacci[i] + fibonacci[i - 1])\n",
    "    return fibonacci    \n",
    "\n",
    "def recursive_fibonacci(n):\n",
    "    if n <= 1:\n",
    "        return n\n",
    "    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)\n",
    "\n",
    "start = timeit.default_timer()\n",
    "fibonacci(40)\n",
    "print('Time taken for normal fibonacci -> ' + str(timeit.default_timer() - start))\n",
    "\n",
    "start = timeit.default_timer()\n",
    "recursive_fibonacci(40)\n",
    "print('Time taken for recursive fibonacci -> ' + str(timeit.default_timer() - start))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "10\\. **Class definition**\n",
    "\n",
    "Define a class `polygon`. The constructor has to take a tuple as input that contains the length of each side. The (unordered) input list does not have to have a fixed length, but should contain at least 3 items.\n",
    "\n",
    "- Create appropriate methods to get and set the length of each side\n",
    "\n",
    "- Create a method `perimeter()` that returns the perimeter of the polygon\n",
    "\n",
    "- Create a method `getOrderedSides(increasing = True)` that returns a tuple containing the length of the sides arranged in increasing or decreasing order, depending on the argument of the method\n",
    "\n",
    "Test the class by creating an instance and calling the `perimeter()` and `getOrderedSides(increasing = True)` methods."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(3, 4, 5)\n",
      "(8, 6, 10)\n",
      "24\n",
      "[10, 8, 6]\n"
     ]
    }
   ],
   "source": [
    "class polygon:\n",
    "    sides = None\n",
    "    def __init__(self, sides:tuple) -> None:\n",
    "        if len(sides) < 3:\n",
    "            raise Exception('Sides should contain at least 3 items.')\n",
    "        self.sides = sides\n",
    "\n",
    "    def get_sides(self) -> tuple:\n",
    "        return self.sides\n",
    "\n",
    "    def set_sides(self, sides:tuple) -> None:\n",
    "            if len(sides) < 3:\n",
    "                raise Exception('Sides should contain at least 3 items.')\n",
    "            self.sides = sides     \n",
    "\n",
    "    def perimeter(self) -> float:\n",
    "        sum = 0\n",
    "        for item in self.sides:\n",
    "            sum += item\n",
    "        return sum    \n",
    "\n",
    "    def get_ordered_sides(self, increasing):\n",
    "        return sorted(self.sides, reverse=not increasing)\n",
    "        \n",
    "\n",
    "triangle = polygon((3, 4, 5))\n",
    "print(triangle.get_sides())\n",
    "triangle.set_sides((8, 6, 10))\n",
    "print(triangle.get_sides())\n",
    "print(triangle.perimeter())\n",
    "print(triangle.get_ordered_sides(False))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "11\\. **Class inheritance**\n",
    "\n",
    "Define a class `rectangle` that inherits from `polygon`. Modify the constructor, if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle.\n",
    "\n",
    "- Create a method `area()` that returns the area of the rectangle.\n",
    "\n",
    "Test the `rectangle` class by creating an instance and passing an appropriate input to the constructor."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "class polygon:\n",
    "    sides = None\n",
    "    def __init__(self, sides:tuple) -> None:\n",
    "        if len(sides) < 3:\n",
    "            raise Exception('Sides should contain at least 3 items.')\n",
    "        self.sides = sides\n",
    "\n",
    "    def get_sides(self) -> tuple:\n",
    "        return self.sides\n",
    "\n",
    "    def set_sides(self, sides:tuple) -> None:\n",
    "            if len(sides) < 3:\n",
    "                raise Exception('Sides should contain at least 3 items.')\n",
    "            self.sides = sides     \n",
    "\n",
    "    def perimeter(self) -> float:\n",
    "        sum = 0\n",
    "        for item in self.sides:\n",
    "            sum += item\n",
    "        return sum    \n",
    "\n",
    "    def get_ordered_sides(self, increasing):\n",
    "        return sorted(self.sides, reverse=not increasing)\n",
    "\n",
    "class rectangle(polygon):\n",
    "    def __init__(self, sides: tuple) -> None:\n",
    "        super().__init__(sides)\n",
    "\n",
    "        #if not(self.sides[0] == self.sides[1] and self.sides[3] == self.sides[2]) or not(self.sides[0] == self.sides[2] and self.sides[1] == self.sides[3]) or not(self.sides[0] == self.sides[3] and self.sides[1] == self.sides[2]):\n",
    "            #raise Exception('These number can not form rectangle')\n",
    "\n",
    "    def area(self):\n",
    "        return self.sides[0] + self.sides[1] + self.sides[2] + self.sides[3]\n",
    "\n",
    "\n",
    "r = rectangle((1, 1, 2, 2))\n",
    "print(r.area())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
