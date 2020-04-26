import requests
def login(func):
    headers = {
        "Content-Type": "application/json"
    }
    json1 = {
        "userAccount": '0903',
        "userPassword": '899b7c59ce77e992ebf5c856c006d915'
    }
    url = "http://106.75.37.93/user/login"
    r = requests.post(url=url,json=json1,headers=headers).json()
    token=r["data"]["token"]
    return func(token)
    return token

@login
def test(obj):
    headers = {
        "Content-Type": "application/json",
        "token":obj
    }
    json = {
	"familyId":77
    }
    url = "http://106.75.37.93/user/userInform"
    r = requests.post(url=url, json=json, headers=headers).json()
    print(r)