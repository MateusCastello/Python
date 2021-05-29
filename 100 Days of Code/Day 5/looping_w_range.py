#Gauss problem > sum all numbers from 1 to 100
#1+2+3...+100
total = 0

for number in range(1,101):
    total += number

print(f"Gauss total: {total}")


#Adding even numbers without an if
even_sum = 0

#Start, Finish, Pace
for number in range(2, 101, 2):
         even_sum += number

print(f"Sum of even numbers: {even_sum}")

#With if
even_sum2 = 0
for number in range(1, 101):
    if number % 2 ==0:
        even_sum2 += number
print(f"Sum of even numbers: {even_sum2}")