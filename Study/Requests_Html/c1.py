from requests_html import HTMLSession
session = HTMLSession()
r = session.get("https://www.biduo.cc/biquge/16_16705/c4845336.html")
newss = r.html.find("div.bookname h1")
for a in newss:
    print(a.text)