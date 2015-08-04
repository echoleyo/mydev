import random 
import time
n = 10**6
k = 10**5

start = time.time()
candies = [random.randrange(0,10**9) for _ in xrange(n)]
# candies = (random.randrange(1,n) for _ in xrange(n))

candies.sort()

def findmin(n, k, candies):
    v = max(candies)
    for i in xrange(n-k+1):
        vnew = candies[i + k -1] - candies[i]
        if vnew < v:
            v = vnew
        if v == 0:
            return v
    return v
    
# def findmin(n, k, candies):
    # # _ll = ( set(i) for i in chunk(n, k))
    # # print "_ll is ready"
    # v = max(candies) - min(candies)
    # i=0
    # while True:
    # # for _l in candies[i:k+i]:
        # _l = candies[i:k+i]
        # vnew = max(_l) - min(_l)
        # if vnew < v:
            # v = vnew
        # if vnew == 0:
            # return vnew
        # i+=1
    # return v
    
def chunk(n, k):
    for i in xrange(n-k+1):
        yield candies[i:k+i]
    

min_diff = findmin(n, k, candies)
# for i in min_diff:
    # print i
    
    
end = time.time()
print "second: %s" %(end - start )
print min_diff