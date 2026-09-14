'''
11. Bus Fare System

Problem Statement:
• Take passenger age.
• Calculate fare based on age category.
• Print the fare in yen.

Acceptance Criteria:
• Age <= 12 (Child) → Fare: 150 yen
• Age <= 17 (Teen) → Fare: 300 yen
• Age <= 59 (Adult) → Fare: 500 yen
• Age >= 60 (Senior) → Fare: 200 yen

Expected Output:
Enter age: 15
Bus fare: 300 yen
'''

age = int(input("Enter age: "))

if 0<age<=12:
    print("Bus Fare: 150 yen")
elif 12 <age<=17:
    print("Bus Fare: 300 yen")
elif 17<age<= 59:
    print("Bus Fare: 500 yen")
elif age>=60:
    print("Bus Fare: 200 yen")
else:
    print("Invalid age")
