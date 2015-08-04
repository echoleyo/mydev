
"""
This function only works in following case once, it's invalid if combines the following cases
    for example ""meet", "meta""
- insert a single character anywhere in s1 to get s2
- remove a single character anywhere in s1 to get s2
- replace a single character anywhere in s1 to get s2
"""

def singleDiff(str1, str2, ignore_case=True):
    if ignore_case:
        str1 = str1.lower() # ignore the case 
        str2 = str2.lower() 
    str_a = sorted(str1)
    str_b = sorted(str2)
    
    if abs(len(str1) - len(str2)) > 1 : 
        return False
    if str1 == str2: # check if it's equal
        return False
    if str_a == str_b: #check if it's equal but different order
        return False
    if len(str1) >= len(str2): #determine longer string
        l_str = str_a
        s_str = str_b
    else:
        l_str = str_b
        s_str = str_a
    
    for i in s_str:
        if i != 
        
    
    # print reduce(lambda x1, x2: x1 in s_str, map(lambda x:x in s_str, l_str))
    return len(filter(lambda x: not x, map(lambda x:x in s_str, l_str))) <= 1

        
str1 = "meeet" 
str2 = "metea" 


print singleDiff(str1, str2, False)
         
            
            
            
            
            
            
            
                
            