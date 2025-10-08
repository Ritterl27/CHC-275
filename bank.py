accounts = ["Sasha","John", "Michael", "Amanda"] #this is the list of all the accounts
balances = [260.67, 508.97, 1004.53, 762.00] #this is a list of the balances for the accounts
check = False 
while check == False:#this ensures the program will continue running until told to stop
    x = input("would you like to open the menu? ") #the program will continue to ask "would you like to open the menu" until it is told something other than "yes"
    if x == ("yes"):
        print("1.deposit")
        print("2.withdraw")
        print("3.view accounts and balances")
        print("4.transfer money")
        print("5.add account")
        print("6.remove account")
        #these print out the functions of the system for the user to view
        x = input("what # action would you like to do? ")
        if x == ("3"):
            accountname4 = input("what is your account name? ")
            index = accounts.index(accountname4) #this connects the name of the account given by the user to the same account in the list
            print(balances[index]) #this connects the account to its balance
        elif x == ("5"):
            accountname = input("what is your account name? ")
            accounts.append(accountname) #this adds the name of the account
            balances.append(0) #this adds another balance for the new account
            index = accounts.index(accountname) #this connects the the name of the account given by the user to the same account that was just added
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
        elif x == ("4"):
            accountname6 = input("what is your account name? ")
            index = accounts.index(accountname6)
            accountname7 = input("what is the transfer account name? ")
            i = accounts.index(accountname7)
            transfer = input("how much would you like to transfer? ")
            transfer = int(transfer)
            balances[i] = balances[i] + transfer
            y = balances[i]
            balances[index] = balances[index] - transfer
            x = balances[index]
            print(f"the transfer account balance is {y} ")
            print(f"your account balance is {x} ")
    else:
        check = True
        print("thanks for using the bank system ")

            
            