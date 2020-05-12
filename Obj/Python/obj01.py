def ask(name = "bobby"):
    print(name)



def decorator_func():
    print("dec start")
    return ask
my_ask = decorator_func()

my_ask("tom")
