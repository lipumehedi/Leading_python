'''
9. Train Schedule & Seat Availability (2D List)
Concepts: 2D Lists · While Loop · Conditionals · Data Types

Problem Statement:
• A railway system manages 4 trains, each with 5 seat classes.
• Each seat class stores the number of available seats.
• Store all data in a 2D list: [train][seat_class].
• Train names: ['Nozomi', 'Hikari', 'Kodama', 'Sakura']
• Seat classes: ['Green', 'Reserved', 'Unreserved', 'Standing', 'Disabled']
• Print the full availability table for all trains.
• Use a while loop to let a user search by train index (0-3); enter -1 to stop.
• For the searched train, print each seat class and mark as 'Available' if seats > 0, else 'Full'.

Acceptance Criteria:
• Define a 2D list with 4 rows (trains) and 5 columns (seat classes).
• Store train names and class names in separate lists.
• Use index access seats[train][class] for all lookups.
• Use while True with break when input == -1.
• Use if/else for Available/Full status.

Expected Output:
========================================
TRAIN SEAT AVAILABILITY
========================================
Train | Green | Reserved | Unreserved | Standing | Disabled
--------------------------------------------------------------------
Nozomi | 12 | 45 | 0 | 0 | 3
Hikari | 0 | 10 | 22 | 15 | 2
Kodama | 5 | 0 | 30 | 40 | 0
Sakura | 8 | 20 | 18 | 0 | 5
Enter train number to check (0-3, or -1 to exit): 1
--- Hikari Seat Status ---
Green Car : Full
Reserved : Available (10 seats)
Unreserved : Available (22 seats)
Standing : Available (15 seats)
Disabled : Available (2 seats)
Enter train number to check (0-3, or -1 to exit): -1
Goodbye!
'''

trains = ['Nozomi', 'Hikari', 'Kodama', 'Sakura']
seat_classes = ['Green', 'Reserved', 'Unreserved', 'Standing', 'Disabled']

seats = [
      [12, 45,  0,  0,  3], #Nozomi
      [0,  10,  22,  15, 2],  #Hikari
      [ 5,  0,  30, 40,  0],  #Kodama
      [8,  20,  18, 0,  5]   #Sakura
]

print("========================================")
print("TRAIN SEAT AVAILABILITY")
print("========================================")
print("Train | Green | Reserved | Unreserved | Standing | Disabled")
print("--------------------------------------------------------------------")

i = 0

while i < len(trains):
    print(f"{trains[i]} | {seats[i][0]} | {seats[i][1]} | {seats[i][2]} | {seats[i][3]} | {seats[i][4]}")
    i += 1

while True:
    train_i = int(input("Enter train number to check (0-3, or -1 to exit): "))

    if train_i == -1:
        print("Goodbye")
        break
    if train_i >= 0 and train_i < len(trains):
        print("---", trains[train_i], "Seat Status ---")

        c = 0
        while c < len(seat_classes):

            if seats[train_index][c] > 0:
                print(f"{seat_classes[c]} : Available ({seats[train_index][c]} seats)")
            
            else:
                print(f"{seat_classes[c]} : Full")
            c += 1
  