import random

#selects a random number for the dice
def dice():
    throw = random.randint(1, 6)
    print(throw)

#defines how many die are cast
def roll():

    print("How many die do you wish to roll? ", end="")
    rolls = int(input())

    for x in range(rolls):
        dice()
    print(f"You've rolled {rolls} die.")

#Asks user whether they want to continue rolling die, or to exit the program
while True:
    roll()
    print("Roll again? Type 'n' to exit or any key to continue")
    again = input()
    if again.lower == 'n':
        break
    else:
        continue 