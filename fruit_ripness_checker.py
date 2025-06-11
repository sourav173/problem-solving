'''
Problem: determine if a fruit is ripe, overripe, or unripe based on its color.(eg-banana:green-unripe, yellow -ripe, brown - overripe)
'''

fruit = input('enter fruit name:').lower()
fruit_color = input("enter fruit color:").lower()

if fruit == 'banana':
    if fruit_color == 'green':
        print("unripe")
    elif fruit_color == 'yellow':
        print('ripe')
    elif fruit_color == 'brown':
        print('overripe')
else:
    print('fruit is not banana')