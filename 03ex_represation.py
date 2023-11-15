#PRE
import math
import timeit
from decimal import Decimal
decider = 3
decider = "ALL"

#####################################################################################################
# Exercise 1 
if decider == 1 or decider == "ALL":
    if decider == "ALL":
        print("--------------------------------Exercise 1-------------------------------------")

    def converter(n, change_to):
    
        if isinstance(n, int) == True:
            if change_to == 'bin':
                result = bin(n)
            elif change_to == 'dec':
                result = str(n)
            elif change_to == 'hex':
                result = hex(n)
            
            print(f"{n} in {change_to} is: {result}")

        elif isinstance(n, str) == True:
            n = n.strip()
            if n.startswith("0b"):
                temp = int(n,2)
                if change_to == 'bin':
                    result = n
                elif change_to == 'dec':
                    result = temp
                elif change_to == 'hex':
                    result = hex(temp)

            elif n.startswith("0x"):
                temp = int(n,16)
                if change_to == 'bin':
                    result = bin(temp)
                elif change_to == 'dec':
                    result = temp
                elif change_to == 'hex':
                    result = n
            else:
                n = int(n)
                if change_to == 'bin':
                    result = bin(n)
                elif change_to == 'dec':
                    result = n
                elif change_to == 'hex':
                    result = hex(n)

            print(f"{n} in {change_to} is: {result}")
        return result

    # Usage
    A = 25
    B,C,D,E,F = 0b11001,0x19,"25",bin(A),hex(A)
    Example = [A,B,C,D,E,F,"bin","dec","hex"]

    for j in range(3):
        temp = Example[len(Example)-3+j]
        for i in range(len(Example)-3):
            converter(Example[i],temp)
            
  
#####################################################################################################
# Exercise 2 
if decider == 2 or decider == "ALL":
    if decider == "ALL":
        print("--------------------------------Exercise 2-------------------------------------\n")

    def bin_to_single(binary_str):

        # preliminaries
        bias = 127
        mantissa = 0

        # Extraction - sign and exponent
        sign = int(binary_str[0])
        exponent = int(binary_str[1:9], 2) - bias

        # Extraction - mantissa
        for i in range(1,len(binary_str[10:])+1):
            temp = int(binary_str[9:][i-1])*pow(1/2,i)
            mantissa += temp 

        # Resolving the sign
        if sign == 0: 
            mantissa += 1
        if sign == 1:
            mantissa = -1*(mantissa + 1)

        # Final result
        value = mantissa*pow(2,exponent)

        return value

    # Usage
    binary_str = "10000100100011001000000000000000"
    result = bin_to_single(binary_str)
    print(binary_str,"in single presision is:",result,"\n")


#####################################################################################################
# Exercise 3 
if decider == 3 or decider == "ALL":
    if decider == "ALL":
        print("--------------------------------Exercise 3-------------------------------------\n")

    Underflow = 1.0
    Overflow = 1.0

    # Underflow
    while True:
        temp = Underflow / 2.0
        if temp == 0.0:
            break
        Underflow = temp

    # Overflow
    while True:
        temp_2 = Overflow * 2.0
        if temp_2 == float('inf'):
            break
        Overflow = temp_2

    print("Approximate underflow and overflow limits are", Underflow,"and",Overflow,"\n")




#####################################################################################################
# Exercise 4 
if decider == 4 or decider == "ALL":
    if decider == "ALL":
        print("--------------------------------Exercise 4-------------------------------------\n")

    n = 1.0
    temp = 1.0

    while (1.0 + temp) != 1.0:
        n = temp
        temp /= 2.0

    print("The machine precision for floating point numbers is:",n,"\n")


#####################################################################################################
# Exercise 5 
if decider == 5 or decider == "ALL":
    if decider == "ALL":
        print("--------------------------------Exercise 5-------------------------------------\n")

    def quadratic(a,b,c):
        discriminant = b**2 - 4*a*c
        sqrt_discriminant = math.sqrt(discriminant)
        x = [0,0,0,0,0,0]
        # a) - done
        x[0] = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        x[1] = (-b-math.sqrt(b**2-4*a*c))/(2*a)
        
        # b) - done 
        x[2] = (2*c)/(-b-math.sqrt(b**2-4*a*c))
        x[3] = (2*c)/(-b+math.sqrt(b**2-4*a*c))
        
        # c) 
        a = Decimal(str(a))
        b = Decimal(str(b))
        c = Decimal(str(c))
        
        x[4] = (2*c) / (-b - Decimal.sqrt(b**2-4*a*c)) 
        x[5] = (2*c) / (-b + Decimal.sqrt(b**2-4*a*c))

        print("Standart formula: x1 = ", x[0],"\n                  x2 = ",x[1],"\n")
        print("Re-expressed formula: x1 = ", x[2],"\n                      x2 = ",x[3],"\n")
        print("Corrected formula: x1 = ", x[4],"\n                   x2 = ",x[5],"\n")
    
    a, b, c = 0.001, 1000, 0.001

    quadratic(a,b,c)

