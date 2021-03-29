from turtle import Turtle, Screen


turtle = Turtle()
screen = Screen()

def forwards():
    turtle.forward(10)

def backwards():
    turtle.back(10)

def clockwise():
    turtle.right(10)

def counter_clockwise():
    turtle.left(10)

def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()
screen.onkey(key='w', fun=forwards)
screen.onkey(key='s', fun=backwards)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='a', fun=counter_clockwise)
screen.onkey(key='c', fun=clear_screen)
screen.exitonclick()