check = False
while check == False:
    option = input("what operation do you want to do? type quit to exit ")
    if option == "addition":
        x = input("what is x? ")
        y = input("what is y? ")
        x = int(x)
        y = int(y)
        sum = x + y
        print(f"the sum of {x} and {y} is {sum}")
    elif option == "subtraction":
         x = input("what is x? ")
         y = input("what is y? ")
         x = int(x)
         y = int(y)
         difference = x - y
         print(f"the difference of {x} and {y} is {difference}")
    elif option == "multiplication":
        x = input("what is x? ")
        y = input("what is y? ")
        x = int(x)
        y = int(y)
        product = x * y
        print(f"the product of {x} and {y} is {product}")
    elif option == "division":
         x = input("what is x? ")
         y = input("what is y? ")
         x = int(x)
         y = int(y)
         quotiant = x / y
    elif option == "quit":
        check = True