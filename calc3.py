check = False
while check == False:
    option = input("what operation do you want to do? (type quit to exit): ").strip().lower()
    try:
        if option == "addition":
            x = input("what is x? ")
            x = int(x)
            y = input("what is y? ")
            y = int(y)
            sum = x + y
            print(f"the sum of {x} and {y} is {sum}")
        elif option == "subtraction":
             x = input("what is x? ")
             x = int(x)
             y = input("what is y? ")
             y = int(y)
             difference = x - y
             print(f"the difference of {x} and {y} is {difference}")
        elif option == "multiplication":
            x = input("what is x? ")
            x = int(x)
            y = input("what is y? ")
            y = int(y)
            product = x * y
            print(f"the product of {x} and {y} is {product}")
        elif option == "division":
             x = input("what is x? ")
             x = int(x)
             y = input("what is y? ")
             y = int(y)
             try:
                quotiant = x / y
                print(f"the quotiant of {x} and {y} is {quotiant}")
             except ZeroDivisionError:
                 print("Error: cannot divide by zero")
    except ValueError:
        print("that is not a number")
    if option == "quit":
        check = True