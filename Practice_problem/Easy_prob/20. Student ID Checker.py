'''
20. Student ID Checker

Problem Statement:
• Take student ID input.
• Check whether ID starts with '260'.
• Print validity message.

Acceptance Criteria:
• ID starts with '260' → Valid Student
• ID does not start with '260' → Invalid Student

Expected Output:
Enter student ID: 2600240464
Valid Student
'''
student_id= input("Enter student ID: ")

if student_id.startswith("260"):
    print("Valid Student")
else:
    print("Invalid Student")