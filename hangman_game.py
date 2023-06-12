import json
import random

with open("text.json", "r") as f:
    try:
        file = f.read()
        file_dict = json.loads(file)
    except Exception as e:
        print(f"Error: {e}")

lifes = file_dict['life']
rand_word = random.choice(file_dict['words'])
letters = []

print("You need to guess the word letter by letter. You have 10 lifes, Have fun!")

while lifes > 0:
    word = ""
    for letter in rand_word:
        if letter in letters:
            word += letter
        else:
            word += "-"
    print(f"Word: {word}")
    print(f"Lifes: {lifes}")

    answer = input("Guess letter> ")
    letters.append(answer)

    if answer in rand_word:
        print("Correct!")
    else:
        print("Wrong!")
        lifes -= 1

    if all(letter in letters for letter in rand_word):
        print(f"Congrats!! The word you guessed is: {rand_word}")
        print(rand_word)
        break

    if lifes == 0:
        print(f"You lost! The word was: {rand_word}")