from turtle import Turtle

# Konstandid
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        # Klassi konstruktor
        super().__init__()
        self.score = 0  # Algseisuga skoor on 0
        with open("data.txt") as data:
            self.high_score =  int(data.read())
        self.color("white")  # Skoori teksti värv on valge
        self.penup()  # Eemaldab joone mis tekib ussi liikumisel
        self.goto(0, 270)  # Liigutab kursori ülemisse paremasse nurka
        self.update_scoreboard()  # Kutsub välja skoori uuendamise meetodi
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)  # Kuvab algseisu skoori
        self.hideturtle()

    def update_scoreboard(self):
        #Uuendab skoori
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
         #Kuvab mängu lõpu sõnumi
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        #Suurendab skoori ja uuendab ekraanil
        self.score += 1
        self.clear()  # Puhastab eelneva skoori
        self.update_scoreboard()  # Kutsub välja uuendatud skoori
