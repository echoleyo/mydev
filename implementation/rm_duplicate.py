'''
Created on Jul 22, 2015

@author: yali
'''


def rm_duplicate(l):
    
    ll = reduce(lambda x, y: x if y in x else x + [y], l, [])
    return "".join(ll)

if __name__ == '__main__':
    print rm_duplicate('1231234567711223asdfasdflkjlkskjlkaj039485jhg l8998')