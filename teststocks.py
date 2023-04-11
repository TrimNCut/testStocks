import random

stocks = {}
digit = 0
balance = 10000
ls_balance = 0
Tesla = random.randrange(50,150000)
Meta = random.randrange(50,150000)
Apple = random.randrange(50,150000)
Google = random.randrange(50,150000)
Netflix = random.randrange(50,150000)
amt = 0
pl = 0
sc_tesla = 1
sc_meta = 1
sc_apple = 1
sc_google = 1
sc_netflix = 1
loan = 0
has_loan = False
share_count = (sc_tesla,sc_meta,sc_apple,sc_google,sc_netflix)
owned = {"tesla": share_count[0], "meta": share_count[1], "apple": share_count[2], "google": share_count[3], "netflix": share_count[4]}
last_price = (0,0,0,0,0)

print("Name of stock : Amount of share(s) stock")
def shares():
    global owned
    if owned["tesla"] > 1 or owned["tesla"] < 1:
        print("Tesla : "+str(owned["tesla"])+" shares")
    else:
        print("Tesla : "+str(owned["tesla"])+" share")
    if owned["meta"] > 1 or owned["meta"] < 1:
        print("Meta : "+str(owned["meta"])+" shares")
    else:
        print("Meta : "+str(owned["meta"])+" share")
    if owned["apple"] > 1 or owned["apple"] < 1:
        print("Apple : "+str(owned["apple"])+" shares")
    else:
        print("Apple : "+str(owned["apple"])+" share")
    if owned["google"] > 1 or owned["google"] < 1:
        print("Google : "+str(owned["google"])+" shares")
    else:
        print("Google : "+str(owned["google"])+" share")
    if owned["netflix"] > 1 or owned["netflix"] < 1:
        print("Netflix : "+str(owned["netflix"])+" shares")
    else:
        print("Netflix : "+str(owned["netflix"])+" share")
    

