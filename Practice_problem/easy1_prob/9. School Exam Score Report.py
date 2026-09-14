'''
9. School Exam Score Report

Problem Statement:
• Given scores = [[85, 90, 78], [92, 88, 95], [70, 75, 80]].
• Each inner list is one student's scores: Maths, Science, English.
• Print the Maths score (index 0) for all 3 students.
• Find and print the highest single score across the entire grid.
• Print the Science score (index 1) for Student 2 (index 1).

Acceptance Criteria:
• Access individual scores using double indexing: scores[row][col].
• Print Maths scores for rows 0, 1, 2.
• Build a flat list using extend() or concatenation, then use max().
• Print the correct Science score for scores[1][1].

Expected Output:
Maths scores -> Student 1: 85 | Student 2: 92 | Student 3: 70
Highest score in class: 95
Student 2's Science score: 88

'''
scores = [[85, 90, 78], [92, 88, 95], [70, 75, 80]]

print("Maths scores -> Student 1: ", scores[0][0], "| Student 2: ", scores[1][0], "| Student 3: ", scores[2][0])

all_scores = scores[0]+scores[1]+scores[2]
print("Highest score in class: ", max(all_scores))
print("Student 2's Science score: ", scores[1][1])




