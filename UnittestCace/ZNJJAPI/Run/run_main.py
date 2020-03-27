# coding=utf-8
import unittest
import json
import os

from UnittestCace.ZNJJAPI.Util.handle_excle import handle

class RunMain:
    def run_case(self):
        url = "E:/UnittestCaseDemo/UnittestCace/ZNJJAPI/Util/Excle_case/case_01.xlsx"
        rows = handle.get_rows(url)
        for i in range(rows):
            print("----->",i)
            data = handle.get_rows_value(url,i+2)
            print(data)

if __name__=="__main__":
    run = RunMain()
    run.run_case()