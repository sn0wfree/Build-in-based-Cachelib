# -*- coding:utf-8 -*-
# this is main function for creating inherit cache system via
# decorator
# Black magic
#
#

import collections
import functools

# LFUCache(Least Frequently Used (LFU) cache implementation.)
# LRUCache(Least Recently Used (LRU) cache implementation.)
# RRCache(Random Replacement (RR) cache implementation.)
# TTLCAche(LRU Cache implementation with per-item time-to-live (TTL) value.)


def cache(func):
    memo = {}

    def _wrapper(*args):
        res = memo.get(args, None)
        if res is not None:
            return res
        else:
            res = func(*args)
            memo[args] = res
        return res
    return _wrapper

# __slots__ = ('key', 'timeout', 'last_time', 'value')


class LcacheMetaclass(type):
    """
    this is metaclass to create class for cache system.
    current it will be used as creating the class which will contri the cache decortor
    """

    def __new__(cls, name, base, attrs):
        if name == 'DictCache':
            return type.__new__(cls, name, base, attrs)


class valueCahce(object):
    __metaclass__ = LcacheMetaclass

    def __init__(self, func, backend='Dict'):
        self.func = func
        self.cache = {}
        pass

    def __call__(self, *args):
        # this is to detect unreachable or unhashable items
        if not isinstance(args, collections.Hashable):
            print 'Noncache'
            return self.func(*args)
        elif args in self.cache.keys():
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__

    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)


@cache
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print([fib(i) for i in list(range(31))])
