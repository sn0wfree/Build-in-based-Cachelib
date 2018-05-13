from CacheLib import LRUDict_Pickled,LRUDict_UnPickled
from functools import wraps
def LRUCache_Pickled(capacity=500):
    memo = LRUDict_Pickled(capacity, Pickled=True)
    
    def Cache(func):
        #try:
        #    from  import wraps
            
        #except ImportError:  # pragma: no cover
            
        @wraps(func)  
        def _wrapper(*args):
            res = memo.get(args, None)
            if res is not None:
                pass
                # return res
            else:
                res = func(*args)
                memo[args] = res
            return res
        return _wrapper
    return Cache

def LRUCache_UnPickled(capacity=500):
    memo = LRUDict_UnPickled(capacity)
    
    def Cache(func):
        @wraps(func)  
        def _wrapper(*args):
            res = memo.get(args, None)
            if res is not None:
                pass
                # return res
            else:
                res = func(*args)
                memo[args] = res
            return res
        return _wrapper
    return Cache
if __name__ == '__main__':
    @LRUCache
    def fib(n):
        if n <= 1:
            return n
        else:
            return fib(n - 1) + fib(n - 2)
    print([fib(i) for i in list(range(31))])
