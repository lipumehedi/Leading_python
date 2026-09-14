'''
7. To-Do App — Task Manager

Problem Statement:
• Start with tasks = ['Buy groceries', 'Call doctor', 'Pay bills'].
• Insert an urgent task 'Submit report' at the top of the list.
• Remove 'Call doctor' as it is completed.
• Print all remaining tasks converted to uppercase.
• If list has more than 2 tasks, print 'Busy day ahead!'; otherwise print 'Light day!'.

Acceptance Criteria:
• Use insert(0, ...) to add to the top.
• Use remove() to delete by value.
• Access each task by index and print with .upper().
• Use len() in if/else for the day summary.

Expected Output:
SUBMIT REPORT
BUY GROCERIES
PAY BILLS
Busy day ahead!
'''

tasks = ["Buy groceries", "Call doctor", "Pay bills"]
tasks.insert(0, "Submit report")
tasks.remove("Call doctor")

print(tasks[0].upper())
print(tasks[1].upper())
print(tasks[2].upper())

if len(tasks) >2:
    print("Busy day ahead!")
else:
    print("Light day!")