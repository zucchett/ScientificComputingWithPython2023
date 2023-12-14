import math
import timeit
import sys
# ------------------ EX 1 ------------------
# 1)  Write a function that converts integer numbers among the bin, dec, and
# hex representations (bin<->dec<->hex). Determine the input type in the function, and pass another argument to choose the output representation.
print("1)  Conversion of integer numbers \n")
#pass the value as a string
def converter(value, output_type):
    #determines the input type
    if(value[1] == "b"):
        t = "bin"
    elif(value[1] == "x"):
        t = "hex"
    else: 
        t = "dec"
    
    converted = value

    #functions bin and hex receive a int as argument, not a str 
    #input of funct. is str -> it must be converted into int (decimal format) 
    if t == "dec":
        dec = int(value)
        if output_type == "bin":
            converted = bin(dec) 
        elif(output_type == "hex"):
            converted = hex(dec) 

    if t == "hex":         
        dec = int(value, 16)    
        if output_type == "bin":
            converted = bin(dec)
        elif(output_type == "dec"):
            converted = dec
            
    if t == "bin":  
        #input is str -> it must be converted into int (decimal format)    
        dec = int(value, 2)  
        if output_type == "hex":
            converted = hex(dec) 
        elif(output_type == "dec"):
            converted = dec
    
    return converted


# input binary
a_bin = "0b111"
print("input value binary format -->", a_bin)
c_dec = converter(a_bin, "dec") 
print("dec -->", c_dec)
c_hex = converter(a_bin, "hex")
print("hex -->", c_hex)


# input hexadecimal
a_hex = "0xAF2"
print("input value hexadecimal format -->", a_hex)
c_dec = converter(a_hex, "dec") 
print("dec -->", c_dec)
c_bin = converter(a_hex, "bin")
print("bin -->", c_bin)

# input decimal
a_dec = "34"
print("input value decimal format -->", a_dec)
c_bin = converter(a_dec, "bin") 
print("dec -->", c_bin)
c_hex = converter(a_dec, "hex")
print("hex -->", c_hex)

print("\n")

# ------------------ EX 2 ------------------
# 2)  converts a 32 bit binary string into a single precision floating point in decimal representation. 
print("2) Convert into single precision floating point")
def convert(v):
    bias = 127 #single precision floating point
    s = int(v[0],2)
    e = v[1:9]
    f = v[9:]
    #exponent in decimal format
    edec = int(e,2)
    print("s: ", s)
    print("e: ", e, "\ne decimal format", edec)
    print("f: ", f) 
    if(edec == 255 and int(f,2) > 0):
        converted = "NaN"
    elif(s == 0 and edec == 255 and int(f,2) == 0):
        converted = "+INF"
    elif(s == 1 and edec == 255 and int(f,2) == 0):
        converted = "-INF"
    else:
        f1 = 0
        for i in range(1,23):
            f1 = f1 + math.pow(2,-i)*int(f[i-1])    
        print("f decimal format: ", f1) 
        converted = math.pow(-1,s)*(math.pow(2,edec-bias)*(1+f1))

    return converted

num = "11000010101100000000000000000000" #-88
print(f"\nnum {num}")
c = convert(num)
print("Converted ->", c)
num2 = "0111111110000011110000000000000" #NaN
print(f"\nnum {num2}")
c2 = convert(num2)
print("Converted ->", c2)
num3 = "00111110100110011001100110011001" #0.3
print(f"\nnum {num3}")
c3 = convert(num3)
print("Converted ->", c3)
num4 = "11000000101100000000000000000000" #-5.5
print(f"\nnum {num4}")
c4 = convert(num4)
print("Converted ->", c4)
num5 = "01111111100000000000000000000000" #+INF
print(f"\nnum {num5}")
c5 = convert(num5)
print("Converted ->", c5)

print("\n")

# ------------------ EX 3 ------------------
#Write a program to determine the approximate underflow and overflow limits (within a factor of 2) for floating point numbers on your computer.
print("3) Approximation of underflow and overflow limits WITHIN A FACTOR OF 2")
under = 1.0
underlimit = under
over = 1.0
overlimit = over
#underflow
while(under != 0):
    underlimit = under
    under = under / 2 #"under" will become so small that it will be approximated to 0 --> underflow   
print("underflow limit = ", underlimit)

#overflow 
while(1/over):
    overlimit = over
    over = over * 2 #it will become so large that 1/over = 0
print("overflow limit = ", overlimit)

#in addition -> computes overflow limit by elevating 2 by 2
print("If we compute overflow limit elevating by 2: ", end = "")
over = 2.0
try:
    while(1):
        overlimit = over
        over = over ** 2 #it will cause a exception out of range
except:
    print(overlimit)

print("\n")

# ------------------ EX 4 ------------------
#write a program to determine the machine precision for floating point numbers.
("4) Machine precision for floating point numbers")
exp = 1 #used to compute epsilon
epsilon = 1.0* 10**-exp
n = 1.0
n_prev = -1.0
print("n = ", n)

