

'''
6. Restaurant Rating Summary

Problem Statement:
• Given ratings = [3.8, 4.5, 2.9, 4.8, 4.1].
• Print the highest and lowest rating.
• Print ratings sorted highest to lowest (keep original unchanged).
• If the top rating is >= 4.5, print 'Top restaurant qualifies for Featured badge!'; otherwise print 'No
featured badge this week'.

Acceptance Criteria:
• Use max() and min() for highest and lowest.
• Use sorted(ratings, reverse=True) — do not modify original list.
• Store the top rating in a variable.
• Use if/else comparing top rating to 4.5.

Expected Output:
Highest: 4.8 | Lowest: 2.9
Ranked: [4.8, 4.5, 4.1, 3.8, 2.9]
Top restaurant qualifies for Featured badge!
'''

rating = [3.8, 4.5, 2.9, 4.8, 4.1]

highest = max(rating)
lowest  = min(rating)
print("Highest:", highest, "| Lowest:", lowest)

ranked = sorted(rating, reverse=True)
top_rating = ranked[0]
print("Ranked:",ranked)

if top_rating >= 4.5:
    print("Top restaurant qualifies for Featured badge!")
else:
    print("No featured badge this week.")