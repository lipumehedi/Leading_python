'''
4. Student Name Formatter
Problem Statement:
• Take 3 student names as input (may be in any case).
• Store each name in a list after converting to title case.
• Print the final list and the total student count.

Acceptance Criteria:
• Use append() to add each name.
• Apply .title() before storing.
• Print the list and use len() for count.

Expected Output:
Enter name 1: ANANYA SHARMA
Enter name 2: kenji tanaka
Enter name 3: OMAR FAROUK
Students: ['Ananya Sharma', 'Kenji Tanaka', 'Omar Farouk']
Total students: 3
'''

students = []

student1 = input("Enter name 1: ")
students.append(student1.title())

student2 = input("Enter name 2: ")
students.append(student2.title())

student3 = input("Enter name 3: ")
students.append(student3.title())

print("Students:", students)
print("Total students:",len(students))