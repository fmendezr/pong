from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, side, shape: str = "square", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.turtlesize(5, 1)
        self.side = side
        self.penup()

        if self.side == "right":
            self.goto((350,0))
        else: 
            self.goto((-350,0))

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 40)
        
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 40)

    def reset_position(self):
        self.goto(self.xcor(),0)