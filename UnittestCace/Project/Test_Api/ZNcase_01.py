# coding=utf-8
import json
import random
import unittest
from UnittestCace.public.base_request import request
from UnittestCace.public.GenPass import GenPass
from UnittestCace.public.handle_excle import handle
from UnittestCace.public.handle_init import handle_ini
from UnittestCace.public.hashlib_md5 import md5_hb


class Znjj(unittest.TestCase):
    def setUp(self):
        print('测试开始')
        rootpath = handle_ini.get_value('rootpath')
        self.url = rootpath + "/Util/Excle_case/case_01.xlsx"
        register = handle_ini.get_value('host')
        self.register_url = register + "/user/register"
        self.login = register + "/user/login"
    @classmethod
    def setUpClass(cls):
        globals()["token"]=None

    def tearDown(self):
        print('测试结束')

    def test_1_test_login(self):
        rows = handle.get_rows(self.url)
        for i in range(rows):
            data = handle.get_rows_value(self.url, i + 2)
            is_run = data[2]
            if is_run == 'yes':
                method = data[6]
                log_url = data[5]
                json1 = eval(data[7])
                headers = eval(data[9])  # 字符串转化字典类型
                res = request.run_main(method, log_url, headers, json1)
                json_res = res
                print(json.dumps(json_res, indent=2, ensure_ascii=False))
                self.assertEqual(json_res["description"], " 登陆成功", msg="登陆失败")

    def test_2_excel(self):
        global user
        user = random.randint(6, 999999)
        play = GenPass()
        pwd = md5_hb(play).Hashlib_md5()
        json1 = {
            "userAccount": user,
            "userPassword": pwd
        }
        headers = {
            "Content-Type": "application/json"
        }
        res = request.run_main('post', self.register_url, headers, json1)
        json_res = res
        register = json_res["description"]
        if register == " 注册成功":
            register = json_res["description"]
        else:
            register = "注册失败,请重新注册"
        print(json.dumps(json_res, indent=2, ensure_ascii=False))
        array = [user, pwd, register]
        handle.write_cell_content(self.url, array)

    def test_3_login(self):
        headers = {
            "Content-Type": "application/json"
        }
        index = 1
        rows = handle.get_rows(self.url, index)
        for i in range(rows):
            data = handle.get_rows_value(self.url, i + 2, index)
            userAccount = data[0]
            if userAccount == user:
                userPassword = data[1]
                json1 = {
                    "userAccount": userAccount,
                    "userPassword": userPassword
                }
                res = request.run_main('post', self.login, headers, json1)
                json_res = res
                globals()["token"]=json_res["data"]["token"]
                print(globals()["token"])
                print(json.dumps(json_res, indent=2, ensure_ascii=False))
                self.assertEqual(json_res["description"], " 登陆成功", msg="登陆失败")
    def test_4_deom(self):
        print(globals()["token"])



if __name__ == "__main__":
    unittest.main()

