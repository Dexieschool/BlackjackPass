import random
import time


facecardvalue = {"B": 10, "V": 10, "H": 10, "A11" : 11, "A1" : 1}






def makedeck():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "B", "V", "H", "A11", 2, 3, 4, 5, 6, 7, 8, 9, 10, "B", "V", "H", "A11", 2,
                    3, 4,
                    5, 6, 7, 8, 9, 10, "B", "V", "H", "A11", 2, 3, 4, 5, 6, 7, 8, 9, 10, "B", "V", "H", "A11"]
    random.shuffle(deck)
    return deck

# maak een hand creator zodat deze nieuwe hand de split kan spelen en weer in de gameplay() function gedaan kan worden<-
def makehandplayer():
    playerhand = []
    return playerhand

def makehanddealer():
    dealerhand = []
    return dealerhand


# voegt een kaart toe aan de hand van de player
# en removed het van de allcards deck
def addtoplayerhand(playerhand,deck):
    checkdeckempty(deck)
    playerhand.append(deck[0])
    del deck[0]


# voegt een kaart toe aan de hand van de dealer
# en removed het van de allcards deck
def addtodealerhand(dealerhand,deck):
    checkdeckempty(deck)
    dealerhand.append(deck[0])
    del deck[0]


# kiest welke value de ace kaart kan zijn
# mogelijk maakt dit algoritmes kapot
def checkiface(playerhand):
    for i in playerhand:
        if i == "A11":
            playerhand[playerhand.index("A11")] = "A1"
            return True

    return False


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


def checkhardsoft(playerhand):
    for i in playerhand:
        if i == "A11":
            return False
    return True

def checkdealerhand(dealerhand):
    sumofhand = 0
    for i in dealerhand:
        if type(i) != int:
            sumofhand += facecardvalue.get(i)
        if type(i) == int:
            sumofhand += i
    if sumofhand > 21:
        if checkiface(dealerhand) == True:
            checkplayerhand(dealerhand)
        return sumofhand
    else:
        return sumofhand


def hit(playerhand,deck):
    addtoplayerhand(playerhand,deck)
    checkplayerhand(playerhand)


def stand():
    return True


def choices(playerhand):
    if len(playerhand) == 1:
        choice = input(str("h = hit, s = stand"))
        if choice == "h":
            return "h"
        if choice == "s":
            stand()
            return "s"
    if playerhand[0] == playerhand[1] and len(playerhand) < 3:
        choice = input(str("h = hit, s = stand,d = doubledown p = split"))
    if playerhand[0] != playerhand[1] and len(playerhand) < 3:
        choice = input(str("h = hit, s = stand, d = doubledown"))
    elif len(playerhand) >= 3:
        choice = input(str("h = hit, s = stand"))

    if choice == "h":
        return "h"
    if choice == "s":
        stand()
        return "s"
    if choice == "p":
        return "p"
    if choice == "d":
        return "d"


def printhand(playerhandvalue,dealerhandvalue,playerhand,dealerhand):
    print(playerhandvalue,"playervalue")
    print(playerhand,"playerhand")
    print(dealerhandvalue,"dealervalue")
    print(dealerhand,"dealerhand")
    # time.sleep(2)


def firstround(playerhand,dealerhand,deck):
    addtodealerhand(dealerhand, deck)
    addtoplayerhand(playerhand, deck)
    addtoplayerhand(playerhand, deck)


def dealerto17(dealerhand,deck):
    sumofhand = 0
    while sumofhand < 17:
        addtodealerhand(dealerhand,deck)
        sumofhand = checkdealerhand(dealerhand)
    return sumofhand


# make double down function
def blackjack(playerhand):
    if checkplayerhand(playerhand) == 21 and len(playerhand) == 2:
        return True
    else:
        return False


def split(playerhand):
    split1 = playerhand[0]
    split2 = playerhand[1]
    newsplit = [[split1],[split2]]
    return newsplit


