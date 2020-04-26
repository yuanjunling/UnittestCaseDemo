def curve_pro():
    a = 25
    def curve(x):
        print('this is a function')
        return a*x*x
    return curve
f = curve_pro()
print(f(2))