#continues until the 2 consecutive numbers will be considered equal
while(n != n_prev): 
    n_prev = n
    #adding smaller value
    n += epsilon 
    print(f"n = n + epsilon = {n_prev} + {epsilon} = ", n)
    #making epsilon smaller
    exp += 1
    epsilon = 1.0 * 10**-exp
#last multiplication must be deleted
epsilon *= 10
print("\nepsilon = precision for floating point numbers = ", epsilon)
print("\nIf we want to express epsilon reducing it by a factor of 2")
#IN ADDITION if we want to express epsilon reducing it by a factor of 2:
eps = 2.0
n = 1.0
n_prev = -1.0
while(n != n_prev):
    n_prev = n
    #adding smaller value
    n += eps
    print(f"n = n + epsilon = {n_prev} + {eps} = ", n)
    #making epsilon smaller
    eps /= 2
eps = eps * 2 #last division detemines n = n_prev so we don't consider it
print("\nBy reducing by a factor of 2, epsilon = precision for floating point numbers = ", eps)
print("\n")

# ------------------ EX 5 ------------------
#Write a function that takes in input three parameters, a,b,c 
#prints out the two solutions to the quadratic equation
print("5) quadratic solution")
def quad_eq(a,b,c):
    x1 = (-b+math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
    return (x1, x2)

def quad_eq_modified(a,b,c):
    num1 = (-b+math.sqrt(math.pow(b,2)-4*a*c)) * (-b-math.sqrt(math.pow(b,2)-4*a*c))  
    den1 = (2*a) *  (-b-math.sqrt(math.pow(b,2)-4*a*c)) 
    num2 = (-b-math.sqrt(math.pow(b,2)-4*a*c)) * (-b+math.sqrt(math.pow(b,2)-4*a*c))  
    den2 = (2*a) *  (-b+math.sqrt(math.pow(b,2)-4*a*c))  
    x1 = num1 / den1
    x2 = num2 / den2
    return (x1, x2)

def quad_eq_closer(a,b,c):
    det = math.pow(b,2)-4*a*c
    det_square = math.sqrt(math.pow(b,2)-4*a*c)
    x1 = (-b)/(2*a) + (det_square)/(2*a)
    x2 = (-b)/(2*a) - (det_square)/(2*a)
    return (x1,x2)

def correct(a,b,c):
    det = math.pow(b,2)-4*a*c
    det_square = math.sqrt(math.pow(b,2)-4*a*c)
    num1 = (-b*10**9+det_square*10**9)/10**9
    num2 = (-b*10**9-det_square*10**9)/10**9
    x1 = num1 / (2*a)
    x2 = num2 / (2*a)
    return (x1, x2)

print("0.001(x^2) + 1000(x) + 0.001 = 0\n")

result = quad_eq(0.001, 1000, 0.001)
print("(x1,x2) =", result)

result2 = quad_eq_modified(0.001, 1000, 0.001)
print("with modified function (x1,x2) =", result2)

result3 = quad_eq_closer(0.001, 1000, 0.001)
print("with third function (x1,x2) =", result3)

correct = correct(0.001, 1000, 0.001)
print("correct(x1,x2) =", correct)


print("\nPrecision of result:")
diff = abs(result[0]) - 1*10**-6
diff_fromcloser = abs(result3[0]) - 1*10**-6
diff_fromcorrect = abs(correct[0]) - 1*10**-6
print("x1 - 1*10**-6 = ", diff)
print("x1_closer - 1*10**-6 = ", diff_fromcloser)
print("x1_correct - 1*10**-6 = ", diff_fromcorrect)

''' 
OBSERVATION:

0.001(x^2) + 1000(x) + 0.001 = 0
(x1,x2) = (-9.999894245993346e-07, -999999.999999)
with modified function (x1,x2) = (-9.999894245993346e-07, -999999.9999990001)

If we compute step by step the solution we have:
determinante = ( (1000)^4 - 4 ) / (1000)^2 = (999'999'999'996) / (1'000'000) = 999'999,999'996
Then we must compute the square -> math.sqrt(999'999,999'996) = 999,999'999'998 = R
Now the rest of formula is (-1000 +- (R)) / (2/1000)
    -1000 +999,999'999'998 = 2*(10)^(-9) 
    -1000 -999,999'999'998 = 1'999,999'999'998 

    Both of them must be divided by (2/1000):
    x1 = - 1*(10)^(-6) 
    x2 = - 999999.999999

The 2 results of quad_eq and quad_eq_modified differ only for the last digits of x2 (in the second case, by multiplying the numerator and the denominator, in the result 
compare other digits 0001). This probably happens due to problems of approximation when we substruct the 2 large numbers very similar each other (at the numerator) 
and then we multiply them.
In the third function I divide by (2a) the 2 terms (-b and the square of determinante) before adding them. As consequence, I obtain a different result,
closer to 1*10**-6 but not equal to it.

So I've decided to increment the order of magnitude of b and of the square before substracting them: I multiply them by 10^9. Then I've reduced the order (dividing the result by the same quantity)
This corresponds to multiply by 1
'''
print("\n")

# ------------------ EX 6 ------------------
#Write a program that implements the function x(x-1)
print("6) The derivative")
def f(x):
    return x*(x-1)

def derivative(fun,x):
    result = []
    for i in range(2,15,2):
        delta = 10**(-i)
        result.append(("delta = 10^-"+str(i), (fun(x+delta) - fun(x))/delta))
    return result

def an_derivative(x):
    return 2*x-1

der = derivative(f,1)
an_der = an_derivative(1)
print("\nderivative computed analytically in x = 1-> 2x-1 =", an_der)
print("Computation of derivative with formula, changing delta:")
for i in range(len(der)):
    print(der[i], "   difference between 2 computations =", abs(der[i][1] - an_der))

''' The value of derivative calculated with delta 10^(-2) is 1.010000000000001
and it differs from the value computed analytically which is = 1
This is due to the approximation introduced by the division between floating point numbers 
implemented in function "derivative". 
We observe that, decreasing delta, the accuracy seems to increase: in fact, the difference
between the 2 results becomes smaller (the value computed  with formula becomes more and more equal to 1.0).
However, when delta becomes < 10^-8, the value calculated with the formula becomes wrong: delta is too small, 
x+delta is considered equal to x. As consequence, the difference f(x+delta)-f(x) is approximated to 0 (the 2 terms are very close)
In fact, if we compute derivative with delta <= 10^-16 , the formula gives derivative = 0'''
delta = 10**(-16)
der = (f(1+delta) - f(1))/delta
print("delta = 10^-16", "   derivative with formula =" ,der , "   difference between 2 computations =", abs(der - an_der))
print("\n")

# ------------------ EX 7 ------------------
#Write a program to compute the integral with N=100. How does the result compare to the true value
print("7) integral of a semicircle")
def integralN(N):
    k = 1
    s = 0
    h = 2/N #slice_size = (1-(-1))/N
    #compute f(x_k) values
    for k in range(1,N+1):
        #taking intervals delta_x with size N/2
        x_k = -1 + h*(k-1) 
        #compute f in x_k
        f_x_k = math.sqrt(1 - (x_k)**2)
        #compute sum
        s = s + f_x_k*h
    return s 

N_input = 100
r = integralN(N_input)
print("integral r = ", r)
#How much can N be increased if the computation needs to be run in less than a second? 
start = 0
end= 0
t = 0
#to observe how the execution time changes when N increases
results_onesec = []
results_onemin = []
print("Now wait for computation...\nExecution in less than 1 sec")
while(t <= 1):
    N_input += 1000000 #we increases N to see how execution time changes 
    t = timeit.timeit(lambda: integralN(N_input),number=1)
    if(t <= 1):
        r = (t, N_input)
        results_onesec.append(r)

for i in range(len(results_onesec)):
    print("execution time %.5f" % results_onesec[i][0], "   N = ", results_onesec[i][1])

#What is the gain in running it for 1 minute?
#it stops when computation with N requires more than 1 min
N_input = 100
print("Now wait for computation...\nExecution in less than 1 min")
while(t <= 60):
    N_input *= 2 #now we can increment N in an exponential way since our "range of time" is bigger
    t = timeit.timeit(lambda: integralN(N_input),number=1)
    if(t <= 60):
        r = (t, N_input)
        results_onemin.append(r)

for i in range(len(results_onemin)):
    print("execution time %.5f" % results_onemin[i][0], "   N = ", results_onemin[i][1] )

'''
****************  results  ********************
Result is similar to the real one --> integral r =  1.5691342555492505
in 1 sec:
execution time 0.33845    N =  1000100
execution time 0.57422    N =  2000100
execution time 0.82528    N =  3000100 <-- integral r =  1.5707963264748595
in 1 min:
execution time 0.00005    N =  200
execution time 0.00010    N =  400
execution time 0.00022    N =  800
execution time 0.00045    N =  1600
execution time 0.00090    N =  3200
execution time 0.00181    N =  6400
execution time 0.00415    N =  12800
execution time 0.00710    N =  25600
execution time 0.01414    N =  51200
execution time 0.02868    N =  102400
execution time 0.05574    N =  204800
execution time 0.10873    N =  409600
execution time 0.21638    N =  819200
execution time 0.44253    N =  1638400
execution time 0.86865    N =  3276800
execution time 1.73249    N =  6553600
execution time 3.45041    N =  13107200
execution time 6.95915    N =  26214400
execution time 13.83652    N =  52428800
execution time 28.04093    N =  104857600
execution time 56.15172    N =  209715200 <-- integral r =  1.5707963267947422 
'''