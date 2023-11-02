#These are the solutions of the tasks presented in the first set of exercises, described in the file 02ex_fundamentals.ipynb

#Exercise 1
#Exercise on number conversion. The input is seen as a string and from then it is modeled as requested for the output.

def converter(inp, notation_out):
    if (type(inp)!=str):
        print("The input should be a number in a bin, dec or hex representation passed as a string and the notation in output should be 'binary', 'decimal' or 'hexadecimal'")
    else:
        if (inp[1]=='b'):
            print("The input type is: binary")
            number_in = 0
            real_len = len(inp)-2
            for i in range(0, real_len):
                number_in += int(inp[i+2])*(2**(real_len-i-1))
            if (notation_out=='binary'):
                return bin(number_in)
            if (notation_out=='decimal'):
                return int(number_in)
            if (notation_out=='hexadecimal'):
                return hex(number_in)
        if (inp[1]!='b')and(inp[1]!='x'):
            print("The input type is: decimal")
            number_in = int(inp)
            if (notation_out=='binary'):
                return bin(number_in)
            if (notation_out=='decimal'):
                return int(number_in)
            if (notation_out=='hexadecimal'):
                return hex(number_in)
        if (inp[1]=='x'):
            print("The input type is: hexadecimal")
            number_in = 0
            hex_dig = '0123456789abdef'
            real_len = len(inp)-2
            for i in range(0, real_len):
                number_in += (hex_dig.index(inp[i+2]))*(16**(real_len-i-1))
            if (notation_out=='binary'):
                return bin(number_in)
            if (notation_out=='decimal'):
                return int(number_in)
            if (notation_out=='hexadecimal'):
                return hex(number_in)
        else:
            print("The string does not correspond to a bin, dec or hex representation of a number")

#This part is just to prove the code works as expected. Removing the '#' will print the different results.       
#z = "10"
#c = "0xa"
#print(converter(z, "binary"))
#print(converter(z, "decimal"))
#print(converter(z, "hexadecimal"))
#print(converter(c, "binary"))
#print(converter(c, "decimal"))
#print(converter(c, "hexadecimal"))

#Exercise 2
#This code converts a binary string of 32 bits in a floating number. It is important to notice that this code adds a number of 
#zeroes in front of the string passed if this has less than 32 characters but it does not deal with input different than a binary
#string. As usual, if we were to take into account also for different inputs (not requested) we could have used an if statement
#or a try/except construct.
print("\n \n \n ")

def floater(string):
    in_len = len(string)
    if(in_len<32):
        m = 32-in_len
        for i in range(0, m):
            string = '0'+string
    s = int(string[0])
    bias = 127
    exp_raw = string[1:9]
    exp = 0
    length = len(exp_raw)
    for i in range(0, length):
        exp += int(exp_raw[i])*(2**(length-i-1))
    t = exp-bias
    mant_raw = string[9:]
    mantissa = 0
    mant_len = len(mant_raw)
    for i in range(0, mant_len):
        mantissa += int(mant_raw[i])/(2**(i+1))
    if (s==1):
        return -(1+mantissa)*2**t
    else:
        return (1+mantissa)*2**t

#The following code is written just to confirm that the function defined is up to what I was looking for. 'a' is not composed of
#32 bits so this examples shows that the code also adds the 0s in front of the binary string in order to get the right floating 
#number.
a = '110000101011000000000000'
print(len(a))
b = floater(a)
print(b)

#Exercise 3
#This code finds the maximum and minimum number achievable by my computer. The while loops are designed so that they show the current 
#numbers they are working on, whereas the last print() function just shows the maximum and minimum numbers obtainable plus the respective 
#number of iterations.
print("\n \n \n ")

import decimal
#By executing the code I find that the under/over-flow limit.
under = 1
over = 1
counter_ov, counter_un = 0, 0
factor = 2
while((under/2)!=0):
    under = under/2
    counter_un += 1
    print("%2d"%counter_un,"%2.7e" %under)
