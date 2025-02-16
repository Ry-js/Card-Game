import time
import random
import math

print("Welcome to the game! Start off with some money and put in a bet. If you pull a basic card, you lose your bet. However, if you draw any of the face cards (or the Ace) then you gain money! The table is as follows:")
time.sleep(1.5)
print("Ace = 2.5x bet")
time.sleep(1.5)
print("King = 2x bet")
time.sleep(1.5)
print("Queen = 1.5x bet")
time.sleep(1.5)
print("Jack = 1.25x bet")
time.sleep(1.5)
print("Best of luck!")
time.sleep(2.5)

cards = []

def CardReset():
    cards.clear()
    ib = 0
    ia = 0
    ik = 0
    iq = 0
    ij = 0
    while ib < 36:
        cards.append('BasicCard')
        ib += 1
    while ia < 4:
        cards.append('Ace')
        ia += 1
    while ik < 4:
        cards.append('King')
        ik += 1
    while iq < 4:
        cards.append('Queen')
        iq += 1
    while ij < 4:
        cards.append('Jack')
        ij += 1

CardReset()

cash = float(100)
print("You have", cash, "dollars.")

while True:
    bet = input("Enter cash bet for the next round: ") 
    if float(bet) <= cash and float(bet) > 0:
# begin play
           print("Good luck!")
           time.sleep(0.5)
           print("You drew...")
           CardDrawn = str(random.choice(cards))
           time.sleep(random.randint(1,5))
           if CardDrawn == 'Ace':
            print("Ace!")
            cash = cash + (float(bet) * 2.5)
            cards.remove('Ace')
           elif CardDrawn == 'King':
            print("King!")
            cash = cash + (float(bet) * 2)
            cards.remove('King')
           elif CardDrawn == 'Queen':
            print("Queen!")
            cash = cash + (float(bet) * 1.5)
            cards.remove('Queen')
           elif CardDrawn == 'Jack':
            print("Jack!")
            cash = cash + (float(bet) * 1.25)
            cards.remove('Jack')
           else:
            print("Basic card...")
            cash = cash - float(bet)
            cards.remove('BasicCard')
    else:
        print("Entered bet is invalid! Enter a valid bet.")
        time.sleep(1)
        continue
    if cash <= 0:
        bankruptprompt = input("You went bankrupt! You want to try again? (Y/N): ")
        if str.casefold(bankruptprompt) == "y":
            continue
        else:
            break
    askagain = input("Play again? You currently have " + str(cash) + " dollars (Y/N): ")
    if str.casefold(askagain) == "y":
       cash = float(cash)
       continue
    if int(cards.count('BasicCard') + cards.count('Ace') + cards.count('King') + cards.count('Queen') + cards.count('Jack')) <= 2:
        print("2 or less cards remain in the deck! Reshuffling and adding all cards back...")
        CardReset()
        continue
    else:
        print("You finished with " + str(cash) + " dollars!")
        break