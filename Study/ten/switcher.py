#字典映射
day = 6
def get_sunday():
    return 'Sunday'
def get_sunday1():
    return 'Sunday1'
def get_sunday2():
    return 'Sunday2'
def get_default():
    return 'Unkown'
switcher = {
    0 : get_sunday,
    1 : get_sunday1,
    2 : get_sunday2
}


day_name = switcher.get(day,get_default)()
print(day_name)