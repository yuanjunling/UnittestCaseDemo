import requests
class Spider():
    url = "https://book.qidian.com/info/1016572786"
    res = requests.get(url=url)
    print(res.text)
