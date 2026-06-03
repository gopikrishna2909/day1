import random
import turtle as t
from turtle import Screen

t.colormode(255)
turtle = t.Turtle()
turtle.shape('turtle')
turtle.color('blue')


# def draw_shape(no_of_sides):
#     angle = 360 / no_of_sides
#     for _ in range(no_of_sides):
#         turtle.forward(100)
#         turtle.left(angle)
#
# for i in range(3,11):
#     draw_shape(i)



# for _ in range(20):
#     turtle.forward(3)
#     turtle.penup()
#     turtle.forward(3)
#     turtle.pendown()

def randomcolor():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r,g,b)

    return colour
turtle.speed("fastest")

def draw(size_of_gap):

    for _ in range(int(360/size_of_gap)):

        turtle.color(randomcolor())
        turtle.circle(80)
        turtle.setheading(turtle.heading() + size_of_gap)

draw(5)


screen = Screen()
screen.exitonclick()

















screen = Screen()
screen.exitonclick()

