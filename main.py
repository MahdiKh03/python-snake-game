from turtle import Screen
from snake import Snake
from time import sleep
from food import Food
from scoreboard import ScoreBoard


snake = None
food = None
scoreboard = None

screen = Screen()

def reset_game():
    global snake, food, scoreboard

    screen.clear()
    screen.setup(600, 600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    screen.listen()

    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

    game_loop()

def game_loop():
    global snake, food, scoreboard

    not_over = True

    while not_over:
        screen.update()
        sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.add_score()

        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            not_over = False

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                not_over = False

    scoreboard.game_over()
    screen.listen()
    screen.onkey(reset_game, "Return")

reset_game()

screen.exitonclick()