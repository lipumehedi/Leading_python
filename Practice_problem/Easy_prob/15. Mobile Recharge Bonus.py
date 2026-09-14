'''
15. Mobile Recharge Bonus

Problem Statement:
• Take recharge amount.
• Provide bonus for recharge above 1000 yen.
• Print bonus result.

Acceptance Criteria:
• Amount > 1000 → Bonus Added: 100 yen
• Amount <= 1000 → No Bonus

Expected Output:
Enter recharge amount: 1500
Bonus Added: 100 yen


'''

amount = float(input("Enter recharge amount: "))

if amount > 1000:
    print("Bonus Added: 100 yen")
else:
    print("No Bonus")