from turtle import Turtle

# Alguspositsioonid ja muud konstandid
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        # Konstruktor, initsialiseerib mao ja määrab selle pea
        self.segments = []  # Mao segmendid
        self.create_snake()  # Kutsub välja meetodi mao loomiseks
        self.head = self.segments[0]  # Mao pea

    def create_snake(self):
        # Meetod loob mao algusasendisse
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # Lisab mao segmendi
        new_segment = Turtle("square")  # Mao segment on ruut
        new_segment.color("white")  # Segment on valge värviga
        new_segment.penup()  # et mitte jätta joont mao liikumisel
        new_segment.goto(position)  # Liigutab segmendi antud asukohta
        self.segments.append(new_segment)  # Lisab segmendi mao segmendiloendisse

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def extend(self):
        # Suurendab mao pikkust lisades uue segmendi viimasele segmendile
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Liigutab mao segmendid edasi, et simuleerida liikumist
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)  # Liigutab mao pea edasi

    def up(self):
        # Liigutab mao üles, kui see ei liigu allapoole
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Liigutab mao allapoole, kui see ei liigu üles
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Liigutab mao vasakule, kui see ei liigu paremale
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Liigutab mao paremale, kui see ei liigu vasakule
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
