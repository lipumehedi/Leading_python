'''

Python sets

keeps only unique items- duplicates vanish automatically

ordered - no
changeable - yes
 duplicate - no
syntax -  {}


# Duplicates removed automatically!
tags = {"python", "coding", "python", "tutorial", "coding"}
print(tags)  # {'python', 'coding', 'tutorial'} — 3 unique items


# Convert a list → set to deduplicate instantly
votes = ["Alice", "Bob", "Alice", "Carol", "Bob"]
unique = set(votes)
print(unique)  # {'Alice', 'Bob', 'Carol'}


Adding & Removing Items
Modify a set — but you can't access items by index
Sets are unordered, so there's no "first" or "second" item. You can't do my_set[0]. But you can add/remove by value.

fruits = {"apple", "banana"}

fruits.add("cherry")       # add one item
fruits.update(["mango", "grape"])  # add multiple

fruits.remove("banana")    # error if missing!
fruits.discard("pineapple") # safe — no error if missing ✓

# Membership check — blazing fast even with millions of items!
if "apple" in fruits:
    print("Found it!")


Set Operations — The Superpower
Sets can do Venn diagram maths: union, intersection, difference
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

A | B   # Union — ALL unique items from both   → {1,2,3,4,5,6,7,8}
A & B   # Intersection — ONLY in BOTH          → {4, 5}
A - B   # Difference — in A but NOT in B       → {1, 2, 3}
A ^ B   # Symmetric diff — in one but not both → {1,2,3,6,7,8}


Reference · Key Set Methods
Method	What it does
.add(x)	Add one item
.update(iter)	Add multiple items from a list, set, etc.
.remove(x)	Remove x — raises error if missing
.discard(x)	Remove x — no error if missing (safer!)
.union(s)	All items from both sets (same as |)
.intersection(s)	Only common items (same as &)
.difference(s)	Items in this set but not in s (same as -)
.issubset(s)	True if all items here are also in s
.issuperset(s)	True if this set contains all of s
.isdisjoint(s)	True if the two sets share no items
.clear()	Remove all items
'''