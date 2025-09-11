x = input("what is x? ")
x = int(x)
if x % 2 == 0:
    print(f"{x} is divisible by 2" )
    print("test")
else:
    print(f"{x} is not divisible by 2")
#else only runs if if statement fails

"""
elif = contraction of else and if
"""
x = input("what is x? ")
x = int(x)
if x % 5 == 0:
    print(f"{x} is divisible by 5")
elif x % 2 == 0:
    print(f"{x} is divisible by 2")
else:
    print(f"{x} is not divisble by 5 or 2")
"""
if we tried a number that is divisible by 5 and 2, only the first one runs
"""
