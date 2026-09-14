'''
2. Hospital Waiting Queue
Problem Statement:
• Start with a pre-defined patient queue: ['Rin', 'Sam', 'Yuki'].
• Add a new patient 'Leo' to the back of the queue.
• Call the first patient (remove from front) and print their name.
• Print the remaining queue and its length.

Acceptance Criteria:
• Use append() to add Leo.
• Use pop(0) to call and remove the first patient.
• Store the removed name and print it in a sentence.
• Print updated list and use len() for count.

Expected Output:
Now calling: Rin
Remaining queue: ['Sam', 'Yuki', 'Leo']
Patients waiting: 3
'''
patient_queue = ['Rin', 'Sam', 'Yuki']

patient_queue.append('Leo')

Call_patient = patient_queue.pop(0)


print("Now calling:", Call_patient)
print("Remaining queue:", patient_queue)
print("Patienrs waiting:", len(patient_queue))
