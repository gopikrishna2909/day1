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

    for j,k in enumerate(choosen_word):
        if k==guess:
            placeholder = placeholder[:j] + guess + placeholder[j+1:]

    if guess not in choosen_word:
        lives -= 1
        if lives == 0:

            print(stages[lives])
            print("game over")
            break
    elif k in choosen_word:
        print(f"you already gueesed the letter: {guess}")
    print("Current progress:", placeholder)
    print(stages[lives])



