
#List comprehension

squares =[]   #traditional way

for x in range(5):
     squares.append(x**2)

#list comprehension way

squares = [
    x**2 for  x in range(5)
]
 #[0, 1, 4, 9, 16]

#Anatomy of the syntax
  # [ expression for item in iterable if condition (optional)]
 
#conditional inside comprehensions

nums = [1, 2, 3, 4, 5, 6 ]
evens =[x for x in nums if x%2==0]
print(evens)
