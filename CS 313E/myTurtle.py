import turtle

def main():

    ttl = turtle.Turtle()

    screen = turtle.Screen()
    screen.title("Class demo of turtle graphics")

    ttl.speed(10)

    ttl.penup()
    ttl.goto(-250,0)
    ttl.pendown()
    ttl.circle(50)

    ttl.fillcolor("blue")
    ttl.penup()
    ttl.goto(-100,0)
    ttl.pendown()
    ttl.begin_fill()
    ttl.circle(50)
    ttl.end_fill()

    ttl.fillcolor("red")
    ttl.penup()
    ttl.goto(50,0)
    ttl.pendown()
    ttl.begin_fill()
    ttl.circle(50,90)
    ttl.left(90)
    ttl.forward(50)
    ttl.left(90)
    ttl.forward(50)
    ttl.left(90)
    ttl.end_fill()

    ttl.fillcolor("green")
    ttl.penup()
    ttl.goto(200,0)
    ttl.pendown()
    ttl.begin_fill()
    ttl.circle(50,steps=4)
    ttl.end_fill()


main()
