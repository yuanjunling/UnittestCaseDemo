# coding=utf-8

from UnittestCace.public.base_request import request
from UnittestCace.public.handle_excle import handle


class RunMain:
    def run_case(self):
        #获取mock全部数据
        url = "E:/UnittestCaseDemo/UnittestCace/ZNJJAPI/Util/Excle_case/case_01.xlsx"
        rows = handle.get_rows(url)
        for i in range(rows):
            data = handle.get_rows_value(url, i + 2)
            is_run = data[2]
            if is_run =='yes':
                method = data[6]
                log_url = data[5]
                json1 =eval(data[7])
                headers = eval(data[9])
                res=request.run_main(method, log_url, headers, json1)
                print(res)

if __name__=="__main__":
    run = RunMain()
    run.run_case()