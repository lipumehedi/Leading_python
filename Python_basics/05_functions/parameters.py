'''
Parameters & Arguments
Python offers a rich variety of parameter types, giving functions enormous flexibility.

Positional Parameters
positional.py
Python

def add(a, b):
    return a + b

print(add(3, 5))   # 8



**Default Parameters
defaults.py
Python
def send_email(recipient, subject, cc=None, priority="normal"):
    """Send an email — cc and priority have sensible defaults."""
    print(f"To: {recipient} | Subject: {subject}")
    print(f"CC: {cc} | Priority: {priority}")

send_email("bob@example.com", "Meeting Notes")
send_email("alice@example.com", "Urgent", priority="high")


-> *args (Variable Positional)
args.py
Python
def total_bill(*items):
    #Sum any number of item prices.
    return sum(items)

print(total_bill(12.5, 8.0, 3.75))   # 24.25
print(total_bill(100, 200))            # 300


-> **kwargs (Variable Keyword)
kwargs.py
Python
def create_profile(**details):
    """Build a user profile from keyword arguments."""
    for key, value in details.items():
        print(f"  {key}: {value}")

create_profile(name="Jane", age=28, city="Tokyo", role="Engineer")
# name: Jane   age: 28   city: Tokyo   role: Engineer


Return Values
The return statement exits a function and optionally sends a value back to the caller. Without it, Python returns None implicitly.

return_values.py
Python
# Returning multiple values (as a tuple)
def min_max(numbers):
    """Return the minimum and maximum of a list."""
    return min(numbers), max(numbers)

low, high = min_max([4, 1, 9, 2, 7])
print(f"Min: {low}, Max: {high}")   # Min: 1, Max: 9

# Early return (guard clause pattern)
def divide(a, b):
    if b == 0:
        return None  # early exit
    return a / b

print(divide(10, 2))   # 5.0
print(divide(10, 0))   # None


_-Scope & Namespaces
Every variable lives in a scope — the region of the program where it's visible. Python follows the LEGB rule for resolving names.

Letter	Scope	Example
L	Local — inside the current function	variables defined inside def
E	Enclosing — outer function (closures)	nested functions
G	Global — module-level	x = 10 at top of file
B	Built-in — Python's built-ins	len, print, range
'''