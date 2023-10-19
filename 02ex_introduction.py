###################1. Global variables####################
print("###################START 1. Global variables###################")
x = 5
def f(alist):
    alist = list(alist)
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed

###################2. List comprehension####################
print("###################START 2. List comprehension###################")
print_odd_squared = [i**2 for i in range(1,10,2)]
print(print_odd_squared) 

###################3. Filter list####################
print("###################START 3. Filter list###################")
def check_words(word, n):
    return len(word) < n

words = ['Write', 'a', 'Python', 'program', 'that', 'sorts', 'the', 'following', 'list', 'of', 'tuples', 'using', 'a', 'lambda', 'function']
n = 5
filtered_words = list(filter(lambda word: check_words(word, n), words))
print(filtered_words)

###################4. Map dictionary####################
print("###################START 4. Map dictionary###################")
def get_key_size(word):
    return len(word)

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
key_size_lsit = list(map(get_key_size, lang))
print(key_size_lsit)

###################5. Lambda functions####################
print("###################START 5. Lambda functions###################")

