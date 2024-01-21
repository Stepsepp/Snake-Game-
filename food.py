from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        #Konstruktor, määrab toidu omadused alguses
        super().__init__()
        self.shape("circle")  #Toidu kuju on ring
        self.penup()  #mitte jätta joont
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Muudab ringi kuju, et oleks nähtavam
        self.color("Yellow")  # Toidu värv on kollane
        self.speed("fastest")  # Seab toidu liikumiskiiruse kiireimaks
        self.refresh()  # Kutsub välja meetodi toidu asukoha värskendamiseks

    def refresh(self):
        # Värskendab toidu asukohta uue suvalise asukohaga
        random_x = random.randint(-280, 280)  # Suvaline x-koordinaat vahemikus [-280, 280]
        random_y = random.randint(-280, 280)  # Suvaline y-koordinaat vahemikus [-280, 280]
        self.goto(random_x, random_y)  # Liigutab toitu uude suvalisse asukohta
