# (Game: pick a card )program that simulates picking a card from a deck of 52 cards.
import random
rank = random.randint(1,13)
suite = random.randint(1,4)

if suite == 1:
    suite = "CLUBS"
elif suite == 2:
    suite = "DIAMOND"
elif suite == 3:
    suite = "HEART"
elif suite == 4:
    suite = "SPADES"

if rank == 1:
    rank = "Ace"
elif rank == 11:
    rank = "Jack"
elif rank == 12:
    rank = "Queen"
elif rank == 13:
    rank = "King"

print("The card you picked is the",rank,"of",suite)