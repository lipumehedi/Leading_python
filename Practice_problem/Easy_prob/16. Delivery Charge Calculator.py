'''
16. Delivery Charge Calculator

Problem Statement:
• Take shopping amount.
• Orders above 5000 yen get free delivery.
• Otherwise, a delivery charge is applied.
• Print delivery result.

Acceptance Criteria:
• Amount > 5000 → Free Delivery
• Amount <= 5000 → Delivery Charge: 500 yen

Expected Output:
Enter amount: 7000
Free Delivery
'''
amount = int(input("Enter amount: "))

if amount > 5000:
    print("Free Delivery")
else:
    print("Delivery Charge: 500 yen.")