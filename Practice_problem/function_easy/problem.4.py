'''
Gym Attendance Tracker
Write gym_attendance(*members). It should print the total number of members who showed up today, list each member's name, and print whether the class is "Full" (≥ 10 members) or "Available".

'''
def gym_attendance(*members):
    print("Today's Attendance:", len(members))
    print("Members:", ", ".join(members))

    if len(members) >= 10:
        print("Status: Full")
    else:
        print("Status: Available")

gym_attendance("Riya", "Arjun",
  "Priya", "Karan")
print("──────────────────────────────")
gym_attendance("A","B","C","D",
  "E","F","G","H","I","J","K")