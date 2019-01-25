import random

def coin_flip():
    flip = random.randint(0,2)
    if flip == 0:
        return "HEAD"
    else:
        return "TAIL"

#MAIN

player1 = []
player2 = []

while True:

    ask = input("Player 1: Head or tails? h/t:")
    flip = coin_flip()

    if ask.upper()[0] == "H" and flip == "HEAD":
        player1.append(1)
        player2.append(0)
        print("player 1 is correct")
    elif ask.upper()[0] == "T" and flip == "TAIL":
        player1.append(1)
        player2.append(0)
        print("player 1 is correct")
    else:
        player1.append(0)
        player2.append(1)
        print("player2 is correct")

    again = input("Again? Y/N:")
    if again.upper()[0] == "Y":
        continue
    else:
        print(f"player1 score board:\n{player1}")
        print(f"player2 score board:\n{player2}")
        player1 = []
        player2 = []
        break
