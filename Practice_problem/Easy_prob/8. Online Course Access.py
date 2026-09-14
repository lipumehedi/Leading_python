'''
8. Online Course Access

Problem Statement:
• Take age and country input.
• Access allowed if age >= 18 OR country is Japan.
• Print access message.

Acceptance Criteria:
• Age >= 18 OR country == 'Japan' → Access Granted
• Age < 18 AND country != 'Japan' → Access Denied

Expected Output:
Enter age: 17
Enter country: Japan
Access Granted
'''

age = int(input("Enter age: "))
country = input("Enter country: ").capitalize()

if age >= 18 or country == "Japan":
    print("Access Granted")
else:
    print("Access Denied")
