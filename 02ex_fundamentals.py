import copy

#Exercise 1
def exercise1():
    def f(alist,x):
        newlist = copy.copy(alist)

        for i in range(x):
            newlist.append(i)

        return newlist
    
    alist = [1, 2, 3]
    x = 5
    ans = f(alist,x)

    print(ans)
    print(alist)

#exercise1()


#Exercise 2
def exercise2():
    ans = [x*x for x in range(10) if x % 2 == 1]
    print(ans)

#exercise2()


#Exercise 3
def exercise3(words,n):
    ans = list(filter(lambda w: len(w) < n, words))
    return ans

#ex3_words = ["My", "name", "is", "Giovanni", "Giorgio"]
#ex3_n = 3
#ex3_ans = exercise3(ex3_words,ex3_n)
#print(ex3_ans)


#Exercise 4
def exercise4(lang):
    ans = list(map(len,lang.keys()))
    return ans

#ex4_lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
#ex4_ans = exercise4(ex4_lang)
#print(ex4_ans)
