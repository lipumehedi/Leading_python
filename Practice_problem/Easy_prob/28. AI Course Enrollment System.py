'''

28. AI Course Enrollment System

Problem Statement:
• Take skill level (beginner / intermediate / advanced) and age.
• Approve enrollment according to conditions.
• Print enrollment result.

Acceptance Criteria:
• Skill: beginner AND age >= 18 → Enrollment Approved
• Skill: intermediate AND age >= 16 → Enrollment Approved
• Skill: advanced AND age >= 14 → Enrollment Approved
• Age below required threshold → Enrollment Denied
• Invalid skill level → Invalid Input
 
Expected Output:
Enter skill level: beginner
Enter age: 20
Enrollment Approved
'''
skill = input("Enter skill level: ")
age = int(input("Enter age: "))

if skill == "beginner":
    if age >= 18:
        print("Entrollment Approved")
    else:
        print("Entrolled Denied")
elif skill == "intermediate":
    if age >= 16:
        print("Entrollment Approved")
    else:
        print("Entrolled Denied")
elif skill == advanced:
    if age >= 14:
        print("Entrollment Approved")
    print("Entrolled Denied")
else:
    print("Invalid Input.")