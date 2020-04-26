#匿名函数
def f(x,y):
    return x+y

f = lambda x,y:x if x>y else y

print(f(3,2))

