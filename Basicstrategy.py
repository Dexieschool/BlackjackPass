
# Het algoritme die keuzes maakt op basis van de playerhand value en de dealerhand value
# checkt ook op splits enof het kan dubbelen
def basicstrategy(playerhand,playervalue,dealervalue,split,canDouble,hard):

    pair = False
    if not split:
        if playerhand[0] == playerhand[1] and len(playerhand) == 2:
            pair = True
        if playerhand[0] == "A1" and playerhand[1] == "A11":
            pair = True

    if pair == False and hard == True:
        if playervalue >= 17:
            return "s"
        elif 2 <= dealervalue <= 6 and 13 <= playervalue <= 16:
            return "s"
        elif 4 <= dealervalue <= 6 and playervalue == 12:
            return "s"
        elif 2 <= dealervalue <= 10 and playervalue == 11 and canDouble == True:
            return "d"
        elif 2 <= dealervalue <= 9 and playervalue == 10 and canDouble == True:
            return "d"
        elif 3 <= dealervalue <= 6 and playervalue == 9 and canDouble == True:
            return "d"
        else:
            return "h"

    elif pair == False and hard == False:
        if 19 <= playervalue <= 21:
            return "s"
        elif playervalue == 18 and 7 <= dealervalue <= 8 or dealervalue == 2:
            return "s"
        elif 13 <= playervalue <= 18 and 5 <= dealervalue <= 6 and canDouble == True:
            return "d"
        elif 15 <= playervalue <= 18 and dealervalue == 4 and canDouble == True:
            return "d"
        elif 17 <= playervalue <= 18 and dealervalue == 3 and canDouble == True:
            return "d"
        else:
            return "h"

    elif pair == True:
        if playerhand[0] == "A11" or playerhand[0] == "A1":
            playerhand[0] = "A11"
            return "p"
        elif playerhand[0] == 8:
            return "p"
        elif playerhand[0] == 10 or playerhand[0] in ["B","V","H"]:
            return "s"
        elif playervalue in [18,14,12] and 2 <= dealervalue <= 6:
            return "p"
        elif playervalue in [6,4] and 2 <= dealervalue <= 7:
            return "p"
        elif playervalue == 10 and 2 <= dealervalue <= 9 and canDouble == True:
            return "d"
        elif playervalue == 8 and 5 <= dealervalue <= 6:
            return "p"
        elif playervalue == 14 and dealervalue == 7:
            return "p"
        elif playervalue == 18 and dealervalue in [7,10,11]:
            return "s"
        elif playervalue == 18 and dealervalue in [8,9]:
            return "p"
        else:
            return "h"

