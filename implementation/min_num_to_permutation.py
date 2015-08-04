'''
Created on Jul 14, 2015

@author: yali
'''


def is_permutation(str1):
    return str1 == str1[::-1]


def min_num_to_palindrome(string):
    if is_permutation(string):
        return 0
    else:
        ss = string[1:]
        st = string[:-1]
        i = 1 
        ii = 1
        while not is_permutation(ss):
            i += 1
            ss = string[i:]
        while not is_permutation(st):
            ii += 1
            st = string[:(-1*ii)]

        return i if i <= ii else ii

if __name__ == '__main__':
    print min_num_to_palindrome("FAS")
    print min_num_to_palindrome("FASASAS")
    print min_num_to_palindrome("Fssss")
    print min_num_to_palindrome("aaaaav")
    print min_num_to_palindrome("Tammy")
    print min_num_to_palindrome("asas")
    print min_num_to_palindrome("aaaaaaRR")