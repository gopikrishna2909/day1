import random
from operator import index
from tokenize import blank_re

cards = [11,2,3,4,5,6,7,8,9,10,10,10]
player = []
computer = []
for _ in range(2):
    player.append(random.choice(cards))
    computer.append(random.choice(cards))



def game():
    player_score = sum(player)
    computer_score = sum(computer)
    print(f"Player Card {player} and Score :{player_score}\nComputer card {computer[0]}")
    black_jack1 = [11,10]
    black_jack2 = [10,11]
    if player == black_jack1 or player == black_jack2:
        print(f"Player wins player cards {player} and player score: {player_score} and computer card {computer} computer score: {computer_score}")
    elif computer == black_jack1 or computer == black_jack2:
        print(f"You loose player cards {player} and player score: {player_score} and computer card {computer} computer score: {computer_score}")
    elif player_score>21:
        if cards[0] in player:
            ace_index = player.index(cards[0])
            player[ace_index] = 1
            player_score = sum(player)
            if player_score>21:
                print(f"you Loose player cards {player} and player score: {player_score} and computer card {computer} computer score: {computer_score}")
            else:
                player_choice = input("Do you want another card? y or n: ")
                if player_choice == "y":
                    player.append(random.choice(cards))
                    print(player)
                    game()
                else:
                    computer_score = sum(computer)
                    while computer_score < 16:
                        computer_score = sum(computer)
                        computer.append(random.choice(cards))
                    if computer_score > 21:
                        print(
                            f"you win player cards {player} and player score: {player_score} and computer card {computer} computer score: {computer_score}")
                    else:
                        if player_score > computer_score:
                            print(
                                f"you win player cards {player} and player score: {player_score} and computer card {computer} computer score: {computer_score}")
                        elif player_score == computer_score:
                            print(
                                f"Draw player cards {player} and player score: {player_score} and computer card {computer} computer score: {computer_score}")
                        else:
                            print(
                                f"You loose player cards {player} and player score: {player_score} and computer card {computer} computer score: {computer_score}")




        else:
            print(f"You Loose player cards {player} and player score: {player_score} and computer card {computer} computer score: {computer_score}")
    else:
        player_choice = input("Do you want another card? y or n: ")
        if player_choice == "y":
            player.append(random.choice(cards))
            print(player)
            game()
        else:
            computer_score = sum(computer)
            while computer_score<16:

                computer.append(random.choice(cards))
                computer_score = sum(computer)
            if computer_score>21 :
                print(f"you win player cards {player} and player score: {player_score} and computer card {computer} computer score: {computer_score}")
            else:
                if player_score>computer_score:
                    print(f"you win player cards {player} and player score: {player_score} and computer card {computer} computer score: {computer_score}")
                elif player_score == computer_score:
                    print(f"Draw player cards {player} and player score: {player_score} and computer card {computer} computer score: {computer_score}")
                else:
                    print(f"You loose player cards {player} and player score: {player_score} and computer card {computer} computer score: {computer_score}")

game()