while(over<float('inf')):
    try:
        #under = under/2
        over = over*2
        counter_ov += 1
        print("%2d"%counter_ov,"%2.7e" %over)
        #print("%2d"%counter,"%2.5e" %under)
    except:
        break
sci_over = decimal.Decimal(over)
print("Iterations for the overflow: ", counter_ov,". Maximum number achieved: ", format(sci_over, '2.5e'),".\nIterations for the underflow: ", counter_un, "Minimum number achieved: ", under, ".")

#Exercise 4
#Exercise on machine precision. There are 2 methods presented, however the second one is more reliable and accurate so the first  
#is presented as just comments.
print("\n \n \n ")

#x = 0
#lit = 1
#counter = 0
#for i in range(2000):
#    y = x
#    lit = lit/2
#    x += lit
#    counter += 1
#    print(counter, x, y, lit)
#    if(y==x):
#        print("Maximum precision: ", lit)
#        break


#Second method (more reliable) to obtain machine precision
x = 1
while(x+1 != 1):
    x = x/2
#x*2 corresponds to the number which is too small to have an effect in the sum with 1
print("Maximum precision: ", x*2)

#Exercise 5
#Exercise on the quadratic formula.
print("\n \n \n ")

import math

def roots(a, b, c):
    num_1 = -b+((b**2)-4*a*c)**(1/2)
    num_2 = -b-((b**2)-4*a*c)**(1/2)
    print("First solution: ", num_1/(2*a))
    print("Second solution: ", num_2/(2*a))
    
a = 0.001
b = 1000
c = 0.001
roots(a,b,c)
#Second task: smaller numbers to be dealt with.
def roots2(a, b, c):
    num_1 = (-b+((b**2)-4*a*c)**(1/2))*(-b-((b**2)-4*a*c)**(1/2))
    num_2 = (-b-((b**2)-4*a*c)**(1/2))*(-b+((b**2)-4*a*c)**(1/2))
    num_a = (-b)**2-(((b**2)-4*a*c)**(1/2))**2
    num_b = (-b)**2-(((b**2)-4*a*c)**(1/2))**2
    den_1 = 2*a*(-b-((b**2)-4*a*c)**(1/2))
    den_2 = 2*a*(-b+((b**2)-4*a*c)**(1/2))
    print("First solution, slightly different formula: ", num_a/den_1)
    print("Second solution, slightly different formula: ", num_b/den_2)

roots2(a,b,c)
#Answer to the second question: as we can see from the results, the ones obtained with the second method are different(just one
#of the two solutions) and this is because of the limits of Python in expressing floating numbers with precision. In this case, 
#when the number becomes too little than the computer starts rounding it thus leading to an inaccurate result.
def roots3(a, b, c):
    num_1 = (-b+math.sqrt((b**2)-4*a*c))*(-b-math.sqrt((b**2)-4*a*c))
    num_2 = (-b-math.sqrt((b**2)-4*a*c))*(-b+math.sqrt((b**2)-4*a*c))
    den_1 = 2*a*(-b-(math.sqrt(b**2)-4*a*c))
    den_2 = 2*a*(-b+math.sqrt((b**2)-4*a*c))
    x1,y1 = (num_1/den_1).as_integer_ratio()
    x2,y2 = (num_2/den_2).as_integer_ratio()
    #print(x1/y1, x2/y2)
    print("First solution, always right formula: ", x1/y1)
    print("Second solution, always right formula: ", x2/y2)

roots3(a,b,c)
#In this case, we make use of the function as_integer_ratio(), which returns the float number as a fraction, which is then 
#computed to find the exact value. The float expressed as a fraction makes it possible to determine the accurate number

#Exercise 6
#Exercise on the derivative
print("\n \n \n ")

def function1(num_1):
    if(type(num_1)==int)or(type(num_1)==float):
        return num_1*(num_1-1)
    else:
        return "The input should be an integer"
