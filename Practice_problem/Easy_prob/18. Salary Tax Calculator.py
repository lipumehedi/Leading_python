'''
18. Salary Tax Calculator

Problem Statement:
• Take salary input.
• Calculate tax percentage based on salary range.
• Print the tax amount.

Acceptance Criteria:
• Salary > 1,000,000 → Tax rate: 30%
• Salary > 500,000 → Tax rate: 10%
• Salary <= 500,000 → Tax rate: 0% (No tax)

Expected Output:
Enter salary: 600000
Tax: 60000.0
'''

salary = int(input("Enter salary: "))

if salary > 1000000:
    tax =salary * 0.30
elif 500000<salary < 1000000:
    tax = salary * 0.10
elif 0<salary<=500000:
    tax = 0
else:
    print("Invalid salary")
print("Tax:", tax)