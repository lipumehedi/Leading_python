#1D list + while loop problem solve

cart = []

i = 0
while i < 5:
    price = float(input(f"Enter price of item{i+1}: "))
    cart.append(price)
    i +=1


c = 0
total = 0
while c<len(cart):
     print(f"item{c+1}: {cart[c]:.2f}")
     total = total+cart[c]
     c +=1

print(f"Total Bill: {total} yen.")
