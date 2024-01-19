#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1
import numpy as np

m=np.arange(12).reshape((3,4))
print(m)
#find total mean
mean1=np.mean(m)
print(mean1)
#find the mean for each row and column
mean2=np.mean(m,axis=0)
print(mean2)
mean3=np.mean(m,axis=1)
print(mean3)


# In[ ]:


#2
import numpy as np

u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])

#outer
outer1=np.outer(u,v)
print(outer1)

#list comprehension
outer2=[[x*y for x in v] for y in u]
print(outer2)

#broadcasting
outer3 = u[:, np.newaxis] * v
print(outer3)



# In[ ]:


#3
import numpy as np
matr=np.random.uniform(low=0.0, high=3.0, size=(10,6))
print(matr)

import numpy.ma as ma
matr=ma.masked_less(matr,0.3)
matr=matr.filled(0)
print(matr)



# In[13]:


#4
import numpy as np
import math

arr=np.linspace(0, 2*math.pi, num=100)


#Extract every 10th element using the slice notation
arr=arr[::10]


#reverse
arr=arr[len(arr)-1:0:-1]


#Extract elements
def function(x):
    return np.abs(np.sin(x) - np.cos(x)) < 0.1

arr = np.linspace(0, 2*np.pi, 100)

filtered_arr = arr[function(arr)]

print(filtered_arr)


# In[39]:


#5
import numpy as np
import math

outer=np.outer(np.arrange(1,11), np.arrange(1,11))
print(outer)

trace= np.trace(outer)
print(trace)

flip=np.fliplr(outer).diagonal()
print(flip)

diagoff=np.diagonal(outer, offset=1)
print(diagoff)


# In[29]:


#6
import numpy as np
import math

cities=["Chicago", "Springfield", "Saint-Louis", "Tulsa", "Oklahoma City", "Amarillo", "Santa Fe", "Albuquerque", "Flagstaff", "Los Angeles"]
miles=np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
km=miles*1.60934
distance=np.abs(km-km[:, np.newaxis])
print(distance)


# In[36]:


#7
import numpy as np
import math
import time

def sieve_of_eratosthenes(N):
    boolean=np.ones(N, dtype=bool)
    boolean[0:2]=False
    for i in range(2,int(np.sqrt(N))+1):
        if boolean[i]:
            boolean[i*i:N:i]=False
        
    prime=np.nonzero(boolean)[0]  
    
    return prime


N=99
primes=sieve_of_eratosthenes(N)
print(primes)


# In[38]:


#8
import numpy as np


walkers=1000
steps=200

arr=np.random.randint(low=-1, high=2, size=(walkers,steps))
summ=np.sum(arr,axis=1)
squared=summ**2
mean=np.mean(squared)


# In[ ]:




