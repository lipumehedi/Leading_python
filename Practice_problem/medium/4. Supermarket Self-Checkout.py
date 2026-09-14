'''
4. Supermarket Self-Checkout
Concepts: Lists · While Loop · Conditionals · Data Types
Problem Statement:
• Use a while loop to keep adding products to a cart.
• Each iteration: ask for product name and price.
• If the user enters 'done' as the product name, stop the loop.
• Store each product and price in two separate lists.
• After the loop, print each item with its price.
• Print total number of items and the total bill amount.

Acceptance Criteria:
• Use while True with a break when name == 'done'.
• Use two lists: one for names, one for prices.
• Use append() to add to both lists.
• Use float() to convert price.
• Use len() for item count and sum() for total bill.

Expected Output:
Enter product (or 'done' to finish): apple
Enter price: 120
Enter product (or 'done' to finish): bread
Enter price: 85
Enter product (or 'done' to finish): done
--- Your Receipt ---
apple : 120.0
bread : 85.0
Total items: 2
Total bill: 205.0
'''

product_names = []
product_prices = []

while True:
    name = input("Enter product (or 'done' to finish): ")

    if name.lower() == "done":
        break
    price = float(input("Enter price: "))

    product_names.append(name)
    product_prices.append(price)
print("--- Your Receipt ---")

i = 0
while i < len(product_names):
    print(f"{product_names[i]} : {product_prices[i]}")
    i += 1
print(f"Total items: {len(product_names)}")
print(f"Total bill: {sum(product_prices)}")

