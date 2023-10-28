import sys
import timeit
import math

#esercizio 1
print('Exercise 1')

def converter(value, type):
    if type == 'dec':
        return int(value)
    elif type == 'bin':
        return bin(value)
    elif type == 'hex':
        return hex(value)

print('1011 in decimal: ', converter(0b1011, 'dec'))
print('1011 in hexadecimal: ', converter(0b1011, 'hex'))
print('20 in binary: ', converter(20, 'bin'))
print('20 in hexadecimal: ', converter(20, 'hex'))
print('AF in decimal: ', converter(0xaf, 'dec'))
print('AF in binary: ', converter(0xaf, 'bin'))
print('')

#esercizio 2
print('Exercise 2')

#bin_string = '110000101011000000000000'
bin_string = '11000000101100000000000000000000' #-5.5

def bin_to_float(str_value):
    sign = int(str_value[0])
    exp = int(str_value[1:9], 2) - 127
    mantissa = 1.0

    k=1
    for i in range(9, 32):
        mantissa = mantissa + int(str_value[i])/2**k
        k+=1

    return -1**sign * mantissa * 2**exp

print('Value in decimal: -5.5, obtained: ', bin_to_float(bin_string))
print('')

#esercizio 3
print('Exercise 3')

def overflow(n):
    temp = n
    #with math.isinf() when the value in too big to be converted into float python generets an exeption, and catching it 
    #we can define the overflow value of float
    try:
        while not math.isinf(n):
            temp = n
            n = n*2
    except:
        return format(temp, '1E')

def underflow(n):
    temp = n
    while n > 0.0:
        temp = n
        n = n/2
    return temp

print('Overflow: ', overflow(1))
print('Underflow: ', underflow(1))
print('')

#esercizio 4
print('Exercise 4')

def precision(n):
    done = True
    unit = 1
    temp = n
    while done:
        unit = unit/2
        temp = n
        n = n + unit
        if temp == n:
            done = False
    return unit

print('Minimum adding which was ininfluence in the sum function: ', precision(3))
print('')

#esercizio 5
print('Exercise 5')

def square_eq(a, b, c):
    delta = math.sqrt(b**2 - 4*a*c)
    roots = []
    if delta >= 0:
        roots.append((-1*b + delta)/(2*a))
        roots.append((-1*b - delta)/(2*a))
    
    return roots

def new_square_eq(a, b, c):
    delta = math.sqrt(b**2 - 4*a*c)
    roots = []
    if delta >= 0:
        roots.append((-1*b + delta) * (-1*b - delta) / (2*a) * (-1*b - delta))
        roots.append((-1*b - delta) * (-1*b + delta) /(2*a) * (-1*b + delta))

    return roots

sol = square_eq(0.001, 1000, 0.001)
sol2 = new_square_eq(0.001, 1000, 0.001)
if len(sol) > 0:
    print('Roots for a=0.001, b=1000 and c=0.001 are: ', sol[0], ' and ', sol[1])
else:
    print('The equation does not have roots')

if len(sol2) > 0:
    print('Roots for a=0.001, b=1000 and c=0.001 with the new function are: ', sol2[0], ' and ', sol2[1])
else:
    print('The equation does not have roots')

'''
The solutions in the second method are not so accurate, 
probably because of the moltiplication added. This creates less accuracy due to the approximation
given by the finit numbers float can represent
'''
print('')

#esercizio 6
print('Exercise 6')

def f(x):
    return x*(x+1)

def derivate(f, x):
    result = []
    #f'(x) = 2x + 1
    analitic = 2*x + 1

    for i in range(2, 14, 2):
        delta = 10**-i
        result.append((f(x + delta) - f(x))/ delta)

    result.append(analitic)
    return result
result = derivate(f, 1)

print("Derivate of the function f(x) = x(x + 1) in x = 1 with in analitic method -> x = ", result[len(result)-1], '\n')
k=0
for i in range(2, 14, 2):
    print("Derivate of the function f(x) = x(x + 1) in x = 1 with delta = 10^-",i, " -> x = ", result[k])
    print("Gap with the analitic result: ", math.fabs(result[k] - result[len(result)-1]), '\n')
    k+=1

print('More the delta is lower, higher is the precision of the derivate function till delta is upper then 10^-8.')
print('After the precision starts getting worse, probably because of approximation problem of float numbers')
print('')

#esercizio 7
print('Exercise 7')

def semicircle(x):
    return math.sqrt(1 - x**2)

def riemann_int(f, N):
    h = 2/N
    sum = 0

    for k in range(N):
        sum = sum + h*f(1-k*h)

    return sum
result = riemann_int(semicircle, 100)

def N_measure():
    done = True
    i = 100
    while done:
        time = timeit.timeit(lambda: riemann_int(semicircle, i), number=1)
        if time < 1:
            #I choose this increment to keep the running time axceptable 
            #and it maintains a good precision
            i+=1000000
        else:
            done = False
    
    return i

def time_measure(N):
    t_init = timeit.default_timer()
    result = riemann_int(semicircle, N*60)
    t_end = timeit.default_timer()
    #print(t_end - t_init)
    return result

print('Riemann Integral: ', result)
N_onesec = N_measure()
print('The accuracy in % of Riemann integral with N = 100 is: ', (result/(math.pi*0.5))*100)
print('N can be increased up to: ', N_onesec, ' to keep the running time less then 1 second')
print('Result after elaborating for 60 seconds: ', time_measure(N_onesec))
'''
The difference between the two result is almost null, 
so it does not worth it discretize so much the domain
'''

