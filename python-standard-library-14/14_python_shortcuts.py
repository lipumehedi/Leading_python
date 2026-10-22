#One-line if. value_if_true if condition else value_if_false:

age = 20
label = "adult" if age >= 18 else "child"
print(label)     


#or for defaults. a or b gives a, unless a is empty or None; then it gives b:

when = None
print(when or "today")   

#continue in a loop. Skip the rest of this round and go to the next item:


for n in [1, 2, 3, 4]:
    if n % 2 == 0:
        continue     
    print(n)

