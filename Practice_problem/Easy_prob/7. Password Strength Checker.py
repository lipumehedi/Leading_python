'''
7. Password Strength Checker

Problem Statement:
• Take password input.
• Password must be at least 8 characters long.
• Password must contain at least one digit.
• Print strength message.

Acceptance Criteria:
• Length >= 8 AND contains at least one digit → Strong Password
• Otherwise → Weak Password

Expected Output:
Enter password: hello123
Strong Password
'''
password = input("Enter password: ")

if not password.isalpha() and not password.isdigit() and len(password) >= 8:
    print("Strong password")
else:
    print("Weak password")
