from turtle import Turtle
from line_middle import LineMiddle

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        self.left_score = 0
        self.right_score = 0

        self.hideturtle()
        self.penup()
        self.color("white")
        self.write_score()
        self.line_middle = LineMiddle()
        
    def write_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 60, "normal"))

    def increment_score(self, side):
        if side == "right":
            self.right_score += 1 
        else:
            self.left_score += 1
        self.write_score()

    def winner(self):
        self.goto(0,0)
        if self.left_score == 11:
            self.write("Left Player Won", align="center", font=("Courier", 60, "normal"))
            return True
        elif self.right_score == 11:
            self.write("Right Player Won", align="center", font=("Courier", 60, "normal"))
            return True
        return False