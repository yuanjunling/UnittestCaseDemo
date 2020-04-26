from enum import Enum #枚举
from enum import IntEnum,unique
#枚举类型不需要实例化 单例模式
@unique
class VIP(IntEnum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

print(VIP.YELLOW.value)
print(VIP.YELLOW.name)
print(VIP['YELLOW'])

a = 1
print(VIP(a))
