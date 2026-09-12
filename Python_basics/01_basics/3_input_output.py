# Python User Input

user_age = input("Please enter your age: ")

print("User's age:", user_age)


'''

Variable-এর Naming Rules

Variable-এর নাম দেওয়ার সময় কিছু নিয়ম মানতে হয়।

✅ Rule 1 — Letter অথবা _ দিয়ে শুরু করতে হবে

সঠিক:
name = "Mehedi"
_count = 10
user_age = 30

ভুল:
1name = "Mehedi"
কারণ variable-এর নাম number দিয়ে শুরু করা যায় না।

✅ Rule 2 — Space ব্যবহার করা যাবে না

ভুল:
first name = "Mehedi"
সঠিক:
first_name = "Mehedi"
এখানে আমরা snake_case ব্যবহার করেছি।

✅ Rule 3 — Case Sensitive

Python-এ capital এবং small letter আলাদা।
Name = "Mehedi"
name = "Hasan"

এগুলো দুইটি আলাদা variable।
print(Name)
print(name)

Output:
Mehedi
Hasan

✅ Rule 4 — Snake Case ব্যবহার করা ভালো

একাধিক word থাকলে underscore _ ব্যবহার করা হয়।
first_name = "Mehedi"
last_name = "Lipu"
user_age = 30
total_score = 95
phone_number = "123456"

এটাকে বলা হয়:
snake_case

Python programming-এ এটা খুব common এবং readable।

❌ Rule 5 — Reserved Keyword ব্যবহার করা যাবে না

Python-এর কিছু শব্দের নিজস্ব special meaning আছে।

যেমন:
if
for
while
True
False
None
এগুলো variable name হিসেবে ব্যবহার করা উচিত/যায় না।

ভুল:
if = 10
5. input() Function

এখন তোমার code-এর সবচেয়ে গুরুত্বপূর্ণ অংশ।

user_age = input("Please enter your age: ")

input() ব্যবহার করে আমরা user-এর কাছ থেকে information নিই।

যেমন:
user_age = input("Please enter your age: ")
print("User's age:", user_age)

তুমি যদি input দাও:30

তাহলে output হবে:
User's age: 30

⚠️ গুরুত্বপূর্ণ: input() সবসময় String দেয়
এটা beginner হিসেবে খুব ভালোভাবে মনে রাখবে।

age = input("Enter your age: ")
তুমি 30 লিখলেও Python এটাকে initially:"30" হিসেবে নেয়।

অর্থাৎ:
age = input(...)
এর result সাধারণত str

6. int() দিয়ে String → Integer

যদি user-এর input দিয়ে mathematical calculation করতে চাও, তাহলে int() ব্যবহার করতে হবে।

তোমার code:

first_number = int(input("Please enter your first number: "))

এখানে আসলে দুইটা কাজ হচ্ছে:

Step 1:
input(...)

User-এর কাছ থেকে input নেয়।

Step 2:
int(...)

সেই input-কে integer-এ convert করে।

অর্থাৎ:

User input "10"
       ↓
    input()
       ↓
     "10"
       ↓
     int()
       ↓
      10

এখন 10 একটি int।
'''