from locust import HttpUser, task, between, SequentialTaskSet, tag

class MyTaskCase(SequentialTaskSet):
    def on_start(self):
        pass

    @task
    def regist_(self):  # 一个方法， 方法名称可以自己改
        url = '/user/login'  # 接口请求的URL地址
        self.headers = {"Content-Type": "application/json"}  # 定义请求头为类变量，这样其他任务也可以调用该变量
        data = {"userAccount":"386224", "userPassword": "216fbdbe29310e9cd82e4b433ae128a6"}  # post请求的 请求体
        # 使用self.client发起请求，请求的方法根据接口实际选,
        # catch_response 值为True 允许为失败 ， name 设置任务标签名称   -----可选参数
        with self.client.post(url, json=data, headers=self.headers, catch_response=True) as rsp:
            if rsp.status_code == 200:
                print(rsp.text)
                rsp.failure('regist_ 接口成功')

class UserRun(HttpUser):
    tasks = [MyTaskCase]
    wait_time = between(0.1, 3)

