import random
import turtle
from turtle import Turtle, Screen



colors = ['red','green','yellow','blue','orange','purple']
y_axis_coordinates = [-70,-40,-10,30,60,90]

screen = Screen()
user_choice = screen.textinput(title='Make a bet', prompt='pick a color of turtle that you think wins: ')
print(user_choice)
all_turtles = []
is_game_on = False

screen.setup(width=500,height=400)
for turtle_index in range(0,6):
    tim = Turtle()
    tim.shape('turtle')
    tim.color(colors[turtle_index])
    tim.penup()
    tim.setposition(-230,y_axis_coordinates[turtle_index])
    all_turtles.append(tim)

if user_choice:
    is_game_on = True

while is_game_on:

    for i in all_turtles:
        if i.xcor()>230:
            is_game_on = False
            winning_color = i.pencolor()
            if user_choice == winning_color:
                print(f"You won, the {winning_color} turtel is the winner")
            else:
                print(f"You lost, the {winning_color} turtel is the winner")
        random_distance = random.randint(0,10)
        i.forward(random_distance)
















screen.exitonclick()