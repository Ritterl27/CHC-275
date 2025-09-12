print("welcome to the calculator")
o = input("what operation do you want to do? ")
if o == "addition":
    x = input("what is x? ")
    y = input("what is y? ")
    x = int(x)
    y = int(y)
    sum = x + y
    print(f"the sum of {x} and {y} is {sum}")
elif o == "subtraction":
    x = input("what is x? ")
    y = input("what is y? ")
    x = int(x)
    y = int(y)
    difference = x - y
    print(f"the difference of {x} and {y} is {difference}")
elif o == "multiplication":
    x = input("what is x? ")
    y = input("what is y? ")
    x = int(x)
    y = int(y)
    product = x * y
    print(f"the product of {x} and {y} is {product}")
elif o == "division":
    x = input("what is x? ")
    y = input("what is y? ")
    x = int(x)
    y = int(y)
    quotiant = x / y
    print(f"the quotiant of {x} and {y} is {quotiant}")
