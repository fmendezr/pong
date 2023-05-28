from turtle import Screen
from time import sleep
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

class PongGame():
    def __init__(self):

        self.game_finished = False
        self.sleep_time = 0.1

        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Pong")
        self.screen.tracer(0)

        self.scoreboard = Scoreboard()

        self.right_paddle = Paddle("right")
        self.left_paddle = Paddle("left")

        self.screen.listen()
        self.screen.onkey(self.right_paddle.move_up, "Up")
        self.screen.onkey(self.right_paddle.move_down, "Down")
        self.screen.onkey(self.left_paddle.move_up, "w")
        self.screen.onkey(self.left_paddle.move_down, "s")

        self.ball = Ball()

        self.main_loop()

        self.screen.exitonclick()

    def handle_game_over(self):
        x_cor_ball = self.ball.xcor()
        if x_cor_ball >= 390:
            self.scoreboard.increment_score("left")
            self.ball.reset_postion() 
            self.left_paddle.reset_position()
            self.right_paddle.reset_position()
            self.sleep_time = 0.1
        elif x_cor_ball <= -390:
            self.scoreboard.increment_score("right")
            self.ball.reset_postion()  
            self.left_paddle.reset_position()
            self.right_paddle.reset_position()
            self.sleep_time = 0.1
        self.game_finished = self.scoreboard.winner()
        

    def main_loop(self):
        while not self.game_finished: 
            x_cor_ball = self.ball.xcor()
            y_cor_ball = self.ball.ycor()
            sleep(self.sleep_time)
            self.screen.update()
            if x_cor_ball == 330 and abs(y_cor_ball - self.right_paddle.ycor()) <= 50:
                self.ball.bounce_paddles()
                self.sleep_time *= 0.8
            if x_cor_ball == -330 and abs(y_cor_ball - self.left_paddle.ycor()) <= 50:
                self.ball.bounce_paddles()
                self.sleep_time *= 0.8
            self.handle_game_over()
            self.ball.move()