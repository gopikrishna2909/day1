import random
import turtle
from turtle import RawTurtle

# import colorgram
# from colorgram import Color
#
# colors = colorgram.extract('download.jpg',50)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)


t = turtle.Turtle
turtle.colormode(255)


colours = [(247, 240, 230), (234, 240, 246), (237, 247, 243), (248, 237, 242), (151, 168, 183), (198, 165, 136), (192, 149, 158), (18, 28, 41), (152, 175, 166), (69, 98, 118), (128, 77, 69), (132, 72, 81), (64, 19, 27), (225, 210, 131), (22, 39, 32), (51, 25, 19), (120, 31, 43), (70, 105, 94), (220, 173, 179), (174, 100, 111), (222, 178, 172), (181, 188, 209), (120, 35, 31), (31, 82, 67), (179, 103, 93), (120, 123, 144), (162, 201, 211), (177, 199, 196), (51, 58, 83), (189, 168, 49), (33, 76, 87), (66, 65, 53), (63, 149, 186), (107, 138, 123)]

t.dot(20,random.choice(colours))



screen = turtle.Screen()
screen.exitonclick()








