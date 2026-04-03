import random

print("Welcome to the Number Guessing Game!")
difficulty_level = input("Choose difficulty level: Type 'easy' or 'hard'")

game_number = random.randint(1,100)
print(game_number)



def game_difficulty():
    if difficulty_level == "easy":
        return 10
    else:
        return 5

def game():

    chances=game_difficulty()

    print(f"You have {chances} chances to guess the number.")
    for i in range(chances,0,-1):

        guess = int(input("Make a guess: "))

        if guess == game_number:
            print("You Win")
            return
        elif guess < game_number:
            print("Too Low")
        else:
            print("Too High")

        if i-1 == 0:
            print("You ran out of chances")
            print(f"The Number was {game_number}")
            return
        else:
            print(f"You have {i-1} chances to guess the number.")


game()
