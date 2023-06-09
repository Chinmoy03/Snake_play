from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        with open("highscore.txt", mode="r") as f:
            self.write(f"SCORE {self.score} HIGH SCORE: {int(f.read())}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def reset(self):

        with open("highscore.txt", mode="r") as f:
            high_score = int(f.read())
        if self.score > high_score:
            with open("highscore.txt", mode="w") as f:
                f.write(str(self.score))
        self.score = 0
        self.update()

