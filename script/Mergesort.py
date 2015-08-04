#=======================================================================
#  Author: Isai Damier
#  Title: Mergesort
#  Project: geekviewpoint
#  Package: algorithm.sorting
#
#  Statement:
#  Given a disordered list of integers (or any other items),
#  rearrange the integers in natural order.
#
#  Sample Input: [8,5,3,1,9,6,0,7,4,2,5]
#
#  Sample Output: [0,1,2,3,4,5,5,6,7,8,9]
#
#  Time Complexity of Solution:
#  Best = Average = Worst = O(nlog(n)).
#
#  Approach:
#   Merge sort is a divide and conquer algorithm. In the divide and
#   conquer paradigm, a problem is broken into pieces where each piece
#   still retains all the properties of the larger problem -- except
#   its size. To solve the original problem, each piece is solved
#   individually; then the pieces are merged back together.
#
#   For illustration, imagine needing to sort an array of 200 elements
#   using selection sort. Since selection sort takes O(n^2), it would
#   take about 40,000 time units to sort the array. Now imagine
#   splitting the array into ten equal pieces and sorting each piece
#   individually still using selection sort. Now it would take 400
#   time units to sort each piece; for a grand total of 10400 = 4000.
#   Once each piece is sorted, merging them back together would take
#   about 200 time units; for a grand total of 200+4000 = 4,200.
#   Clearly 4,200 is an impressive improvement over 40,000. Now
#   imagine greater. Imagine splitting the original array into
#   groups of two and then sorting them. In the end, it would take about
#   1,000 time units to sort the array. That's how merge sort works.
#
#  NOTE to the Python experts:
#     While it might seem more "Pythonic" to take such approach as
#
#         mid = len(aList) / 2
#         left = mergesort(aList[:mid])
#         right = mergesort(aList[mid:])
#
#     That approach take too much memory for creating sublists.
#======================================================================= 
num = 1

def mergesort( aList ):
  _mergesort( aList, 0, len( aList ) - 1 )

 
def _mergesort( aList, first, last ):
  global num
  print "aList-> %s, first-> %s, last-> %s" %(aList, first, last)
  # break problem into smaller structurally identical pieces
  mid = ( first + last ) / 2
  print "mid = ( first + last ) / 2 -> %s" %mid
  print "if first < last: -> %s" % (first < last)
  print "------done rescu %s" %num
  num += 1
  if first < last:
    print "in first half"
    _mergesort( aList, first, mid )
    print "in second half"
    _mergesort( aList, mid + 1, last )
    print "aList: %s" %aList

 
  # merge solved pieces to get solution to original problem
  a, f, l = 0, first, mid + 1
  print "a->%s, f->%s, l->%s" %(a, f, l)
  tmp = [None] * ( last - first + 1 )
  print "tmp = [None] * ( last - first + 1 ) -> %s" %tmp
 
  print "f <= mid and l <= last: =>%s " %(f <= mid and l <= last)
  while f <= mid and l <= last:
    if aList[f] < aList[l] :
      print "in while loop"
      print "aList: %s" %aList
      tmp[a] = aList[f]
      print "tmp: %s" %tmp
      f += 1
    else:
      tmp[a] = aList[l]
      l += 1
    a += 1
  print "f ->%s, mid->%s" % (f , mid )
  print "if f <= mid  -> %s" % (f <= mid )
  if f <= mid :
    print "mid: %s" % mid
    print "tmp[a:] -> %s" %tmp[a:] 
    print "tmp[a:] = aList[f:mid + 1]"
    tmp[a:] = aList[f:mid + 1]
    print "aList[f:mid + 1]--> %s" %aList[f:mid + 1]
    print "aList: %s" %aList
 
  if l <= last:
    print "last: %s" % last
    tmp[a:] = aList[l:last + 1]
    print "if l <= last"
    print "aList: %s" %aList
 
  a = 0
  while first <= last:
    print "first <= last"
    print "aList: %s" % aList
    print "tmp[a]: %s" % tmp[a]
    print "after aList[first] = tmp[a]"
    aList[first] = tmp[a]
    print "aList: %s" % aList
    first += 1
    a += 1


aList = [15,8,59,69,45,23]
num = 0
print mergesort(aList)