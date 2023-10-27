import math
import numpy

# ################## exercise 1 ##################
# print("\n--- --- EXERCISE 1 --- ---")
# print("--- bin hex dec conversions ---\n")

# def convert (num, destination):
#     match num[1]:
#         case 'b':
#             print("the detected base is BIN")
#             num = int(num, 2)
#         case 'x': 
#             print("the detected base is HEX")
#             num = int(num, 16)
#         case _:
#             print("the detected base is DEC")
#             num = int(num)
        
#     match destination:
#         case 1:
#             return int(num)
#         case 2:
#             return bin(num)
#         case 3:
#             return hex(num)

# print("the number prefix is 0x for HEX, 0b for BIN and no prefix for DEC.")
# num = input("please insert a number in HEX, BIN or DEC: ")
# print("select the destination base")
# print("\t1 for DEC")
# print("\t2 for BIN")
# print("\t3 for HEX")
# try:
#     destination = int(input("please select 1, 2 or 3: "))
#     num = convert(num, destination)
#     print("the conversion yields", num)
# except:
#     print("not a valid number!")


# input("\npress ENTER to proceed to the next exercise...")

# ################## exercise 2 ##################
# print("\n--- --- EXERCISE 2 --- ---")
# print("--- single precision float ---\n")

# print("please enter a 32-bit binary string")
# theString = input()
# if(len(theString) != 32):
#     print("the string is not 32 bits long")
#     print("i will proceed to fill the remaining bits to zero")
#     theString = theString.ljust(32, '0')
#     print("the resulting string is")
#     print(theString)
# sign = 0
# if(theString[0] == '0'):
#     sign = +1
# else:
#     sign = -1
# print("sign=", sign)
# exp = int(theString[1:9], 2) - 127
# print("exponent=", exp)
# mantissa = 1
# for i in range(9, 32):
#     if(theString[i] == '1'):
#         mantissa += 1/(2**(i-8))
# print("mantissa=", mantissa)
# out = sign*mantissa*(2**exp)
# print("the float representation is", out)
# input("\npress ENTER to proceed to the next exercise...")

# ################## exercise 3 ##################
# print("\n--- --- EXERCISE 3 --- ---")
# print("--- underflow and overflow ---\n")

# overflow = float(1)
# half = float()
# underflow = float(1)
# while abs(overflow*2) != float('inf'):
#     overflow = overflow*2
# print("overflow:", overflow)
# print("if we further multiply by 2, we obtain", overflow*2)

# while abs(underflow/2) != float(0):
#     underflow = underflow/2
# print("underflow:", underflow)
# print("if we further divide by 2, we obtain", underflow/2)
# input("\npress ENTER to proceed to the next exercise...")

# ################## exercise 4 ##################
# print("\n--- --- EXERCISE 4 --- ---")
# print("--- float precision ---\n")

# one = float(1)
# small = float(1)
# while one != one+small/2:
#     small = small/2
# print("the smallest I can add to 1 is", small)
# print("after that, addition has no effect")

# input("\npress ENTER to proceed to the next exercise...")

# ################## exercise 5 ##################

# def solve(a, b, c):
#     delta = math.sqrt(b**2-(4*a*c))
#     s1 = (-b+delta)/(2*a)
#     s2 = (-b-delta)/(2*a)
#     return (s1, s2)

# def stupidSolve(a, b, c):
#     delta = math.sqrt(b**2-(4*a*c))
#     s1 = ((-b+delta)*(-b-delta))/((2*a)*(-b-delta))
#     s2 = ((-b-delta)*(-b+delta))/((2*a)*(-b+delta))
#     return (s1, s2)

# def betterStupidSolve(a, b, c):
#     delta = math.sqrt(b**2-(4*a*c))
#     s1 = ((-b+delta)/(2*a))*((-b-delta)/(-b-delta))
#     s2 = ((-b-delta)/(2*a))*((-b+delta)/(-b+delta))
#     return (s1, s2)

# print("\n--- --- EXERCISE 5 --- ---")
# print("--- quadratic ---\n")
# print("solve quadratic ax^2+bx+c=0")
# try:
#     a = float(input("insert a: "))
#     b = float(input("insert b: "))
#     c = float(input("insert c: "))

