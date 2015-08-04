'''
Created on Aug 4, 2015

@author: yali
'''


def find_index(l, item):
    if item in l:
        return l.index(item) 
    else:
        for i, value in enumerate(l):
            if item < value:
                return i
        return len(l)

if __name__ == '__main__':
    print find_index([1,3,4,5], 2)
    print find_index([5,4,3,1], 2)
    print find_index([1,3,4,5], 7)
    print find_index([1,3,4,5, 6,7,8,9,13,15,16], 12)
    print find_index([1,3,4,5, 6,7,8,9,13,15,16], "a")
    print find_index([1,3,4,5, 6,7,8,9,13,15,16], "a")