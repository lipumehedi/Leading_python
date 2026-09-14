'''
6. Library Book Search System
Concepts: Lists · While Loop · String Methods · Conditionals

Problem Statement:
• A library has a pre-defined list of book titles.
• Use a while loop to let the user search for books repeatedly.
• Each iteration: take a book title as input.
• If the user types 'exit', stop the loop.
• Search by converting both the input and list items to lowercase for comparison.
• Print 'Book found!' or 'Book not available' accordingly.
• Count and print total searches made after the loop ends.

Acceptance Criteria:
• Pre-define a list of at least 5 book titles.
• Use while True with a break on 'exit'.
• Use .lower() on both input and list item for comparison.
• Use a counter variable incremented each search.
• Print total search count after the loop.

Expected Output:
Enter book title (or 'exit' to quit): Python Crash Course
Book found!
Enter book title (or 'exit' to quit): Harry Potter
Book not available.
Enter book title (or 'exit' to quit): exit

Total searches made: 2
'''

books = [
    "Python Crash Course",
    "Clean Code",
    "Machine Learing Basics",
    "Software development ",
    "Data Structures"
]

search_count = 0

while True:
    book_title = input("Enter book title (or 'exit' to quit): ")
     
    if book_title.lower() == "exit":
        break

    search_count += 1
    found = False

    i = 0
    while i< len(books):
        if book_title.lower() == books[i].lower():
            found = True
            break
        i += 1
        
    if found:
        print("Book found!")
    else:
        print("Book not available.")
print(f"Total searches made: {search_count}")

     