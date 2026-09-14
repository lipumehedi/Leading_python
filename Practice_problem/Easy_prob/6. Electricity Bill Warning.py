'''
6. Electricity Bill Warning

Problem Statement:
• Take electricity unit input.
• Check whether usage exceeds 500 units.
• Print warning accordingly.

Acceptance Criteria:
• Units > 500 → Print: High Bill
• Units <= 500 → Print: Normal Bill

Expected Output:
Enter units: 700
High Bill
'''

units = float(input("Enter units:"))

if 0<=units < 500:
    print("Low bill")
elif units>=500:
    print("High Bill")
else:
    print("Invalid units(units>=0)")