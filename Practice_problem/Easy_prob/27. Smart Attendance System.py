'''
27. Smart Attendance System

Problem Statement:
• Take attendance percentage and assignment submission status (yes/no).
• Students need both conditions fulfilled for exam eligibility.
• Print eligibility result.

Acceptance Criteria:
• Attendance >= 75% AND assignment submitted (yes) → Eligible for final exam
• Attendance < 75% → Not eligible (low attendance)
• Assignment not submitted (no) → Not eligible (missing assignment)

Expected Output:
Enter attendance: 80
Assignment submitted? yes
Eligible for final exam

'''
attendance = int(input("Enter attendance: "))
assignment = input("Assignment submitted?(yes/no).: ")

if attendance >= 75 and assignment == "yes":
    print("Eligible for final exam")
elif attendance < 75:
    print("NOt eligible(low attendance)")
else:
    print("Not eligible(missing assignment)")