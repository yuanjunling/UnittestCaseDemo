import requests,json

session = requests.session()
headers = {
            "Content-Type": "application/json"
        }

json1 = {
                    "userAccount":151001,
                    "userPassword":"a047a095710f46c941d771898c893eb5"
                }
url = "http://106.75.37.93/user/login"

res = session.post(url=url,json=json1,headers=headers).json()

