num = 5
"""
this creates a variable, named num, and its attribute is the number 5
"""

"""
print (<variable name)
"""
print(num)
x=10
print(x)
"""
now we can do 4 basic function arithmatic
adding +
subtracting -
multiplying *
dividing /
"""
print(num + x)
print(x - num)
print(num * x)
print(x / num)

sum = num + x
print(sum)
"""
consistently update variables
"""
x=5
y=10
z=0
#z is our working variable, we save results of operations into z
z = x + y
print(z)
#z is now set to 15
z = z/2
print(z)
"""
data types:
numerical (integers, decimal numbers)
strings: collection of individual characters taht come together and are stored under one variable name
"""
name = "Liam Ritter"
occupation = 'Student'
print(name)
print(occupation)
"""
F strings (format strings)
"""
print(f"My name is {name}, and my occupation is {occupation}")
"""
concatenation:combining two strings together
"""
first = "Calvert"
second = "Hall"
school = first + second
print(school)