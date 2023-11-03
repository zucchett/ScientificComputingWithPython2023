import math
import timeit


# 1. Number representation
def ConvertNumber(number, outputType):

    # 1.bin, 2. dec, or 3.hex

    if outputType == 1:
        return bin(number)
    elif outputType == 2:
        return str(number)
    elif outputType == 3:
        return hex(number)
    else:
        print("Wrong operation number....")

# means 1.bin, 2. dec, or 3.hex
# print(f"{ConvertNumber(number=25, outputType=3)}")


# 2. 32-bit floating point number
def BinaryToFloat(binaryStr):

    signBit = int(binaryStr[0])
    exponent = int(binaryStr[1:9], 2)
    fraction = int(binaryStr[9:], 2)

    exponentBias = 127
    mantissaBits = 23

    finalExponent = exponent - exponentBias

    mantissa = 1 + (fraction / (2**mantissaBits))

    result = (-1)**signBit * mantissa * 2**finalExponent

    return result

# print(BinaryToFloat("110000101011000000000000"))


# 3. Underflow and overflow
def FindLimits():

    underflowLimit = 1.0
    overflowLimit = 1.0

    while not (underflowLimit / 2 == 0):
        underflowLimit /= 2

    while not (overflowLimit * 2 == float('inf')):
        overflowLimit *= 2

    print(f"Underflow limit: {underflowLimit}")
    print(f"Overflow limit: {overflowLimit}")

# FindLimits()


# 4. Machine precision
def FindMachinePrecision():

    precision = 1.0

    while 1.0 + precision != 1.0:
        prePrecision = precision
        precision /= 100
        # print(f"Pre: {prePrecision}, Now: {precision}, 1 + {precision} = {1.0 + precision}")

    return prePrecision


# print(f"Machine precision: {FindMachinePrecision()}")


# 5. Quadratic solution

# 5. a
def StandardQuadratic(a=None, b=None, c=None):

    a = 0.001
    b = 1000
    c = 0.001

    difference = b**2 - 4*a*c
    sqrtDifference = math.sqrt(difference)

    if difference >= 0:

        firstRoot = (-b + sqrtDifference) / (2*a)
        secondRoot = (-b - sqrtDifference) / (2*a)

        print(
            f"A. StandardQuadratic -> Root 1st: {firstRoot}\tRoot 2nd: {secondRoot}")

        return firstRoot, secondRoot
    else:
        print("A. StandardQuadratic -> Has no any real roots")

        return None


# 5. b
def QuadraticReexpressed(a=None, b=None, c=None):

    a = 0.001
    b = 1000
    c = 0.001

    difference = b**2 - 4*a*c
    sqrtDifference = math.sqrt(difference)

    denominator = -b - sqrtDifference

    firstRoot = (2*c) / denominator

    secondRoot = (2*c) / (-b + sqrtDifference)

    print(
        f"B. QuadraticReexpressed -> Root 1st: {firstRoot}\tRoot 2nd: {secondRoot}")

    return firstRoot, secondRoot


# (c) Function to compute roots accurately
def QuadraticAccurate(a=None, b=None, c=None):

    a = 0.001
    b = 1000
    c = 0.001

    difference = b**2 - 4*a*c
    sqrtDifference = math.sqrt(difference)

    if difference >= 0:
        if b >= 0:

            firstRoot = (-b - sqrtDifference) / (2*a)
            secondRoot = (2*c) / (-b - sqrtDifference)

        else:

            firstRoot = (2*c) / (-b + sqrtDifference)
            secondRoot = (-b + sqrtDifference) / (2*a)

        print(
            f"C. QuadraticAccurate -> Root 1st: {firstRoot}\tRoot 2nd: {secondRoot}")

        return firstRoot, secondRoot
    else:
        print("C. QuadraticAccurate -> Has no any real roots")
        return None

# Answer: In the re-expressed formula, we avoid the direct subtraction. This can help mitigate cancellation errors, then we have more accurate results. While in part a, because we substract two close values, it might lead to a loss of precision.

# StandardQuadratic()
# QuadraticReexpressed()
# QuadraticAccurate()


# 6. The derivative
def Derivative():

    def f(x):
        return x * (x - 1)

    deltas = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]

    for delta in deltas:

        numerical_derivative = (f(1 + delta) - f(1)) / delta
        absolute_error = abs(1 - numerical_derivative)

        print(f"Delta = {delta}\t derivative = {numerical_derivative}\t error = {absolute_error}")

# a)
# the absolute error between the numerical derivative and the true derivative decreases when delta becomes smaller, meaning to achieve more accuracy, we lower the delta.

# b)
# This is because the numerical derivative is still an approximation. Reducing the delta improves the accuracy, but it does not eliminate the approximation error entirely.

# Derivative()



# 7. Integral of a semicircle
def Semicircle(x):
    return math.sqrt(1 - x**2)


def CalculateIntegral(N):

    h = 2 / N
    integralResult = 0
    for k in range(1, N + 1):

        xK = -1 + k * h
        integralResult += h * Semicircle(xK)

    trueValue = math.pi / 2
    error = abs(integralResult - trueValue)
    print(f"Result for N = {N}: {integralResult}\tTrue value: {trueValue}\tAbsolute error: {error}")

    return integralResult


def CalculateIntegralTimeit():

    nValues = [100, 1000, 10000, 100000, 1000000]
    executionTimes = []

    iterations = 100

    for N in nValues:
        executionTime = timeit.timeit(
            lambda: CalculateIntegral(N), number=iterations)
        executionTimes.append(executionTime)

    for N, timeTaken in zip(nValues, executionTimes):
        print(f"N = {N}, Execution Time ({iterations} iterations): {timeTaken:.6f} seconds")

    estimatedGains = [(60 / timeTaken) for timeTaken in executionTimes]
    for N, gain in zip(nValues, estimatedGains):
        print(f"Estimated Gain for N = {N}: {gain:.0f} times")


# CalculateIntegral(100)
# CalculateIntegralTimeit()

# a) For me it was reported: Absolute error: 0.0016620712456461018, so the result is very close to true value.

# b)
# Therefore, the largest N that can be computed up to one second is N = 10000 which is around 1.016408 for me.
# To estimate the gain in running the computation for 1 minute, we can calculate how many times the computation can be performed in 1 minute, we select N = 10000 as it is the largest N to be computed up to 1 second.
# After running the function, for me it can be runned 59 times.
# Estimated Gain for N = 10000: 59 times
