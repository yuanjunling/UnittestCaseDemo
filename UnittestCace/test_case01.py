# coding=utf-8
from Base.base_request import request
import requests
import unittest
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)

url = "https://www.baidu.com"
data = {
    "username": "1111",
    "password": "22222"
}


class TestCase01(unittest.TestCase):
    def setUp(self):
        print('测试开始')

    def tearDown(self):
        print('测试结束')

    @classmethod
    def setUpClass(cls):
        print('class开始执行')

    @classmethod
    def tearDownClass(cls):
        print('class执行结束')

    def test_01(self):
        res = request.run_main('get', url, data)
        print(res)

    def test_02(self):
        print("case02")

    def test_03(self):
        print("case03")


if __name__ == "__main__":
    suite = unittest.TestSuite()  # 创建测试套件
    suite.addTest(TestCase01('test_01'))  # 把测试案例添加到测试套件
    runner = unittest.TextTestRunner()
    runner.run(suite)  # 运行测试套件
