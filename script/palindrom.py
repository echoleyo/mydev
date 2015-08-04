'''
Created on Jul 30, 2015

@author: yali
'''


def palindrom(word):
    word = word[:-1]
    drow = word[::-1]
    return word + drow





if __name__ == '__main__':
    print palindrom("aaabbaaas")
