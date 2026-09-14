def supermarket_bill(customer_name, *items, discount=0, **extras):
    subtotal = 0
    for item in items:
        name = item[0]
        price = item[1]
        subtotal += price
    discount_amount = subtotal * (discount / 100)
    loyalty_points = extras.get("loyalty_points", 0)
    if extras.get("gift_wrap", False):
        gift_wrap = 50
    else:
        gift_wrap = 0
    total = subtotal - discount_amount - loyalty_points + gift_wrap
    return subtotal, discount_amount, loyalty_points, gift_wrap, total
subtotal, disc, loyalty, gift, total = supermarket_bill(
    "Meena",
    ("Milk 1L", 65),
    ("Bread", 45),
    ("Eggs 12pk", 90),
    discount=10,
    loyalty_points=20,
    gift_wrap=True
)
print("Customer : Meena")
print("── Items ──")
print("  Milk 1L ¥65")
print("  Bread ¥45")
print("  Eggs 12pk ¥90")
print(f"Subtotal : ¥{subtotal}")
print(f"Discount (10%): -¥{int(disc)}")
print(f"Loyalty pts {loyalty}: -¥{loyalty}")
print(f"Gift wrap : +¥{gift}")
print("──────────────────")
print(f"You pay: ¥{int(total)}")