#     (s1, s2) = solve(a, b, c)
#     print("\nfirst correct solution x1 =", s1)
#     print("second correct soltion x2 =", s2)

#     (s1, s2) = stupidSolve(a, b, c)
#     print("\nfirst dumb solution x1 =", s1)
#     print("second dumb soltion x2 =", s2)

#     print("this is the solution multiplying and dividing by -b*delta")
#     print("the smaller root is accurate, but x2 is different.")
#     print("this is because the result of a large number times (-b*delta)")
#     print("when divided by a small number (2a) has a worse approximation")
#     print("so when the value is big we get a bigger error.")
#     print("we can counter-measure this undesired effect by forcing to")
#     print("evaluate the division separately from the actual result.")
#     print("in this way we get that the result of the division")
#     print("(-b*delta)/(-b*delta) is more precise.")

#     print("\nthe result with the latter method is the following")


#     (s1, s2) = betterStupidSolve(a, b, c)
#     print("first better dumb solution x1 =", s1)
#     print("second better dumb soltion x2 =", s2)
# except:
#     print("please insert valid numbers")

# input("\npress ENTER to proceed to the next exercise...")

# ################## exercise 6 ##################
# print("\n--- --- EXERCISE 6 --- ---")
# print("--- derivative ---\n")

# def fun(x):
#     return x*(x-1)

# def derivate(fun, x, delta):
#     return (fun(x+delta) - fun(x))/delta

# def analyticalDreivative(x):
#     return 2*x-1

# deltas = [10**(-2*x) for x in range(1, 8)]
# print("f(1)=", fun(1))
# errors = []
# for delta in deltas:
#     print("delta=", delta, "\tf'(1)=", derivate(fun, 1, delta), "\tanalytical f'(1)=", analyticalDreivative(1))
#     error = derivate(fun, 1, delta) - analyticalDreivative(1)
#     print("\t\terror=", error)
#     errors.append(error)

# print("""\nthe two values differ because of two things:
# first of all, from a mathematical standpoint, the definition
# of derivative has a limt for delta approaching zero. we are, 
# however, using a small but finite and non infinitesimal value 
# for delta, leading to an error. this is the dominant factor
# for the first terations where the delta is not too small. 
# then, as we decrease the value of delta, the error becomes 
# dominated by the fact that we are dividing a small difference 
# by a really small value, so the floating point representation 
# starts to break down.""")

# input("\npress ENTER to proceed to the next exercise...")

################## exercise 7 ##################
print("\n--- --- EXERCISE 7 --- ---")
print("--- integral ---\n")

def circle(x):
    return math.sqrt(1-x**2)

def riemann(fun, steps, start, end):
    integral = 0
    for x in numpy.linspace(start, end, steps):
        integral += ((end-start)/steps)*(fun(x))
    return integral

print("calculating the integral of a unit radius semicircle")
steps = 100
area = riemann(circle, steps, -1, 1)
print("using", steps, "iterations: ", area)
print("approximate error:", math.pi/2-area)

if __name__ == '__main__':
    import timeit
    time_exec = 0
    print("\ngradually increasing number of steps to get to 1 second...")
    print("this can be different based on the CPU and running tasks\n")
    steps = 1000000
    while time_exec < 1:
        launchStr = "riemann(circle,"+str(steps)+", -1, 1)"
        time_exec = timeit.timeit(launchStr, setup="from __main__ import riemann, circle", number = 1)
        steps += 100000
        print(steps, "steps: %.6fs" % time_exec)
    print("\nwith", steps, "steps, we get:")
    area = riemann(circle, steps, -1, 1)
    error = math.pi/2 - area
    print("calculated area:", area)
    print("error:", error)

    print("\ntrying to run the code for a minute, we get the following:")
    print("the result is already calculated, if you want to repeat the")
    print("calculations, please remove the comment in the code\n")

    # area = riemann(circle, steps*60, -1, 1)
    # error = math.pi/2 - area
    # print("calculated area:", area)
    # print("error:", error)

    print("calculated area: 1.570796314893865")
    print("error: 1.1901031493621872e-08")

    print("\nthe increase in precision is only marginal.")

input("\npress ENTER to exit...")


