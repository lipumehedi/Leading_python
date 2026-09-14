marks = []

while True:
    mark = input(" ")
    if mark == "stop":
        break
    marks.append(int(mark))
total = 0
i =0
while i < len(marks): 
    total += marks[i]
    i += 1

average = total /len(marks)

print("Class average: ", average)