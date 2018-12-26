
# coding: utf-8

# In[1]:


from functools  import lru_cache
def memoize(f):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function

def fib_o(n):
    return n if n < 2 else fib_o(n-2) + fib_o(n-1)

@memoize
def fib(n):
    return n if n < 2 else fib(n-2) + fib(n-1)

@lru_cache()
def fib_l(n):
    return n if n < 2 else fib_l(n-2) + fib_l(n-1)


# In[3]:


import time
tStart = time.time()
print(fib_o(35))
tEnd = time.time()
print("It cost %f sec" % (tEnd - tStart))


# In[4]:


tStart = time.time()
print(fib(35))
tEnd = time.time()
print("It cost %f sec" % (tEnd - tStart))


# In[5]:


tStart = time.time()
print(fib_l(35))
tEnd = time.time()
print("It cost %f sec" % (tEnd - tStart))

