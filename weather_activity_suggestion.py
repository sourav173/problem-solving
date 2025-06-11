'''
problem: suggest an activity based on the weather (eg-sunny -go for walk, rainy-read a book, snowy-build a snowman).
'''

weather = input('enter weather:').lower()

if weather == 'sunny':
    print('go for walk')
elif weather == 'rainy':
    print('read a book')
elif weather == 'snowy':
    print('build a snowman')