import turtle
turtle.screensize(1200,1200)
turtle.bgcolor('black')
t5=turtle.Turtle()
move=1


def draw_square(some_turtle):

    for i in range (1,5):
        some_turtle.forward(150)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("orange")
    brad.speed(20)
    brad.pensize(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)

    # t5.speed(0)
    for i in range(10):
        for i in range(4):
            t5.pu()
            t5.goto(1, 5)
            t5.pd()
            t5.color('cyan')
            t5.pensize(2)
            t5.circle(30, steps=4)
            t5.right(100)
    t5.speed(0)
    #center
    for i in range(10):
        for i in range(4):
            t5.pu()
            t5.goto(1, 8)
            t5.pd()
            t5.color('cyan')
            t5.pensize(3)
            t5.circle(30, steps=4)
            t5.right(100)
     #upper
    for i in range(10):
        for i in range(4):
            t5.pu()
            t5.goto(1, 270)
            t5.pd()
            t5.color('cyan')
            t5.pensize(2)
            t5.circle(30, steps=4)
            t5.right(100)
    #         #down
    for i in range(10):
        for i in range(4):
            t5.pu()
            t5.goto(1, -270)
            t5.pd()
            t5.color('cyan')
            t5.pensize(2)
            t5.circle(30, steps=4)
            t5.right(100)
            #left
    for i in range(10):
        for i in range(4):
            t5.pu()
            t5.goto(270, 8)
            t5.pd()
            t5.color('cyan')
            t5.pensize(2)
            t5.circle(30, steps=4)
            t5.right(100)
            #right
    for i in range(10):
        for i in range(4):
            t5.pu()
            t5.goto(-270, 8)
            t5.pd()
            t5.color('cyan')
            t5.pensize(2)
            t5.circle(30, steps=4)
            t5.right(100)
    window.exitonclick()

draw_art()