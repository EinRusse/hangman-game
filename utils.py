import requests
import json


def start_game():
    print("Welcome to hangman!")
    right_input = False
    while right_input == False:
        answer = input("Start game?")
        right_input = True if answer == "y" else False


def get_random_word() -> str:
    response = requests.get("https://random-words-api.vercel.app/word")
    return response.json()[0]["word"].lower()


def show_guessed_word(word: str, guessed: list[str], right_words: list[str]):
    i = 0
    result = ""
    while i < len(word):
        if i + 1 == len(word):
            if word[i] in guessed and word[i] in right_words:
                result += "%s" % (word[i])
            else:
                result += "_"
        else:
            if word[i] in guessed and word[i] in right_words:
                result += "%s " % (word[i])
            else:
                result += "_ "
        i += 1
    return result
