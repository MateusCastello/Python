numbers_list = [x for x in range(1, 1001)]

for number in numbers_list:
    prime_numbers = [any(number % i == 0 for i in range(number, len(numbers_list)))]

print(prime_numbers)


prime_numbers = [number for number in range(2, N + 1) if all(number % n for n in range(2, number))]
