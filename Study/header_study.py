# coding=utf-8
import requests
import json
import hashlib
imooc = "imooc.com"
md5 = hashlib.md5()
md5.update(imooc.encode('utf-8'))
res = md5.hexdigest()
print(res)
data = str({"user": '1111'})
md5.update(data.encode('utf-8'))
res1 = md5.hexdigest()
print(res1+res)
