'''
problem: print the multiplication table for a given number up to 10, but skip the fifth iteration
'''


number = 3

for i in range(1, 11):
    if i == 5:
        continue
    for j in range(1, 11):
        print(i, '*', j, '=', i * j)
