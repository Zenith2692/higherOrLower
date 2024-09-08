# HigherOrLower

import random

# Card constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9','10', 'Jack', 'Queen', 'King')

NCARDS = 8

# Pass in the deck and this function returns a random card from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop() # Pop one off the top of the deck and return
    return thisCard

# Pass in a deck and this function returns a shuffled copy of the deck
def shuffle(deckListIn):
    deckListOut = deckListIn.copy() # Make a copy of the starting deck
    random.shuffle(deckListOut)
    return deckListOut

# Main code
print("Welcome to Higher or Lower")
print("You have to choose whether or not the next card will be higher or lower"
      "than the current card.")
print("Getting it right adds 20 points, while getting it wrong subtracts 15 points.")
print("You have 50 points to start off with.")
print()

startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True:
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardSuit = currentCardDict['suit']
    currentCardValue = currentCardDict['value']
    print("starting card is: " + currentCardRank + " of " + currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS):
        answer = input("Will the next card be higher or lower than the " + currentCardRank + " of " + currentCardSuit +
                       "? (enter h or l): ")
        answer = answer.casefold() # Force lower case
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print("The next card is " + nextCardRank + " of " + nextCardSuit)

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print("You've got it right, it was higher.")
                score = score + 20
            else:
                print("Sorry, it was not higher.")
                score = score - 15

        elif answer == 'l':
            if nextCardValue < currentCardValue:
                print("You've got it right, it was lower")
                score = score + 20
            else:
                print("Sorry, it was not lower.")
                score = score - 15

        print("Your score is: ", score)
        print()
        currentCardValue = nextCardValue
        currentCardSuit = nextCardSuit
        currentCardRank = nextCardRank

    goAgain = input("To play again press ENTER, or 'q' to quit: ")
    if goAgain == 'q':
        break

print("OK bye")