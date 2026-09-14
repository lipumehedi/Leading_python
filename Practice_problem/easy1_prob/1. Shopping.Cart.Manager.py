'''
1. Shopping Cart Manager
Problem Statement:
• Take item names as input one by one (3 items).
• Store all items in a list using append().
• Print the full cart and the total number of items.

Acceptance Criteria:
• Start with an empty list.
• Use append() to add each item.
• Print the list.
• Print the count using len().

Expected Output:
Enter item 1: milk
Enter item 2: eggs
Enter item 3: bread
Your cart: ['milk', 'eggs', 'bread']
Total items: 3
'''

shopping_cart = [] 

item1 = input("Enter item 1: ")
shopping_cart.append(item1) 

item2 = input("Enter item 2: ") 
shopping_cart.append(item2)  

item3 = input("Enter item 3: ")
shopping_cart.append(item3)  

print("Your cart:", shopping_cart) 
print("Total items:", len(shopping_cart)) 






