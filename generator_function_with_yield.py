'''
problem: write a generator function yields even numbers up to a specified limit.
'''

#using yield
def even_generator(limit):
    for i in range(2, limit + 1, 2):
        # print(i)
        # return i
        yield i



for num in even_generator(10):
    print(num)


def even_generator(limit):
    li = []
    for i in range(2, limit + 1, 2):
        li.append(i)
    return li

for num in even_generator(10):
    print(num)


    # def fun(m):
    #     for i in range(m):
    #         yield i
    #



    # call the generator function
    # for n in fun(5):
    #     print(n)