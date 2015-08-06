'''
Created on Aug 6, 2015

@author: yali
'''


def merge_sort(l):
    if len(l) > 1:
        mid = len(l) // 2
        ll = l[:mid]
        rl = l[mid:]
        merge_sort(ll)
        merge_sort(rl)

        i = 0
        j = 0
        k = 0
        while i < len(ll) and j < len(rl):
            if ll[i] < rl[j]:
                l[k] = ll[i]
                i += 1
            else:
                l[k] = rl[j]
                j += 1
            k += 1

        while i < len(ll):
            l[k] = ll[i]
            i += 1
            k += 1
        while j < len(rl):
            l[k] = rl[j]
            j += 1
            k += 1
        return l
#        print "***l: %s" % l
#        print "===len(l): %s" % len(l)

if __name__ == '__main__':
    l = [11, 2, 4, 3, 66, 55, 33, 675, 343, 232, 1, 34, 234, 778, 23423, -5, -1, 0, 0, 4, 55]
    print "Original list: %s" % l
    print merge_sort(l)
