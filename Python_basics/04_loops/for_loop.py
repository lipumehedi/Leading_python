#For loop

#-> Iterating over a known sequence/collection.
#-> Usually known in advance (length of sequence).
#-> Low (bounded by sequence length)
#-> for i in range(5):

#Basic Syntax
for variable in sequence:
    # block of code (loop body)
    statement(s)

#Range() function

#range(5) -> 0,1,2,3,4 -> 0 to stop-1
#range(2, 6) -> 2,3,4,5 -> start to stop-1
#range(0, 10, 2) -> 0,2,4,6,8 -> start to stop-1, incrementing by step

'''
#*Basic example

for i in range(5)
print(i)
output: 0 1 2 3 4

*negative step

for i in range(10, 0, -1):
    print(i)
Output: 10 9 8 7 6 5 4 3 2 1

* stepping by more than 1
  for i in range(0, 21, 3):
       print(i)

output: 0 3 6 9 12 15 18

*converting range() to a list

numbers = list(range(1, 6))
       print(numbers)
Output: [1, 2, 3, 4, 5]

*Using range() with len() for Index-Based Access

fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(i, "->", fruits[i])

* Looping through a list
 
fruits =["apple", "banana", "cherry"]
for i in fruits:
    print(i)
output: apple banana cherry

* Sum of a list
numbers = [4, 8, 15, 16, 23, 42]
total = 0
for n in numbers:
    total += n
print("Total:", total)
op: Total: 108


* Finding the maximum value manually
numbers = [4, 8, 15, 16, 23, 42]
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
print("Largest:", largest)
Output: Largest: 42

* Counting items that meet a condition

words = ["cat", "elephant", "dog", "butterfly", "ant"]
count = 0
for word in words:
    if len(word) > 3:
        count += 1
print("Words longer than 3 letters:", count)
Output: Words longer than 3 letters: 3

* Building a New List Inside a Loop
numbers = [1, 2, 3, 4, 5]
doubled = []
for n in numbers:
    doubled.append(n * 2)
print(doubled)
Output: [2, 4, 6, 8, 10]

*Looping through a string
for i in "Python":
    print(i)
Output: P y t h o n

*Looping in Reverse with reversed()
nums = [1, 2, 3, 4, 5]
for n in reversed(nums):
    print(n)
Output: 5 4 3 2 1

* Looping in Sorted Order with sorted()
names = ["Carol", "alice", "Bob"]
for name in sorted(names):
    print(name)
output: Bob
        Carol
        alice
*Sort in reverse order
for name in sorted(names, reverse=True):
    print(name)
output: alice
        Carol
        Bob

* The enumerate() function
enumerate(iterable, start=0)

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
Output: 0 apple 1 banana 2 cherry

* starting the count from a Different number
fruits = ["apple", "banana", "cherry"]
for position, fruit in enumerate(fruits, start=1):
    print(f"{position}. {fruit}")
Output: 1. apple 2. banana 3. cherry

* Nested for loops
m*n
for i in range(1, 4):
    for j in range(1, 4):
         print(i, "*", j, "=", i*j)
output: 1 * 1 = 1 1 * 2 = 2 1 * 3 = 3 2 * 1 = 2 2 * 2 = 4 2 * 3 = 6 3 * 1 = 3 3 * 2 = 6 3 * 3 = 9

* printing a star pattern

for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()
Output: *
        * *
        * * *
        * * * *

* Loop control statements

#-> Continue
bnp = ["Abul", "Babul", "Dabul"]
for i in bnp:
     if i == "Abul":
          continue
      print(i)
'''