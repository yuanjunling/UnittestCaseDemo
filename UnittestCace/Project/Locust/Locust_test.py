# coding=utf-8
from locust import HttpLocust,TaskSet,task

class MyBlogs(TaskSet):
    @task(1)
    def get_blog(self):
        headers = {
            "Content-Type": "application/json"
        }
        json1 = {
            "userAccount": "231643",
            "userPassword": "7afa1728db5fd807a45bf948071e1434"
        }
        req = self.client.post("http://106.75.37.93/user/login",headers=headers,json=json1)
        if req.status_code ==200:
            print(req.text)
            print("success")
        else:
            print("fails")

class websitUser(HttpLocust):
    task_set = MyBlogs
    min_wait = 3000
    max_wait = 6000
if __name__ == "__main__":
    import os
    os.system("locust -f E:/UnittestCaseDemo/UnittestCace/Project/Locust/Locust_test.py --host=http://106.75.37.93/user/login") #http://localhost:8089/ UI地址

