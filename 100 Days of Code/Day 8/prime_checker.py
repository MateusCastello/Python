number = int(input("Inset the number to check if it is prime: "))

is_prime = True

if number == 2 or number == 3:
    is_prime = True
elif number %2 == 0:
    is_prime = False
elif number %3 == 0:
    is_prime = False
else:
    for i in range(5, number):
        if number % i == 0:            
            is_prime = False

if is_prime:
    print("Prime")
else:
    print("Not prime")