'''
Created on Jul 22, 2015

@author: yali
'''


def is_substring(str1, str2):
    if len(str1) < len(str2):
        return False
    else:
        return str2 in 2 * str1
    
if __name__ == '__main__':
    print is_substring("waterloo", "loowater")