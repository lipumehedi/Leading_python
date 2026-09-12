#Python Control Flow

#Conditional

#Conditional statements in Python are used to execute certain blocks of code based on specific conditions. These statements help control the flow of a program, making it behave differently in different situations.
'''
If Statement: The simplest form. A block of code runs only if the condition is True.
The simplest form. A block of code runs only if the condition is Ture.
 if condition: only true then runs
 
age = 20
if age >= 18:
print ("you are an adult.")



If.Else Statement
  Provides an alternative path when the condition is False
  age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")

age = int(input("Enter your age: "))

if age>= 20:
    print("you are an adult.")
else:
    print("You are a minor")


If-elif-else statement

 if condition1:
     #block 1
 elif condition2:
     #block2
 elif condition3:
     #block3
else:
   #default block

mark = int (input("Enter your marks:"))

 if marks>=80:
    print("A+")
  elif marks>=70:
    print("A")
 elif marks>=60:
    print("A-")
 elif marks>=50:
    print("B")
 elif marks>=40:
    print("C")
 elif marks>=33:
    print("D")
else :
    print("F")


Logical Operators
and - Both conditions must be True
age = 25
has_id = True
if age >= 18 and has_id:
  print("Entry allowed")

mark = int (input("Enter your marks:"))

 if marks>=80 and marks<=100:   ##if marks>=70 and marks<=79:
    print("A+")                    print("A")
  elif marks>=70 and marks<=79:    ##elif marks>=80 and marks<=100:
    print("A")                           print("A+")
 elif marks>=60 and marks<=69:
    print("A-")
 elif marks>=50 and marks<=59:
    print("B")
 elif marks>=40 and marks<=49:
    print("C")
 elif marks>=33 and marks<=39:
    print("D")
else :
    print("F")


or - At least one condition must be True
is_weekend = True
is_holiday = False
if is_weekend or is_holiday:
    print("No work today")


not Reverse the truth value
is_raining = True
if not is_raining:
    print("Let's go outside")
else:
    print("Bashay thako")



-age>=25
-Nationality = "Bangladeshi" NG
-Gender ="Male" or "Female"

=================================

age = int (input("Enter your age: "))
nationality = input("Enter your Nationality: ")
gender = input("Enter your gender: ")

if nationality !=  "Bangladeshi" and age>=25:
        print("OK")
else:
         print("NG")

Nested if statement
Nested if..else means an if-else statement inside another if statement.

CGPA > 3.5
first interview > 80 --> second interview
second interview > 90 --> HR interview
Non smoker --> offter letter
==========================================
cgpa = float (input("Enter candidate CGPA: "))
if cgpa>3.5:
     print("You are selected for first interview")
     score = int (input("Enter candidate's first interview score: "))
      if score>80:
        print("yoe are selected for second interview")
        second_score = int (input("Enter candidate's second interview score: "))
         if second_score>90:
              print("you are selected for the dope tese")
              is_smoker = input("Enter if the candidate is smoker or non smoker")
               if is_smoker =="non smoker":
                   print("Congratulations! you are hired")
                 else:
                       print("You failed the dope test")
          else:
               print("you are not selected dope test")
 
       else:
          print("you are not selected for second interview")
else:
    print("Sorry your CGPA is not adequate enough.")
    
    '''