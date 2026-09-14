'''
1. School Exam Score Tracker
Concepts: 3D Lists · While Loop · Indexing · Data Types

Problem Statement:
• A school tracks exam scores for 2 grades, each with 3 subjects, and 4 students per subject.
• Store all scores in a 3D list: [grade][subject][student].
• Grade names: ['Grade 10', 'Grade 11']
• Subject names: ['Math', 'Science', 'English']
• Use a while loop with index to print scores for each grade and subject.
• For each subject, calculate and print the average score (rounded to 1 decimal).
• Find and print the highest score overall, and which grade and subject it belongs to.
• Count students who scored below 50 in any subject (failing students).

Acceptance Criteria:
• Define a 3D list with shape [2][3][4].
• Use three levels of index access: scores[g][s][st].
• Calculate averages using a while loop — no built-in sum() or avg().
• Track highest score and its location using variables.
• Count failing students using a counter variable inside nested while loops.

Expected Output:

========================================
EXAM SCORE REPORT
========================================
Grade: Grade 10
Math | Scores: 72 85 61 90 | Average: 77.0
Science | Scores: 55 48 79 83 | Average: 66.3
English | Scores: 88 91 74 65 | Average: 79.5
Grade: Grade 11
Math | Scores: 95 88 77 69 | Average: 82.3
Science | Scores: 60 72 85 91 | Average: 77.0
English | Scores: 45 78 83 90 | Average: 74.0
Highest score: 95
Grade: Grade 11 | Subject: Math | Student 1
Failing students (below 50): 2


'''

grade_names = ["Grade 10", "Grade 11"]
subject_names = ["Math", "Science", "Englsih"]

scores = [
    [
        [72, 85, 61, 90 ],  #Math
        [55, 48, 79, 83],  #Science
        [88, 91, 74, 65]   #English
     ],
     [
        [95, 88, 77, 69],  #Math
        [60, 72, 85, 91],  #Science
        [45, 78, 83, 90]
     ]

]

print("========================================")
print("EXAM SCORE REPORT")
print("========================================")

highest_score = scores[0][0][0]
highest_grade = " "
highest_subject = " "
highest_student = 0

failing_students = 0


g = 0
while g < len(scores):
    print("Grade: ", grade_names[g])

    s = 0
    while s < len(scores[g]):
        total = 0
        score_text = " "
        
        st = 0
        while st < len(scores[g][s]):
            score = scores[g][s][st]

            score_text += str(score) + " "
            total += score

            #track highest score
            if score > highest_score:
                highest_score = score
                highest_grade = grade_names[g]
                highest_subject = subject_names[s]
                highest_student = st + 1
            #count failing students
            if score < 50:
                failing_students += 1
            st += 1
        
        average =round(total / len(scores[g][s]), 1)
        print(f"{subject_names[s]} | Scores: {score_text} | Average: {average}")

        s += 1
    g += 1
print(f"Highest score: {highest_score}")
print(f"Grade: {highest_grade} | Subject: {highest_subject} | Student: {highest_student}" )
print(f"Failing students (below 50): {failing_students}")


