'''
4. Username Validator

Problem Statement:
• Take username input.
• Username must contain only alphabets.
• Length must be at least 5 characters.
• Print validity message.

Acceptance Criteria:
• Only alphabets AND length >= 5 → Valid username
• Contains non-alphabets OR length < 5 → Invalid username
Expected Output:
Enter username: Refadul
Valid username
'''

user_name = input("Enter username: ")

if user_name.isalpha and len(user_name) >= 5:
    print("Valid username")
else:
    print("Invalid username")