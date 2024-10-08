from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score=0
        self.color("white")
        self.goto(x=0,y=270)
        self.update_scoreboard()

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}",align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center",font=FONT)