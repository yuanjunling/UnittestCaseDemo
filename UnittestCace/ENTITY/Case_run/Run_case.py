# coding=utf-8

import unittest
import HTMLTestRunner_PY3
import time

from UnittestCace.Project.Test_Api import ZNcase_01
from UnittestCace.public.handle_init import handle_ini
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(ZNcase_01.Znjj))
now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
rootpath = handle_ini.get_value('rootpath')
file_path = rootpath + "/Report/"

wwwa = file_path + now + "report.html"
with open(wwwa, 'wb') as f:
    runner = HTMLTestRunner_PY3.HTMLTestRunner(
        f, verbosity=2, title='智能家居测试报告', description='执行人：袁军令')
    runner.run(suite)
f.close()
