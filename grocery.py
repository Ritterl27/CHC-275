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
while Check == False:
    
    print("welcome to the online grocery store")
    print("1. add to cart")
    print("2. remove items")
    print("3. check out")
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
            print(cartmoney)
            print(cart)
        elif x == "apples":
            index = foods.index("apples")
            cartmoney = cartmoney - price[index]
            print(cartmoney)
        elif x == "rawsteak":
            index = foods.index("raw steak")
            cartmoney = cartmoney - price[index]
            print(cartmoney)
        elif x == "milk":
            index = foods.index("milk")
            cartmoney = cartmoney - price[index]
            print(cartmoney)
        elif x == "orangejuice":
            index = foods.index("orange juice")
            cartmoney = cartmoney - price[index]
            print(cartmoney)
        elif x == "eggs":
            index = foods.index("eggs")
            cartmoney = cartmoney - price[index]
            print(cartmoney)
        elif x == "rice":
            index = foods.index("rice")
            cartmoney = cartmoney - price[index]
            print(cartmoney)
        elif x == "loafofbread":
            index = foods.index("loaf of bread")
            cartmoney = cartmoney - price[index]
            print(cartmoney)


    """
    sub_total = 10.75
    tax = sub_total *0.06
    total = sub_total + tax

    
    
    """


