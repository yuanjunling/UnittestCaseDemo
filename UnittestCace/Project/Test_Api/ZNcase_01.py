# coding=utf-8
import unittest
import json
import os
from UnittestCace.public.base_request import request
from UnittestCace.public.handle_excle import handle

base_path = os.getcwd()


class Znjj(unittest.TestCase):
    def setUp(self):
        print('测试开始')
        self.url = "/user/login"

    def tearDown(self):
        print('测试结束')

    def test_1_login(self):
        json1 = {
            "userAccount": "8002",
            "userPassword": "e10adc3949ba59abbe56e057f20f883e"
        }

        headers = {
            "Content-Type": "application/json"
        }
        log_url = self.url
        res = request.run_main('post', log_url, headers, json1)

        global json_res
        json_res = res
        print(json.dumps(json_res, indent=2, ensure_ascii=False))
        self.assertEqual(json_res["description"], " 登陆成功", msg="登陆失败")

    def test_2_excel(self):
        url = "E:/UnittestCaseDemo/UnittestCace/ENTITY/Util/Excle_case/case_01.xlsx"
        print(handle.get_cell_value(url, 2, 3))
        print(handle.get_rows_value(url,2))


if __name__ == "__main__":
    unittest.main()