def checkdeckempty(deck):
    if not deck:
        print("a new deck is shuffled")
        makedeck()
        return True
    if deck:
        return False


def basicstrategy(playerhand,dealerhand,split,canDouble):

    hard = checkhardsoft(playerhand)
    pair = False
    if not split:
        if playerhand[0] == playerhand[1] and len(playerhand) == 2:
            pair = True

    if pair == False and hard == True:
        if checkplayerhand(playerhand) >= 17:
            return "s"
        elif 2 <= checkdealerhand(dealerhand) <= 6 and 13 <= checkplayerhand(playerhand) <= 16:
            return "s"
        elif 4 <= checkdealerhand(dealerhand) <= 6 and checkplayerhand(playerhand) == 12:
            return "s"
        elif 2 <= checkdealerhand(dealerhand) <= 10 and checkplayerhand(playerhand) == 11 and canDouble == True:
            return "d"
        elif 2 <= checkdealerhand(dealerhand) <= 9 and checkplayerhand(playerhand) == 10 and canDouble == True:
            return "d"
        elif 3 <= checkdealerhand(dealerhand) <= 6 and checkplayerhand(playerhand) == 9 and canDouble == True:
            return "d"
        else:
            return "h"

    elif pair == False and hard == False:
        if 19 <= checkplayerhand(playerhand) <= 21:
            return "s"
        elif checkplayerhand(playerhand) == 18 and 7 <= checkdealerhand(dealerhand) <= 8 or checkdealerhand(dealerhand) == 2:
            return "s"
        elif 13 <= checkplayerhand(playerhand) <= 18 and 5 <= checkdealerhand(dealerhand) <= 6 and canDouble == True:
            return "d"
        elif 15 <= checkplayerhand(playerhand) <= 18 and checkdealerhand(dealerhand) == 4 and canDouble == True:
            return "d"
        elif 17 <= checkplayerhand(playerhand) <= 18 and checkdealerhand(dealerhand) == 3 and canDouble == True:
            return "d"
        else:
            return "h"

    elif pair == True:
        if playerhand[0] == "A11" or playerhand[0] == 8:
            return "p"
        elif playerhand[0] == 10 or playerhand[0] in ["B","V","H"]:
            return "s"
        elif checkplayerhand(playerhand) in [18,14,12] and 2 <= checkdealerhand(dealerhand) <= 6:
            return "p"
        elif checkplayerhand(playerhand) in [6,4] and 2 <= checkdealerhand(dealerhand) <= 7:
            return "p"
        elif checkplayerhand(playerhand) == 10 and 2 <= checkdealerhand(dealerhand) <= 9 and canDouble == True:
            return "d"
        elif checkplayerhand(playerhand) == 8 and 5 <= checkdealerhand(dealerhand) <= 6:
            return "p"
        elif checkplayerhand(playerhand) == 14 and checkdealerhand(dealerhand) == 7:
            return "p"
        elif checkplayerhand(playerhand) == 18 and checkdealerhand(dealerhand) in [7,10,11]:
            return "s"
        elif checkplayerhand(playerhand) == 18 and checkdealerhand(dealerhand) in [8,9]:
            return "p"
        else:
            return "h"


#TODO als 2 Acen er in zitten telt het verkeerd fix dit AF!
#TODO kleine a en grote A als de grote A hard wordt het een kleine a met de waarde van 1 AF!
#TODO bugtesting fout(wint te veel geld gaat ergens fout)
#TODO laten runnen voor heel lang kijken wat de resultaten zijn(werkt)
#TODO Card counting (moet nog gedaan worden)


