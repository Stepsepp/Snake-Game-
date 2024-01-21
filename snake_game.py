from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# Ekraani seadistamine
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Keelab automaatse ekraani värskendamise, et parandada animatsiooni

# Initsialiseerime mängu objektid
snake = Snake()
food = Food()
scoreboard = Scoreboard()



# Noolte kuulamine ja vastavad funktsioonid
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # Värskendab ekraani
    time.sleep(0.1)
    snake.move()  # Kutsub välja madu liigutava funktsiooni

    # Toit ja mao kokkupõrge
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Kontroll, kas madu kokkupõrkas seinaga
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280or snake.head.ycor() < -280):
        scoreboard.reset()
        snake.reset()


    # Kontroll, kas madu kokkupõrkas oma sabaga
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# Kui mäng on lõppenud, ootame kasutajalt sulgemiskäsku
screen.exitonclick()
