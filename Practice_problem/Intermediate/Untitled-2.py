subjects = ["Math", "Science", "English"]
grade = []

i = 0
while i<3:
    grade.append([])
    j = 0
    while j<len(subjects):
        score = int(input(f"Enter Score for Student{i+1},{subjects[j]}:"))
        grade[i].append(score)
        j+=1
    i+=1

i = 0
while i < 3:

    j = 0
    total = 0
    while j<len(subjects):
        print(f"students{i+1} - {subjects[j]: {grade[i][j]}}")
        total = total + grade[i][j]
        j+=1
    average =total/3
    print(f"Students{i+1} Average: {average}")  
    i+=1
