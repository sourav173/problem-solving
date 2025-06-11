'''
Problem: choose a mode of transportation based on the distance (eg - <3km walk, 3-15km bike, >15km car
'''


distance = int(input('enter distance in km:'))

if distance > 15:
    print('use car')
elif distance >= 3:
    print('use bike')
elif distance < 3:
    print('use leg')