x = 1
delta = 10**(-2)
num = function1(x+delta) - function1(x)
den = delta
der = num/den
real_der = 2*x-1
print("Value obtained using the definition: ", der)
print("Real value of the derivative: ", real_der)
print("The difference between the two values is: ", abs(der-real_der))
#The value printed is 1.010000000000001, while the actual value when computed analytically is just 1.
#The inaccuracy in the result given by the program is due to the delta being still too large: when we compute the limit we are taking
#smaller and smaller value of delta close to 0, so delta=10^-2 is still too large.
delta1 = 10**-4
delta2 = 10**-6
delta3 = 10**-8
delta4 = 10**-10
delta5 = 10**-12
delta6 = 10**-14
num1, num2, num3, num4, num5, num6 = function1(x+delta1) - function1(x), function1(x+delta2) - function1(x), function1(x+delta3) - function1(x), function1(x+delta4) - function1(x), function1(x+delta5) - function1(x), function1(x+delta6) - function1(x)
der1, der2, der3, der4, der5, der6 = num1/delta1, num2/delta2, num3/delta3, num4/delta4, num5/delta5, num6/delta6
#Answer to the second task: as we decrease the value of delta the result gets closer and closer to the right value. However if we take a too 
#little delta than the numbers are not accurately computed anymore and the result starts increasing.
print("With delta=", delta1, " : ", der1)
print("With delta=", delta2, " : ", der2)
print("With delta=", delta3, " : ", der3)
print("With delta=", delta4, " : ", der4)
print("With delta=", delta5, " : ", der5)
print("With delta=", delta6, " : ", der6)
def accuracy(num_1, num_2):
    return abs(num_1-num_2)*100
acc1, acc2, acc3, acc4, acc5, acc6 = accuracy(der1,x), accuracy(der2,x), accuracy(der3,x), accuracy(der4,x), accuracy(der5,x), accuracy(der6,x)
#As we can see from the various print() function, the best delta is 10^-8. The accuracy, expressed in %, represent how much the value of the 
#derivative calculated with the respective delta differs from the actual value, which is 1. As we can easily see, this difference has the littlest 
#value for delta=10^-8
print("Accuracy with delta=", delta1, " : ", acc1, "%")
print("Accuracy with delta=", delta2, " : ", acc2, "%")
print("Accuracy with delta=", delta3, " : ", acc3, "%")
print("Accuracy with delta=", delta4, " : ", acc4, "%")
print("Accuracy with delta=", delta5, " : ", acc5, "%")
print("Accuracy with delta=", delta6, " : ", acc6, "%")

#Exercise 7
#Exercise on the value of the integral.
print("\n \n \n ")

import timeit
def integral_R(N):
    value = 0
    h = 2/N
    for i in range(1, N+1):
        value += h*((1-((-1+(i-1)*h))**2)**(1/2))
    return value
result = integral_R(100)
print(result)
#It is smaller than the accurate value because N is too small (its value should be much higher).
#DISCLAIMER: the value of number is set to 1 and therefore the computation is done only once. This means that the values we obtain 
#are not very reliable as if we compute the code again we could get similar but still different. If we set a higher value of number 
#then we obtain a much more reliable result, however the number of N obtained is much littler.
def measure_exec_time(N):
    return timeit.timeit(lambda: integral_R(N), number=1)
max_N_sec = 1
while(measure_exec_time(max_N_sec)<1):
    t = max_N_sec *2
    print(max_N_sec)
    if(measure_exec_time(t)<1):
        max_N_sec *= 2
    else:
        max_N_sec += 100
print("The maximum N achieved under a second is: ", max_N_sec)
max_N_min = 1
while(measure_exec_time(max_N_min)<60):
    print(max_N_min)
    max_N_min += 1000000
maxN_minute = max_N_min-1000000
print("The maximum N achieved in a minute is: ", maxN_minute)
print("The value of the integral obtained with N max is: ", integral_R(maxN_minute))

#The gain in running the function for a minute is that the result given by the function will be much closer to the actual result of the integral.

#End of the exercises: I add an extra input in order to keep the code running for the last exercises.
input('Press ENTER to close the second set of exercises')