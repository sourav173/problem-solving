'''
Problem: assign a letter grade based on a student's score A(90-100), B(80-89),C(70-79),D(60-69),F(BELOW 60)
'''
score = int(input("Enter student's score:"))

if score <= 100:
    if score <60:
        print('F')
    elif score < 70:
        print('D')
    elif score < 80:
        print('C')
    elif score <90:
        print("B")
    else:
        print("A")

else:
    print("Write between 0 - 100")