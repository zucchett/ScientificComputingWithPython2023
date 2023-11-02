{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can solve these exercises in the room or at home. For this week, and the next 3 weeks, exercises have to be solved by creating a single dedicated `.py` file called `01ex_introduction.py`.\n",
    "\n",
    "You can divide the individual exercises in the source code with appropriate comments (`#`).\n",
    "\n",
    "The exercises need to run without errors with `python3 01ex_introduction.py`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1\\. **The HelloWorld replacement**\n",
    "\n",
    "a) Write a program that:\n",
    "- prints the numbers from 1 to 100\n",
    "- but for multiples of three print \"`Hello`\" instead of the number and for the multiples of five print \"`World`\"\n",
    "- for numbers which are multiples of both three and five print \"`HelloWorld`\".\n",
    "\n",
    "b) Put the result in a tuple and substitute \"`Hello`\" with \"`Python`\" and \"`World`\" with \"`Works`\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "Hello\n",
      "4\n",
      "World\n",
      "Hello\n",
      "7\n",
      "8\n",
      "Hello\n",
      "World\n",
      "11\n",
      "Hello\n",
      "13\n",
      "14\n",
      "Hello World\n",
      "16\n",
      "17\n",
      "Hello\n",
      "19\n",
      "World\n",
      "Hello\n",
      "22\n",
      "23\n",
      "Hello\n",
      "World\n",
      "26\n",
      "Hello\n",
      "28\n",
      "29\n",
      "Hello World\n",
      "31\n",
      "32\n",
      "Hello\n",
      "34\n",
      "World\n",
      "Hello\n",
      "37\n",
      "38\n",
      "Hello\n",
      "World\n",
      "41\n",
      "Hello\n",
      "43\n",
      "44\n",
      "Hello World\n",
      "46\n",
      "47\n",
      "Hello\n",
      "49\n",
      "World\n",
      "Hello\n",
      "52\n",
      "53\n",
      "Hello\n",
      "World\n",
      "56\n",
      "Hello\n",
      "58\n",
      "59\n",
      "Hello World\n",
      "61\n",
      "62\n",
      "Hello\n",
      "64\n",
      "World\n",
      "Hello\n",
      "67\n",
      "68\n",
      "Hello\n",
      "World\n",
      "71\n",
      "Hello\n",
      "73\n",
      "74\n",
      "Hello World\n",
      "76\n",
      "77\n",
      "Hello\n",
      "79\n",
      "World\n",
      "Hello\n",
      "82\n",
      "83\n",
      "Hello\n",
      "World\n",
      "86\n",
      "Hello\n",
      "88\n",
      "89\n",
      "Hello World\n",
      "91\n",
      "92\n",
      "Hello\n",
      "94\n",
      "World\n",
      "Hello\n",
      "97\n",
      "98\n",
      "Hello\n",
      "World\n"
     ]
    }
   ],
   "source": [
    "for i in range (1,101):\n",
    "    if i%15 == 0:\n",
    "        print (\"Hello World\")\n",
    "    elif i%3==0:\n",
    "        print (\"Hello\")\n",
    "    elif i%5==0:\n",
    "        print (\"World\")\n",
    "    else :\n",
    "        print (i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2, 'python', 4, 'works', 'python', 7, 8, 'python', 'works', 11, 'python', 13, 14, 'python works', 16, 17, 'python', 19, 'works', 'python', 22, 23, 'python', 'works', 26, 'python', 28, 29, 'python works', 31, 32, 'python', 34, 'works', 'python', 37, 38, 'python', 'works', 41, 'python', 43, 44, 'python works', 46, 47, 'python', 49, 'works', 'python', 52, 53, 'python', 'works', 56, 'python', 58, 59, 'python works', 61, 62, 'python', 64, 'works', 'python', 67, 68, 'python', 'works', 71, 'python', 73, 74, 'python works', 76, 77, 'python', 79, 'works', 'python', 82, 83, 'python', 'works', 86, 'python', 88, 89, 'python works', 91, 92, 'python', 94, 'works', 'python', 97, 98, 'python', 'works')\n"
     ]
    }
   ],
   "source": [
    "result = []\n",
    "for i in range (1,101):\n",
    "    if i%15 == 0:\n",
    "        result.append('python works')\n",
    "    elif i%3==0:\n",
    "        result.append('python')\n",
    "    elif i%5==0:\n",
    "        result.append('works')\n",
    "    else :\n",
    "        result.append(i)\n",
    "print(tuple(result)) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2\\. **The swap**\n",
    "\n",
    "Write a program that swaps the values of two input variables `x` and `y` from command line (whatever the type).\n",
    "\n",
    "Try to do that without using a temporary variable, exploiting the Python syntax."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "left, right = input().split(' ')\n",
    "print(left, right, end='=>')\n",
    "left, right = right, left\n",
    "print(left, right)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3\\. **Computing the distance**\n",
    "\n",
    "Write a program that calculates and prints the euclidean distance between two given points $u$ and $v$ in a 2D space, where $u$ and $v$ are both 2-tuples $(x,y)$.\n",
    "\n",
    "Example: if $u=(3,0)$ and $v=(0,4)$, the function should return $5$.\n",
    "\n",
    "*Hint:* in order to compute the square root, import the `math` library with `import math` and use `math.sqrt()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "u=(float(input()),float(input()))\n",
    "v=(float(input()),float(input()))\n",
    "d= math.sqrt((u[0]-v[0])**2+(u[1]-v[1])**2)\n",
    "print(d) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4\\. **Counting letters**\n",
    "\n",
    "Write a program that calculates the number of times each character occurs in a given string. Ignore differences in capitalization.\n",
    "\n",
    "The test strings are:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "s1 = \"Write a program that prints the numbers from 1 to 100. \\\n",
    "But for multiples of three print Hello instead of the number and for the multiples of five print World. \\\n",
    "For numbers which are multiples of both three and five print HelloWorld.\"\n",
    "s2 = \"The quick brown fox jumps over the lazy dog\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "s1 = \"Write a program that prints the numbers from 1 to 100. \\\n",
    "But for multiples of three print Hello instead of the number and for the multiples of five print World. \\\n",
    "For numbers which are multiples of both three and five print HelloWorld.\"\n",
    "s2 = \"The quick brown fox jumps over the lazy dog\"\n",
    "\n",
    "s1 , s2 = s1.lower(), s2.lower()\n",
    "\n",
    "for i in s1:\n",
    "    print(i , \": \",s1.count(i) + s2.count(i))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5\\. **Isolating the unique**\n",
    "\n",
    "Write a program that determines and counts the unique numbers (numbers with only one occurrence) in the list:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,\n",
    " 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,\n",
    " 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,\n",
    " 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,\n",
    " 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,\n",
    " 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,\n",
    " 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]\n",
    "\n",
    "result = {}\n",
    "\n",
    "for i in range(len(l)):\n",
    "    c = 0\n",
    "    for j in range(len(l)):\n",
    "        if l[i] == l[j]:\n",
    "            c+=1\n",
    "            result[l[i]] = c\n",
    "#print(result)\n",
    "uniques = []\n",
    "for key, value in result.items():\n",
    "    if value == 1:\n",
    "        uniques.append(key)\n",
    "print(uniques)    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Do the same exploiting only the Python data structures."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "6\\. **Casting**\n",
    "\n",
    "Write a program that:\n",
    "* reads from command line two variables, that can be either `int`, `float`, or `str`.\n",
    "* use the `try`/`except` expressions to perform the addition of these two variables, only if possible\n",
    "* print the result without making the code crash for all the `int`/`float`/`str` input combinations."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = input('enter your value: ')\n",
    "b = input('enter your value: ')\n",
    "try:\n",
    "     if not a.isnumeric() and not b.isnumeric():\n",
    "          c = a + b\n",
    "     else:\n",
    "          c = float(a) + float(b)\n",
    "except:\n",
    "     c = 'can not add integer to string!'\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a=input(\"input 1:\")\n",
    "b=input(\"input 2:\")\n",
    "try:\n",
    "    try:\n",
    "        a,b=float(a),float(b)\n",
    "        c=a+b\n",
    "        print(c)\n",
    "   \n",
    "    except: \n",
    "        try:\n",
    "            a=int(a)\n",
    "            print('can not add integer to string!')            \n",
    "        except:\n",
    "             b=int(b)\n",
    "             print('can not add integer to string!')\n",
    "except: \n",
    "    c=a+b \n",
    "    print(c)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "7\\. **Cubes**\n",
    "\n",
    "Create a list of the cubes of *x* for *x* in *[0, 10]* using:\n",
    "\n",
    "a) a for loop\n",
    "\n",
    "b) a list comprehension"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "cubes = [i**3 for i in range(0, 11)]\n",
    "print(cubes)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "8\\. **List comprehension**\n",
    "\n",
    "Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = []\n",
    "for i in range(3):\n",
    "    for j in range(4):\n",
    "        a.append((i, j))\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print([(i, j) for i in range(3) for j in range(4)])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "9\\. **Nested list comprehension**\n",
    "\n",
    "> A Pythagorean triple is an integer solution to the Pythagorean theorem $a^2+b^2=c^2$. The first Pythagorean triple is (3, 4, 5).\n",
    "\n",
    "Find and put in a tuple all unique Pythagorean triples for the positive integers $a$, $b$ and $c$ with $c < 100$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "result = []\n",
    "c, m = 0, 2\n",
    "while c < 100 :\n",
    "    for n in range(1, m) :\n",
    "        a = m * m - n * n\n",
    "        b = 2 * m * n\n",
    "        c = m * m + n * n\n",
    "        if c > 100 :\n",
    "            break\n",
    "        result.append((a, b, c))\n",
    "        m = m + 1\n",
    "print(tuple(result))        "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "10\\. **Normalization of a N-dimensional vector**\n",
    "\n",
    "Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers, and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "n = int(input('Enter the number of dimensions: '))\n",
    "vector = []\n",
    "square_sum = 0\n",
    "for i in range(n):\n",
    "    vector.append(int(input()))\n",
    "    square_sum += vector[i]**2\n",
    "size = math.sqrt(square_sum)\n",
    "for i in range(n):\n",
    "    vector[i] = vector[i] / size\n",
    "print(vector)    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "11\\. **The Fibonacci sequence**\n",
    "\n",
    "Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using only `for` or `while` loops."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "fibonacci = [1, 1]\n",
    "for i in range(1, 19):\n",
    "    fibonacci.append(fibonacci[i] + fibonacci[i - 1])\n",
    "print(fibonacci)    "
   ]
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
 "nbformat_minor": 4
}
