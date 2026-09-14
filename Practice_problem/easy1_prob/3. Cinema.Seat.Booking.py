'''
3. Cinema Seat Booking
Problem Statement:
• Given seats = [10, 11, 12, 13, 14, 15, 16].
• Print the first and last seat using indexing (no len()).
• Slice 3 seats starting at index 2 and store as booked_seats.
• If booked_seats has exactly 3 seats, print confirmation; otherwise print 'Booking failed'.

Acceptance Criteria:
• Use seats[0] for first seat and seats[-1] for last.
• Use seats[2:5] to extract exactly 3 seats.
• Use len(booked_seats) == 3 inside an if/else.
• Print both the seat numbers and the confirmation message.

Expected Output:
First seat: 10 | Last seat: 16
Booked seats: [12, 13, 14]
Booking confirmed for 3 seats! 
'''
cinema_seats = [10, 11, 12, 13, 14, 15, 16]
first_seat = cinema_seats[0]
last_seat = cinema_seats[-1]
print("First seat:", first_seat, " | Last seat:", last_seat)

booked_seats = cinema_seats[2:5]
print("Booked seats:", booked_seats)

if len(booked_seats) == 3:
    print("Booking confirmed for 3 seats!")
else:
    print("Booking failed.")
