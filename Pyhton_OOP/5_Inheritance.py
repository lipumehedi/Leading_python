class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return "Animal makes a sound"
    

class Dog(Animal):
    def speak(self):
        return "Dog barks"
    
class Cat(Animal):
    def speak(self):
        return "Cat meows"
    

dog1 = Dog("Buddy")
cat1 = Cat("Mimi")

print(dog1.name)
print(dog1.speak())

print(cat1.name)
print(cat1.speak())