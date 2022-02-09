year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 == 0:
        print("Leap")
    elif year % 100 == 0:
        print("Not Leap")
    else:
        print("Leap")
else:
    print("Not Leap")