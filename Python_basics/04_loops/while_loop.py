'''
What is a Loop?   
 A loop is a control-flow structure that repeats a block of code either a fixed number of times or until some condition is met.Instead of writing repetitive instructions by hand, loops let you express iteration concisely and efficiently.

python provides two fundamental loop constructs:

while loop- Condition controlled
for loop- collection-controlled

#both loops support special clauses(break, continue, pass, else) and compose with python's rich ecosystem of iterables, generators and the itertools module.


THe while Loop
A while loop repeatedly executes its body as long as a given condition evaluates to True. It is condition-controlled- you use it when you don't know in advance how many iterations are needed.




          while condition:
    # loop body - executed while condition is truthy
    statement(s)
  

count = 5
while count > 0:
      print(f"T-minus {count}")
      count -= 1
print("Liftoff! *")


count = 0
count = count+1 --1
count = count+1   --2
count = count+1   --3
count +=1


infinite loops & break
 Sometimes an infinite loop(while True)is the cleanest pattern- pair it with break to exit when needed. cannot use infinite loops always.

 #classic interactive input loop
while True:
          user_input = input("Enter a number (or 'q' to quit):")
          if user_input = "q":
              print("Goodbye")
               break
           print(f"You entered: {int(user_input)}"
 
example:

count = 0
while count<3:
          user_pin = int(input("Enter pin:"))
          if user_pin==1234:
                print("Login Successful")
                break
           else:
               count +=1
                if count>2:
                    print("Try again is 24 hours")

#Simple account login system with while loop and lock after 3 failed attempts

correct_username = "admin"
correct_password = "1234"

attemts = 0
max_attempts = 3

while attemps < max_attempts:
   username = input("Enter username: ")
   password = input("Enter password: ")
   
   if username == correct_username and password == correct_password:
         print("Login successful!")
         break
    else:
         attemts +=1
         remaining = max_attempts - attempts
         print("Incorrect username or password.")
         if remaining >0:
            print(f"Attempts remaining: {remaing}")
#Lock account after 3 failed attempts

if attempts == max_attempts:
   print(f"Account locked due to too many failed login attempts.") 

+1--> increment
-1-->decrement   
'''