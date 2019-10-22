from random_words import RandomWords

#How many lives or difficulty setting
print("Welcome to hangman, choose how many lives you wish to have? Choose from 5 - 10. ", end='')
lives = int(input())

#selection of the number of lives for the game
def lives_selection():
    if lives > 10:
        print("That's too many lives, please input again")

    elif lives <= 4:
        print("That's too few lives, please input again")

    else:
        print(f"You've chosen to have {lives} lives for this game.")
        print("Make your first guess! ", end="")

#hangman game chooses word and outputs length
r = RandomWords()
hangman = r.random_word()
split = list(hangman)
found_letters = []
print(split)

def main():
    global count
    count = len(split)
    print(f"There are: {count} letters in this word")


#conditions of the hangman game
def conditions_game():
    global lives, count, split, found_letters

    while True:
        guess = input()
        if lives == 1:
            print("Oh no, hangman wins!")
            break
        elif count == 1:
            print("You've won!")
            break
        elif guess.isdigit():
            print("Error, please insert a letter")
        elif guess.isspace():
            print("Error, please insert a letter")
        elif len(guess) > 1:
            print("Error, please insert one letter at a time")
        elif guess in split:
            print(f"{guess} is in the word!")
            count = count -1
            split.remove(guess)
            found_letters.append(guess)
            print(f"There are {count} more letters to guess!")
        elif guess not in split:
            print(f"{guess} is not in the word...")
            lives = lives -1
            print(f"You have {lives} lives left...")

        else:
            break
main()
lives_selection()
conditions_game()