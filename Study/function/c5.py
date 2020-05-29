from c6 import Human
class Student(Human):
    sum = 0
    def __init__(self,school,name,age):
        self.school = school
        print(self.__class__.sum)
        super().__init__(name,age)
    def do_homework(self):
        super(Student,self).do_homework()
        print('english homework')
    @classmethod #类对象
    def plus_sum(cls):
        cls.sum +=1
        print(cls.sum)
    @staticmethod #静态对象
    def add(x,y):
        print('This is a static method')
Student.plus_sum()

student1 = Student('人民小学','石敢当',18)
student1.do_homework()
student1.get_name()
print(student1.name)
print(student1.age)
print(student1.school)