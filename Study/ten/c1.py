import re

a = 'C0C++1Java2C#3Python4Javascript'

r = re.findall('Python',a)
if len(r) > 0:
    print("字符串中包含python")