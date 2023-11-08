list_A= []
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0 :
        list_A.append('HelloWorld')
    elif i % 3 == 0 :
        list_A.append("Hello")
    elif i % 5 == 0 :
        list_A.append("World")
    else :
        list_A.append(i)
print(f'the result for part A is : {tuple(list_A)}')

for i in range(0,len(list_A)) :
    if list_A[i] == 'Hello' :
        list_A[i] = 'Python'
    elif list_A[i] =='World' :
        list_A[i] = 'Works'
    elif list_A[i] =='HelloWorld':
        list_A[i] = 'pythonworks'
    else :
        continue    
print(f'the result for part B is : {tuple(list_A)}')     

#------------------------------------------------------------------------------------------
x = input('please insert "X" = ')
y = input('please insert "Y" = ')
x,y = y,x
print(f'the new result for "x" is = {x} and for "y" is {y}')
#-------------------------------------------------------------------------------------------------
import math
# in this part user should input value of the point for "x" and for "y", for example user insert 3,4 for "x" and 5,6 for "y", the input should be exactly like example.
x = tuple(input('please insert your first tuple : ').split(','))
y = tuple(input('please insert your second tuple : ').split(','))
x_value = int(x[0])-int(x[1])
y_value = int(y[1])-int(y[0])
distance = math.sqrt((x_value**2) + (y_value**2))
print(f'the distance is : {distance}')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
counter = {}
for i in s1:
    if i.isalpha() == True :
        i = i.upper()
        counter[i] = counter.get(i,0) + 1
print(counter)
#-----------------------------------------------------------------------------------------------------------------------------------------
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
unique_list = []

for i in l :
    if l.count(i) == 1 :
        unique_list.append(i)

print(f'this is our unique list : {unique_list}')
print(f'the number of unique number is : {len(unique_list)}')
#------------------------------------------------------------------------------------------------------------------------------------------------------
x1 = input('please insert your first variables : ')
x2 = input('please insert your second variables : ')
input_list,int_list,float_list,str_list= [x1,x2],[],[],[]
for i in range(0,2) :
    try :
        int_list.append(int(input_list[i]))
    except :
        try :
            float_list.append(float(input_list[i]))
        except :
            str_list.append(input_list[i])

final_list = int_list + float_list + str_list
try : 
    print(f'the sum of the value is : {sum(final_list)}')
except :
    print(f'These entries cannot be added together, and the result is : {final_list[0]} + {final_list[1]}')  
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
# the code for the the part A of the question : 
list_1 = []
for i in range(0,11) :
    list_1.append(i**3)
print(f'the list with "for" loop is like :  {list_1}')
# the code for the part B of the question : 
list_2 = []
list_2 = [i**3 for i in range(0,11)]
print(f'the list with "list comprehention is like that : {list_2}')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
import itertools
result_list = [(i,j) for i,j in itertools.product([0,1,2],[0,1,2,3])]
print(result_list)
#-----------------------------------------------------------------------------------------------------------------------------
#we have the limitation for "c" that it should be smaller than 100
m,n,result_list,c= 2,1,[],0
while c < 100 :
    for n in range(1,m+1):
        a = ((m**2) - (n**2))
        b = 2 * m * n
        c = ((m**2) + (n**2))
        if a == 0 or c > 100 :
            break
        else :
            result_list.append((a,b,c))
    m += 1
print(result_list)
#--------------------------------------------------------------------------------------------------------------------------------------
from math import sqrt
# we insert a vector in list for example :
vector,sum= [1,4,6,7,5,6],0
for  i in vector :
    sum  = sum + (i**2)
total = sqrt(sum)
normal_vector = [i/total for i in vector]
print(normal_vector)
#---------------------------------------------------------------------------------------------------------------------------------------------
fibo_list = [0,1,1]
for i in range (3,19):
    next_fibo_value = fibo_list[i-2] + fibo_list[i-1]
    fibo_list.append(next_fibo_value)
print(fibo_list)    
#--------------------------------------------------------------------------------------------------------------------------------------------------