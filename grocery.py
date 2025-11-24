Check = False
file = open("foods.txt","r")
buffer = file.readlines()
file.close()
foods = []
price = []
cart = []
cartmoney = 0
for line in buffer:
        line = line.strip()
        line = line.split(",")
        foods.append(line[0])
        line[1] = float(line[1])
        price.append(line[1])
print("welcome to the online grocery store")
while Check == False:
    print("1. add to cart")
    print("2. remove items")
    print("3. check out")
    print("4. quit")
    x = input("please select a function ")
    if x == "1":
        print(foods)
        print(price)
        x = input("what would you like to purchase? (0-8) ")
        if x == "0":
            index = foods.index("bananas")
            cart.append("bananas")
            cartmoney = cartmoney + price[index]
        elif x == "1":
            index = foods.index("apples")
            cart.append("apples")
            cartmoney = cartmoney + price[index]
        elif x == "2":
            index = foods.index("raw steak")
            cart.append("raw steak")
            cartmoney = cartmoney + price[index]
        elif x == "3":
            index = foods.index("milk")
            cart.append("milk")
            cartmoney = cartmoney + price[index]
        elif x == "4":
            index = foods.index("orange juice")
            cart.append("orange juice")
            cartmoney = cartmoney + price[index]
        elif x == "5":
            index = foods.index("eggs")
            cart.append("eggs")
            cartmoney = cartmoney + price[index]
        elif x == "6":
            index = foods.index("rotisserie chicken")
            cart.append("rotisserie chicken")
            cartmoney = cartmoney + price[index]
        elif x == "7":
            index = foods.index("rice")
            cart.append("rice")
            cartmoney = cartmoney + price[index]
        elif x == "8":
            index = foods.index("loaf of bread")
            cart.append("loaf of bread")
            cartmoney = cartmoney + price[index]
        else:
            print("that is not a food available")
        print(cart)
        print(cartmoney)
        
    elif x == "2":
        print(cart)
        x = input("what would you like to remove? ").strip().lower().replace(" ", "")
        if x == "bananas":
            index = foods.index("bananas")
            cartmoney = cartmoney - price[index]
            cart.remove("bananas")
            print(f"your cart balance is {cartmoney}")
            print(f"your cart is {cart}")
        elif x == "apples":
            index = foods.index("apples")
            cartmoney = cartmoney - price[index]
            cart.remove("apples")
            print(f"your cart balance is {cartmoney}")
            print(f"your cart is {cart}")
        elif x == "rawsteak":
            index = foods.index("raw steak")
            cartmoney = cartmoney - price[index]
            cart.remove("raw steak")
            print(f"your cart balance is {cartmoney}")
            print(f"your cart is {cart}")
        elif x == "milk":
            index = foods.index("milk")
            cartmoney = cartmoney - price[index]
            cart.remove("milk")
            print(f"your cart balance is {cartmoney}")
            print(f"your cart is {cart}")
        elif x == "orangejuice":
            index = foods.index("orange juice")
            cartmoney = cartmoney - price[index]
            cart.remove("orange juice")
            print(f"your cart balance is {cartmoney}")
            print(f"your cart is {cart}")
        elif x == "eggs":
            index = foods.index("eggs")
            cartmoney = cartmoney - price[index]
            cart.remove("eggs")
            print(f"your cart balance is {cartmoney}")
            print(f"your cart is {cart}")
        elif x == "rice":
            index = foods.index("rice")
            cartmoney = cartmoney - price[index]
            cart.remove("rice")
            print(f"your cart balance is {cartmoney}")
            print(f"your cart is {cart}")
        elif x == "loafofbread":
            index = foods.index("loaf of bread")
            cartmoney = cartmoney - price[index]
            cart.remove("loaf of bread")
            print(f"your cart balance is {cartmoney}")
            print(f"your cart is {cart}")
    elif x == "3":
        tax = cartmoney *0.06
        total = cartmoney + tax
        print(f"the total cost for your purchase is ${total}")
    elif x == "4":
        Check = True
        print("thanks for using the grocery program")
    else:
        print("that is not a function of the grocery program")


