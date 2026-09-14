'''
1. Voting Eligibility Checker

Problem Statement:
• Take the user's age as input.
• Convert the input into integer.
• Check whether age is 18 or above.
• Print proper eligibility message.

Acceptance Criteria:
• Age >= 18 → Print: Eligible for voting
• Age < 18 → Print: Not eligible for voting
Expected Output:
Enter your age: 20
Eligible for voting
'''
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible for voting")   
else:
     print("NOt Eligible for voting")
