import turtle, math

def main():

    hi = turtle.Turtle()

    screen = turtle.Screen()
    screen.title("Turtle Graphics Test Program")
    screen.setup(700,700,0,0)
    screen.bgcolor("blue")
    radius = 100

    hi.pencolor("white")
    hi.fillcolor("white")
    #hi.begin_fill()
    line = 2 * radius * math.sin(math.radians(72))
    hi.goto(0,0)
    hi.left(162)
    hi.forward(radius)
    hi.right(162)
    for turns in range(5):
        hi.forward(line)
        hi.right(144)
    #hi.end_fill()
    hi.pendown()
    #hi.ht()
    
    print(math.sin(72))

main()
