from turtle import Turtle
ALIGNMENT="center"
FONT=("arial",24,"normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.write(f"Score = {self.score}",align=ALIGNMENT,font=FONT)
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.write(f"Score = {self.score}",align=ALIGNMENT,font=FONT)
    def increase_score(self):
        #self.clear()
        self.score+=1
        self.clear()
        self.write(f"Score = {self.score}",align=ALIGNMENT,font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("Game over",align="center",font=FONT)

