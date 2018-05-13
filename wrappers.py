from CacheLib import LastUpdatedOrderedDict
from CacheLib import LastUpdatedOrderedDict


def Dictcache(capacity=250):
    # LRU
    # thsi cache cannot cache some unhash items
    memo = LeastRecentlyUsedOrderedDict(capacity)

    def Cache(func):
        def _wrapper(*args):
            res = memo.get(args, None)
            if res is not None:
                return res
            else:
                res = func(*args)
                memo[args] = res
            return res
        return _wrapper
    return Cache


def LRUCache(capacity=250):
    memo = LRUDictCache(capacity)

    def Cache(func):
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
