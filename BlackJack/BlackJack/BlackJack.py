from random import randint

pDoubleAce = False
dDoubleAce = False
command = ""

pcard1 = randint(2, 14)             #cards are asigned to a value between 2 and 14
pcard2 = randint(2, 14)
if pcard1 == 11 and pcard2 == 11:   #if the player has a double Ace, the second Ace has the value 1
    pDoubleAce = True

dcard1 = randint(2, 14)
dcard2 = randint(2, 14)
if dcard1 == 11 and dcard2 == 11:   #same here
    dDoubleAce = True

playerCards = [pcard1, pcard2]  #dealers cards
dealerCards = [dcard1, dcard2]  #players cards
pTrueCards = []                 #trueCards show the value of the card in real terms
dTrueCards = []

i = 0
while i < len(dealerCards):
    if dealerCards[i] == 12:
        dTrueCards.append("J")
        dealerCards[i] = 10     #the value of J, Q, K in BJ is 10
    elif dealerCards[i] == 13:
        dTrueCards.append("Q")
        dealerCards[i] = 10
    elif dealerCards[i] == 14:
        dTrueCards.append("K")
        dealerCards[i] = 10
    elif dealerCards[i] == 11:  #the value of A in BJ is 11 or 1 --> for now 11
        dTrueCards.append("A")
    else:
        dTrueCards.append(str(dealerCards[i]))
    i = i + 1

i = 0
while i < len(playerCards):
    if playerCards[i] == 12:
        pTrueCards.append("J")
        playerCards[i] = 10
    elif playerCards[i] == 13:
        pTrueCards.append("Q")
        playerCards[i] = 10
    elif playerCards[i] == 14:
        pTrueCards.append("K")
        playerCards[i] = 10
    elif playerCards[i] == 11:
        pTrueCards.append("A")
    else:
        pTrueCards.append(str(playerCards[i]))
    i = i + 1

if pDoubleAce == True:
    playerCards[1] = 1
if dDoubleAce == True:
    dealerCards[1] = 1

print("Welcome to BlackJack by BT --> h for Hit, s for Stand, / for Split (only if pair), d for Double")
print("Dealer rule: dealer stops at 17")
print("")
print("")
print("Dealer's cards: " + str(dTrueCards[0]) + " *")                                           #the dealer's and player's cards are presented
print("")
print("Your cards: " + str(pTrueCards[0]) + " " + str(pTrueCards[1]))

if playerCards[0] == 11 and playerCards[1] == 10 or playerCards[1] == 11 and playerCards[0] == 10:  #the player instantly wins if he has a BlackJack (sum of A and 10/J/Q/K)
    print("")
    print("BlackJack!")
    print("""You won!
Your cards were: """, end = ' ')
    i = 0
    while i < len(playerCards):
        print(str(pTrueCards[i]) + " ", end = ' ')
        i = i + 1
    print("")
    print("The dealers cards: ", end = ' ')
    i = 0
    while i < len(dealerCards):
        print(str(dTrueCards[i]) + " ", end = ' ')
        i = i + 1
    print("")
    quit()
else:
    command = input("What shall't be: ")
    print("")

