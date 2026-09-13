'''
Introduction to Function


function

function holo reusable block of code  that performs a specific task.
ekbar function likhle setike jotobar iccha call kora jai.

Core Benefits
Benefit	Explanation
Reusability	Write once, use many times — no copy-paste errors.
Modularity	Break a large problem into small, solvable pieces.
Readability	A well-named function makes code read like English prose.
Testability	Isolated logic is far easier to unit-test.
Abstraction	Hide complexity — callers don't care about internals.
'''

#Defining Functions

def greet(name):
     message = f"Hello, {name}! Welcome to Python."
     return message
# Calling the function
result = greet("Alice")
print(result)   # Hello, Alice! Welcome to Python.



def greet():
     message = f"Hello, Welcome to python."

#calling the function
result = greet()
print(result)

*parameters

def greet(name, roll, marital_status):
    message = f"Hello, {name}, {roll}, {marital_status}! Welcome to Python."
    return message

#calling the function
std1 = greet("alif", 1, "Unmarried")
print(std1)

std2 = greet("Mahir", 2, "married")
print(std2)

std3 = greet("Fardin", 3, "married")
print(std3)


#sum

def addition(a,b):
    sum = a+b
    return sum

#call the function
process_1 = addition(5, 10)
print(process_1)

process_2 = addition(10, 23)
print(process_2)

#while way

def addition(a,b):
    sum = a+b
    return sum

while True:
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    summation = addition(num1, num2)
    print("Your summation is", summation)
