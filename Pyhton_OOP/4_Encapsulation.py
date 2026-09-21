class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks
        
    def get_marks(self):
        return self.__marks
    def set_marks(self, marks):
        self.__marks = marks
    def is_passed(self):
        return self.__marks >= 40 

student1 = Student("Mehedi", 75)

print(student1.get_marks())

student1.set_marks(85)

print(student1.get_marks())
print(student1.is_passed())       

student2 = Student("Rahim", 35)
print(student2.is_passed())