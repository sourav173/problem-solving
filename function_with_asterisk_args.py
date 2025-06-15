'''
problem: while a function that takes variables number of arguments and return their sum
'''

def sum_all(*args):
    print(*args)
    # print(args) #return tuple
    for i in args:
        print("Multiplication",i *2)
    return sum(args)

print(sum_all(1,2,4,5))
# print(sum_all(1,2,4,5,6,7,8))
# print(sum_all(1,2,4,5,8,8,6,6))