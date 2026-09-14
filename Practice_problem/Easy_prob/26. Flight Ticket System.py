'''
26. Flight Ticket System

Problem Statement:
• Take nationality and passport validity (yes/no).
• Allow booking only if passport is valid.
• Print booking result.

Acceptance Criteria:
• Passport valid (yes) → Ticket Booking Allowed
• Passport invalid (no) → Ticket Booking Denied

Expected Output:
Enter nationality: Bangladesh
Is passport valid? yes
Ticket Booking Allowed
'''
nationality = input("Enter nationality: ")
passport = input("Is passport valid? ")

if passport == "yes":
    print("Ticket Booking Allowed.")
else:
    print("Ticket Booking Denied.")