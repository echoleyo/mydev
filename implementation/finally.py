'''
Created on Jul 29, 2015

@author: yali
'''

def final():
    try:
        print "try"
        raise
    except Exception as e:
        raise e
    finally:
        print "tear down"


if __name__ == '__main__':
    final()