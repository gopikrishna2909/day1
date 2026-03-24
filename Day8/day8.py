# def greet(name):
#     print(f"Hi {name}")
#     print(f"Good morning {name}")
# greet("Kittu")
from traceback import print_tb

#Function with more than one Input
# def greet(name, location):
#     print(f"Hi {name}")
#     print(f"what is it like in {location}")
# # greet("Vijayawada","Kittu") ---> Positional Argument
# greet(location="Vijayawada", name="Kittu") ----> Keyword Argument
name = input("What is your name:\n")
location = input("what is your location:\n")

def greet():
    print(f"Hi {name}")
    print(f"what is it like in {location}")

greet()