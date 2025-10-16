check = False
large = []
medium = []
small = []
while check == False:
    x = input("what is the size of your mushroom?(type stop to end program) ")
    if x == "stop":
        check = True
        print(f"your large mushrooms are {large}")
        print(f"your medium mushrooms are {medium}")
        print(f"your small mushroom are {small}")
    else:
        x = int(x)
        if x < 100:
            small.append(0)
            index = large.index(x)
        elif x > 100 and x < 200:
            medium.append(0)
        elif x > 200 or x == 200:
            large.append(0)
    