def gamestart(money,deck):
    print("Saldo: {}$".format(money))
    victory = 0
    loss = 0
    draw = 0


    # bet = int(input("how much do you bet: "))
    bet = 1
    # usebot = str(input("do you want to use the bot y or no: "))
    usebot = "y"
    playerhand = makehandplayer()
    dealerhand = makehanddealer()


    money -= bet
    firstsplit = False
    doubledown = False
    canDouble = True
    firstround(playerhand,dealerhand,deck)
    checkplayer = checkplayerhand(playerhand)
    checkdealer = checkdealerhand(dealerhand)
    printhand(checkplayer, checkdealer,playerhand,dealerhand)



    while True:
        if blackjack(playerhand) == True:
            victory += 1
            money += bet + bet * 1.5
            print("you got a blackjack so you win: {}".format(bet + bet*1.5))
            break

        if checkplayerhand(playerhand) > 21:
            print("over 21 you lose: {}".format(bet))
            loss += 1
            break

        checkplayer = checkplayerhand(playerhand)
        if usebot == "y":
            choice = basicstrategy(playerhand,dealerhand,firstsplit,canDouble)
        if usebot != "y":
            choice = choices(playerhand)


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
            print("doubledown")
            printhand(checkplayerhand(playerhand), checkdealerhand(dealerhand), playerhand, dealerhand)
            hit(playerhand,deck)
            doubledown = True
            break


        checkplayer = checkplayerhand(playerhand)
        checkdealer = checkdealerhand(dealerhand)
        printhand(checkplayer,checkdealer,playerhand,dealerhand)


        if checkplayer > checkdealer:
            print("more points than dealer so you win: {} ".format(bet*2))
            victory += 1
            money += bet*2
            break
        if checkplayer == checkdealer:
            print("equal score so draw you get your moneyback")
            draw += 1
            money += bet
            break
        if checkdealer > 21:
            print("dealer is over 21 so you win: {} ".format(bet * 2))
            victory += 1
            money += bet*2
            break
        if checkdealer > checkplayer:
            print("dealer has more points than you so you lose: {}".format(bet))
            loss += 1
            break


    while doubledown == True:
        money -= bet
        bet *= 2

        print("Double Down!")
        # time.sleep(0.5)
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
                print("more points than dealer so you win: {} ".format(bet*2))
                victory += 1
                money += bet*2
                break
            if checkplayer == checkdealer:
                print("equal score so draw you get your moneyback")
                draw += 1
                money += bet
                break
            if checkdealer > 21:
                print("dealer is over 21 so you win: {} ".format(bet * 2))
                victory += 1
                money += bet*2
                break
            if checkdealer > checkplayer:
                print("dealer has more points than you so you lose: {}".format(bet))
                loss += 1
                break

    if firstsplit == True:
        newhands = split(playerhand)
        money -= bet


        for hands in newhands:
            printhand(checkplayerhand(hands), checkdealerhand(dealerhand),hands,dealerhand)
            while True:
                if usebot == "y":
                    choice = basicstrategy(hands,dealerhand,firstsplit,canDouble)
                if usebot != "y":
                    choice = choices(hands)

                checkplayer = checkplayerhand(hands)
                if blackjack(playerhand) == True:
                    victory += 1
                    money += bet + bet * 1.5
                    print("you got a blackjack you win: {}".format(bet+bet*1.5))
                    break
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
        for hands in newhands:
            checkplayer = checkplayerhand(hands)
            checkdealer = checkdealerhand(dealerhand)
            printhand(checkplayerhand(hands), checkdealerhand(dealerhand),hands,dealerhand)
            if checkplayer > 21:
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













def playthegame():
    print("welcome to blackjack")

    wins = 0
    losses = 0
    draws = 0



    deck = makedeck()
    game = input(str("Do you want to play a game y or n: "))
    chipvalue = int(input("what is the value of your chips: "))
    while game == "y":

        played = gamestart(chipvalue,deck)

        wins += played[0]
        losses += played[1]
        draws += played[2]
        chipvalue = played[3]

        # game = input(str("Do you want to play another game y or n: "))
        game = "y"
        print("Wins: {} Losses: {} Draws: {}".format(wins,losses,draws))
        if len(deck) < 10:
            deck = makedeck()
    if game == "n":
        print("thanks for playing")
        return False
    print("thanks for playing")

playthegame()