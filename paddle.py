from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_cord, y_cord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_cord, y_cord)


    def go_up(self):
        y_cord = self.ycor()
        if y_cord < 240:
            new_y_axis = y_cord + 20
            self.goto(self.xcor(), new_y_axis)

    def go_down(self):
        y_cord = self.ycor()
        if y_cord > -240:
            new_y_axis = self.ycor() - 20
            self.goto(self.xcor(), new_y_axis)
