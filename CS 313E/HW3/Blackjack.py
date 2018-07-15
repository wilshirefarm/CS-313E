#  File: Blackjack.py
#  Description: Blackjack game
#  Student's Name: Wilshire Liu
#  Student's UT EID: WL7583
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: 9/20/16
#  Date Last Modified: 9/23/16

import random

class Card:

    #initiates a card object
    def __init__(self, pip, suit):
        self.suit = suit
        self.pip = pip
        if (isinstance(pip, int)):    #if it's a number, that is the value
            self.value = pip
        elif (pip == "J" or pip == "Q" or pip == "K"):    #Jack, Queen, King is 10 points
            self.value = 10
        else: self.value = 11    #otherwisre, it's an ace which is 11 points at first

    #dunder str for card
    def __str__(self):
        return str(self.pip) + str(self.suit)

class Deck:

    #initiates a deck object
    def __init__(self):
        self.cardList = []
        #uses nested loop to create all 52 cards in a deck
        for s in ["C", "D", "H", "S"]:
            for p in [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]:
                self.cardList.append(Card(p, s))

    #dunder str for deck
    def __str__(self):
        listOfCards = ""
        #uses a loop to create the format of the deck output
        for i in range(len(self.cardList)):
            if (i % 13 == 0 and i != 0):
                listOfCards = listOfCards + "\n" + str(self.cardList[i]).rjust(4)
            else:
                listOfCards = listOfCards + str(self.cardList[i]).rjust(4)
        return listOfCards

    #shuffles deck
    def shuffle(self):
        #random.seed(25)
        #random.seed(50)
        random.shuffle(self.cardList)

    #deals one card to a player
    def dealOne(self, player):
        player.handTotal = player.handTotal + self.cardList[0].value    #increments the hand's total when card is dealt
        player.hand.append(self.cardList[0])    #adds the first card in the shuffled deck to the player's hand
        if (self.cardList[0].pip == "A"):    #numberOfAcesAsEleven keeps track of how many aces a player receives and is counted as 11 points
            player.numberOfAcesAsEleven += 1
        return self.cardList.pop(0)    #.pop removes the card from the deck

class Player:

    #initiates a player object
    def __init__(self):
        self.hand = []
        self.handTotal = 0
        self.numberOfAcesAsEleven = 0

    #dunder str for player
    def __str__(self):
        hand = ""
        for i in self.hand:
            hand = hand + str(i) + "  "
        return hand

#method that lets player goes first
def yourTurn(cardDeck, you, dealer):
    inPlay = True    #the switch in the while loop
    if ((you.hand[0].value == 11 and you.hand[1].value != 11) or (you.hand[0].value != 11 and you.hand[1].value == 11)):    #if only one ace is in a hand
        print("Assuming 11 points for the ace you were dealt for now")
        if (you.handTotal == 21):
            if (dealer.handTotal == 21):    #dealer wins if dealer has 21 and player also has 21
                print("You hold " + str(you) + "for a total of " + str(you.handTotal) + " but dealer also has a blackjack so dealer wins")
                inPlay = False
            else:
                print("You were dealt a blackjack so you win!")    #otherwise, player wins
                inPlay = False
        else:
            if(dealer.handTotal == 21):    #if dealer has 21, and you don't, dealer wins
                print("You hold " + str(you) + "for a total of " + str(you.handTotal) + ", but the dealer was dealt a blackjack so dealer wins")
                inPlay = False
            else: print("You hold " + str(you) + "for a total of " + str(you.handTotal))
    elif (you.hand[0].value == 11 and you.hand[1].value == 11):    #for the rare case of getting dealt 2 aces
        print("Two aces is 22 points, switching an ace from 11 points to 1 point")
        you.numberOfAcesAsEleven -= 1    #subtracts 1 from the number of aces as 11 points
        you.handTotal -= 10
        print("You hold " + str(you) + "for a total of " + str(you.handTotal))
    else:    #if you were not dealt an ace at first
        if(dealer.handTotal == 21):
            print("You hold " + str(you) + "for a total of " + str(you.handTotal) + " but dealer has 21 so dealer wins")
            inPlay = False
        else: print("You hold " + str(you) + "for a total of " + str(you.handTotal))
    while (inPlay):    #loop to go through the hit/stay process
        choice = int(input("1 (hit) or 2 (stay)? "))
        if (choice == 1):
            print("")
            print("Card dealt:", cardDeck.dealOne(you))
            print("New total: ", you.handTotal)
            if (you.handTotal > 21 and you.numberOfAcesAsEleven == 0):
                print("You bust! Dealer Wins")    #no aces and above 21 means you bust
                inPlay = False
            elif (you.handTotal > 21 and you.numberOfAcesAsEleven > 0):
                print("Over 21, switching an ace from 11 points to 1 point")    #above 21 and has aces so swtiches ace from 11 points to 1 point
                you.numberOfAcesAsEleven -= 1
                you.handTotal -= 10
                print("New total:", you.handTotal)
            elif (you.handTotal == 21):
                print("21!")
                inPlay = False
        elif (choice == 2): inPlay = False

