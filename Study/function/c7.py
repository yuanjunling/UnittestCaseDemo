#装饰器
import time
def decorator(func):
    def wrapper(*args,**kwargs):
        print(time.time())
        func(*args,**kwargs)
    return wrapper




@decorator
def f2(func_name,func_age):
    print("装饰器"+func_name+func_age)

@decorator
def f3(func_name,func_age,**kwargs):
    print("装饰器"+func_name+func_age)
    print(kwargs)
f2('test1','test2')
f3('test1','test2',a=1,b=2,c='123')

