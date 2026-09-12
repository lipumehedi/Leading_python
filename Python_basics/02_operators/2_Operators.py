#Differing way of printing
'''
first_number =int(input("please enter your first number: "))
second_number =int(input("please enter your second number: "))
result = first_number + second_number
print("sumation of the given 2 numbers is :",result)
 
''' #typecasting


#x = "sorry "*1000
#print(x)
'''
Docstring / multicomment
jojoj
'''
#user_input = input("please enter your name: ")
#print("Your Name:", user_input)

# String concatenation
#first_name = input("Enter your first name: ")
#last_name = input("Enter your last name: ")

#full_name = first_name + " " + last_name
#print("Your full name is:", full_name)
#print("Your full name is:",first_name + " " + last_name )



#print("sorry "*1000) #string repataion

#first_name = "Lipu"
#last_name = "Mehedi"
#full_name =first_name + last_name #normal Approch

#full_name = " ".join([first_name, last_name]) #join approch
#print(" ".join([first_name, last_name]))

#full_name = "{} {}".format(last_name,first_name) #combine approch


#print("{} {}".format(last_name,first_name))


#Normal approch --> Dyamic message
# Join Approch --> URl construction
# combine approch/ format approch--> file path


 # method

#name = "mahfuz vai is our hero"
#print(name.capitalize())
#print(name.capitalize())
#print(name.lower())
#print(name.title())

number = 5
number = 10
number = 15
print(number) #override

#comparison Operators
5 == 5 	# True - Equal to
5 != 3	# True - Not equal
5 > 3	# True Greater than
5 < 3 	#False Less than
5 >= 5	#True Greater than or equal to
5 <= 4 	#False Less than or equal to


text = "Hello world, how are you doing?"

# String operation
# text = "32m"
# new_text = text.replace("world!", "Joy") # Replace a substring
# new_text = text.strip() #Strip white space from both side
# new_text = text.lstrip() # remove heading white space
# new_text = text.rstrip() # remove tailing white space
# new_text = text.startswith("Bello") # check if a string starts with a substring
# new_text = text.endswith("boing?") # check if a string ends with a substring
# new_text = text.find("world") # find the position of a substring
# new_text = text.count("Joy") # count occurance of substring in a string
# new_text = text.istitle() # check if the string is titlecased
# new_text = text.strip().title() # using multiple method in a single line
# new_text = text.isspace() # Check if a string contains only white space
# new_text = text.isdigit() # checks if the string contains only numerics
# new_text = text.isalpha() # checks if the string contains only alpahbetic
# new_text = text.isalnum() # Checks if the string contains either alphabetic or numeric.


# print(new_text)
# name = input("Enter your name:")
# age = int(input("Enter your age: "))   # convert str → int
# print("You are", name, "and your age is: ", age)
# print(f"You are {name} and your age is: {age} ") #f-string

text = "siddikia"
# print(len(text)) # calculate the length of a string
# print(text[0]) # printing a particular index of a string (index counting always strats from 0)
# print(text[-1]) # print the last index of a string
# print (text[0:5]) # String slicing(note: excludes upper limit)
# print(text[:5]) # slicing ( if I want start from index 0, mentioning lower limit is not necessary )
# print(text[2:]) # slicing (If I want to print upto end of a string, then we don't have to mention the upper limit)
# print(type(text)) # checks the data type
age = None
print(type(age))
