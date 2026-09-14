queue = []

while True:
    action = input("Enter action: ")
    if action == "quit":
        break
    if action == "add":
        name = input("Patient name: ")
        queue.insert(len(queue), name)
        print("Queue: ", queue)
    
    if action == "emergency":
        name = input("Patient name: ")
        queue.insert(0, name)
        print("Queue: ", queue)
    if action == "next":
        patient = queue.pop(0)
        print("Calling: ", patient, "Queue: ", queue)
