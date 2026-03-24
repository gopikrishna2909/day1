import random
from stages import *
from word_list import words

lives = 6
choosen_word = random.choice([word.lower() for word in words])
placeholder = ""
for i in range(len(choosen_word)):
    placeholder += "_"
print("Welcome to the Hangman Game!")
print("The word has", choosen_word)
print("Current progress:", placeholder)
while placeholder != choosen_word:
    print(f'''you have {lives}/6 chances to guess the word''')
    guess = input("Guess a letter: ").lower()

    if guess in placeholder:
        print(f"you already gueesed the letter: {guess}")

    for j,k in enumerate(choosen_word):
        if k==guess:
            placeholder = placeholder[:j] + guess + placeholder[j+1:]

    if guess not in choosen_word:
        lives -= 1
        if lives == 0:

            print(stages[lives])
            print(f"the correct word is {choosen_word}, you loose, game over")
            break
    if placeholder == choosen_word:
        print("you win")
    print("The correct word is :", placeholder)




