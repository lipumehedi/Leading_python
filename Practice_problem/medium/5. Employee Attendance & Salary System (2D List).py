
'''
5. Employee Attendance & Salary System (2D List)
Concepts: 2D Lists · While Loop · Conditionals · Data Types · String Methods

Problem Statement:
• A company tracks employee attendance using a 2D list.
• Each row stores one employee's data: [name, days_present, daily_wage].
• The company has 4 employees — define the 2D list with pre-filled data.
• Use a while loop to process each employee and calculate their monthly salary.
• Deduct 10% from salary if days present is below 20.
• Add a 5% bonus if days present is 26 or more.
• Otherwise pay exact salary (days_present x daily_wage).
• Print a formatted payroll report for all employees.

Acceptance Criteria:
• Define a 2D list with 4 rows, each as [name, days_present, daily_wage].

• Use a while loop with index to iterate through the list.
• Access values using records[i][0], records[i][1], records[i][2].
• Use if/elif/else for deduction, bonus, and standard pay.
• Use .title() when printing names.
• Print a clean payroll table with status (Deducted / Bonus / Standard).

Expected Output:
=================================================
MONTHLY PAYROLL REPORT
=================================================
Name | Days | Daily Wage | Salary | Status
-------------------------------------------------
Aiko Yamamoto | 28 | 2000 | 58800 | Bonus
Kenji Mori | 18 | 1500 | 24300 | Deducted
Hana Sato | 22 | 1800 | 39600 | Standard
Riku Tanaka | 26 | 2500 | 68250 | Bonus
-------------------------------------------------
Total Payroll: 190950
'''


records = [
    ["Aiko Yamamoto", 28, 2000],
    ["Kenji Mori", 18, 1500],
    ["Hana Sato", 22, 1800],
    ["Riku Tanaka", 26, 2500]
]
print("=================================================")
print("MONTHLY PAYROLL REPORT")
print("=================================================")
print("Name | Days | Daily Wage | Salary | Status")
print("-------------------------------------------------")

i = 0
total_payroll = 0

while i < len(records):
    name = records[i][0]
    days = records[i][1]
    wage = records[i][2]

    salary = days * wage

    if days < 20:
       salary = salary - (salary * 0.10)
       status = "Deducted"
    
    elif days >= 26:
        salary = salary + (salary * 0.05)
        status = "Bonus"
    else:
        status = "Standard"
    salary = int(salary)

    print(f"{name.title()} | {days} | {wage} | {salary} | {status}")
    total_payroll += salary
    i += 1
print("-------------------------------------------------")
print(f"Total Payroll: {total_payroll}")