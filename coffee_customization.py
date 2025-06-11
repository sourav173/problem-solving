'''
problem: customize a coffee order: "small", "medium", or "large" with an option "extra shot" of espresso
'''

order_size = "Medium"
extra_shot = True

if extra_shot:
    coffee = order_size + " coffe with an extra shot"
else:
    coffee = order_size + " coffee"

print("Order: ",coffee)