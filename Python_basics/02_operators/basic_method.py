#1. Different ways of printing
first_number = int(input("Please enter your first number: "))
second_number = int(input("Please enter your second number: "))

result = first_number + second_number

print("Summation of the given 2 numbers is:", result)
'''
এখানে:
input() → user-এর কাছ থেকে input নেয়।
int() → input-কে string থেকে integer বানায়।
+ → দুইটি number যোগ করে।
print() → result দেখায়।
Example:
Please enter your first number: 10
Please enter your second number: 20

Summation of the given 2 numbers is: 30
'''
# Type Casting
#int("10")
#মানে "10" string-কে 10 integer-এ convert করা।
#Common type casting:
#int()
#float()
#str()
#bool()

#2. String Repetition
x = "sorry " * 1000
print(x)
#* দিয়ে string repeat করা যায়।
print("Hello " * 3)
#Output: Hello Hello Hello

#এখানে "Hello " তিনবার print হবে।

#3. Comment / Multicomment
#Single-line comment
# This is a comment
# দিয়ে comment লিখলে Python সেটা execute করে না।

#Multiline comment / Docstring
'''
This is
multiple line
text
'''
#এটা technically Python-এর multi-line string। সাধারণত documentation-এর জন্য """ ... """ বা ''' ... ''' ব্যবহার করা হয়।

#4. User Input
user_input = input("Please enter your name: ")
print("Your Name:", user_input)
#User যদি লিখে: Lipu
#Output: Your Name: Lipu
'''
  #গুরুত্বপূর্ণ:
input() সবসময় string return করে।
তাই: age = input("Enter age: ") ,এখানে age হবে string।
Number হিসেবে চাইলে: age = int(input("Enter age: "))
'''
#5. String Concatenation

#Concatenation = দুই বা তার বেশি string জোড়া লাগানো।

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = first_name + " " + last_name

print(full_name)


first_name = Lipu
last_name = Mehedi
#তাহলে: Lipu Mehedi
#এখানে: " " একটা space।

#6. String join()
first_name = "Lipu"
last_name = "Mehedi"

print(" ".join([first_name, last_name]))
#Output: Lipu Mehedi
#join() ব্যবহার করে অনেকগুলো string সুন্দরভাবে combine করা যায়।
'''
Example:
words = ["Python", "is", "easy"]
print(" ".join(words))
Output: Python is easy
'''
#7. format()

#তোমার example: full_name = "{} {}".format(last_name, first_name)
#যদি:
first_name = "Lipu"
last_name = "Mehedi"

#তাহলে: Mehedi Lipu ''' {} হলো placeholder।

#তবে modern Python-এ f-string বেশি ব্যবহার করা হয়।
full_name = f"{first_name} {last_name}"
print(full_name) #এটাই বর্তমানে সবচেয়ে সহজ ও readable approach।

#8. String Methods

name = "mahfuz vai is our hero"
capitalize()
print(name.capitalize())
#Output: Mahfuz vai is our hero #শুধু প্রথম character capital করে।

lower()
print(name.lower()) #সব lowercase: mahfuz vai is our hero

upper()
print(name.upper()) #সব uppercase: MAHFUZ VAI IS OUR HERO

title()
print(name.title()) #প্রতিটি word-এর প্রথম letter capital: Mahfuz Vai Is Our Hero

#9. Variable Override

#code:
number = 5
number = 10
number = 15
print(number)

Output: 15

#কারণ একই variable-এ নতুন value দিলে পুরনো value replace হয়ে যায়।
'''
এটাকে সহজভাবে বললে:
number = 5     → number-এর value 5
number = 10    → 5 replace হয়ে 10
number = 15    → 10 replace হয়ে 15

তাই শেষ পর্যন্ত: 15
'''
#10. Comparison Operators

#এগুলো True অথবা False return করে।
Equal
5 == 5
Result: True

#Not equal
5 != 3
Result: True

#Greater than
5 > 3
Result:True

#Less than
5 < 3
Result:False

#Greater than or equal
5 >= 5
Result: True

#Less than or equal
5 <= 4
Result: False

