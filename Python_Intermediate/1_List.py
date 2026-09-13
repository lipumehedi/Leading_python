'''
python Lists


What is a list?
- A list is python's most versatile built-in data structure.it is an ordered, mutable sequence(changeable) that can hold items of any type - integers, strings,  floats, Booleans, objects, even other list - all at once.

 CHARACTERISTICS
   - ordered(insertion order kept)
   - Mutable(can be changed)
   - Allows duplicates
   - Zero indexed
   - Heterogenous types allowed(vinnodormi)

USE CASES
   - Sequences of items
   - Stacks and queues
   - Storing query results
   - Building datasets
   - Matrix rows

INTERNAL MODEL
   - Dynamic array
   - Stores references(pointer)
   - O(1) random access
   - Amortized O(1) append
   - O(n) insert/delete at middle
 


Creating Lists
 
  #Empty list
   empty = [] --> Literal syntax. Faster
   empty = list() --> Constructor syntax. Slower

  #Integer list (literal)
   numbers = [1,2,3,4,5,]
  #Mixed types - valid in python
   mixed = [42, hello, 3.14, True, False, None]
  # From a string - list of characters
    chars = list("Python")   #['P','y','t','h','o','n']
  #From range
   nums =list(range(1,6))    #[1,2,3,4,5]


Accessing Elements
 ** List items are indexed, the first item has index [0], the second item has index [1] etc.
    python also supports negative indexing - counting backwards form the end.


  # index :  0    1     2    3    4    5
  # neg idx: -6   -5   -4   -3    -2   -1


Slicing
 
    Slicing extract a portion of a list and returns a new list. The original is never modified.
    Syntax: list[start : stop : step] - the stop index is always exclusive

     [0,1,2,3,4,5,6,7,8,9]
lst[2:5]   indices 2,3,4                   [2,3,4]
lst[:4]    from start to index 3           [0,1,2,3]
lst[6:]    from index 6 to end             [6,7,8,9]
lst[:]     entire  list(shallow copy)      [0,1,2,3,4,5,6,7,8,9]
lst[::2]   every 2nd element               [0,2,4,6,8]
lst[1::2]  odd-positioned indices          [1,3,5,7,9]
lst[::-1]  full list reversed              [9,8,7,6,5,4,3,2,1,0]
lst[7:2:-1] step-1 from index 7downto 3    [7,6,5,4,3]
lst[-3:]    last 3 element                 [7,8,9]
lst[:-2]    everything except last 2       [0,1,2,3,4,5,6,7]

Slice Assignment
you can assign to a slice to replace, insert, or delete a chunk of the list in one operation.

Modifying Lists
   colors = ["red", "green", "blue"]
  #change a single element
    colors[1] = "yellow"   #['red', 'yellow', 'blue']
 #change multiple element
    colors[0:2] = ["pink", "grey"]  #['pink', 'grey', 'blue']

  #Delete one element by index
    del colors[0]    #['grey', 'blue']
  #Delete a slice
    del colors[0:2]   #[]

Concatenation & Repetition
   a = [1,2]
   b = [3,4]
    = + creates a brand new list
  c = a + b        #[1,2,3,4,] - a & b unchanged

Built-in Methods
append - last e add kora.
'''
#fruits1 = ["Strawberry", "Apple", "melon","mango","orange","kiwi", "lyche"]
#fruits2 = ["guava", "grapes", "Banana"]
#print(fruits[::2])
#print(fruits[:-2])
#guava, grapes, banana
#fruits[1:4] = ["guava", "grapes", "banana"]
#fruits[2] =["guava"]
#del fruits[0:3]
#fruits =fruits1 + fruits2
#print(fruits)
#num = [1,2,3,4,5,1,6,7,8,1,100]
#----Add operation in a list----
#num.append()
#num.append(["foysal", "atiq"])
#num.extend(["foysal",0])
#num.insert(0,"foysal")
#num.insert(3, "Foysal")
#num[2:5] =["foysal", "atiq", "mahir"]
#remove=num.remove(8)
#pop = num.pop(2)
#num.clear()
#print(pop)
#print(num.index(1))
#print(num.count(1))
#fruits2 = ["guava", "grapes", "Banana"]
#fruits2 = ["Strawberry", "apple", "Melon","mamma", "Mango","Orange","Kiwi", "Lyche"]
#fruits2.sort()
#print(fruits2)

#fruits2.sort(reverse =True)
#fruits2.sort(key=len)

#fruits2.reverse()
#print(fruits2)

#fruits1 = ["Strawberry", "Apple", "melon","mango","orange","kiwi", "lyche"]
fruits = ["Strawberry","apple","Melon","Orange","kiwi", "Lychi","Pear"]

print(fruits[6:2:-1]) #*['Pear', 'Lychi', 'Kiwi', 'Orange']