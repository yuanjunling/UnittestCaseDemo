from dataclasses import dataclass
@dataclass
class Student():
    name:str
    age:int
    chool_name:str

    def test(self):
        print(self.name)

stu = Student('7yue',18,'Tsinghua')
stu.test()