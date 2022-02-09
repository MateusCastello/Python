print("Welcome to the rollercoaster!")
height = int(input("What is your heigt in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = input("What is your age? ")

    if age < 12:
        print("Your ticket is $5")
    elif age <=18:
        print("Your ticket is $7")
    else:
        print("Your ticket is $12")
else:
    print("Sorry, you hava to grow taller before you can ride.")