from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(x=x_cor,y=y_cor)
        self.shapesize(stretch_wid=5,stretch_len=1)


    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)




