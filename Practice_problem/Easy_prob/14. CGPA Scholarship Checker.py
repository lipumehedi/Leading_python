'''
14. CGPA Scholarship Checker

Problem Statement:
• Take CGPA input.
• Determine scholarship category based on CGPA.
• Print scholarship result.

Acceptance Criteria:
• CGPA >= 3.80 → Full Scholarship
• CGPA >= 3.50 → Half Scholarship
• CGPA >= 3.00 → Quarter Scholarship
• CGPA < 3.00 → No Scholarship

Expected Output:
Enter CGPA: 3.85
Full Scholarship

'''
cgpa = float(input("Enter CGPA: "))

if cgpa >= 3.80:
    print("Full Scholarship")
elif cgpa >= 3.50:
    print("Half Scholarship")
elif cgpa >= 3.00:
    print("Quarter Scholarship")
else:
    print("NO Scholarship")