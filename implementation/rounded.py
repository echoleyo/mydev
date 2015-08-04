'''
Created on Jul 12, 2015

@author: yali
'''
import decimal

def rounded(number, s=None):
    #12.339 -> 12.34
    num = float(number)
    dec = abs(decimal.Decimal(str(num)).as_tuple().exponent)
    m = 10 * dec
    _num = num * m
    _num % 5  

            
    
    #print #round(number, 2)
    
if __name__ == '__main__':
    rounded(0.935)