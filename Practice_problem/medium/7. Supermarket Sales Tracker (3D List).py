
#7. Supermarket Sales Tracker (3D List)
'''
Concepts: 3D Lists · Indexing · Data Types · print

Problem Statement:
• A supermarket chain has 2 branches, each with 3 product categories, each category tracking sales
for 4 weeks.
• Store all weekly sales figures in a 3D list: [branch][category][week].
• Branch names: ['Shibuya', 'Shinjuku']
• Category names: ['Food', 'Drinks', 'Snacks']
• Print a full sales report: for each branch, show each category's 4-week sales.
• Calculate and print the total sales for each branch.
• Find and print which branch had the highest single-week sale and in which category.

Acceptance Criteria:
• Define a 3D list with shape [2][3][4] (2 branches, 3 categories, 4 weeks).
• Use three levels of index access: sales[b][c][w].
• Sum all values in a branch using nested index access (no sum()).
• Track the highest single weekly sale and its branch/category using variables.
• Print branch and category names from their respective lists.

Expected Output:
========================================
SUPERMARKET SALES REPORT
========================================
Branch: Shibuya
Food | Week 1: 120000 Week 2: 135000 Week 3: 118000 Week 4: 142000
Drinks | Week 1: 85000 Week 2: 90000 Week 3: 88000 Week 4: 95000
Snacks | Week 1: 45000 Week 2: 50000 Week 3: 47000 Week 4: 53000
Branch Total: 1068000
Branch: Shinjuku
Food | Week 1: 155000 Week 2: 160000 Week 3: 148000 Week 4: 170000
Drinks | Week 1: 92000 Week 2: 98000 Week 3: 94000 Week 4: 102000
Snacks | Week 1: 60000 Week 2: 65000 Week 3: 58000 Week 4: 70000
Branch Total: 1272000
Highest single-week sale: 170000
Branch: Shinjuku | Category: Food | Week 4
'''

branches = ["Shibuya", "Shinjuku"]
categories =["Food", "Drinks", "Snacks"]

sales = [
    [
        [120000, 135000, 118000, 142000],
        [85000, 90000, 88000, 95000],
        [45000, 50000, 47000, 53000]
    ],
    [
        [155000, 160000, 148000, 170000],
        [92000, 98000, 94000, 102000],
        [60000, 65000, 58000, 70000]
    ]
]

highest_sale = 0
highest_branch = " "
highest_category = " "
highest_week = 0

print("========================================")
print("SUPERMARKET SALES REPORT")
print("========================================")

b = 0
while b < len(branches):
    print(f"Brance: {branches[b]}")
    branch_total = 0
    
    c = 0
    while c < len(categories):
        print(categories[c], "| Week 1:", sales[b][c][0], "Week 2:", sales[b][c][1], "Week 3:", sales[b][c][2], "Week 4:", sales[b][c][3],)

        w = 0
        while w < 4:
            branch_total += sales[b][c][w]
            
            if sales[b][c][w] > highest_sale:
                highest_sale = sales[b][c][w]
                highest_branch = branches[b]
                highest_category = categories[c]
                highest_week = w + 1
            
            w += 1
        c += 1

    print(f"Branch Total: {branch_total}")
  

    b += 1

print(f"Highest single-week sale: {highest_sale}")
print(f"Branch: {highest_branch} | Category: {highest_category} | Week: {highest_week}")