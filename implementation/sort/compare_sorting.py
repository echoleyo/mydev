'''
Created on Aug 6, 2015

@author: yali
'''
from random import randrange
from merge_sort import merge_sort
from quick_sort import qsort
import time


def timer(func, *args, **kwargs):
    def _wrapper(*args, **kwargs):
        t = time.time()
        func(*args, **kwargs)
        print time.time() - t
    return _wrapper

@timer
def insert_sort(l):
    for i in range(1, len(l)):
        while i > 0 and l[i] < l[i - 1]:
            l[i - 1], l[i] = l[i], l[i - 1]
            i -= 1
    return l

@timer
def merge(l):
    return merge_sort(l)

@timer
def quick(l):
    return qsort(l)

if __name__ == '__main__':
    ll = [randrange(1, 12200) for i in xrange(22222)]
    quick(ll)
    merge(ll)
    insert_sort(ll)
