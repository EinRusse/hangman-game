import requests
from utils import start_game, get_random_word, show_guessed_word


start_game()

random_word = get_random_word()

guessed_letters = set()
unique_letters = set(random_word)
lives = 5

while lives > 0:
    guessed_word = show_guessed_word(random_word, guessed_letters, unique_letters)
    guess = input("Guess a letter!\n%s\n\nLives: %s\n-> " % (guessed_word, lives))
    if len(guess) > 1 or len(guess) == 0:
        print("Wrong input!")
    elif guess.lower() in unique_letters:
        guessed_letters.add(guess.lower())
        if len(unique_letters.intersection(guessed_letters)) == len(unique_letters):
            print("You've guessed! its %s!" % (random_word))
            break
    else:
        lives -= 1

if len(unique_letters.intersection(guessed_letters)) < len(unique_letters):
    print("You lose! its %s!" % (random_word))
