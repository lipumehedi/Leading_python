'''
2. Hospital Medicine Inventory System
Concepts: While Loop · Lists · Conditionals · Data Types · String Methods

Problem Statement:
• A hospital pharmacy records incoming medicine stock every day.
• Each medicine entry has: name, quantity (int), and unit price (float).
• Use a while loop to keep accepting entries until the pharmacist types 'done'.
• Store medicine names (title case), quantities, and unit prices in three separate lists.
• After entry is complete, print the full inventory table.
• For each medicine, calculate total value (quantity x unit price).
• Mark stock status: quantity >= 100 → 'Sufficient', quantity >= 50 → 'Low', below 50 → 'Critical'.
• Print the medicine with the highest total stock value at the end.

Acceptance Criteria:
• Use while True with break when name == 'done'.
• Use .title() on medicine name before storing.
• Use int() for quantity and float() for unit price.
• Use three separate lists for names, quantities, and prices.
• Use append() to add to all three lists.
• Use a while loop with index to print the table and find max value.
• Use if/elif/else for stock status.
• Track highest value medicine using a variable.

Expected Output:
Enter medicine name (or 'done'): paracetamol
Enter quantity: 200
Enter unit price: 15.5
Enter medicine name (or 'done'): amoxicillin
Enter quantity: 45
Enter unit price: 80.0
Enter medicine name (or 'done'): ibuprofen
Enter quantity: 75
Enter unit price: 25.0
Enter medicine name (or 'done'): done

==========================================================
PHARMACY INVENTORY REPORT
==========================================================
Medicine | Qty | Unit Price | Total Value | Status
----------------------------------------------------------
Paracetamol | 200 | 15.5 | 3100.0 | Sufficient
Amoxicillin | 45 | 80.0 | 3600.0 | Critical
Ibuprofen | 75 | 25.0 | 1875.0 | Low
----------------------------------------------------------
Highest value stock: Amoxicillin (3600.0 yen)
'''



medicine_names = []
quantities = []
unit_prices = []

while True:
    name = input("Enter medicine name (or 'done'):")
    if name.lower()=="done":
        break
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter unit price: "))

    medicine_names.append(name.title())
    quantities.append(quantity)
    unit_prices.append(price)

print("==========================================================")
print("PHARMACY INVENTORY REPORT")
print("==========================================================")
print("Medicine | Qty | Unit Price | Total Value | Status")
print("----------------------------------------------------------")

i = 0
highest_value = 0
highest_medecine = " "

while i  < len(medicine_names):
    total_value = quantities[i] * unit_prices[i]
    if quantities[i] >= 100:
        status = "Sufficient"
    elif quantities[i] >= 50:
        status = "Low"
    else:
        status = "Critical"
    print(f"{medicine_names[i]} | {quantities[i]} | {unit_prices[i]} | {total_value} | {status}")

    if total_value > highest_value:
        highest_value = total_value
        highest_medecine = medicine_names[i]
        i += 1
print("----------------------------------------------------------")
print(f"Highest value stock: {highest_medecine} ({highest_value} yen.)")
