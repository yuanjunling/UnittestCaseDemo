import re
#概况字符集 \d \D
a = 'python1@@11 11java678php'#

r = re.findall('[a-z]{3,6}',a)
print(r)