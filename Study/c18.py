def app(a):
    def add(oa):
        t = a*oa*oa
        return t
    return add

App = app(1)
print(App(10))