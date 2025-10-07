accounts = ["Sasha","John", "Michael", "Amanda"]
balances = [260.67, 508.97, 1004.53, 762.00]
check = False
while check == False:
    x = input("would you like to open the menu? ")
    if x == ("yes"):
        print("1.deposit")
        print("2.withdraw")
        print("3.view accounts and balances")
        print("4.transfer money")
        print("5.add account")
        print("6.remove account")
        x = input("what # action would you like to do? ")
        if x == ("3"):
            accountname4 = input("what is your account name? ")
            index = accounts.index(accountname4)
            print(balances[index])
        elif x == ("5"):
            accountname = input("what is your account name? ")
            accounts.append(accountname)
            balances.append(0)
            print("your account has been added")
        elif x == ("6"):
            accountname2 = input("what is your account name? ")
            index = accounts.index(accountname2)
            accounts.pop(index)
            balances.pop(index)
            print("your account and balance has been removed. ")
        elif x == ("1"):
            accountname3 = input("what is your account name? ")
            index = accounts.index(accountname3)
            x = input("how much would you like to add? ")
            x = int(x)
            balances[index] = balances[index] + x
            y = balances[index]
            print(f"your new balance is {y} ")
        elif x ==("2"):
            accountname5 = input("what is your account name? ")
            index = accounts.index(accountname5)
            x = input("how much would you like to withdraw? ")
            x = int(x)
            balances[index] = balances[index] - x
            y = balances[index]
            print(f"your new balance is {y} ")
            
            