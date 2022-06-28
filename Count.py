
HiLow = {"2": 1, "3": 1, "4": 1, "5": 1, "6": 1, "7": 0, "8": 0, "9": 0, "10": -1, "B": -1, "V": -1, "H": -1, "A11": -1}


# kijkt hoeveel voor het aantal remaining cards
def count(deck):
    left = 52 - deck
    return left


# card counting berekent de count van het hele deck
def checkrunningcount(passed):
    count = 0
    for i in passed:
        i = str(i)
        count += HiLow.get(i)
    return count

# dit is het algoritme die suggesties geeft over wanneer het handig is om meer of minder in te zetten
def favor(runningcount):
    if runningcount >= 3:
        return "The count({}) is higher than 3 so next round will be advantageous for you".format(runningcount)
    if runningcount <= -3:
        return "The count({}) is lower than 3 so next round will be disadvantageous for you".format(runningcount)
    else:
        return "The count({}) is neutral so you are advised to bet a normal amount".format(runningcount)