'''
22. Smart Login Security System

Problem Statement:
• Take username, password, and OTP.
• Verify all credentials before login approval.
• Print login result.

Acceptance Criteria:
• Correct username: admin
• Correct password: 12345
• Correct OTP: 9999
• All three correct → Login Approved
• Wrong username → Invalid Username
• Wrong password → Wrong Password
• Wrong OTP → Invalid OTP

Expected Output:
Enter username: admin
Enter password: 12345
Enter OTP: 9999
Login Approved
'''
username = input("Enter username: ")
password = input("Enter password: ")
otp = input("Enter OTP: ")

if username == "admin":
    if password == "12345":
        if otp == "9999":
            print("Login Approved")
        else:
            print("Invalid OTP")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")
