'''
Created on Jul 29, 2015

@author: yali
'''
import time
from test.test_sax import start


def wrapper(func, *args, **kwargs):
    def _function(*args, **kwargs):
        print "Started..."
        start = time.time()
        func(*args, ** kwargs)
        print "Finished, took %s seconds." % float(time.time() - start)
    return _function


def error_handle(func, *args, **kwargs):
    def _function(*args, **kwargs):
        try:
            print "try"
            func(*args, ** kwargs)
        except Exception as e:
            raise e
        finally:
            print "Teardown."
    return _function

@wrapper
@error_handle
def reverse_list(l):
    print "%s" % time
    reversed(l)

if __name__ == '__main__':
    reverse_list(range(90000000))
