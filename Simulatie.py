import random
import time
import Basicstrategy
import Count

# Global values for the cards
facecardvalue = {"B": 10, "V": 10, "H": 10, "A11" : 11, "A1" : 1}


# global list for passed cards
def globalpassed():
    global passed
    passed = []
    return passed

# createsdeck and shuffles it
def makedeck():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "B", "V", "H", "A11", 2, 3, 4, 5, 6, 7, 8, 9, 10, "B", "V", "H", "A11", 2,
                    3, 4,
                    5, 6, 7, 8, 9, 10, "B", "V", "H", "A11", 2, 3, 4, 5, 6, 7, 8, 9, 10, "B", "V", "H", "A11"]
    random.shuffle(deck)
    return deck

def makehand():
    hand = []
    return hand


# voegt een kaart toe aan de hand van de player
# en removed het van de allcards deck en voegt het toe aan de passed cards
def addtoplayerhand(playerhand,deck):
    playerhand.append(deck[0])
    passed.append(deck[0])
    del deck[0]


# voegt een kaart toe aan de hand van de dealer
# en removed het van de allcards deck en voegt het toe aan de passed cards
def addtodealerhand(dealerhand,deck):
    dealerhand.append(deck[0])
    passed.append(deck[0])
    del deck[0]


# kijkt verandert de grote ace naar de kleine ace waarneer het nodig is
def checkiface(playerhand):
    for i in playerhand:
        if i == "A11":
            playerhand[playerhand.index("A11")] = "A1"
            return True

    return False


# telt de totale value van de hand van de player
# plus kijkt of de grote ace verandert moet worden naar de kleine
def checkplayerhand(playerhand):
    sumofhand = 0
    for i in playerhand:
        if type(i) != int:
            sumofhand += facecardvalue.get(i)
        if type(i) == int:
            sumofhand += i
    if sumofhand > 21:
        if checkiface(playerhand) == True:
            checkplayerhand(playerhand)
        return sumofhand
    else:
        return sumofhand

# kijkt of er nog een grote ace in de hand zit
def checkhardsoft(playerhand):
    for i in playerhand:
        if i == "A11":
            return False
    return True

# telt de totale value van de dealer
# plus kijkt of de grote ace verandert moet worden naar de kleine
def checkdealerhand(dealerhand):
    sumofhand = 0
    for i in dealerhand:
        if type(i) != int:
            sumofhand += facecardvalue.get(i)
        if type(i) == int:
            sumofhand += i
    if sumofhand > 21:
        if checkiface(dealerhand) == True:
            sumofhand = checkdealerhand(dealerhand)
        return sumofhand
    else:
        return sumofhand

# geeft een kaart naar de playerhand en checkt het
def hit(playerhand,deck):
    addtoplayerhand(playerhand,deck)
    checkplayerhand(playerhand)


# dit zijn de keuzes die de player heeft en returnd deze keuze
# deze functie verandert op basis of er gesplit is en of al gedubbeldowned is
def choices(playerhand):
    if len(playerhand) == 1:
        choice = input(str("h = hit, s = stand: "))
        if choice == "h":
            return "h"
        if choice == "s":
            return "s"
    if playerhand[0] == playerhand[1] and len(playerhand) < 3:
        choice = input(str("h = hit, s = stand,d = doubledown p = split: "))
    if playerhand[0] != playerhand[1] and len(playerhand) < 3:
        choice = input(str("h = hit, s = stand, d = doubledown: "))
    elif len(playerhand) >= 3:
        choice = input(str("h = hit, s = stand: "))

    if choice == "h":
        return "h"
    if choice == "s":
        return "s"
    if choice == "p":
        return "p"
    if choice == "d":
        return "d"


# print alle info over de hand van de player en van de dealer
def printhand(playerhandvalue,dealerhandvalue,playerhand,dealerhand):
    print(playerhandvalue,"playervalue")
    print(playerhand,"playerhand")
    print(dealerhandvalue,"dealervalue")
    print(dealerhand,"dealerhand")
    # time.sleep(2)

# het maken van een game van blackjack de player heeft 2 kaarten en de dealer een.
def firstround(playerhand,dealerhand,deck):
    addtoplayerhand(playerhand, deck)
    addtoplayerhand(playerhand, deck)
    addtodealerhand(dealerhand, deck)


