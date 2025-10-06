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
            print(accounts,balances)
        if x == ("5"):
            accountname = input("what is your account name? ")
            accounts.append(accountname)
            balances.append(0)
            print("your account has been added")
        elif x == ("6"):
            accountname2 = input("what is your account name? ")
            accounts.remove(accountname2)
            print("your account has been removed, your money is lost :( ")
        
            