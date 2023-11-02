{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can solve these exercises in the room or at home. For this week, and the next 3 weeks, exercises have to be solved by creating a single dedicated `.py` file called `03ex_representation.py`.\n",
    "\n",
    "You can divide the individual exercises in the source code with appropriate comments (`#`).\n",
    "\n",
    "The exercises need to run without errors with `python3 03ex_representation.py`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1\\. **Number representation**\n",
    "\n",
    "Write a function that converts integer numbers among the bin, dec, and hex representations (bin<->dec<->hex).\n",
    "Determine the input type in the function, and pass another argument to choose the output representation."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0x6a\n"
     ]
    }
   ],
   "source": [
    "def number_representation(number, mode):\n",
    "    base = -1\n",
    "    if mode == 'bin':\n",
    "        return bin(int(number))\n",
    "    if mode == 'dec':\n",
    "        return int(number)\n",
    "    if mode == 'hex':\n",
    "        return hex(int(number)) \n",
    "    return(int(number, base))          \n",
    "\n",
    "print(number_representation('106', 'hex'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2\\. **32-bit floating point number**\n",
    "\n",
    "Write a function that converts a 32 bit binary string (for example, `110000101011000000000000`) into a single precision floating point in decimal representation. Interpret the various bits as sign, fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12759040.0\n"
     ]
    }
   ],
   "source": [
    "def converter(number):\n",
    "    return(float(int(number, 2)))\n",
    "\n",
    "print(converter('110000101011000000000000'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3\\. **Underflow and overflow**\n",
    "\n",
    "Write a program to determine the approximate underflow and overflow limits (within a factor of 2) for floating point numbers on your computer. \n",
    "\n",
    "*Hint*: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed the under/over-flow limits."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "The over flow is: 8.988466e+307\n",
      "The under flow is: 1.112537e-308\n",
      "I do the loop for 1023 times to reach the overflow and underflow.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "undflow = 1\n",
    "ovflow = 1\n",
    "for i in range(1023):\n",
    "    undflow = undflow / 2\n",
    "    ovflow  = ovflow  * 2\n",
    "scientific_undflow=\"{:e}\".format(undflow)\n",
    "scientific_ovflow=\"{:e}\".format(ovflow)\n",
    "print(f'\\nThe over flow is: {scientific_ovflow}')\n",
    "print(f'The under flow is: {scientific_undflow}')\n",
    "print(f'I do the loop for 1023 times to reach the overflow and underflow.\\n')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4\\. **Machine precision**\n",
    "\n",
    "Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.\n",
    "\n",
    "*Hint*: define a new variable by adding an increasingly smaller value and check when the addition starts to have no effect on the number."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Step 0\n",
      "2.1\n",
      "Step 1\n",
      "2.11\n",
      "Step 2\n",
      "2.1109999999999998\n",
      "Step 3\n",
      "2.1111\n",
      "Step 4\n",
      "2.11111\n",
      "Step 5\n",
      "2.111111\n",
      "Step 6\n",
      "2.1111111\n",
      "Step 7\n",
      "2.11111111\n",
      "Step 8\n",
      "2.111111111\n",
      "Step 9\n",
      "2.1111111111\n",
      "Step 10\n",
      "2.11111111111\n",
      "Step 11\n",
      "2.111111111111\n",
      "Step 12\n",
      "2.1111111111111\n",
      "Step 13\n",
      "2.1111111111111103\n",
      "Step 14\n",
      "2.111111111111111\n",
      "Step 15\n",
      "2.111111111111111\n",
      "Step 16\n",
      "2.111111111111111\n",
      "Step 17\n",
      "2.111111111111111\n",
      "Step 18\n",
      "2.111111111111111\n",
      "Step 19\n",
      "2.111111111111111\n",
      "After 14 steps there is no difference in numbers.\n"
     ]
    }
   ],
   "source": [
    "var = 2\n",
    "add = 1e-1\n",
    "for i in range(20):\n",
    "    var = var + add\n",
    "    add = add * 1e-1\n",
    "    print(f'Step {i}')\n",
    "    print(var)\n",
    "    \n",
    "print(\"After 14 steps there is no difference in numbers.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5\\. **Quadratic solution**\n",
    "\n",
    "Write a function that takes in input three parameters $a$, $b$ and $c$ and prints out the two solutions to the quadratic equation $ax^2+bx+c=0$ using the standard formula:\n",
    "$$\n",
    "x=\\frac{-b\\pm\\sqrt{b^2-4ac}}{2a}\n",
    "$$\n",
    "\n",
    "(a) use the function to compute the solution for $a=0.001$, $b=1000$ and $c=0.001$\n",
    "\n",
    "(b) re-express the standard solution formula by multiplying the numerator and the denominator by $-b\\mp\\sqrt{b^2-4ac}$ and again find the solution for $a=0.001$, $b=1000$ and $c=0.001$. How does it compare with what has been previously obtained, and why? (add the answer to a Python comment)\n",
    "\n",
    "(c) write a function that computes the roots of a quadratic equation accurately in all cases"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[-9.999894245993346e-07, -999999.999999]\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "def quadratic(a, b, c):\n",
    "    delta = math.sqrt((b**2) - (4*a*c))\n",
    "    roots = []\n",
    "    roots.append((-b + delta) / (2 * a))\n",
    "    roots.append((-b - delta) / (2 * a))\n",
    "    return roots\n",
    "\n",
    "print(quadratic(0.001, 1000, 0.001))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "6\\. **The derivative**\n",
    "\n",
    "Write a program that implements the function $f(x)=x(x−1)$\n",
    "\n",
    "(a) Calculate the derivative of the function at the point $x = 1$ using the derivative definition:\n",
    "\n",
    "$$\n",
    "\\frac{{\\rm d}f}{{\\rm d}x} = \\lim_{\\delta\\to0} \\frac{f(x+\\delta)-f(x)}{\\delta}\n",
    "$$\n",
    "\n",
    "with $\\delta = 10^{−2}$. Calculate the true value of the same derivative analytically and compare it with the answer your program gives. The two will not agree perfectly. Why?\n",
    "\n",
    "(b) Repeat the calculation for $\\delta = 10^{−4}, 10^{−6}, 10^{−8}, 10^{−10}, 10^{−12}$ and $10^{−14}$. How does the accuracy scale with $\\delta$?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.0000999999998899\n"
     ]
    }
   ],
   "source": [
    "def f(x):\n",
    "    return x * (x - 1)\n",
    "\n",
    "def f_derivative(x, sigma = 0.0001):\n",
    "    if sigma < 0.00000000000001:\n",
    "        raise Exception('Can not devide by zero')\n",
    "    return (f(x + sigma) - f(x)) / sigma   \n",
    "\n",
    "print(f_derivative(1))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "7\\. **Integral of a semicircle**\n",
    "\n",
    "Consider the integral of the semicircle of radius 1:\n",
    "$$\n",
    "I=\\int_{-1}^{1} \\sqrt(1-x^2) {\\rm d}x\n",
    "$$\n",
    "which is known to be $I=\\frac{\\pi}{2}=1.57079632679...$.\n",
    "\n",
    "Alternatively we can use the Riemann definition of the integral:\n",
    "$$\n",
    "I=\\lim_{N\\to\\infty} \\sum_{k=1}^{N} h y_k \n",
    "$$\n",
    "\n",
    "with $h=2/N$ the width of each of the $N$ slices the domain is divided into and where\n",
    "$y_k$ is the value of the function at the $k-$th slice.\n",
    "\n",
    "(a) Write a program to compute the integral with $N=100$. How does the result compare to the true value?\n",
    "\n",
    "(b) How much can $N$ be increased if the computation needs to be run in less than a second? What is the gain in running it for 1 minute? Use `timeit` to measure the time."
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
      "1.5691342555492505\n",
      "1.5707963267948966\n",
      "1.5707963266264928\n",
      "1.5707963267948966\n",
      "The time is about 1 second :  2.5470131999999808\n",
      "1.5707963267942726\n",
      "1.5707963267948966\n",
      "The time is about 1 minute : 141.90151840000004\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "import timeit\n",
    "starttime = timeit.default_timer()\n",
    "def func(N):\n",
    "    lim_1 = -1  \n",
    "    lim_2 = 1\n",
    "    h = (lim_2 - lim_1) / N\n",
    "    I = 0 \n",
    "    for k in range(N):\n",
    "        x = lim_1 + h * k\n",
    "        y_k = math.sqrt(1-x**2)\n",
    "        I += h* y_k\n",
    "    print(I)\n",
    "    print(math.pi/2)\n",
    "\n",
    "# a) The answers is similar but they are different from second float number.\n",
    "func(100)\n",
    "\n",
    "# b) if N = 4600000 the code run in less than a second\n",
    "starttime1 = timeit.default_timer()\n",
    "func(4600000)\n",
    "print(\"The time is about 1 second : \" , timeit.default_timer() - starttime1)\n",
    "\n",
    "# c) if N = 280000000 the code run in less than a minute and the answers is similar but they are different from 11th float number.\n",
    "starttime2 = timeit.default_timer()\n",
    "func(280000000)\n",
    "print(\"The time is about 1 minute :\" , timeit.default_timer() - starttime2)"
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
 "nbformat_minor": 2
}
