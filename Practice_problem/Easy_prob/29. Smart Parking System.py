'''
29. Smart Parking System

Problem Statement:
• Take vehicle type (bike / car / truck) and parking hours.
• Calculate total parking fee based on vehicle type and duration.
• Print total fee.

Acceptance Criteria:
• bike → 100 yen/hour
• car → 300 yen/hour
• truck → 500 yen/hour
• Other → Invalid vehicle type

Expected Output:
Enter vehicle type: car
Enter parking hours: 5
Total fee: 1500 yen

'''
vehicle = input("Enter vehicle type (bike / car / truck): ")
hours = int(input("Enter parking hours: "))

if vehicle == "bike":
    print("Total fee: ", 100*hours, "yen.")
elif vehicle == "car":
    print("Total fee: ", 300*hours, "yen.")
elif vehicle == "truck":
    print("Total fee: ", 500*hours, "yen.")
else:
    print("Invalid vehical type")
