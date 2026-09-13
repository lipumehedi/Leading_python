#lambda functions

#A lambda is an anonymous, single-expression function. It's useful when you need a small function briefly — commonly passed as an argument to map(), filter(), or sorted().

#form
def square(x): return x ** 2

square_lambda = lambda x: x ** 2

'''

map() — Transform Every Element
map(function, iterable) applies a function to each element and returns a new iterator of results. Think of it as a conveyor belt: every item passes through the same operation.
'''

# General form
result = list(map(function, iterable))

# With a named function
def square(x): return x ** 2
list(map(square, [1, 2, 3, 4]))   # [1, 4, 9, 16]

# Same thing with lambda (no need to name the function)
list(map(lambda x: x ** 2, [1, 2, 3, 4]))   # [1, 4, 9, 16]


prices = [1200, 3500, 850, 4999, 620]

# Apply 20% discount to every price
discounted = list(map(lambda p: round(p * 0.80, 2), prices))

print("Original :", prices)
print("After 20% off:", discounted)
# Original :      [1200, 3500, 850, 4999, 620]
# After 20% off:  [960.0, 2800.0, 680.0, 3999.2, 496.0]

# map() over two iterables simultaneously
quantities = [2, 1, 5, 1, 3]
line_totals = list(map(lambda p, q: p * q, discounted, quantities))
print("Line totals:", line_totals)
# Line totals: [1920.0, 2800.0, 3400.0, 3999.2, 1488.0]

'''

filter() — Keep Only What Passes the Test

filter(function, iterable) passes each element through a test function. If the function returns True, the element is kept; if False, it is discarded. The result is a filtered iterator.
'''

nums = [1,2,3,4,5,6]
result = filter(lambda x: x%2 == 0, nums)
print(list(result))

output : [2, 4, 6]

'''
Job Portal: Filter Eligible Candidates
A recruitment platform filters applicants who meet minimum experience and age requirements before forwarding to the hiring manager.
'''
'''
sorted() — Order by Any Criterion
sorted(iterable, key=None, reverse=False) returns a new sorted list without modifying the original. The key parameter accepts any function — and lambda is the natural fit for extracting a sort field on the fly.
'''

Syntax
sorted_syntax.py
Python

# Basic — sorts numbers/strings by default ordering
sorted([3, 1, 4, 1, 5])            # [1, 1, 3, 4, 5]
sorted([3, 1, 4], reverse=True)   # [4, 3, 1]

# key= accepts any function
words = ["banana", "fig", "apple", "kiwi"]
sorted(words, key=len)            # ['fig', 'kiwi', 'apple', 'banana']

# lambda as key — sort strings by last character
sorted(words, key=lambda w: w[-1])
# ['banana', 'apple', 'fig', 'kiwi']

# sorted() never modifies the original — .sort() does (in-place, lists only)
original = [3, 1, 2]
new_list = sorted(original)   # original is still [3, 1, 2]

filter_candidates.py
Python
candidates = [
    {"name": "Alice",  "age": 28, "experience": 4},
    {"name": "Bob",    "age": 21, "experience": 1},
    {"name": "Carol",  "age": 35, "experience": 8},
    {"name": "Dave",   "age": 19, "experience": 0},
    {"name": "Eve",    "age": 30, "experience": 3},
]

# Eligible: age >= 23 AND at least 3 years experience
eligible = list(filter(
    lambda c: c["age"] >= 23 and c["experience"] >= 3,
    candidates
))

print("Shortlisted candidates:")
for c in eligible:
    print(f"  {c['name']} | Age: {c['age']} | Exp: {c['experience']} yrs")
# Alice | Age: 28 | Exp: 4 yrs
# Carol | Age: 35 | Exp: 8 yrs
# Eve   | Age: 30 | Exp: 3 yrs