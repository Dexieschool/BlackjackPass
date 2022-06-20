import random


passedcards = []




def makedeck():
    global allcardsdeck
    allcardsdeck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "B", "V", "H", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "B", "V", "H", "A", 2,
                    3, 4,
                    5, 6, 7, 8, 9, 10, "B", "V", "H", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "B", "V", "H", "A"]
    random.shuffle(allcardsdeck)
    global passedcards
    passedcards = []


facecardvalue = {"B": 10, "V": 10, "H": 10}

globalplayerhand = []
globaldealerhand = []
# maak een hand creator zodat deze nieuwe hand de split kan spelen en weer in de gameplay() function gedaan kan worden<-





# voegt een kaart toe aan de hand van de player
# en removed het van de allcards deck
def addtoplayerhand(playerhand):
    checkdeckempty()
    playerhand.append(allcardsdeck[0])
    passedcards.append(allcardsdeck[0])
    del allcardsdeck[0]


# voegt een kaart toe aan de hand van de dealer
# en removed het van de allcards deck
def addtodealerhand(dealerhand):
    checkdeckempty()
    dealerhand.append(allcardsdeck[0])
    passedcards.append(allcardsdeck[0])
    del allcardsdeck[0]


# kiest welke value de ace kaart kan zijn
# mogelijk maakt dit algoritmes kapot
def checkiface(playerhand):
    for i in playerhand:
        if i == "A":
            return True

    return False

def resethand():
    globalplayerhand.clear()
    globaldealerhand.clear()



def checkplayerhand(playerhand):
    sumofhand = 0
    for i in playerhand:
        if type(i) != int and i != "A":
            sumofhand += facecardvalue.get(i)
        if type(i) == int:
            sumofhand += i
        if i == "A":
            sumofhand += 11
    if sumofhand > 21 and checkiface(globalplayerhand) == True:
        sumofhand -= 10
    if sumofhand > 21:
        return sumofhand
    else:
        return sumofhand


def checkdealerhand(dealerhand):
    sumofhand = 0
    for i in dealerhand:
        if type(i) != int and i != "A":
            sumofhand += facecardvalue.get(i)
        if type(i) == int:
            sumofhand += i
        if i == "A":
            sumofhand += 11
    if sumofhand > 21 and checkiface(globaldealerhand) == True:
        sumofhand -= 10
    if sumofhand > 21:
        return sumofhand
    else:
        return sumofhand


def hit(playerhand):
    addtoplayerhand(playerhand)
    checkplayerhand(globalplayerhand)


def stand():
    return True


def choices(playerhand):
    if len(playerhand) == 1:
        choice = input(str("h = hit, s = stand"))
        if choice == "h":
            hit(playerhand)
            return "h"
        if choice == "s":
            stand()
            return "s"
    if playerhand[0] == playerhand[1]:
        choice = input(str("h = hit, s = stand,d = doubledown p = split"))
    if playerhand[0] != playerhand[1] and len(playerhand) < 3:
        choice = input(str("h = hit, s = stand, d = doubledown"))
    elif len(playerhand) >= 3:
        choice = input(str("h = hit, s = stand"))

    if choice == "h":
        hit(playerhand)
        return "h"
    if choice == "s":
        stand()
        return "s"
    if choice == "p":
        return "p"
    if choice == "d":
        hit(playerhand)
        return "d"



def printhand(playerhandvalue,dealerhandvalue,playerhand,dealerhand):
    print(playerhandvalue,"playervalue")
    print(playerhand,"playerhand")
    print(dealerhandvalue,"dealervalue")
    print(dealerhand,"dealerhand")

def firstround():
    addtodealerhand(globaldealerhand)
    addtoplayerhand(globalplayerhand)
    addtoplayerhand(globalplayerhand)

def dealerto17(dealerhand):
    sumofhand = 0
    while sumofhand < 17:
        addtodealerhand(globaldealerhand)
        sumofhand = checkdealerhand(dealerhand)
    return sumofhand


# make double down function
def blackjack(playerhand):
    if checkplayerhand(playerhand) == 21 and checkiface(playerhand):
        return True
    else:
        return False


def split():
    split1 = globalplayerhand[0]
    split2 = globalplayerhand[1]
    newsplit = [[split1],[split2]]
    return newsplit


def checkdeckempty():
    if not allcardsdeck:
        print("a new deck is shuffled")
        makedeck()
        passedcards = []
        return True
    if allcardsdeck:
        return False

