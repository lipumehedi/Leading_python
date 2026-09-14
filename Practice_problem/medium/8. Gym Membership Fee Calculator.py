'''
8. Gym Membership Fee Calculator

Concepts: While Loop · Conditionals · Data Types · print

Problem Statement:
• Use a while loop to process multiple gym members.
• Each iteration: take member name, age (int), and plan (basic/premium/vip).
• Calculate monthly fee: basic=2000, premium=4000, vip=7000.
• Members aged 60 and above get a 20% senior discount on any plan.
• Members aged 15 and below get a 30% student discount on any plan.
• If the user enters 'stop' as the name, exit the loop.
• After loop, print total members processed and total revenue collected.

Acceptance Criteria:
• Use while True with break on name == 'stop'.
• Use int() for age, .lower() for plan comparison.
• Use if/elif/else for plan fee selection.
• Apply senior/student discount using separate if/elif conditions.
• Track member count and total revenue with variables outside the loop.
 
Expected Output:
Enter member name (or 'stop' to exit): Aiko
Enter age: 65
Enter plan (basic/premium/vip): premium
Aiko -> Plan: premium | Fee: 4000 | Discount: 20% | Payable: 3200.0
Enter member name (or 'stop' to exit): Kenji
Enter age: 14
Enter plan (basic/premium/vip): basic
Kenji -> Plan: basic | Fee: 2000 | Discount: 30% | Payable: 1400.0
Enter member name (or 'stop' to exit): stop
Total members: 2
Total revenue: 4600.0
'''
total_members = 0
total_revenue = 0.0

while True:
    name = input("Enter member name (or 'stop' to exit): ")
    if name.lower() == 'stop':
        break
    age = int(input("Enter age: "))
    plan = input("Enter plan (basic/premium/vip): ").lower()

    if plan == "basic":
        fee = 2000
    elif plan == "premium":
        fee = 4000
    else:
        fee = 7000

    #discount selection
    if age >= 60:
        discount = 20
    elif age <= 15:
        discount = 30
    else:
        discount = 0
    payable = fee * (100 - discount)/100
    print(f"{name} -> Plan: {plan} | Fee: {fee} | Discount: {discount}% | Payable: {payable}")

    total_members += 1
    total_revenue += payable

print(f"Total members: {total_members}")
print(f"Total revenue: {total_revenue}")