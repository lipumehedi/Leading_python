'''
Electricity bill - slab system

Write electricity_bill(units) that returns the bill amount using India's slab system: 0–100 units @ ¥3/unit; 101–300 @ ¥5/unit; above 300 @ ¥7/unit. The returned value should be used to print the final bill separately — do not print inside the function.

'''
def electricity_bill(units):
    if units <= 100:
        return units * 3
    elif units <= 300:
        return 300 + (100 * 5)
    else:
        return 300 + 1000 + (150 * 7)

bill = electricity_bill(80)
print(f"Bill: ¥{bill}")

bill = electricity_bill(200)
print(f"Bill: ¥{bill}")

bill = electricity_bill(450)
print(f"Bill: ¥{bill}")   