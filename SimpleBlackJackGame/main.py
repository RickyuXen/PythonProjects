from blackjackfunctions import*

###
#  simple oop version of blackjack; ignores deck sizes
#  author: Ricky Mach
#  made for fun
###

def main():
    playagain = 'Y'
    bustStatus = False
    dealerBlackjack = False
    playerBusted = player("none")
    userChoice = 'A'
    print("Hello")
    # dealer
    dealer = player("Dealer")

    # player hand
    playerName = input("Please enter in your game name: ")
    userPlayer = player(playerName)

    while(playagain != 'N'):
        # player set up
        while userChoice != 'P':
            userChoice = input("What would you like to do?: Add funds (A) Check Balance (B) Play game (P)\n>>>>>>>>>>>")
            if userChoice == 'A':
                userPlayer.addFunds()
            if userChoice == "B":
                print(userPlayer.wallet)
        userChoice = 'A' # set userChoice to be able to add funds again later

        # user must bet an amount
        userBet = input("How much would you like to bet?: $")
        winamount = 2* userPlayer.betAmount(userBet)

        # distribute cards to computer and player
        userPlayer.game()
        dealer.game()
        # print out status of game
        printStatus(dealer, userPlayer)

        # check for dealer blackjack
        if dealer.total == 21:
            dealerBlackjack = True
        
        # ask for user input in game
        userInput = 'L'
        while userInput != 'S' and not bustStatus and not dealerBlackjack:
            userInput = input("Hit or Stand? (H/S):")
            if userInput == 'H':
                userPlayer.hit()
                printStatus(dealer, userPlayer)
                bustStatus, playerBusted = bust(userPlayer)    # check for busts
        
        # dealer hands, simple alogirthm, if < 17, hit once and stand
        if dealer.total < 17 and not bustStatus:
            dealer.hit()
            bustStatus, playerBusted = bust(dealer)
            printStatus(dealer, userPlayer) # print status of dealer hands

        # Determine winnings
        if userPlayer.total > dealer.total and not bustStatus and not dealerBlackjack:
            userPlayer.winAmount += 1
            userPlayer.wallet += winamount
            print(f"{userPlayer.name} wins! ${winamount} added to your account!")
        elif userPlayer.total == dealer.total and not bustStatus:
            print("Tie! No winnings")
            userPlayer.wallet += winamount / 2
        elif userPlayer.total < dealer.total and not bustStatus and not dealerBlackjack:
            print(f"Dealer wins! you lose ${winamount/2}")
        elif dealerBlackjack:
            print(f"Dealer wins blackjack! You lose ${winamount/2}")
        else: # There was a bust
            print(f"{playerBusted.name} busts!")
            if playerBusted.getName("Dealer"):
                userPlayer.winAmount += 1
                userPlayer.wallet += winamount
                print(f"{userPlayer.name} wins! ${winamount} added to your account!")
            else:
                print("You lose, sorry")
            
        
        # wipe cards, reset booleans
        userPlayer.reset()
        dealer.reset()
        bustStatus = False
        dealerBlackjack = False
        playerBusted = player("none")

        playagain = input("Play again? (Y or N): ")
        


if __name__ == "__main__":
    main()