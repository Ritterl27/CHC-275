x = input("what is the first number? ")
y = input("what is the second number? ")
x = int(x)
y = int(y)
if x > y:
    print("num 1 wins")
elif x < y:
    print("num 2 wins")
elif x == y:
    print("its a tie")