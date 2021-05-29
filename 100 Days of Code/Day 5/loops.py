#Basic list loop
fruits = ["Apple", "Peach", "Pear", "Melon"]

for fruit in fruits:
    print(fruit)
    print(fruit+" pie")

#Average Heights without sum()
student_heights = [180, 124, 165, 154, 187, 150, 175, 176, 167, 190]
avg_height = 0

for student in student_heights:
    avg_height += student

avg_height = avg_height/len(student_heights)
print(f"the average height is {round(avg_height)}")
