from random import *
# blackjackfunctions.py

global dict 
dict = {1:"A", 11: "J", 12: "Q", 13: "K"}
# Blackjack functions
def giveCards(hands):
    
    c1 = randint(1,13)
    c2 = randint(1,13)
    if c1 in dict:
        hands.append(dict[c1])
    else:
        hands.append(c1)
    if c2 in dict:
        hands.append(dict[c2])
    else:
        hands.append(c2)
    cardtotal = min(c1, 10) + min(c2, 10)

    # special case: A
    if c1 == 1 or c2 == 1:
        cardtotal += 10

    return int(cardtotal)

def bust(playerP):
    if playerP.total > 21:
        return True, playerP
    else:
        return False, playerP
    
def printStatus(dealerP, playerP):
    print(f"Dealer: {dealerP.hands} : {dealerP.total}")
    print(f"{playerP.name} : {playerP.hands} : {playerP.total}")

class player:
    def __init__(self, name):
        self.name = name
        self.hands = []
        self.total = 0
        self.wallet = 0
        self.winAmount = 0
        self.mostA = 1

    def hit(self):
        newC = randint(1,13)
        if newC in dict:
            self.hands.append(dict[newC])
        else:
            self.hands.append(newC)

        # check number of A's, subtract accordingly

        # check for special case : A
        self.total += min(newC, 10)
        if self.total <= 10 and newC == 1:
            self.total += 11 
        if self.total > 21 and 'A' in self.hands and self.mostA > 0:
            self.total -= 10 
            self.mostA -= 1

    def game(self):
        self.total = giveCards(self.hands)

    def addFunds(self):
        amount = int(input("Please enter funds to add: $"))
        self.wallet += amount

    def betAmount(self, amount):
        if self.wallet < int(amount):
            print("Balance too low, bet is set to $0")
        else:
            self.wallet -= int(amount)
            return int(amount)
        return int(0)

    def getName(self, name):
        if self.name == name:
            return True
        return False
    
    def reset(self):
        self.hands = []
        self.total = 0