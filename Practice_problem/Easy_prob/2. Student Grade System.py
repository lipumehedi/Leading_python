'''
2. Student Grade System

Problem Statement:
• Take student's marks as input.
• Use if-elif-else to determine grade.
• Print the grade based on marks.

Acceptance Criteria:
• Marks >= 90 → A+
• Marks >= 80 → A
• Marks >= 70 → B
• Marks >= 60 → C
• Marks < 60 → F (Fail)

Expected Output:
Enter your marks: 85
A
'''

marks =int(input("Enter your marks: "))

if 90<= marks and marks <= 100:
    print("Grade: A+")
elif 80<= marks <90:
    print("Grade: A")
elif 70<=marks <80:
    print("Grade: B")
elif 60<=marks < 70:
    print("Grade: C")
elif 0<= marks <60:
    print("F(Fail)")
else:
    print("Invalid number")
