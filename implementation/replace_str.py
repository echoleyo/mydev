
def replace_str(strs, char_a, char_b ):
    newstr = ''
    for i in strs:
        if i == char_a:
            newstr += char_b
        else:
            newstr += i
    return newstr

 
#"".join([a for a in strs if a == char_a ])

print replace_str("hello", "o", "0")