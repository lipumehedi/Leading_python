'''
25. Hospital Emergency Priority System

Problem Statement:
• Take age and emergency level (scale 1-10).
• Determine patient treatment priority.
• Print priority level.

Acceptance Criteria:
• Age >= 60 OR emergency level >= 7 → Priority Treatment
• Age >= 18 AND emergency level >= 4 → Normal Treatment
• Otherwise → Standard Queue

Expected Output:
Enter age: 65
Enter emergency level: 6
Priority Treatment
'''
age = int(input("Enter age: "))
emergency_lvl = int(input("Enter emergency Level: "))

if age >= 60 or emergency_lvl >=7:
    print("Priority Treatment")
elif age >= 18 and emergency_lvl >=4:
    print("Normal Treatment")
else:
    print("Standard Queue")