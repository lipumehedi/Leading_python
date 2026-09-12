# ==========================================
# Python Basics
# ==========================================

# 1. Input and Type Casting

first_number = int(input("Please enter your first number: "))
second_number = int(input("Please enter your second number: "))

result = first_number + second_number

print("Summation of the given 2 numbers is:", result)


# 2. String Repetition

print("Sorry " * 5)


# 3. String Concatenation

first_name = "Lipu"
last_name = "Mehedi"

full_name = first_name + " " + last_name

print(full_name)


# 4. F-string

name = "Lipu"
age = 30

print(f"You are {name} and your age is {age}")


# 5. Comparison Operators

print(5 == 5)
print(5 != 3)
print(5 > 3)
print(5 < 3)


# 6. String Methods

text = "Hello World"

print(text.lower())
print(text.upper())
print(text.title())
print(text.replace("World", "Python"))


# 7. String Length

print(len(text))


# 8. String Indexing

print(text[0])
print(text[-1])


# 9. String Slicing

print(text[0:5])
print(text[:5])
print(text[2:])


# 10. Data Type

age = None
print(type(age))

