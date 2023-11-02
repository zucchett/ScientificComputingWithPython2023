######################## NUMBER REPRESENTATION ########################
print("1. NUMBER REPRESENTION")
def convert_integer(num, base_output):
    if base_output == 'bin':
        return bin(num)
    elif base_output == 'dec':
        return str(num)
    elif base_output == 'hex':
        return hex(num)

if __name__ == "__main__":
    input_number = 502
    output_base = "dec"
    result = convert_integer(input_number, output_base)
    print(result)

###########################32-bit floating point number######################
print("2. 32-bit floating point number")

def convert_binary_float(bin):
    if len(bin) != 32:
        raise ValueError("The input binary must have exactly 32 bits!.")
    # Interpreting sign bit, exponent bits, and mantissa bits
    sign = int(bin[0])
    exponent = bin[1:9]
    mantissa = bin[9:]

    # Calculate the exponent and mantissa values
    exp_val = int(exponent, 2) - 127
    mantissa_val = 1.0

    for i in range(len(mantissa)):
        if mantissa[i]== '1':
            mantissa_val = mantissa_val+ 1 / (2 ** (i + 1))

    result= (-1) ** sign * 2 ** exp_val * mantissa_val
    return result

if __name__ == "__main__":
    bin_num= "110000101011000000000000"
    result = convert_binary_float(bin_num)
    print(result)

###########################Underflow and overflow######################
print("3. Underflow and overflow")
if __name__ == "__main__":
    overflow= 1.0
    underflow=1.0

    while underflow / 2 != 0.0:
        underflow /= 2
    while overflow * 2 != float('inf'):
        overflow = overflow*2
    print("The underflow limit:", underflow)
    print("The overflow limit:", overflow)
###########################Machine precision######################
print("4. Machine precision")
machine_precision= 1.0
while 1.0 + machine_precision / 2 != 1.0:
    machine_precision /= 2

print("Machine precision = ", machine_precision)

###########################Quadratic solution######################
print("5. Quadratic solution")
import math
def equation_solution(a, b, c):
    L=[]
    L[0]= (-b-math.sqrt(b**2-4*a*c))/2*a
    L[1]= (-b+math.sqrt(b**2-4*a*c))/2*a
    return(L)
if __name__ == "__main__":
    # a
    print("The result for a=0.001 , b=1000 and c = 0.001 is :", equation_solution(0.001,1000,0.001))
# b
def equation_solution_modified(a, b,c):
    L_mod=[]
    L_mod[0] = (2 * c) / (-b - math.sqrt(b ** 2 - 4 * a * c))
    L_mod[1] = (2 * c) / (-b + math.sqrt(b ** 2 - 4 * a * c))
    return (L_mod)
if __name__ == "__main__":
    print("The result for a=0.001 , b=1000 and c = 0.001 is :", equation_solution_modified(0.001,1000,0.001))

###########################The derivative######################
print("6. The derivative")

def function(x):
    return x*(x-1)
# a
delta = 0.01
x=1
derivate= (function(x + delta) - function(x)) / delta

# b
delta_list=[0.0001, 0.000001, 0.00000001, 0.0000000001]
for i in range(len(delta_list)):
    print((function(x + delta_list[i]) - function(x)) / delta_list[i])

###########################Integral of a semicircle######################
print("7. Integral of a semicircle")
import math
import timeit
def integral(N):
    radius = 1.0
    width = 2 * radius / N
    integral = 0.0
    # Calculate the integral using a loop
    for i in range(N):
        x = -radius + i * width
        y = math.sqrt(radius**2 - x**2)
        area = width * y
        integral += area
    return integral

if __name__ == "__main__":
    N = 100
    result= integral(N)
    print(result)
# b
    time_1s = timeit.timeit(lambda: integral(N), number=1)
    print(f"Time to compute for N", time_1s)

    N = 100000000
    time_1min = timeit.timeit(lambda: integral(N), number=1)
    print(f"Time to compute for Nis", time_1min)
