import requests
import json
url = "http://192.168.60.55:6789/user/login"
json1 = {
    "userAccount": "8001",
    "userPassword": "e10adc3949ba59abbe56e057f20f883e"
}
headers = {
    "Content-Type": "application/json"
}
res = requests.post(url, json=json1, headers=headers, verify=False).json()
# verify=False 忽略https和http验证
json_res = res
# ensure_ascii=False 解决json.dumps 中文返回乱码
print(json.dumps(json_res, indent=2, ensure_ascii=False))
print(res['description'])
print(res['data']['token'])
token = res['data']['token']
print(token)
