'''
Fast food order system
Write place_order(item, size="Medium", extra_sauce=False). Most customers order Medium and skip extra sauce — the defaults handle that. Print a confirmation with all three values.
'''
def place_order(item, size="Medium", extra_sauce="No"):
    print(f"Order: {item} | Size: {size} | Sauce: {extra_sauce}" )

place_order("Burger")
place_order("Fries", size="Large")
place_order("Wrap", "Small", "Yes")