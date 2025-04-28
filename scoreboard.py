from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.write(f"Score : {self.score}", move=False, align="center", font=("Autumn", 18, "normal"))
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over.", move=False, align="center", font=("Autumn", 25, "normal"))
        self.goto(0, -50)
        self.write("Press Enter to restart.", move=False, align="center", font=("Autumn", 15, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", move=False, align="center", font=("Autumn", 18, "normal"))