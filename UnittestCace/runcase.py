#!/usr/bin/python3
# coding=utf-8
import unittest
import test_case01
import test_case02
import test_case03
import os
# testunit = unittest.TestSuite()
# testunit.addTest(unittest.makeSuite(test_case01.TestCase01))
# testunit.addTest(unittest.makeSuite(test_case02.TestCase02))
# testunit.addTest(unittest.makeSuite(test_case03.TestCase03))
# runner = unittest.TextTestRunner()
# runner.run(testunit)
case_path = os.getcwd()+"/UnittestCace/"
print(case_path)
discover = unittest.defaultTestLoader.discover(case_path)
unittest.TextTestRunner().run(discover)  # 批量执行
