'''
problem: calculate the count sum of even numbers up to a given number n.
'''

n = int(input('enter number:'))

sum_even = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum_even += 1
print("Sum of even number: ",sum_even)