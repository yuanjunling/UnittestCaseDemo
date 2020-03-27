# coding=utf-8
import requests
import json
# 上传文件

file = {
    "fileField": ("文件名称", open("路径", "rb"), "image/png"),
    "type": "1"
}

# 下载文件
download_url = "testurl"
res = requests.get(download_url)
with open("mukewang.apk", "wb") as f:
    f.write(res.content)
