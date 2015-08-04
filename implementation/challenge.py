'''
Created on Jul 29, 2015

@author: yali
'''
x = "hwe"
assert isinstance(x, str),  "Failed."

theory = """}#)$[]_+(^_@^][]_)*^*+_!{&$##]((](}}{[!$#_{&{){
*_{^}$#!+]{[^&++*#!]*)]%$!{#^&%(%^*}@^+__])_$@_^#[{{})}$*]#%]{}{][@^!@)_[}{())%)
())&#@*[#}+#^}#%!![#&*}^{^(({+#*[!{!}){(!*@!+@[_(*^+*]$]+@+*_##)&)^(@$^]e@][#&)(
%%{})+^$))[{))}&$(^+{&(#%*@&*(^&{}+!}_!^($}!(}_@@++$)(%}{!{_]%}$!){%^%%@^%&#([+[
_+%){{}(#_}&{&++!@_)(_+}%_#+]&^)+]_[@]+$!+{@}$^!&)#%#^&+$@[+&+{^{*[@]#!{_*[)(#[[
]*!*}}*_(+&%{&#$&+*_]#+#]!&*@}$%)!})@&)*}#(@}!^(]^@}]#&%)![^!$*)&_]^%{{}(!)_&{_{
+[_*+}]$_[#@_^]*^*#@{&%})*{&**}}}!_!+{&^)__)@_#$#%{+)^!{}^@[$+^}&(%%)&!+^_^#}^({
*%]&@{]++}@$$)}#]{)!+@[^)!#[%@^!!"""

#theory = open("temp.txt")

key = "#@!$%+{}[]_-&*()*^@/"
new2 =""

print()
for letter in theory:
    if letter not in key:
        new2 += letter.strip()
#         print ">%s<" %letter

print(new2)

import string

original = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc " \
    "dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq " \
    "rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu " \
    "ynnjw ml rfc spj."

table = string.maketrans(
    "abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"
)

print original.translate(table)

import pickle, urllib

handle = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(handle)
handle.close()
print type(data)
print data

for elt in data:
    print "".join([e[1] * e[0] for e in elt])
    