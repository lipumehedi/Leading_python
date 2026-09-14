'''
13. Login System with Nested Conditions

Problem Statement:
• Take username and password.
• Verify username first, then verify password.
• Print login result.


Acceptance Criteria:
• Correct username: admin
• Correct password: 12345
• Both correct → Login Successful
• Wrong username → Invalid Username
• Wrong password → Wrong Password

Expected Output:
Enter username: admin
Enter password: 12345
Login Successful
'''
cor_name = "admin"
cor_pass = "12345"

username =input("Enter your username: ")
password =input("Enter your password: ")

if username == cor_name:
    if password == cor_pass:
        print("Login Successful")
    else:
        print("Wrong password")
else:
    print("Invalid username")

