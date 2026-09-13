#Dictionaries
#dictonary maps a key to a value

student = {
    "name":   "Aiko",
    "age":    22,
    "grade":  "A",
    "passed": True
}
print(student)
print(len(student))  # 4 key-value pairs

'''
ordered - 3.7+
changeable - yes
dup key - no

syntax - {key:value}

'''
#*Get values by key — two ways (one is much safer!)

student = {"name": "Aiko", "age": 22}

# Method 1: [ ] — crashes with KeyError if key missing
print(student["name"])           # "Aiko"

# Method 2: .get() — returns None or default if missing ✓
print(student.get("score", "N/A"))  # "N/A" — no crash!

# Get all keys, values, or pairs
student.keys()    # dict_keys(["name", "age"])
student.values()  # dict_values(["Aiko", 22])
student.items()   # dict_items([("name","Aiko"),("age",22)])


#Adding & Changing Items
#Same syntax for both adding a new key and updating an existing one
student = {"name": "Aiko", "age": 22}

student["grade"] = "A"    # ADD new key
student["age"]   = 23    # UPDATE existing key

# update() — add or change multiple pairs at once
student.update({"city": "Tokyo", "grade": "A+"})


#Removing Items
#Four ways to delete entries
student = {"name": "Aiko", "age": 22, "grade": "A"}

removed = student.pop("grade")  # remove key, return value → "A"
del student["age"]               # delete by key
student.popitem()                 # remove last inserted pair
student.clear()                   # wipe everything → {}


#*· Looping Through a Dictionary
#Loop over keys, values, or both at the same time
student = {"name": "Aiko", "age": 22, "grade": "A"}

for key in student:               # loop over keys
    print(key)                    # name, age, grade

for value in student.values():    # loop over values
    print(value)                  # Aiko, 22, A

for key, value in student.items():  # ← MOST USEFUL!
    print(f"{key}: {value}")


#Nested Dictionaries
#Dicts can contain other dicts — perfect for real-world data
#Almost all real data is nested. A school has students. Each student has details. A dict inside a dict handles this perfectly.

school = {
    "s1": {"name": "Alice", "grade": "A"},
    "s2": {"name": "Bob",   "grade": "B"},
}
# Access nested values with chained keys
print(school["s1"]["name"])   # "Alice"

# Loop through all students
for sid, info in school.items():
    print(f"{info['name']} got {info['grade']}")

'''
*Method	What it does
.get(key, def)	Get value — returns def if key missing (no crash)
.keys()	Return all keys as a view
.values()	Return all values as a view
.items()	Return all (key, value) pairs
.update(d2)	Add/update from another dict
.pop(key)	Remove key and return its value
.popitem()	Remove and return last inserted pair
.setdefault(k,v)	Get value; insert k:v if key missing
.clear()	Remove all items
.copy()	Return a shallow copy
dict.fromkeys(ks)	Create dict from a list of keys
'''