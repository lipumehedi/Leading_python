'''
1. Bank Transaction History Tracker
Concepts: While Loop · Lists · String Methods · Conditionals · Data Types

Problem Statement:

• A bank records every transaction a customer makes during a session.
• Each transaction has a type (deposit/withdraw) and an amount.
• The session starts with a balance of 100000 yen.
• Use a while loop — keep taking transactions until the customer types 'done'.
• For each transaction: store the type (uppercase) and amount in two separate lists.
• If withdraw and amount > current balance, reject it: print 'Rejected: Insufficient balance' and do NOT
store it.
• Update balance after each valid transaction.
• After the session ends, print the full transaction history with running balance,
• the total number of deposits, total number of withdrawals, and closing balance.

Acceptance Criteria:

• Start balance = 100000.
• Use while True with break when input == 'done'.
• Use .upper() on transaction type before storing.
• Use two lists: one for types, one for amounts — only store valid transactions.
• Use append() to add to each list.
• Use a counter for deposits and another for withdrawals.
• Use a while loop with index to print the history table.
• Use len() to confirm total transactions stored.

Expected Output:
 
Opening Balance: 100000
Enter transaction type (deposit/withdraw or 'done'): deposit
Enter amount: 20000
Enter transaction type (deposit/withdraw or 'done'): withdraw
Enter amount: 50000
Enter transaction type (deposit/withdraw or 'done'): withdraw
Enter amount: 90000
Rejected: Insufficient balance
Enter transaction type (deposit/withdraw or 'done'): withdraw
Enter amount: 30000
Enter transaction type (deposit/withdraw or 'done'): done
============================================
TRANSACTION HISTORY
============================================
No. | Type | Amount | Balance

--------------------------------------------
1 | DEPOSIT | +20000 | 120000
2 | WITHDRAW | -50000 | 70000
3 | WITHDRAW | -30000 | 40000
--------------------------------------------
Total Deposits : 1
Total Withdrawals: 2
Closing Balance : 40000

'''




balance = 100000

types = []
amounts = []

deposit_count = 0
withdraw_count = 0

print(f"Opening Balance: {balance}")

while True:
    t_type = input("Enter transaction type(deposit/withdraw or 'done'): ")
    if t_type.lower() == "done":
        break
    amount = int(input("Enter amount: "))
    t_type = t_type.upper()

    if t_type == "withdraw" and amount > balance:
        print("Rejected: Insufficient balance")
    else:
        types.append(t_type)
        amounts.append(amount)
        if t_type == "DEPOSIT":
            balance += amount
            deposit_count += 1
        else:
            balance -= amount
            withdraw_count += 1
print("============================================")
print("TRANSACTION HISTORY")
print("============================================")
print("No. | Type | Amount | Balance")
print("--------------------------------------------")
running_balance = 100000
i = 0
while i < len(types):
    if types[i] == "DEPOSIT":
        running_balance += amounts[i]
        amt_str = "+" + str(amounts[i])
    else:
        running_balance -= amounts[i]
        amt_str = "-" + str(amounts[i])
    print(f"{i+1} | {types[i]} | {amt_str[i]} | {running_balance}")
    i +=1
print("--------------------------------------------")
print(f"Total Deposits : {deposit_count}")
print(f"Total Withdrawals: {withdraw_count}")
print(f"Closing Balance : {running_balance}")