# nadat de player stay heeft gekozen moet de dealer naar 17
# deze functie zorgt ervoor dat er telkens kaarten aan de hand
# worden toegevoegd totdat de total boven 17 is.
def dealerto17(dealerhand,deck):
    sumofhand = 0
    while sumofhand < 17:
        addtodealerhand(dealerhand,deck)
        sumofhand = checkdealerhand(dealerhand)
    return sumofhand


# kijkt of er een blackjack is
def blackjack(playerhand):
    if checkplayerhand(playerhand) == 21 and len(playerhand) == 2:
        return True
    else:
        return False

# split de playerhand in 2 hands
def split(playerhand):
    split1 = playerhand[0]
    split2 = playerhand[1]
    newsplit = [[split1],[split2]]
    return newsplit

# Het spel
def gamestart(money,deck):
    print("Saldo: {}$".format(money))
    victory = 0
    loss = 0
    draw = 0

    truecount = Count.checkrunningcount(passed)
    highorlow = Count.favor(truecount)
    print(highorlow)

    bet = int(input("how much do you bet: "))

    # je kan "mod" invoeren om de basicstrategy helemaal alleen te laten spelen
    usebot = str(input("do you want the algorithm to help you: y or n "))
    playerhand = makehand()
    dealerhand = makehand()

    money -= bet
    firstsplit = False
    doubledown = False
    canDouble = True

    firstround(playerhand,dealerhand,deck)
    printhand(checkplayerhand(playerhand), checkdealerhand(dealerhand),playerhand,dealerhand)

    while True:

        if blackjack(playerhand) == True:
            dealerto17(dealerhand,deck)
            print(dealerhand, "dealerhand")
            if blackjack(dealerhand) == True:
                print("equal score so draw you get your money back")
                draw += 1
                money += bet
                break
            victory += 1
            money += bet * 6 /5 + bet
            print("you got a blackjack so you win: {}".format(bet* 6/5+ bet))
            break

        if checkplayerhand(playerhand) > 21:
            print("over 21 you lose: {}".format(bet))
            loss += 1
            break

        hard = checkhardsoft(playerhand)
        playervalue = checkplayerhand(playerhand)
        dealervalue = checkdealerhand(dealerhand)
        if usebot == "y":
            todo = Basicstrategy.basicstrategy(playerhand,playervalue,dealervalue,firstsplit,canDouble,hard)
            print("The basicstrategy says you have to {} here".format(todo))
            choice = choices(playerhand)
        if usebot == "n":
            choice = choices(playerhand)
        if usebot == "mod":
            choice = Basicstrategy.basicstrategy(playerhand,playervalue,dealervalue,firstsplit,canDouble,hard)

        if choice == "h":
            print("hit")
            hit(playerhand,deck)
            printhand(checkplayerhand(playerhand), checkdealerhand(dealerhand), playerhand, dealerhand)
            canDouble = False

            continue
        if choice == "s":
            print("stay")
            dealerto17(dealerhand,deck)
        if choice == "p":
            print("split")
            firstsplit = True
            canDouble = False
            break
        if choice == "d":
            hit(playerhand,deck)
            doubledown = True
            break

        checkplayer = checkplayerhand(playerhand)
        checkdealer = checkdealerhand(dealerhand)
        printhand(checkplayer,checkdealer,playerhand,dealerhand)

        if checkplayer > checkdealer:
            print("more points than dealer so you win: {} ".format(bet))
            victory += 1
            money += bet*2
            break

        if checkplayer == checkdealer:
            print("equal score so draw you get your moneyback")
            draw += 1
            money += bet
            break

        if checkdealer > 21:
            print("dealer is over 21 so you win: {} ".format(bet))
            victory += 1
            money += bet*2
            break

        if checkdealer > checkplayer:
            print("dealer has more points than you so you lose: {}".format(bet))
            loss += 1
            break

    while doubledown == True:
        money -= bet
        bet = bet * 2
        print("Double Down!")
        checkplayer = checkplayerhand(playerhand)
        checkdealer = checkdealerhand(dealerhand)
        printhand(checkplayer, checkdealer, playerhand, dealerhand)

        if checkplayer > 21:
            print("over 21 you lose: {}".format(bet))
            loss += 1
            break

        elif checkplayer <= 21:
            dealerto17(dealerhand,deck)
            checkplayer = checkplayerhand(playerhand)
            checkdealer = checkdealerhand(dealerhand)
            printhand(checkplayer, checkdealer, playerhand, dealerhand)
            if checkplayer > checkdealer:
                print("more points than dealer so you win: {} ".format(bet))
                victory += 1
                money += bet*2
                break

            if checkplayer == checkdealer:
                print("equal score so draw you get your moneyback")
                draw += 1
                money += bet
                break

            if checkdealer > 21:
                print("dealer is over 21 so you win: {} ".format(bet))
                victory += 1
                money += bet*2
                break

            if checkdealer > checkplayer:
                print("dealer has more points than you so you lose: {}".format(bet))
                loss += 1
                break

    if firstsplit == True:
        # split de hand in twee nieuwe hands
        newhands = split(playerhand)
        money -= bet

        # loopt door elke hand heen een speelt daarmee verder tot dat er voor stand is gekozen
        for hands in newhands:
            printhand(checkplayerhand(hands), checkdealerhand(dealerhand),hands,dealerhand)
            while True:

                hard = checkhardsoft(hands)
                playervalue = checkplayerhand(hands)
                dealervalue = checkdealerhand(dealerhand)
                if usebot == "y":
                    todo = Basicstrategy.basicstrategy(hands,playervalue,dealervalue,firstsplit,canDouble,hard)
                    print("The basicstrategy says you have to {} here".format(todo))
                    choice = choices(hands)
                if usebot == "n":
                    choice = choices(hands)
                if usebot == "mod":
                    choice = Basicstrategy.basicstrategy(playerhand,playervalue,dealervalue,firstsplit,canDouble,hard)

                checkplayer = checkplayerhand(hands)
                if checkplayer > 21:
                    print("over 21 you lose {}".format(bet))
                    loss += 1
                    break
                if choice == "h":
                    hit(hands,deck)
                    printhand(checkplayerhand(hands), checkdealerhand(dealerhand), hands, dealerhand)
                    continue
                if choice == "s":
                    break

        dealerto17(dealerhand,deck)
        # kijkt naar de uitkomsten van de gespeelde hands
        for hands in newhands:
            checkplayer = checkplayerhand(hands)
            checkdealer = checkdealerhand(dealerhand)
            printhand(checkplayerhand(hands), checkdealerhand(dealerhand),hands,dealerhand)
            if checkplayer > 21:
                continue
            if blackjack(dealerhand) == True:
                loss += 1
                print("dealer has blackjack so you lose: {}".format(bet))
                continue
            if checkplayer > checkdealer:
                victory += 1
                money += bet * 2
                print("you have more points than dealer so you win: {} ".format(bet*2))
                continue
            if checkplayer == checkdealer:
                print("equal score so draw so you get your money back")
                money += bet
                draw += 1
                continue
            if checkdealer > 21:
                print("dealer is over 21 so you win: {} ".format(bet*2))
                victory += 1
                money += bet * 2
                continue
            if checkdealer > checkplayer:
                print("dealer has more points than you so you lose: {}".format(bet))
                loss += 1
                continue

    print("Saldo: {}$".format(money))
    return victory,loss,draw,money


# het spel starten
def playthegame():
    print("welcome to blackjack")

    wins = 0
    losses = 0
    draws = 0

    # maakt deck en een passed cards list
    globalpassed()
    deck = makedeck()

    game = input(str("Do you want to play a game y or n: "))
    chipvalue = int(input("what is the value of your chips: "))
    while game == "y":

        played = gamestart(chipvalue,deck)

        wins += played[0]
        losses += played[1]
        draws += played[2]
        chipvalue = played[3]

        game = input(str("Do you want to play another game y or n: "))
        print("Wins: {} Losses: {} Draws: {}".format(wins,losses,draws))

        # checkt of het deck groot genoeg is om te spelen
        if len(deck) < 12:
            deck = makedeck()
            globalpassed()
    if game == "n":
        print("thanks for playing")
        return False
    print("thanks for playing")

playthegame()