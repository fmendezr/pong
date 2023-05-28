from turtle import Turtle

class LineMiddle(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        self.hideturtle()
        self.goto(0, 300)
        
        for x in range(300, -300, -15):
            self.goto(0, x)
            self.dot(5, "white")