"""
We can see that both results are close, but they are not the same. We would expect the results to be same because we are not changing the formula.
Floating point representation tends to be inaccurate when dealing with adding or subtracting very large and very small numbers - which is also our 
case. This error can be then propagated through the whole calculation resulting (in the worst case) in nonsensical result.Other source of error 
is due to nature of binary representation and the need of rounding. Computer representation does not allow recurring so even thou we can say 
that one-third is 0.333 with the last three recurring (example in base 10 - analogy to representing 1/10 in binary). Computer does not do that 
and it rounds up to have a finite number. This inevitably leads to errors.
"""

#####################################################################################################
# Exercise 6 
if decider == 6 or decider == "ALL":
    if decider == "ALL":
        print("--------------------------------Exercise 6-------------------------------------")
    
    def f(x):
        return x * (x - 1)

    def num_der(x, delta):
            return (f(x + delta) - f(x)) / delta

    def al_der(x):
            return 2*x - 1  

    point_of_interest = 1
    deltas = [1e-2, 1e-4, 1e-6, 1e-8, 1e-12, 1e-14]


    for delta in deltas:
        numeric_result = num_der(point_of_interest, delta)
        analytic_result = al_der(point_of_interest)
        print(f"For delta = {delta}:")
        print(f"Numeric derivative: {numeric_result}")
        print(f"True derivative: {analytic_result}")
        print(f"Absolute error: {abs(numeric_result - analytic_result)}")
        print() 

    print(
    """
    Numeric and analytic derivation is close but there is an error. The source of this error is adding or subtracting very large and very small numbers. 
    Even though we would expect that with increasingly small delta the error would go to zero, that is not the case. We are adding very small number to a 
    large number (with respect to delta) and that can signalize a potential for an error. \n""")


#####################################################################################################
# Exercise 7
if decider == 7 or decider == "ALL":
    if decider == "ALL":
        print("--------------------------------Exercise 7-------------------------------------\n")

        # Define the function that represents the semicircle
    def semicircle(x):
        return math.sqrt(1 - x**2)

    # Riemann sum function
    def riemann_integral(N,lower_bound,upper_bound):
        h = 2.0 / N
        step = (upper_bound-lower_bound)/N
        integral = 0.0
        for k in range(N):
            x_k = lower_bound + k * step
            integral += semicircle(x_k) * h
        return integral

    #a)
    N = 100
    Boundary = [-1,1]
    Exact = math.pi/2
    Riemann = riemann_integral(N,Boundary[0],Boundary[1])
    error = abs(Exact-Riemann)

    print("Exact solution: ",Exact,"Riemann's integral: ",Riemann,"Error: ",error,"\n")

    print(
    """
    Error between exact and our solution is not zero. There is an error. The error is due to finite number 
    of N. In our solution we have a small width of our rectangle. In exact solution the width is infinitely small. 
    We can make it more accurate by increasing N. But even with very large N the two solutions will never be 
    exactly the same due to rounding errors described in the previous exercise. \n""")

    #b)
    time_seconds = 1.0
    time_minutes = 60.0  

    max_N = 1
    
    print("Starting: Run in less than a second 1 second")
    while True:
        time_taken = timeit.timeit("riemann_integral(max_N,Boundary[0],Boundary[1])",globals=globals(), number=1000)
        if time_taken > time_seconds:
            break
        max_N += 100 
    
    print(f"Maximum N for computation in less than 1 second: {max_N} \n")

    print("Starting: Gain in running it for 1 minute")
    max_N_1_minute = 70000 # N for 1 minute

    Riemann = riemann_integral(max_N_1_minute,Boundary[0],Boundary[1])
    error = abs(Exact-Riemann)

    print("One minute gian: Exact solution: ",Exact,"Riemann's integral: ",Riemann,"Error: ",error,"\n")
    