'''
3. ATM Withdrawal System
Concepts: While Loop · Conditionals · Data Types

Problem Statement:
• Set an initial account balance of 50000.
• Use a while loop to keep allowing withdrawals until the user types 0 to exit.
• Each iteration: ask for withdrawal amount.
• If amount > balance, print 'Insufficient funds'.
• If amount <= 0, exit the loop.
• Otherwise, deduct amount and print updated balance.
• After the loop, print the final balance.

Acceptance Criteria:
• Use a while True loop with a break condition.
• Use int() or float() to convert input.
• Use if/elif/else inside the loop.
• Print balance after every successful withdrawal.
• Print final balance after loop ends.
 
Expected Output:
Balance: 50000
Enter withdrawal amount (0 to exit): 10000
Withdrawal successful. Remaining balance: 40000
Enter withdrawal amount (0 to exit): 60000
Insufficient funds.
Enter withdrawal amount (0 to exit): 0
Thank you! Final balance: 40000
'''

balance = 50000

print(f"Balance: {balance}")

while True:
    amount = int(input("Enter withdrawal amount (0 to exit): "))
    if amount == 0:
        break
    elif amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        print(f"Withdrawal successful. Remaining balance: {balance}")
print(f"Thank you! Final balance: {balance}")


