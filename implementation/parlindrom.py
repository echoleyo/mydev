'''
Created on Jul 30, 2015

@author: yali
'''


def parlindrom(word):
    new = word[:-1]
    drow = word+new[::-1]
    if drow == drow[::-1]:
        return drow

if __name__ == '__main__':
    print parlindrom("mother")
#     print parlindrom("tostotor")
#     print parlindrom("Chris")
#     print parlindrom("Chriss")
"""
aaab -> baaab
erter

"""
def  shortPalin( S):
    k=0
    lis=len(S)
    for i in range(len(S)/2):
        if S[i]==S[lis-1-i]:
            k=k+1
        else :break
    S=S[k:lis-k]
    lis=len(S)
    prev=0
    w=len(S)
    tot=0
    for i in range(len(S)):
        if i>=w:
            break;
        elif S[i]==S[lis-1-i]:
             tot=tot+lcs(S[prev:i])
             prev=i
             w=lis-1-i
    tot=tot+lcs(S[prev:i])
    return tot

def  lcs( S):
    if (len(S)==1):
        return 1
    li=len(S)
    X=[0 for x in xrange(len(S)+1)]
    Y=[0 for l in xrange(len(S)+1)]
    for i in range(len(S)-1,-1,-1):
        for j in range(len(S)-1,-1,-1):
            if S[i]==S[li-1-j]:
                X[j]=1+Y[j+1]
            else:
                X[j]=max(Y[j],X[j+1])
        Y=X
    return li-X[0]
print shortPalin("aaah")
