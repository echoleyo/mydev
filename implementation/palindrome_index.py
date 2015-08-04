'''
Created on Aug 3, 2015

@author: yali
'''

times = raw_input()


def is_palindrome(s):
    return s == s[::-1]

lines = []
t = 1
while int(times) >= t:
    lines.append(raw_input("string: "))
    t += 1

for s in lines:
    if is_palindrome(s):
        print "-1"
    else:
        ss = s[1:]
        i = 0
        while not is_palindrome(ss):
            i += 1
            ss = s[:i] + s[(i+1):]
        print i  