#2D list + while loop

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






#Nested List(2D Lists)
#    A nested list is a list where each element is itself a list- commonly used to represent matrices, grids, or tables. Access uses double indexing: matrix[row][col].

#* Define a 3*3 matrix(3by3)
matrix  = [
        [1,2,3],  #row 0
        [4,5,6],  #row 1
        [7,8,9]   #row 2
]
'''
example
      meat = ["Chicken", "Mutton", "Buffalo"],
      dairy = ["Milk", "Butter", "Yogurt"],
      masala = ["Tandoori", "BBQ", "Garam" ]

groceries = [ ["Chicken",  "Mutton", "Buffalo"],
              ["Milk" ["abc","def"],     "Butter", "Yogurt"],
              ["Tandoori", "BBQ",    "Garam" ]]
print(groceries[0][0])
print(groceries[0][1])
print(groceries[0][2])
print(groceries[1][0])
print(groceries[1][1])
print(groceries[1][2])
print(groceries[1][0][1]) def
print(groceries[1][1 ]) butter


groceries = [ ["Chicken",  "Mutton", ["abc" ,"def"]]
              ["Milk",     "Butter", "Yogurt"]
              ["Tandoori", "BBQ",    "Garam" ]
]

print(groceries[0][2][0])


groceries = [ ["Chicken",  "Mutton", "Buffalo"]
              ["Milk",     "Butter", "Yogurt"]
              ["Tandoori", "BBQ",    "Garam" ]
]

print(groceries[1]) #full index output

groceries[1][0]= "lassi"

print(groceries[1])  #element replace



sum 
   addition = [1,5,6,9]
   result = sum(addition)
   print(result)
'''