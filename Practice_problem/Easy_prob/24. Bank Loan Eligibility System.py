'''
24. Bank Loan Eligibility System

Problem Statement:
• Take salary and years of experience.
• Approve loan if both conditions are satisfied.
• Print loan result.

Acceptance Criteria:
• Salary >= 300,000 AND Experience >= 2 years → Loan Approved
• Salary < 300,000 → Salary requirement not met
• Experience < 2 → Experience requirement not met

Expected Output:
Enter salary: 400000
Enter experience: 3
Loan Approved
'''
salary = float(input("Enter salary:"))
experience = int(input("ENter experience: "))

if salary >= 300000 and experience >= 2:
    print("Loan Approved.")
elif salary < 300000 :
    print("Salary requirement not met.")
else:
    print("Experience requirement not met.")