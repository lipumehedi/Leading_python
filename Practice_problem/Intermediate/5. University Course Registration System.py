'''
5. University Course Registration System
Concepts: 3D Lists · 2D Lists · While Loop · String Methods · Conditionals · Data Types
Problem Statement:
• A university has 3 departments, each offering 4 courses.
• Each course stores: [course_name, credits, max_seats, enrolled].
• Store this in a 3D list: [department][course][field].
• Department names: ['Engineering', 'Business', 'Arts']
• Print the full course catalog for all departments using nested while loops with index.
• Mark each course as 'Open' if enrolled < max_seats, else 'Full'.
• Use a while loop to allow a student to register: enter department number (0-2) and course
• number (0-3). Enter -1 to exit.
• If the course is full, print 'Registration failed: Course is full'.
• If open, increment enrolled by 1 and confirm registration.
• After exiting, print total successful registrations made during the session.
Acceptance Criteria:
• Define a 3D list with shape [3][4][4].
• Use index access courses[d][c][3] to read/update enrolled count.
• Use nested while loops with index to print the catalog.
• Use while True with break when input == -1.
• Update courses[d][c][3] += 1 after a successful registration.
• Count and print total successful registrations after the loop.
Expected Output:
============================================
UNIVERSITY COURSE CATALOG
============================================
Department: Engineering
0. Algorithms | Credits: 3 | Seats: 30 | Enrolled: 28 | Open

1. Networks | Credits: 3 | Seats: 25 | Enrolled: 25 | Full
2. Databases | Credits: 2 | Seats: 35 | Enrolled: 10 | Open
3. AI Basics | Credits: 4 | Seats: 20 | Enrolled: 20 | Full
Department: Business
0. Marketing | Credits: 3 | Seats: 40 | Enrolled: 38 | Open
1. Finance | Credits: 3 | Seats: 30 | Enrolled: 30 | Full
2. Management | Credits: 2 | Seats: 35 | Enrolled: 20 | Open
3. Economics | Credits: 4 | Seats: 25 | Enrolled: 25 | Full
Department: Arts
0. History | Credits: 3 | Seats: 30 | Enrolled: 15 | Open
1. Philosophy | Credits: 3 | Seats: 20 | Enrolled: 20 | Full
2. Literature | Credits: 2 | Seats: 25 | Enrolled: 10 | Open
3. Fine Arts | Credits: 4 | Seats: 20 | Enrolled: 18 | Open
Enter department number (0-2, or -1 to exit): 0
Enter course number (0-3): 1
Registration failed: Course is full.
Enter department number (0-2, or -1 to exit): 0
Enter course number (0-3): 0
Registered successfully for Algorithms! (Enrolled: 29/30)
Enter department number (0-2, or -1 to exit): -1
Total successful registrations this session: 1
'''

departments = ["Engineering", "Business", "Arts"]

courses =[
    [
        ["Algorithms", 3, 30, 28],
        ["Networks", 3, 25, 25],
        ["Databases", 2, 35, 10],
        ["AI Basics", 4, 20, 20]
    ],
    [
        ["Marketing", 3, 40, 38],
        ["Finance", 3, 30, 30],
        ["Management", 2, 35, 20],
        ["Economics", 4, 25, 25]
    ],
    [ 
        ["History", 3, 30, 15],
        ["Philosophy", 3, 20, 20],
        ["Literature", 2, 25, 10],
        ["Fine Arts", 4, 20, 18]
    ]
]
print("============================================")
print("UNIVERSITY COURSE CATALOG")
print("============================================")


d = 0
while d < len(departments):
    print(f"Department:{departments[d]}")

    c = 0
    while c < len(courses[d]):
        course_name = courses[d][c][0].title()
        credits = courses[d][c][1]
        max_seats = courses[d][c][2]
        entrolled = courses[d][c][3]

        if entrolled < max_seats:
            status = "Open"
        else:
            status = "Full"
        print(f"{c}. {course_name} | Credits: {credits} | Seats: {max_seats} | Emtrolled: {entrolled} | {status}")

        c +=1
    d += 1

successful_registrations = 0
while True:
    dept_num = int(input("Enter department number (0-2, or -1 to exit):"))

    if dept_num == -1:
        break
    course_num = int(input("Enter course number (0-3): "))

    max_seats = courses[dept_num][course_num][2]
    entrolled = courses[dept_num][course_num][3]

    if entrolled >= max_seats:
        print("Registration failed: Course is full.")
    else:
        courses[dept_num][course_num][3] += 1
        successful_registrations = 1

        course_name =  courses[dept_num][course_num][0]
        print(
            f"Registered successfully for {course_name}! " 
            f"(Entrolled: {courses[dept_num][course_num][3]}/{max_seats})"
            )

print(f"Total successful registrations this session: { successful_registrations }")