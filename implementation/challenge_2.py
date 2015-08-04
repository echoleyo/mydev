'''
Created on Jul 30, 2015

@author: yali
'''
s = "New to Python or choosing between Python 2 2 2 and Python 3? Read Python 2 or Python 3."
d = {}
for i in s.split(" "):
    print i, d.get(i,0)
    d[i] = d.get(i ,0) +1    
print d



def g7(n):
    for i in range(0, n+1):
        if i % 7 == 0:
            yield i
[i for i in g7(1000)]

from operator import itemgetter

# t = [('John', '120', '90'), ('Aony', '47', '91'), ('Bony', '17', '93'), ('Ason', '21', '85'), ('Tom', '39', '88')]
# 
# for i in t:
#     print i
# 
# print "---"
# 
# for ii in sorted(t, key=lambda x: x[1]):
#     print ii

# print sorted(t, itemgetter(0,1,2))