
# coding: utf-8

# In[1]:


import time
import sys
# sys.setrecursionlimit(1000000)
def fib_o(n):
    if n < 2:
        return n
    else:
        return fib_o(n-1) + fib_o(n-2)



# In[2]:


tStart = time.time()
print(fib_o(35))
tEnd = time.time()
print("It cost %f sec" % (tEnd - tStart))


# In[3]:


cache = {} 
# def cache_find(n):
#     if n not in cache.keys():
#         cache[n] = fib(n)
#         print(cache)
#     return cache[n]

def use_cache(func):
    def wrapper(n):
        if n not in cache.keys():
            cache[n] = fib_o(n)
            # print(cache)
        return cache[n]
    return wrapper

@use_cache
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)




# In[ ]:


tStart = time.time()
print(fib(35))
tEnd = time.time()
print("It cost %f sec" % (tEnd - tStart))

