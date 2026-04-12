import random

from game_data import data



game_list = []
score = 0



def game():
    global game_list

    while len(game_list)!=2:
        name = random.choice(data)
        if name not in game_list:
            game_list.append(name)

    print(f"Compare A: {game_list[0]['name']} a {game_list[0]['description']}, from {game_list[0]['country']}\n\nAgainst B: {game_list[1]['name']} a {game_list[1]['description']}, from {game_list[1]['country']}")






def compare(score_card):
    global game_list
    game_over = True
    while game_over:
        game()
        user_input = input("Who has more followers? Type 'A' or 'B'").lower()
        if user_input == "a":
            if game_list[0]["follower_count"]>game_list[1]["follower_count"]:
                score_card += 1
                game_list = [game_list[1]]
                print(f"Your right! current score: {score_card}")
            else:
                print(f"Your wrong! current score: {score_card}")
                return
        elif user_input == "b":
            if game_list[1]["follower_count"]>game_list[0]["follower_count"]:
                score_card += 1
                game_list = [game_list[1]]
                print(f"Your right! current score: {score_card}")
            else:
                print(f"Your wrong! current score: {score_card}")
                return



compare(score)
print(game_list)