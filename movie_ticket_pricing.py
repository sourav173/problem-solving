'''
problem: movie tickets are priced based on age: $12 for adults (18 or over), $8 for children.
Everyone gets $2 discount on Wednesday.
price = 12 if age >= 18 else 8
'''
from zoneinfo import reset_tzpath

age = int(input("enter your age:"))
day = input("enter the day:")
ticket_price = 0

if age < 18:
    ticket_price = 8
else:
    ticket_price = 12

if day.lower() == "wednesday":
    ticket_price = ticket_price - 2
    print("Your ticket price is {}".format(ticket_price))
else:
    print("Your ticket price is {}".format(ticket_price))
