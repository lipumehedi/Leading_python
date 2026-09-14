'''
21. Advanced E-commerce Discount System

Problem Statement:
• Take membership status and cart amount.
• Apply discount rules based on amount range.
• Print final payable bill.

Acceptance Criteria:
• Member + Amount >= 20,000 → 3% discount
• Member + Amount >= 10,000 → 2% discount
• Member + Amount < 10,000 → 1% discount
• Non-member → No discount (full price)

Expected Output:
Are you a member? yes
Enter amount: 30000
Final bill: 29100.0
'''
membership = input("Are you a menmber?").lower()
amount = float(input("Enter amount: "))

if membership == "yes":
    if amount >= 20000:
        print("Final Bill:", amount * 0.97)
    elif amount >= 10000:
        print("Final Bill:", amount*0.98)
    else:
        print("Final Bill:", amount*0.99)
else:
    print("Final Bill:", amount)