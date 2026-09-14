'''
10. Inventory Stock Checker

Problem Statement:
• Given a list of product quantities: [0, 5, 12, 0, 3].
• Print the total number of products.
• Print the maximum and minimum stock quantity.
• Replace the first 0-quantity item by updating index 0 with value 8.
• Print the updated list.

Acceptance Criteria:
• Use len() for total count.
• Use max() and min() for stock extremes.
• Use direct index assignment: stock[0] = 8.
• Print the updated list.

Expected Output:
Total products: 5
Max stock: 12 | Min stock: 0
Updated stock: [8, 5, 12, 0, 3]
'''
product_quantities = [0, 5, 12, 0, 3]
print("Total products:", len(product_quantities))

print("Max stock:", max(product_quantities),"| Min stock:", min(product_quantities))

product_quantities[0]= 8
print("Updated stock:", product_quantities)