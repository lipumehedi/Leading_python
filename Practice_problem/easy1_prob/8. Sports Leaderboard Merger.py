
'''
8. Sports Leaderboard Merger

Problem Statement:
• Given region_a = [88, 74, 95, 61] and region_b = [79, 91, 85, 70].
• Merge both lists into one using extend().
• Sort the merged list in descending order.
• Slice the top 3 scores.
• If the highest score is above 90, print 'A score above 90 made it to the podium!'; otherwise print 'No
score above 90 this season'.

Acceptance Criteria:
• Use extend() to merge — do not use the + operator.
• Use .sort(reverse=True) for descending sort.
• Use slice [:3] for top 3 scores.
• Use if/else comparing merged[0] > 90.

Expected Output:
All scores: [95, 91, 88, 85, 79, 74, 70, 61]
Top 3 finalists: [95, 91, 88]
A score above 90 made it to the podium!
'''
region_a = [88, 74, 95, 61]
region_b = [79, 91, 85, 70]

region_a.extend(region_b)

region_a.sort(reverse=True)

top = region_a[:3]

print("All scores:",region_a)
print("Top 3:", top)

if region_a[0] > 90:
    print("A score above 90 made it to the podium!")
else:
    print("No score above 90 this season")

