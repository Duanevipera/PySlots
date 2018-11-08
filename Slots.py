#Terry Rucker
#Slots

#makes it possible to use the random module
import random

import time


#declares the integer variable "money" and sets it to 100
money = 100

#sets the array for the items to be used in the slots
slots = ["Cherries", "Oranges", "Plums", "Bells", "Melons", "Bars"]

    
#displays how much money player has
print("You currently have ",money," to play with.")


while (money > 0):
    bet = int(input("how much would you like bet?"))

    if bet > money:
        continue #restarts the loop if bet is greater than amount of money

    #decreases amount of money by the amount of the bet
    money = money - bet
 #   for i in range (6):
    #displays the random choices from the array.       
    results1 = random.choice(slots)
    print(results1)

    time.sleep(1.0)
       
    results2 = random.choice(slots)
    print(results2)

    time.sleep(1.0)
            
    results3 = random.choice(slots)
    print(results3)

    time.sleep(1.0)

    
    
#determines if all three slot items are the same
    if results1 == results2 and results2 == results3:
        if results1 == "Cherries":
            print ("Winner 3 Cherries!")
            bet = bet * 10
            money = money + bet
            print(money)
        elif results1 == "Oranges":
            print ("Winner 3 Oranges!")
            bet = bet * 5
            money = money + bet
            print(money)
        elif results1 == "Plums":
            print ("Winner 3 Plums!")
            bet = bet * 2
            money = money + bet
            print(money)
        elif results1 == "Bells":
            print ("Winner 3 Bells!")
            bet = bet * 12
            money = money + bet
            print(money)
        elif results1 == "Melons":
            print ("Winner 3 Melons!")
            bet = bet * 20
            money = money + bet
            print(money)
        elif results1 == "Bars":
            print ("Winner 3 Bars!")
            bet = bet * 100
            money = money + bet
            print(money)

        #determines if 2 slot items are the same
    elif results1 == results2 or results2 == results3 or results1 == results3:
                    print ("Winner 2 are the same")
                    bet = bet * 2
                    money = money + bet
                    print("You now have ",money," to play with")
                    continue

        
        #defaults if there is no win        
    else:
           print ("Sorry, You Lose")
           print("You still have ",money," to bet with.")


    
        
        
        
            




print(money)

#keep_playing = "true"
