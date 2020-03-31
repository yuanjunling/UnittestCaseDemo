# coding=utf-8
import unittest
import hashlib
import json,random

from UnittestCace.public.GenPass import GenPass
from UnittestCace.public.base_request import request
from UnittestCace.public.handle_excle import handle
from UnittestCace.public.handle_init import handle_ini
from openpyxl import load_workbook
class Znjj(unittest.TestCase):
    def setUp(self):
        print('测试开始')
        rootpath = handle_ini.get_value('rootpath')
        self.url = rootpath+"/Util/Excle_case/case_01.xlsx"
        register = handle_ini.get_value('host')
        self.register_url = register + "/user/register"

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
        user = random.randint(6,999999)
        play = GenPass()
        Password_md5 = play
        md5 = hashlib.md5()
        md5.update(Password_md5.encode("utf-8"))
        Password = md5.hexdigest()
        json1 = {
             "userAccount":user,
             "userPassword":Password
        }
        headers = {
            "Content-Type":"application/json"
        }
        res = request.run_main('post',self.register_url,headers,json1)
        json_res = res
        register=json_res["description"]
        if register==" 注册成功":
            register = json_res["description"]
        else:
            register="注册失败"
        print(json.dumps(json_res, indent=2, ensure_ascii=False))
        # workbook1 = load_workbook(self.url)
        # sheet = workbook1['Mysheet']
        # sheet.append([user,Password,register])
        # workbook1.save(self.url)
        array = [user,Password,register]
        handle.write_cell_content(self.url,array)
if __name__ == "__main__":
    unittest.main()
