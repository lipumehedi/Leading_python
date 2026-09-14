'''
10. Hospital Patient Management System
Concepts: All — print · String Methods · Conditionals · Lists · While Loop · Data Types

Problem Statement:
• Use a while loop to register patients until the user types 'done'.
• For each patient: take name, age (int), and severity level (1–10, int).
• Store all patient records in a 2D list: each row is [name, age, severity].
• After registration, print all patients with their details.
• Apply priority rules:
• • Age >= 60 OR severity >= 7 → Priority Treatment
• • Age >= 18 AND severity >= 4 → Normal Treatment
• • Otherwise → Standard Queue
• Print priority status next to each patient.
• Count and print how many patients fall in each priority category.

Acceptance Criteria:

• Use while True with break on name == 'done'.
• Use .title() on patient name before storing.
• Use int() for age and severity.
• Store each patient as a list [name, age, severity] inside a 2D list.
• Use if/elif/else for priority classification.
• Use three counter variables for priority, normal, and standard counts.

Expected Output:
Enter patient name (or 'done'): tanaka hiroshi
Enter age: 68
Enter severity (1-10): 5
Enter patient name (or 'done'): yuki sato
Enter age: 25
Enter severity (1-10): 8
Enter patient name (or 'done'): done
--- Patient Report ---
Tanaka Hiroshi | Age: 68 | Severity: 5 -> Priority Treatment
Yuki Sato | Age: 25 | Severity: 8 -> Priority Treatment
Priority Treatment : 2
Normal Treatment : 0
Standard Queue : 0
'''
patients = []

while True:
    name = input("Enter patient name (or 'done'): ")
    
    if name.lower() == "done":
        break

    age = int(input("Enter age: "))
    severity = int(input("Enter severity (1-10): "))

    patient = [name.title(), age, severity]
    patients.append(patient)

priority_count = 0
normal_count = 0
standard_count = 0
print("--- Patient Report ---")

i = 0
while i < len(patients):
    name = patients[i][0]
    age = patients[i][1]
    severity = patients[i][2]

    if age >= 60 or severity >= 7:
        status = "Priority Treatment"
        priority_count += 1
    elif age >= 18 and severity >= 4:
        status = "Normal Treatment"
        normal_count += 1
    else:
        status = "Standard Queue"
        standard_count += 1
    print(f"Name: {name} | Age: {age} | Severity: {severity} -> {status}")
    
    i += 1

print(f"Priority Treatment: {priority_count}")
print(f"Normal Treatment: {normal_count}")
print(f"Standard Queue: {standard_count}")