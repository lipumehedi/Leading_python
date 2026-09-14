'''
9. Product Stock Checker

Problem Statement:
• Take product quantity input.
• Check whether quantity is greater than zero.
• Print stock status.

Acceptance Criteria:
• Quantity > 0 → In Stock
• Quantity <= 0 → Out of Stock

Expected Output:
Enter quantity: 5
In Stock
'''
qty =int(input("Enter quantity: "))

if qty > 0:
    print("In stock")
else:
    print("Out of stock")