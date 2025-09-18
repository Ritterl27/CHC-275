fish = input("what kind of fish do you have, carnivorous, salt water, or community? ")
if fish == ("carnivorous"):
    q = input("do you already have it? (yes or no) ")
    if q == ("yes"):
        print("too bad ")
    elif q == ("no"):
        print("enjoy ")
elif fish == ("salt water"):
    print("you're a fancy fish parent")
elif fish == ("community"):
    print("you should get more than one")
else:
    print("i dont think thats a kind of fish")