print("Stocks")
while True:
    Tesla = random.randrange(10,100000)
    print("Tesla : $" + str(Tesla))
    Meta = random.randrange(10,100000)
    print("Meta : $" + str(Meta))
    Apple = random.randrange(10,100000)
    print("Apple : $" + str(Apple))
    Google = random.randrange(10,100000)
    print("Google : $" + str(Google))
    Netflix = random.randrange(10,100000)
    print("Netflix : $" + str(Netflix))
    last_price = (Tesla,Meta,Apple,Google,Netflix)
    print("")
    ask = input("Buy | Sell | Skip | Balance | Shares | Loan : ").lower()
    if ask == "buy":
        stock = input("Which stock do you want to buy : ").lower()
        amt = int(input("How many shares do you want to buy : "))
        if stock == "tesla":
            price = Tesla*amt
            if price > balance:
                print("You don't have enough money")
            else: 
                balance = balance - price
                print("Bought "+ stock +" worth of $" +str(price) + " remaining balance is $"+str(balance))
                last_price = (Tesla*amt,Meta*amt,Apple*amt,Google*amt,Netflix*amt)
                sc_tesla += amt
                share_count = (sc_tesla,sc_meta,sc_apple,sc_google,sc_netflix)
                owned = {"tesla": share_count[0], "meta": share_count[1], "apple": share_count[2], "google": share_count[3], "netflix": share_count[4]}
                
        elif stock == "meta":
            price = Meta*amt
            if price > balance:
                print("You don't have enough money")
            else: 
                balance = balance - price
                print("Bought "+ stock +" worth of $" +str(price) + " remaining balance is $"+str(balance))
                last_price = (Tesla*amt,Meta*amt,Apple*amt,Google*amt,Netflix*amt)                
                sc_meta += amt
                share_count = (sc_tesla,sc_meta,sc_apple,sc_google,sc_netflix)
                owned = {"tesla": share_count[0], "meta": share_count[1], "apple": share_count[2], "google": share_count[3], "netflix": share_count[4]}

                
        elif stock == "apple":
            price = Apple*amt
            if price > balance:
                print("You don't have enough money")
            else: 
                balance = balance - price
                print("Bought "+ stock +" worth of $" +str(price) + " remaining balance is $"+str(balance))
                last_price = (Tesla*amt,Meta*amt,Apple*amt,Google*amt,Netflix*amt)
                sc_apple += amt
                share_count = (sc_tesla,sc_meta,sc_apple,sc_google,sc_netflix)
                owned = {"tesla": share_count[0], "meta": share_count[1], "apple": share_count[2], "google": share_count[3], "netflix": share_count[4]}

        elif stock == "google":
            price = Google*amt
            if price > balance:
                print("You don't have enough money")
            else: 
                balance = balance - price
                print("Bought "+ stock +" worth of $" +str(price) + " remaining balance is $"+str(balance))
                last_price = (Tesla*amt,Meta*amt,Apple*amt,Google*amt,Netflix*amt)
                sc_google += amt
                share_count = (sc_tesla,sc_meta,sc_apple,sc_google,sc_netflix)
                owned = {"tesla": share_count[0], "meta": share_count[1], "apple": share_count[2], "google": share_count[3], "netflix": share_count[4]}

        elif stock == "netflix":
            price = Netflix*amt
            if price > balance:
                print("You don't have enough money")
            else: 
                balance = balance - price
                print("Bought "+ stock +" worth of $" +str(price) + " remaining balance is $"+str(balance))
                last_price = (Tesla*amt,Meta*amt,Apple*amt,Google*amt,Netflix*amt)
                sc_netflix += amt
                share_count = (sc_tesla,sc_meta,sc_apple,sc_google,sc_netflix)
                owned = {"tesla": share_count[0], "meta": share_count[1], "apple": share_count[2], "google": share_count[3], "netflix": share_count[4]}

    elif ask == "sell":
        print("Name of stock : Amount of share(s) stock")
        shares()
        stock = input("Which stock do you want to sell : ").lower()
        amt = int(input("How many shares do you want to sell : "))

        if stock == "tesla":
            if sc_tesla > amt or sc_tesla == amt:
                ls_balance = balance
                last_price = (Tesla,Meta,Apple,Google,Netflix)
                sc_tesla -= amt
                share_count = (sc_tesla,sc_meta,sc_apple,sc_google,sc_netflix)
                owned = {"tesla": share_count[0], "meta": share_count[1], "apple": share_count[2], "google": share_count[3], "netflix": share_count[4]}
                profit  = Tesla - last_price[0]
                balance += profit
                if ls_balance > balance or ls_balance == balance:
                    print("Loss made! Balance is $"+str(balance))
                else:
                    if has_loan == True:
                        loan -= profit
                        balance -= loan
                    print("Profit of $" + str(profit) + " made! Balance is $"+ str(balance))

            else:
                print("You can't sell "+str(amt)+" shares meanwhile you have only "+str(share_count[0])+" shares")
        
        elif stock == "meta":
            if sc_meta > amt or sc_meta == amt:
                ls_balance = balance
                last_price = (Tesla,Meta,Apple,Google,Netflix)
                sc_meta -= amt
                share_count = (sc_tesla,sc_meta,sc_apple,sc_google,sc_netflix)
                owned = {"tesla": share_count[0], "meta": share_count[1], "apple": share_count[2], "google": share_count[3], "netflix": share_count[4]}
                profit  = Tesla - last_price[1]
                balance += profit
                if ls_balance > balance or ls_balance == balance:
                    print("Loss made! Balance is $"+str(balance))
                else:
                    if has_loan == True:
                        loan -= profit
                        balance -= loan
                    print("Profit of $" + str(profit) + " made! Balance is $"+ str(balance))

            else:
                print("You can't sell "+str(amt)+" shares meanwhile you have only "+str(share_count[1])+" shares")
        
        elif stock == "apple":
            if sc_apple > amt or sc_apple == amt:
                ls_balance = balance
                last_price = (Tesla,Meta,Apple,Google,Netflix)
                sc_apple -= amt
                share_count = (sc_tesla,sc_meta,sc_apple,sc_google,sc_netflix)
                owned = {"tesla": share_count[0], "meta": share_count[1], "apple": share_count[2], "google": share_count[3], "netflix": share_count[4]}
                profit  = Tesla - last_price[2]
                balance += profit
                if ls_balance > balance or ls_balance == balance:
                    print("Loss made! Balance is $"+str(balance))
                else:
                    if has_loan == True:
                        loan -= profit
                        balance -= loan
                    print("Profit of $" + str(profit) + " made! Balance is $"+ str(balance))

            else:
                print("You can't sell "+str(amt)+" shares meanwhile you have only "+str(share_count[2])+" shares")
        
        elif stock == "google":
            if sc_google > amt or sc_google == amt:
                ls_balance = balance
                last_price = (Tesla,Meta,Apple,Google,Netflix)
                sc_google -= amt
                share_count = (sc_tesla,sc_meta,sc_apple,sc_google,sc_netflix)
                owned = {"tesla": share_count[0], "meta": share_count[1], "apple": share_count[2], "google": share_count[3], "netflix": share_count[4]}
                profit  = Tesla - last_price[3]
                balance += profit
                if ls_balance > balance or ls_balance == balance:
                    print("Loss made! Balance is $"+str(balance))
                else:
                    if has_loan == True:
                        loan -= profit
                        balance -= loan
                    print("Profit of $" + str(profit) + " made! Balance is $"+ str(balance))

            else:
                print("You can't sell "+str(amt)+" shares meanwhile you have only "+str(share_count[3])+" shares")

        elif stock == "netflix":
            if sc_netflix > amt or sc_netflix == amt:
                ls_balance = balance
                last_price = (Tesla,Meta,Apple,Google,Netflix)
                sc_netflix -= amt
                share_count = (sc_tesla,sc_meta,sc_apple,sc_google,sc_netflix)
                owned = {"tesla": share_count[0], "meta": share_count[1], "apple": share_count[2], "google": share_count[3], "netflix": share_count[4]}
                profit  = Tesla - last_price[4]
                balance += profit
                if ls_balance > balance or ls_balance == balance:
                    print("Loss made! Balance is $"+str(balance))
                else:
                    if has_loan == True:
                        loan -= profit
                        balance -= loan
                    print("Profit of $" + str(profit) + " made! Balance is $"+ str(balance))
                    
            else:
                print("You can't sell "+str(amt)+" shares meanwhile you have only "+str(share_count[4])+" shares")
                            
    elif ask == "skip":
        print("Skipped!")
    elif ask == "balance":
        balance = balance
        print("Your balance is $"+str(balance))
    elif ask == "shares":
        shares()
    elif ask == "loan":
        if has_loan == False:
            loan = int(input("Enter amount of loan (Max loan is $10000) : "))
            balance += loan
        elif has_loan == True:
            print("Pay up loan first!")
    else:
        print("Wrong input entered!")
    print("")