#⭐ খুব গুরুত্বপূর্ণ
'''
= আর == এক জিনিস না।

x = 10
মানে value assign করা।
আর: x == 10
মানে x-এর value 10 কিনা check করা।
'''

#11. String replace()
text = "Hello world, how are you doing?"
new_text = text.replace("world", "Lipu")
print(new_text)
#Output: Hello Lipu, how are you doing?

#replace() কোনো text-এর অংশ পরিবর্তন করে।

#12. strip()
text = "   Hello World   "
print(text.strip())
#Output: Hello World
#দুই পাশের extra space remove করে।

lstrip()
text.lstrip()
#বাম পাশের space remove করে।

rstrip()
text.rstrip()
#ডান পাশের space remove করে।

#13. startswith()
text = "Hello World"
print(text.startswith("Hello"))
Output: True

#মানে string "Hello" দিয়ে শুরু হয়েছে কিনা check করছে।

#14. endswith()
print(text.endswith("World"))

Output: True

#মানে string "World" দিয়ে শেষ হয়েছে কিনা check করছে।

#15. find()
text = "Hello world"

print(text.find("world"))

#এটা "world" কোথা থেকে শুরু হয়েছে সেই index return করবে।

#Python-এ index শুরু হয়: 0 থেকে।

#16. count()
text = "hello hello hello"

print(text.count("hello"))

Output: 3 
#কতবার "hello" আছে সেটা count করে।


#17. isdigit()
text = "12345"

print(text.isdigit())

Output: True
#শুধু digit আছে কিনা check করে।

"123".isdigit()    # True
"abc".isdigit()    # False

#18. isalpha()
"Hello".isalpha()

Output: True

#শুধু alphabet আছে কিনা check করে।

"Hello123".isalpha()

Output: False

#19. isalnum()

#isalpha + numeric দুইটাই allow করে।

"Hello123".isalnum()
Output: True

কিন্তু: "Hello 123".isalnum()

Output: False
#কারণ space আছে।

#20. f-string ⭐

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"You are {name} and your age is: {age}")

#এটা Python-এ খুব গুরুত্বপূর্ণ।

#যদি:
name = Lipu
age = 30
#Output: You are Lipu and your age is: 30
#আমি recommend করব তুমি f-string ভালোভাবে practice করো।

#21. len()
text = "siddikia"
print(len(text))
#len() string-এর কতগুলো character আছে সেটা বলে।

#22. String Index
text = "siddikia"

#Index হবে: s  i  d  d  i  k  i  a | 0  1  2  3  4  5  6  7

#তাই:
print(text[0])
Output: s

আর:print(text[7])
Output: a

#23. Negative Index

#Python-এ পিছন থেকেও index করা যায়।

 #s  i  d  d  i  k  i  a
 #0  1  2  3  4  5  6  7
 #-8 -7 -6 -5 -4 -3 -2 -1

তাই: print(text[-1])

#Output: a -1 = last character 

#24. String Slicing 
text = "siddikia"
print(text[0:5])
Output: siddi

Important: text[start:end]
#এখানে end index include হয় না।

#অর্থাৎ: text[0:5] মানে: 0, 1, 2, 3, 4 শুরু থেকে

print(text[:5])
#মানে: text[0:5] শেষ পর্যন্ত

print(text[2:])
#মানে index 2 থেকে শেষ পর্যন্ত।

#25. type()
text = "siddikia"
print(type(text))

#Output: <class 'str'> # মানে text হচ্ছে string।

#26. None 
#code:
age = None
print(type(age))
#Output: <class 'NoneType'>
#None মানে কোনো value নেই / value এখনো নির্ধারণ করা হয়নি।

#Example:
result = None #মানে এখন result-এর কোনো actual value নেই।
পরে: result = 100 #তখন value দেওয়া হলো।

'''
এই order-এ এগুলো ভালো করে practice করো:
1. print()
2. input()
3. int(), float(), str()
4. Variables
5. String concatenation
6. f-string ⭐
7. String methods
8. Comparison operators
9. len()
10. Indexing
11. Slicing
12. type()
13. None
'''