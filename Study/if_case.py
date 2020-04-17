import random
Num1 = random.randint(0, 10)
Num2 = random.randint(0, 10)
if Num1 > Num2:
    print('1赢了')
elif Num1 == Num2:
    print('平局')
else:
    print('2赢了')
