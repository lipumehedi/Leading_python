'''
Recursion, File handling


itself call

def countdown(n):
     'if n==0:
         print("Done!")  base case
         return'
     print(n)
     countdown(n-1)

print(countdown(10))



File handling

A beginner's guide to opening, reading, writing and safely closing files - with example built around everybody situation in japan.


Why file handling matters
Opening a file with open()
File modes explained
Reading a file
Writing to a file
Appending to a file
The with statement
File paths
Handling missing files
Working with CSV-style data
Practice exercises


1.Why file handling matters

-> Every program you have written so far loses its data the moment it stops running. Variables disappear, lists, reset, everything is gone. File handling is how a program remembers things after it close.

Think of a konbini cash register.It needs to keep a record of every sale, even after the store closes for the night and the machine is switched off. That record has to live somewhere other than memory. In python, that "somewhere" is usually a file on disk.

2. Opening a file with open()
 new file format txt
 file handling - py

 file = open("dairy.txt", "t")
 content = file.read()
 print(content)
 file.close


3. File modes explained

A string, define which mode you want to open the file in:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exist
 
"r+" - Read and Write. open a file for reading and write, error if the file dose not exist.


In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode



4. Reading a file

#whole file as one string

file = open("lipu.txt", "r")
content = file.read()
print(content)
file.close -> close
 
 -same as close auto
with open("lipu.txt", "r") as file:
    text = file.read()
    print(text)

# one line at a time

with open("lipu.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline()
    print(first_line)
    print(second_line)
    
 
#every line is a list

with open("lipu.txt", "r") as file:
    first_line = file.readlines()
 
    print(first_line)

5. Writing to a file

# write only and erase existing content
#file na thakleo new file create
with open("lipu.txt", "w") as file:
    # \n = new line
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
 
 

#list ke single single line e convert

items = ["Onigiri\n", "Green tea\n", "Umbrella\n"]

with open("shopping_list.txt", "w") as file:
    file.writelines(items)
    

6. Append

#Append
with open("study_log.txt", "a") as file:
    file.write("july 12: Received 20 new JLPt N2 vocabulary words\n")
    file.write("july 30: Received 20 new JLPt N2 vocabulary words\n")


7. File paths

When you write open("notes.txt"), Python looks for that file in the same folder as the script that is currently running. This is called a relative path.


9. Handling missing files

# Handling missing file

try:
    with open("budget.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("That file dose not exist yet.")

10. Working with CSV-style data

A lot real files store one record per line, with values separated by commas. You do not need a special library to read cases like this, just split each line.


total = 0

with open("csv.txt", "r") as file:
    for line in file:
        name, price = line.split(",")
        total += int(price)
print("Total spent: ￥" + str(total))
'''