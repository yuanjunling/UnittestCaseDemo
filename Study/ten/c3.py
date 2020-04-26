import re

a = 'abc,acc,adc,aec,afc,ahc'#

r = re.findall("a[^cf]c",a) #\d 元字符 [] 字符集 或关系 ^取反 c-f取范围[c-f]
print(r)