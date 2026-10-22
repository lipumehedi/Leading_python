from dataclasses import dataclass, asdict
#The @ line is called a decorator. It adds extra abilities to the class below it; here it writes the setup code that you would otherwise have to type yourself.
@dataclass
class Student:
    name: str
    age: int
    city: str = "Tokyo"
    
s = Student("Rahim", 24)

print(s.name)
print(s.city)
print(s)
print(asdict(s))

#asdict turns an object into a dictionary. The opposite direction uses **, which unpacks a dictionary into named arguments:
info = {"name": "Karim", "age": 30}
k = Student(**info)
print(k)