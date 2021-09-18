#Assigning variables from input values

a = input("a: ")
b = input("b: ")

print("a = " + a)
print("b = " + b)

#Switching values
a, b = b, a 

"""
Or
c = a 
a = b
b = c
"""

print("Now:")
print("a = " + a)
print("b = " + b)
