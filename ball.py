from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.penup()
        self.x_move = 10 
        self.y_move = 10

    def move(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        if y_cor > 270 or y_cor < -270:
            self.bounce_screen()
        self.goto(x_cor + self.x_move, y_cor + self.y_move)
        
    def reset_postion(self):
        self.goto(0,0)
        self.bounce_paddles()

    def bounce_paddles(self):
        self.x_move *= -1 
    
    def bounce_screen(self):
        self.y_move *= -1 