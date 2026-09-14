'''
17. Website Age Restriction

Problem Statement:
• Take user's age.
• Users below 13 cannot create accounts.
• Print account creation result.

Acceptance Criteria:
• Age >= 13 → Account creation allowed
• Age < 13 → Account creation denied

Expected Output:
Enter age: 12
Account creation denied
'''
age = int(input("Enter age: "))

if age >=13:
    print("Account creation allowed")
else:
    print("Account creation denied")