#method that lets dealer go next
def dealerTurn(cardDeck, you, dealer):
    inPlay = True
    if (dealer.handTotal == 21 or (you.handTotal == 21 and len(you.hand) == 2)):    #if player and dealer has 21 at first, game ends
        inPlay = False
    elif (you.handTotal > 21):    #if player gets above 21, game ends.
        inPlay = False
    else:  
        print("Dealer's turn now")
        print("Your hand: " + str(you) + "  for a total of " + str(you.handTotal))
        print("Dealer's hand: " + str(dealer) + "  for a total of " + str(dealer.handTotal))
        print("")
        if (dealer.numberOfAcesAsEleven > 0):
            print("Assuming 11 points for the ace the dealer was dealt for now")
            if (dealer.hand[0].value == 11 and dealer.hand[1].value == 11):    #for the rare case of dealer getting two aces dealt at first
                print("Two aces is 22 points, switching an ace from 11 points to 1 point")
                dealer.numberOfAcesAsEleven -= 1
                dealer.handTotal -= 10
                print("Dealer holds " + str(dealer) + "now for a total of " + str(dealer.handTotal))
    while(inPlay):
        if (dealer.handTotal < 21):
            if (dealer.handTotal >= you.handTotal):    #once the dealer gets higher than the player but under 21, dealer wins
                print("Dealer wins!")
                print("")
                inPlay = False
            else:
                print("Dealer hits:", cardDeck.dealOne(dealer))
                print("New total:", dealer.handTotal)
                print("")
                if (dealer.handTotal == 21):    #if dealer gets 21 points, dealer wins
                    print("Dealer got 21! Dealer wins, you lose")
                    print("")
                    inPlay = False
        elif (dealer.handTotal > 21):
            if (dealer.numberOfAcesAsEleven > 0):
                print("Over 21, switching an ace from 11 points to 1 point")    #if dealer has an ace, dealer can switch an ace from 11 points to 1 point
                dealer.numberOfAcesAsEleven -= 1
                dealer.handTotal -= 10
                print("New total:", dealer.handTotal)
                print("")
            else:
                print("Dealer has " + str(dealer.handTotal) + ". Dealer busts! You win")    #if dealer still gets over 21 with ace(s) as 1 point, dealer loses
                print("")
                inPlay = False

def main():

    cardDeck = Deck()
    print("Initial Deck:")
    print(cardDeck, "\n")

    #shuffles deck
    cardDeck.shuffle()
    print("Shuffled Deck:")
    print(cardDeck, "\n")

    #initiates player and dealer and then deals 2 cards to each
    you = Player()
    dealer = Player()
    cardDeck.dealOne(you)
    cardDeck.dealOne(dealer)
    cardDeck.dealOne(you)
    cardDeck.dealOne(dealer)

    print("Deck after dealing two cards to each: ")
    print(cardDeck)
    print("\n")

    #shows face up cards
    print("You show", you.hand[1], "faceup.")
    print("Dealer shows", dealer.hand[1], "faceup.")
    print("")
    print("You go first.")
    print("")
    #player goes first, and then dealer goes
    yourTurn(cardDeck, you, dealer)
    print("")
    dealerTurn(cardDeck, you, dealer)

    #shows end game results
    print("Game Over.")
    print("Final hands:")
    print("    You:    ", you)
    print("    Dealer: ", dealer)
    
main()
