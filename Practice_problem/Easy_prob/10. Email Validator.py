'''
10. Email Validator

Problem Statement:
• Take email input.
• Email must contain '@'.
• Email must end with '.com'.
• Print validity message.

Acceptance Criteria:
• Contains '@' AND ends with '.com' → Valid Email
• Missing '@' OR does not end with '.com' → Invalid Email

Expected Output:
Enter email: abc@gmail.com
Valid Email
'''
email = input("Enter email: ")

if email.count("@")>=1 and email.endswith(".com"):
    print("Valid Email")
else:
    print("Invalid Email")