def gamestart(money):
    victory = 0
    loss = 0
    draw = 0
    print("Saldo: {}$".format(money))

    bet = int(input("how much do you bet: "))
    money -= bet
    firstsplit = False
    doubledown = False

    firstround()
    checkplayer = checkplayerhand(globalplayerhand)
    checkdealer = checkdealerhand(globaldealerhand)
    printhand(checkplayer, checkdealer,globalplayerhand,globaldealerhand)

    while True:
        if blackjack(globalplayerhand) == True:
            victory += 1
            money = money + bet + bet * 1.5
            print("you got a blackjack so you win: {}".format(bet+bet*1.5))
            break
        choice = choices(globalplayerhand)
        checkplayer = checkplayerhand(globalplayerhand)
        checkdealer = checkdealerhand(globaldealerhand)
        printhand(checkplayer,checkdealer,globalplayerhand,globaldealerhand)
        if checkplayer > 21:
            print("over 21 you lose: {}".format(bet))
            resethand()
            loss += 1
            break
        if choice == "h":
            continue
        if choice == "s":
            dealerto17(globaldealerhand)
        if choice == "p":
            firstsplit = True
            break
        if choice == "d":
            doubledown = True
            break
        checkplayer = checkplayerhand(globalplayerhand)
        checkdealer = checkdealerhand(globaldealerhand)
        printhand(checkplayer,checkdealer,globalplayerhand,globaldealerhand)
        if checkplayer > checkdealer:
            print("more points than dealer so you win: {} ".format(bet*2))
            resethand()
            victory += 1
            money += bet*2
            break
        if checkplayer == checkdealer:
            print("equal score so draw you get your moneyback")
            resethand()
            draw += 1
            money += bet
            break
        if checkdealer > 21:
            print("dealer is over 21 so you win: {} ".format(bet * 2))
            resethand()
            victory += 1
            money += bet*2
            break
        if checkdealer > checkplayer:
            print("dealer has more points than you so you lose: {}".format(bet))
            resethand()
            loss += 1
            break

    if doubledown == True:
        money -= bet
        bet *= 2
        checkplayer = checkplayerhand(globalplayerhand)
        checkdealer = checkdealerhand(globaldealerhand)
        printhand(checkplayer, checkdealer, globalplayerhand, globaldealerhand)
        if checkplayer > 21:
            print("over 21 you lose: {}".format(bet))
            resethand()
            loss += 1
        elif checkplayer <= 21:
            dealerto17(globaldealerhand)
            checkplayer = checkplayerhand(globalplayerhand)
            checkdealer = checkdealerhand(globaldealerhand)
            printhand(checkplayer, checkdealer, globalplayerhand, globaldealerhand)
            if checkplayer > checkdealer:
                print("more points than dealer so you win: {} ".format(bet*2))
                resethand()
                victory += 1
                money += bet*2
            if checkplayer == checkdealer:
                print("equal score so draw you get your moneyback")
                resethand()
                draw += 1
                money += bet
            if checkdealer > 21:
                print("dealer is over 21 so you win: {} ".format(bet * 2))
                resethand()
                victory += 1
                money += bet*2
            if checkdealer > checkplayer:
                print("dealer has more points than you so you lose: {}".format(bet))
                resethand()
                loss += 1






    if firstsplit == True:
        newhands = split()
        money -= bet
        for hands in newhands:
            checkplayer = checkplayerhand(hands)
            checkdealer = checkdealerhand(globaldealerhand)
            printhand(checkplayer, checkdealer,hands,globaldealerhand)
            while True:
                choice = choices(hands)
                checkplayer = checkplayerhand(hands)
                checkdealer = checkdealerhand(globaldealerhand)
                printhand(checkplayer, checkdealer,hands,globaldealerhand)
                if blackjack(globalplayerhand) == True:
                    victory += 1
                    money += bet
                    bet = bet * 1.5
                    money += bet
                    print("you got a blackjack you win: {}".format(bet+bet*1.5))
                    break
                if checkplayer > 21:
                    print("over 21 you lose {}".format(bet))
                    loss += 1
                    break
                if choice == "h":
                    continue
                if choice == "s":
                    break
        dealerto17(globaldealerhand)
        for hands in newhands:
            checkplayer = checkplayerhand(hands)
            checkdealer = checkdealerhand(globaldealerhand)
            printhand(checkplayer, checkdealer,hands,globaldealerhand)
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
                print("dealer has more points than you so you lose: {}".format(bet*2))
                loss += 1
                continue
    resethand()

    playagain =  input(str("Do you want to play again? y or n: "))
    if playagain == "y":
        gamestart(money)
    if playagain == "n":
        return












def playthegame():
    print("welcome to blackjack")
    makedeck()
    game = input(str("Do you want to play a game y or n: "))
    if game == "y":
        chipvalue = int(input("what is the value of your chips: "))

        gamestart(chipvalue)
    if game == "n":
        print("thanks for playing")
        return False
    print("thanks for playing")

playthegame()