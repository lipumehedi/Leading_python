words = ["banana", "Kiwi", "apple"]
#sorted returns a new sorted list.
print(sorted(words))
print(sorted(words, key=len))
print(sorted(words, key=lambda w: w[-1]))
#The last line sorts by the last letter (a, e, i). lambda w: w[-1] is a tiny function without a name.
def last_letter(w):
    return w[-1]

#Add reverse=True to sort from biggest to smallest:
totals = {"food": 1849, "rent": 52000, "transport": 230}
print(sorted(totals.items(), key=lambda pair: pair[1], reverse=True))
