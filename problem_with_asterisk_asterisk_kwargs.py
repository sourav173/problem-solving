'''
problem: create a function that accepts any number of keyword arguments and prints them in the format key:value
'''
#
# def print_kwargs(name,power):
#     print("Name ",name, " power: ", power)
#
# print_kwargs(power="captain", name="jack" )
# print_kwargs(name="shaktiman")
# print_kwargs(power="captain", name="jack", enemy="davy jones" )

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

print_kwargs(power="captain", name="jack" )
print_kwargs(name="shaktiman")
print_kwargs(power="captain", name="jack", enemy="davy jones" )