i = 0
while i != 1:
    if command == "h":                          #the player hits to get a new card

        j = 0
        sumP = 0
        newCard = randint(2, 14)

        if newCard == 12:
            pTrueCards.append("J")
            newCard = 10
        elif newCard == 13:
            pTrueCards.append("Q")
            newCard = 10
        elif newCard == 14:
            pTrueCards.append("K")
            newCard = 10
        elif newCard == 11:
            pTrueCards.append("A")
        else:
            pTrueCards.append(str(newCard))
        playerCards.append(newCard)

        while j < len(playerCards):
            sumP = sumP + playerCards[j]
            j = j + 1

        j = 0
        if sumP > 21:                           #there is a case, in which the Ace represents the value 1 --> but only if the sum is over 21 with an Ace of the value 11
            while j < len(playerCards):
                if playerCards[j] == 11:        #checks if there is an Ace
                    playerCards[j] = 1          #if yes, then the Ace's value is only 1
                    sumP = sumP - 10
                    break
                else:
                    j = j + 1

        j = 0
        if sumP <= 21:
            print("Your new Cards: ", end = ' ')
            while j < len(pTrueCards):
                print(str(pTrueCards[j]) + " ", end = ' ')
                j = j+ 1
            print("")
            command = input("What shall't be: ")

        else:                                       #player loses if the sum of his cards is over 21
            print("""

You lost!
Your cards were: """, end = ' ')
            j = 0
            while j < len(playerCards):
                print(str(pTrueCards[j]) + " ", end = ' ')
                j = j+ 1
            print("")
            print("The dealers cards: ", end = ' ')
            j = 0
            while j < len(dealerCards):
                print(str(dTrueCards[j]) + " ", end = ' ')
                j = j+ 1
            i = 1
            print("")
    
    elif command == "s":                        #the player can stand and the dealers cards are turned over

        sumP = 0
        sumD = 0

        j = 0
        while j < len(playerCards):
            sumP = sumP + playerCards[j]
            j = j + 1
        j = 0
        while j < len(dealerCards):
            sumD = sumD + dealerCards[j]
            j = j + 1


        j = 0
        while j != 1:
            if sumD < 17:                   #dealer hits
                newCard = randint(2, 14)
                if newCard == 12:
                    dTrueCards.append("J")
                    newCard = 10
                elif newCard == 13:
                    dTrueCards.append("Q")
                    newCard = 10
                elif newCard == 14:
                    dTrueCards.append("K")
                    newCard = 10
                elif newCard == 11:
                    dTrueCards.append("A")
                else:
                    dTrueCards.append(str(newCard))
                sumD = sumD + newCard
                dealerCards.append(newCard)

                h = 0
                if sumD > 21:                           
                    while h < len(dealerCards):
                        if dealerCards[h] == 11:        
                            dealerCards[h] = 1          
                            sumD = sumD - 10
                            break
                        else:
                            h = h + 1

            elif sumD >= 17 and sumD < 21:                  #most of the times the dealer stops hitting at 17
                j = 1
                i = 1
                if sumP > sumD:                                #the player wins if his sum is bigger
                    print("""

You won!
Your cards were: """, end = ' ')
                    h = 0
                    while h < len(playerCards):
                        print(str(pTrueCards[h]) + " ", end = ' ')
                        h = h + 1
                    print("")
                    print("The dealers cards: ", end = ' ')
                    h = 0
                    while h < len(dealerCards):
                        print(str(dTrueCards[h]) + " ", end = ' ')
                        h = h + 1
                    print("")
                elif sumP < sumD:                              #the player loses if his sum is smaller
                    print("""

You lost!
Your cards were: """, end = ' ')
                    h = 0
                    while h < len(playerCards):
                        print(str(pTrueCards[h]) + " ", end = ' ')
                        h = h + 1
                    print("")
                    print("The dealers cards: ", end = ' ')
                    h = 0
                    while h < len(dealerCards):
                        print(str(dTrueCards[h]) + " ", end = ' ')
                        h = h + 1
                    print("")
                else:                                           #it's a tie if both have the same sum
                    print("""

It's a tie!
Your cards were: """, end = ' ')
                    h = 0
                    while h < len(playerCards):
                        print(str(pTrueCards[h]) + " ", end = ' ')
                        h = h + 1
                    print("")
                    print("The dealers cards: ", end = ' ')
                    h = 0
                    while h < len(dealerCards):
                        print(str(dTrueCards[h]) + " ", end = ' ')
                        h = h + 1
                    print("")
            else:                           #player wins if dealer goes over 21
                j = 1
                i = 1
                print("""

You won!
Your cards were: """, end = ' ')
                h = 0
                while h < len(playerCards):
                    print(str(pTrueCards[h]) + " ", end = ' ')
                    h = h + 1
                print("")
                print("The dealers cards: ", end = ' ')
                h = 0
                while h < len(dealerCards):
                    print(str(dTrueCards[h]) + " ", end = ' ')
                    h = h + 1
                print("")
    else:
        print("")
        command = input("Oops! There might be a mistake with ur input. Please only use h, s, / or d. ")
        print("")
