'''
30. Smart Software Engineer Recruitment System

Problem Statement:
• Take Python skill score, problem solving score, communication skill (good/bad), and
years of experience.
• Check all hiring conditions.
• Print recruitment result.

Acceptance Criteria:
• Python skill score >= 80
• Problem solving score >= 75
• Communication skill == good
• Years of experience >= 2
• All 4 conditions met → Selected for Final HR Round
• Any condition fails → Not Selected

Expected Output:
Enter Python skill score: 85
Enter problem solving score: 80
Enter communication skill (good/bad): good
Enter years of experience: 2
Selected for Final HR Round
'''

python_score = int(input("Enter Python skill score: "))
problem_score = int(input("Enter problem solving score: "))
communication = input("Enter communication skill (good/bad): ")
experience = int(input("Enter years of experience: "))

if python_score >= 80 and problem_score >= 75 and communication == "good" and experience >= 2:
    print("Selected for Final HR Round.")
else:
    print("Not Selected.")