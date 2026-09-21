class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
s1 = Student("Karan", 20, "Male")
s2 = Student("Arjun", 22, "Male")
print(s1.name, s1.age, s1.gender)
print(s2.name, s2.age, s2.gender)