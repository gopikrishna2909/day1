# from turtle import Turtle,Screen
#
# kitty = Turtle()
# kitty.pencolor('blue')
# kitty.shape('turtle')
# for _ in range(4):
#     kitty.forward(100)
#     kitty.left(90)
#
#
#
#
# my_screen = Screen()
# my_screen.exitonclick()






class User:
    def __init__(self,userid,username):
        self.userid = userid
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1




user1 = User("001","Gopi")
user2 = User("002","Kittu")

user1.follow(user2)

print(user1.following)
print(user1.followers)
print(user2.followers)
print(user2.following)

