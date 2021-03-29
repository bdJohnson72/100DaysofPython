"""
For Day 19 in 100 days of Python
"""

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=520)
user_bet = screen.textinput(title='Make your bet', prompt='Which color turtle will win the race')
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


def setup():
    y_axis = 0
    x_axis = -250
    positive = 30
    negative = -30
    for index, color in enumerate(COLORS):
        turtle = Turtle(shape='turtle')
        turtle.color(color)
        turtle.penup()
        turtles.append(turtle)
        if index == 0:
            turtle.goto(x_axis, y_axis)
        elif index % 2 != 0:
            turtle.goto(x_axis, negative)
            negative -= 30
        else:
            turtle.goto(x_axis, positive)
            positive += 30


def start_race():
    go = True
    while go:
        for turtle in turtles:
            turtle.forward(random.randint(1, 10))
            if turtle.xcor() > 240:
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print("You Won")
                    go = False
                else:
                    print("You lost")
                    go = False


if __name__ == '__main__':
    setup()
    if user_bet:
        start_race()
        screen.exitonclick()
