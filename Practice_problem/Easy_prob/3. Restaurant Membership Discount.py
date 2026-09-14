'''
3. Restaurant Membership Discount
Problem Statement:
• Take membership status (yes/no).
• Take total bill amount.
• Members get 10% discount.
• Non-members pay full price.
• Print final bill.
Acceptance Criteria:
• Member (yes): Final bill = bill amount × 0.90
• Non-member (no): Final bill = full bill amount

Expected Output:
Are you a member? yes
Enter bill amount: 5000
Final bill: 4500.0
'''

member = input("Are you a member?(Yes/No): ").lower()
bill = float(input("Enter bill amount: "))

if member == "yes":
    final_bill = bill * 0.90
else:
    final_bill = bill
print("Final bill:", final_bill)