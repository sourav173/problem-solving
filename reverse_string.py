'''
reverse a string using a loop
'''

input_str = "Python"

reversed_string = ""

for char in input_str:
    reversed_string = char + reversed_string
print(reversed_string)