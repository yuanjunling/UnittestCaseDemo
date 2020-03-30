# coding=utf-8
import unittest
import json

from UnittestCace.public.base_request import request
from UnittestCace.public.handle_excle import handle
from UnittestCace.public.handle_init import handle_ini


class Znjj(unittest.TestCase):
    def setUp(self):
        print('测试开始')
        rootpath = handle_ini.get_value('rootpath')
        self.url = rootpath+"/Util/Excle_case/case_01.xlsx"

    def tearDown(self):
        print('测试结束')

    def test_1_login(self):
        rows = handle.get_rows(self.url)
        for i in range(rows):
            data = handle.get_rows_value(self.url, i + 2)
            is_run = data[2]
            if is_run == 'yes':
                method = data[6]
                log_url = data[5]
                json1 = eval(data[7])
                headers = eval(data[9])#字符串转化字典类型
                res = request.run_main(method, log_url, headers, json1)
                global json_res
                json_res = res
                print(json.dumps(json_res, indent=2, ensure_ascii=False))
                self.assertEqual(json_res["description"], " 登陆成功", msg="登陆失败")

    def test_2_excel(self):
        url = "E:/py_Api/UnittestCace/ENTITY/Util/Excle_case/case_01.xlsx"
        print(handle.get_cell_value(url, 2, 3))
        print(handle.get_rows_value(url,2))


if __name__ == "__main__":
    unittest.main()
