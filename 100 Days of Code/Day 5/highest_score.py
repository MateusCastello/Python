#highest score without max()
student_scores = [34,78, 65, 89, 86, 55, 91, 64, 89, 15]
highest = 0

for score in student_scores:
    if score > highest:
        highest = score

print(f"The highest score in the class is: {highest}")