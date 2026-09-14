'''
23. University Admission System

Problem Statement:
• Take GPA and IELTS score.
• Check minimum eligibility requirements.
• Print admission result.

Acceptance Criteria:
• GPA >= 3.5 AND IELTS >= 6.5 → Eligible for admission
• GPA < 3.5 → GPA requirement not met
• IELTS < 6.5 → IELTS requirement not met

Expected Output:
Enter GPA: 3.8
Enter IELTS: 7
Eligible for admission
'''
gpa = float(input("Enter GPA: "))
ielts = float(input("Enter IELTS: "))

if  gpa >= 3.5 and ielts >= 6.5:
    print("Eligible for admission.")
elif gpa < 3.5:
    print("GPA requirement not met.")
else:
    print("IELTS requirement not met")