'''
19. Traffic Signal System

Problem Statement:
• Take traffic signal color.
• Print appropriate action.

Acceptance Criteria:
• green → Go
• yellow → Slow Down
• red → Stop
• Other → Invalid Signal

Expected Output:
Enter signal: green
Go
'''
signal = input("Enter signal: ")

if signal == "green":
    print("Go")
elif signal == "yellow":
    print("Slow Down")
elif signal == "red":
    print("Stop")
else:
    print("Invalid Signal")