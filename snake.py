import turtle
import time

s = turtle.Screen()
s.bgcolor("black")
s.title("Snake")

snake_movement = False

def draw_walls():
    north_wall = turtle.Turtle()
    east_wall = turtle.Turtle()
    south_wall = turtle.Turtle()
    west_wall = turtle.Turtle()

    north_wall.color("green")
    east_wall.color("green")
    south_wall.color("green")
    west_wall.color("green")

    north_wall.shape("square")
    east_wall.shape("square")
    south_wall.shape("square")
    west_wall.shape("square")

    north_wall.penup()
    east_wall.penup()
    south_wall.penup()
    west_wall.penup()

    north_wall.goto(0, 315)
    east_wall.goto(315, 0)
    south_wall.goto(0, -315)
    west_wall.goto(-315, 0)

    north_wall.shapesize(1.5, 300, 1)
    east_wall.shapesize(300, 1.5, 1)
    south_wall.shapesize(1.5, 300, 1)
    west_wall.shapesize(300, 1.5, 1)



snake_head = turtle.Turtle()
snake_head.shape("square")
snake_head.color("green")
snake_head.shapesize(.5, .5, .5)
snake_head.penup()
snake_head.forward(10)


def up():
    snake_head.setheading(90)





def down():
    snake_head.setheading(270)

 


def left():
    snake_head.setheading(180)


def right():
    snake_head.setheading(0)
    while snake_movement:
        snake_head.forward(1)
        time.sleep(.01)

def start():
    global snake_movement
    print("start")
    snake_movement = True
    moving()


draw_walls()
s.listen()

s.onkey(start, "Return")


def moving():
    while snake_movement:
        snake_head.forward(1)
        time.sleep(.01)
        print("snake moving")
        s.onkey(up, "Up")
        s.onkey(left, "Left")
        s.onkey(down, "Down")
        s.onkey(right, "Right")

s.mainloop()
