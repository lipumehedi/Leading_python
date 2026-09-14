'''
5. ATM PIN Verification

Problem Statement:
• Take PIN input.
• Verify entered PIN with the correct PIN.
• Print access message.

Acceptance Criteria:
• Correct PIN is: 1234
• Entered PIN == 1234 → Access Granted
• Entered PIN != 1234 → Access Denied

Expected Output:
Enter PIN: 1234
Access Granted
'''
pin = int(input("Enter PIN: "))
correct_pin = 1234
if pin == correct_pin:
    print("Access Granted")
else:
    print("Access Denied")
