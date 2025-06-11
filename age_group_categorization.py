age = int(input("Enter your age: "))

if age > 0:
    if age < 13:
        print("child")
    elif age < 20:
        print("teenager")
    elif age < 60:
        print("adult")
    else:
        print("senior")
else:
    print("age can't be 0")