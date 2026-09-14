'''
Water bill calculator
Write water_bill(units_consumed, rate_per_unit). The function should print a bill showing units consumed, rate, and total payable.

'''

def water_bill(unit_consumed, rate_per_unit):
    bill = (unit_consumed*rate_per_unit)
    print(f"Units Used : {unit_consumed}")
    print(f"Rate : ¥{rate_per_unit}/unit")
    print(f"Total Bill: ¥{bill}")
    

water_bill(120, 5)
print("──────────────────")
water_bill(300, 5)


