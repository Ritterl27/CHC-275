#this is a bank sytem that can depoit/withdraw money, transfer money, add/remove accounts, and view accounts and their balances
accounts = ["Sasha","John", "Michael", "Amanda"] #this is the list of all the accounts
balances = [260.67, 508.97, 1004.53, 762.00] #this is a list of the balances for the accounts
check = False #used to create while loop (program will continue running)
while check == False:#this ensures the program will continue running until "check = True"
    x = input("would you like to open the menu? ") #the program will continue to ask "would you like to open the menu" until it is told something other than "yes"
    if x == ("yes"):
        print("1.deposit")
        print("2.withdraw")
        print("3.view accounts and balances")
        print("4.transfer money")
        print("5.add account")
        print("6.remove account")
        #these print out the functions of the system for the user to view
        x = input("what # action would you like to do? ") #asks for a numeric value that corresponds to a function of the system
        if x == ("3"):
            accountname4 = input("what is your account name? ")
            index = accounts.index(accountname4) #this connects the name of the account given by the user to the same account in the list
            print(balances[index]) #this connects the account to its balance
        elif x == ("5"):
            accountname = input("what is your account name? ") #this creates the variable for the account to be added
            accounts.append(accountname) #this adds the name of the account
            balances.append(0) #this adds a new balance for the new account
            index = accounts.index(accountname) #this connects the the name of the account given by the user to the same account that was just added
            print("your account has been added")
        elif x == ("6"):
            accountname2 = input("what is your account name? ") #this creates the variable for the account to be removed
            index = accounts.index(accountname2) #this links the account to an index so the balance can also be removed
            accounts.pop(index) #removes the account
            balances.pop(index) #removes the balance for the account
            print("your account and balance has been removed. ")
        elif x == ("1"):
            accountname3 = input("what is your account name? ") #this creates the variable for the account that is being deposited into
            index = accounts.index(accountname3) #this links the account to an index so the balance can be added with the money deposited
            x = input("how much would you like to add? ") #creates a variable for the money that will be deposited
            x = int(x) #makes the value an integar
            balances[index] = balances[index] + x #adds the current balance of the account to the value that is being deposited
            print(f"your new balance is {balances[index]} ") #prints new balance value
        elif x ==("2"):
            accountname5 = input("what is your account name? ") #this creates the variable for the account that is being withdrawn from
            index = accounts.index(accountname5) #this links the account to an index so the money being withdrawn can be removed from the balance
            x = input("how much would you like to withdraw? ") #creates a variable for the money that will be withdrawn
            x = int(x) #makes the value an integar
            balances[index] = balances[index] - x #subtracts the value being withdrawn from the balance value
            print(f"your new balance is {balances[index]} ") #prints new balance value
        elif x == ("4"):
            accountname6 = input("what is your account name? ") #this creates the variable for the account that is transferring money
            index = accounts.index(accountname6)#this links the account to an index so the money being transferred can be withdrawn from the balance of the account transferring money
            accountname7 = input("what is the transfer account name? ") #this creates the variable for the account that money is being transferred to
            i = accounts.index(accountname7) #this links the account to an index so the money being transferred can be added to the balance of the recieving account
            transfer = input("how much would you like to transfer? ") #asks for the amount of money being transferred
            transfer = int(transfer) #makes transfer value an integar that can be added/subtracted
            balances[i] = balances[i] + transfer #adds the value of the recieving accounts balance with the money value being transferred
            balances[index] = balances[index] - transfer #subtracts the value being transferred from the balance of the transferring account
            print(f"{accountname7}'s balance is {balances[i]} ") #prints new balance of the transfer account
            print(f"your account balance is {balances[index]} ") #prints new balance of the transferring account
    else:
        check = True #stops program from looping
        print("thanks for using the bank system ")

            
            