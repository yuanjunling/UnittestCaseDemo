

class Student:
    name = ''
    age = 0
    def __init__(self):
        print('test')

    def print_file(self):
        print('name: ' + self.name)
        print('age: '+ str(self.age))

student = Student()
student.__dict__