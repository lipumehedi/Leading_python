'''
4. Warehouse Stock Manager
Concepts: 2D Lists · While Loop · String Methods · Lists · Conditionals
Problem Statement:
• A warehouse manager adds product stock records using a while loop.
• Each record contains: [product_name, category, quantity, unit_price].
• Accept records until the manager types 'done'.
• Store each record as a list inside a 2D list.
• Use .title() on product name and .upper() on category before storing.
• After entry, print the full inventory table using a while loop with index.
• For each item, compute total stock value (quantity x unit_price).
• Classify stock: quantity >= 100 --> 'High', quantity >= 50 --> 'Medium', below 50 --> 'Low'.
• Print the product with the highest stock value at the end.
Acceptance Criteria:
• Use while True with break when name == 'done'.
• Store records as: inventory.append([name, category, qty, price]).
• Access using inventory[i][0] through inventory[i][3].
• Use if/elif/else for stock level classification.
• Track highest value product using a variable and index.
Expected Output:

Enter product name (or 'done'): bolt
Enter category: hardware
Enter quantity: 250
Enter unit price: 12.5
Enter product name (or 'done'): cable
Enter category: electronics
Enter quantity: 40
Enter unit price: 350.0
Enter product name (or 'done'): done
=============================================================
WAREHOUSE INVENTORY REPORT
=============================================================
Product | Category | Qty | Unit Price | Total Value | Stock
-------------------------------------------------------------
Bolt | HARDWARE | 250 | 12.5 | 3125.0 | High
Cable | ELECTRONICS | 40 | 350.0 | 14000.0 | Low
-------------------------------------------------------------
Highest value product: Cable (14000.0 yen)
'''
inventory = []

while True:
    name = input("Enter product name (or 'done'): ")
    
    if name == "done":
        break

    category = input("Enter category: ")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter unit price: "))

    name = name.title()
    category =category.upper()

    inventory.append([name, category, qty, price])

print("=============================================================")
print("WAREHOUSE INVENTORY REPORT")
print("=============================================================")
print("Product | Category | Qty | Unit Price | Total Value | Stock")
print("-------------------------------------------------------------")



highest_value = 0
highest_product = " "


i = 0
while i < len(inventory):
    name = inventory[i][0]
    category = inventory[i][1]
    qty = inventory[i][2]
    price = inventory[i][3]

    total_value = qty * price

    if qty >=100:
        stock_level = "High"
    elif qty >= 50:
        stock_level = "Medium"
    else:
        stock_level = "Low"
    print(f"{name} | {category} | {qty} | " 
     f"{price} | {total_value} | {stock_level}")
    
    
    if total_value > highest_value:
        highest_value = total_value
        highest_product = name
    
    i += 1

print("-------------------------------------------------------------")
print(f"Highest value product: {highest_product} ({highest_value} yen)")
