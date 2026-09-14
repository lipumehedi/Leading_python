'''
Online product listing

'''
def list_product(product_name, price, **specs):
    print(f"{product_name} - ¥{price:,}")

    for key, value in specs.items():
        print(f"{key.title()} : {value}")

list_product("Laptop", 65000,
  brand="Dell", ram="16GB",
  storage="512GB SSD")
print("──────────────────────")
list_product("T-Shirt", 799,
  colour="Navy", size="L",
  material="Cotton")