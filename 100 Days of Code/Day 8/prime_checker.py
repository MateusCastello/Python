number = int(input("Inset the number to check if it is prime: "))

is_prime = True

if number % 2 == 0:
    is_prime = False
elif number % 3 == 0:
    is_prime = False
elif number == 2:
    is_prime = True
else:
    for i in range(2, number):
        if number % i == 0:            
            is_prime = False

if is_prime:
    print("Prime")
else:
    print("Not prime")