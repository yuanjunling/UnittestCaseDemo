import re

a = 'C0C++1Java2C#3Python4Javascript'

r = re.findall('\d',a) #\d 元字符
print(r)