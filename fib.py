
# coding: utf-8
import time

def memoize(f):
    cache_list = {}
    def add_memoize(*args):
        if args in cache_list:
            return cache_list[args]
        else:
            cache_list[args] = f(*args)
            return cache_list[args]
    return add_memoize

def fib_o(n):
    return n if n < 2 else fib_o(n-2) + fib_o(n-1)

@memoize
def fib(n):
    return n if n < 2 else fib(n-2) + fib(n-1)


tStart = time.time()
print('origin fib(35):')
print(fib_o(35))
tEnd = time.time()
print("It cost %f sec" % (tEnd - tStart))

tStart = time.time()
print('with cache fib(35):')
print(fib(35))
tEnd = time.time()
print("It cost %f sec" % (tEnd - tStart))


