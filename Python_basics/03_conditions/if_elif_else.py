# ==========================================
# Python Control Flow
# Conditional Statements
# ==========================================


# ==========================================
# 1. If Statement
# ==========================================

age = 20

if age >= 18:
    print("You are an adult.")


# ==========================================
# 2. If-Else Statement
# ==========================================

age = 10

if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")


# User Input Example

age = int(input("Enter your age: "))

if age >= 20:
    print("You are an adult.")
else:
    print("You are a minor.")


# ==========================================
# 3. If-Elif-Else Statement
# ==========================================

marks = int(input("Enter your marks: "))

if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("A-")
elif marks >= 50:
    print("B")
elif marks >= 40:
    print("C")
elif marks >= 33:
    print("D")
else:
    print("F")


# ==========================================
# 4. Logical Operator - AND
# Both conditions must be True
# ==========================================

age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")


# Marks Example Using AND

marks = int(input("Enter your marks: "))

if marks >= 80 and marks <= 100:
    print("A+")
elif marks >= 70 and marks <= 79:
    print("A")
elif marks >= 60 and marks <= 69:
    print("A-")
elif marks >= 50 and marks <= 59:
    print("B")
elif marks >= 40 and marks <= 49:
    print("C")
elif marks >= 33 and marks <= 39:
    print("D")
else:
    print("F")


# ==========================================
# 5. Logical Operator - OR
# At least one condition must be True
# ==========================================

is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("No work today")


# ==========================================
# 6. Logical Operator - NOT
# Reverses the truth value
# ==========================================

is_raining = True

if not is_raining:
    print("Let's go outside.")
else:
    print("Stay at home.")


# ==========================================
# 7. Multiple Conditions
# ==========================================

age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ")
gender = input("Enter your gender: ")

if nationality != "Bangladeshi" and age >= 25:
    print("OK")
else:
    print("NG")