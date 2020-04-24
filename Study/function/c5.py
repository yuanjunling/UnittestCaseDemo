from c6 import Human
class Student(Human):
    # sum = 0
    def __init__(self,school,name,age):
        self.school = school
        super(Student,self).__init__(name,age)
    def do_homework(self):
        super(Student,self).do_homework()
        print('english homework')

student1 = Student('人民小学','石敢当',18)
student1.do_homework()
# print(student1.name)
# print(student1.age)
# print(student1.school)