'''
problem:check if a number is prime
'''

number = 28
is_prime = True

if number > 1:
    for num in range(2, number):
        if( number % num) == 0:
            is_prime = False
            break
print(number,"is prime")