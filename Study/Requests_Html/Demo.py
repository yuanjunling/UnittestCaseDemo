from requests_html import HTMLSession
import re
class Demo:
    url = "https://www.biduo.cc/biquge/53_53723/"
    def fiction(self):
        ''' 建立Session：'''
        session = HTMLSession()

        # 打开Url检查返回码
        r = session.get(Demo.url)
        if r.status_code==404:
            print("url open failed: {}".format(r.url))
        return r
    def analysis(self,htmls):
        anchors = []
        news = htmls.html.find('div#list dd a')
        #查找内容并检查返回内容
        if news==None:
            print("article empty")
        for value in news:
            '''获取Element内容中的信息(文本/链接)'''
            anchor = {'text':value.text,'links':value.absolute_links}
            anchors.append(anchor)
        return anchors
    def __refine(self,anchors):
        '''数据精炼'''
        l= lambda anchor:{
            'title':anchor['text'].strip(),#strip()去掉字符串多余空格
            'links':anchor['links']
        }
        return map(l,anchors)
    def __sort(self,anchors):
        '''数据排序'''
        anchors=sorted(anchors,key=self.__sort_seed,reverse=True)
        return anchors

    def __sort_seed(self,anchor):
        return anchor['title']

    def __show(self,anchors):
        for anchor in anchors:
            print(anchor['title'] + '--------' + str(anchor['links']))
    def go(self):
        htmls = self.fiction()
        anchors=self.analysis(htmls)
        anchors=list(self.__refine(anchors))
        # for a in anchors:
        #     print(a)
        anchors = self.__sort(anchors)
        self.__show(anchors)
demo = Demo()
demo.go()
