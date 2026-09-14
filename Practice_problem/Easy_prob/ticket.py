queue =[]

while True:
    name = input("")
    if name.lower() == "start":
        break
    queue.append(name)
i = 0
while i< len(queue):
    print("Serving:", person, "Remaining: ", len(queue))