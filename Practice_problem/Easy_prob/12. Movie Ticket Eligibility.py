'''
12. Movie Ticket Eligibility

Problem Statement:
• Take age input.
• Only users aged 18 or above can watch the movie.
• Print eligibility message.

Acceptance Criteria:
• Age >= 18 → You can watch the movie
• Age < 18 → You cannot watch the movie

Expected Output:
Enter age: 22
You can watch the movie
'''
age =int(input("Enter age: "))

if age >= 18:
    print("You can watch the movie.")
elif 0<age<18:
    print("You cannot watch the movie.")
else:
    print("Invalid age")