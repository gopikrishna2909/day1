import random

from decorator import append

actors = {"Mahesh":10,
          "NTR":2,
          "RamaCharan":8,
          "Nani":7,
          "PK":1,
          "Sesh":6,
          "Prabhas":9,
          "Venky":5,
          "Chiru":4,
          "Balaya":3
          }

game =[]

score = 0
def start_game():
    global game
    while len(game)!=2:
        name = random.choice(list(actors.keys()))
        if name not in game:
            game.append(name)
    print(game)


def end_game(score_card):
    global game
    restart = True
    while restart:
        start_game()
        user_input = input(f"Type 'A' for {game[0]}\nType 'B' for {game[1]}: ").lower()
        if user_input == "a":
            if actors[game[0]]>actors[game[1]]:
                score_card+=1
                game = [game[0]]
                print(score_card)
            else:
                print("you lost")
                restart =False


        elif user_input == "b":
            if actors[game[1]]>actors[game[0]]:
                score_card += 1
                game = [game[1]]
                print(score_card)
            else:
                print("you lost")
                restart = False





end_game(score)
