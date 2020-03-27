# coding=utf-8
import requests
import json


class BaseRequest:
    def send_post(self, url, headers, json):
        res = requests.post(url=url, json=json, headers=headers).json()
        return res

    def send_get(self, url, headers, json=None):
        res = requests.get(url=url ,params=json,headers=headers).json()
        return res

    def run_main(self, method, url, headers, json):
        if method == 'get':
            res = self.send_get(url,headers,json=None )
        else:
            res = self.send_post(url, headers, json)

        return res


request = BaseRequest()
