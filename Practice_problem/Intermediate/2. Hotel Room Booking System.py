'''
2. Hotel Room Booking System
Concepts: 2D Lists · While Loop · String Methods · Conditionals

Problem Statement:
• A hotel manages 5 rooms, each with 3 fields: [room_type, price_per_night, is_available].
• Pre-fill the 2D list with data for 5 rooms.
• Room types: Standard, Deluxe, Suite, Family, Executive.
• Use a while loop to display all rooms and their availability status.

• Allow the user to book a room by entering a room number (1-5); enter 0 to exit.
• If the room is already booked (is_available == 0), print 'Room not available'.
• If available, set is_available to 0 and print booking confirmation with total cost for 3 nights.
• After exiting, print total rooms booked and total revenue collected.

Acceptance Criteria:
• Define a 2D list with 5 rows, each as [room_type, price, is_available].
• Use index access rooms[i][0], rooms[i][1], rooms[i][2].
• Use a while loop with index to print the room table.
• Use while True with break when input is 0.
• Update rooms[i][2] = 0 after a successful booking.
• Track bookings count and revenue with variables outside the loop.

Expected Output:
========================================
HOTEL ROOM AVAILABILITY
========================================
No. | Type | Price/Night | Status
----------------------------------------
1 | Standard | 5000 | Available
2 | Deluxe | 8000 | Available
3 | Suite | 15000 | Available
4 | Family | 10000 | Available
5 | Executive | 20000 | Available
Enter room number to book (0 to exit): 2
Booking confirmed! Deluxe room for 3 nights.
Total cost: 24000 yen
Enter room number to book (0 to exit): 2
Room not available.
Enter room number to book (0 to exit): 0
Total rooms booked : 1
Total revenue : 24000 yen
'''

rooms = [
    ["Standard", 5000, 1],
    ["Deluxe", 8000, 1],
    ["Suice", 15000, 1],
    ["Family", 10000, 1],
    ["Executive", 20000, 1]
]

booked_rooms = 0
total_revenue = 0

print("========================================")
print("HOTEL ROOM AVAILABILITY")
print("========================================")
print("No.  | Type  | Price/Night  |  Status")
print("----------------------------------------")

i = 0
while i < len(rooms):
    if rooms[i][2] == 1:
        status = "Available"
    else:
        status = "Booked"
    print(f"{i+1} | {rooms[i][0]} | {rooms[i][1]} | {status}")
    i +=1
while True:
    room_no = int(input("Enter room number to book (0 to exit): "))
    if room_no == 0:
        break
    if room_no > 0 and room_no <= 5:
        r = room_no - 1
        if rooms[r][2] == 0:
            print("Room not available.")
        else:
            rooms[r][2] = 0
            total_cost = rooms[r][1]*3

            booked_rooms = booked_rooms + 1
            total_revenue = total_revenue + total_cost

            print(f"Booking confirmed! {rooms[r][0]} room for 3 nights.")
            print(f"Total cost: { total_cost} yen ")
print(f"Total rooms booked : {booked_rooms}")
print(f"Total revenue : {total_revenue}")
  
        

    

