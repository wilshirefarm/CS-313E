#  File: USFlag.py
#  Description: Draws out the US flag with turtle graphics
#  Student's Name: Wilshire Liu
#  Student's UT EID: WL7583
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: 9/13/16
#  Date Last Modified: 9/15/16

import turtle, math

def main():

    #Method that draws a red stripe
    def drawFilledRectangle(ttl,startx,starty,width,height,fillColor):
        ttl.goto(startx, starty)
        ttl.fillcolor(fillColor)
        ttl.begin_fill()
        ttl.forward(width)
        ttl.left(90)
        ttl.forward(height)
        ttl.left(90)
        ttl.forward(width)
        ttl.left(90)
        ttl.forward(height)
        ttl.end_fill()
        ttl.left(90)

    #Method that draws a white star
    def drawWhiteStar(ttl,radius,startx,starty):
        ttl.penup()
        ttl.pencolor("white")
        ttl.fillcolor("white")
        line = 2 * radius * math.sin(math.radians(72))
        ttl.goto(startx,starty)
        ttl.begin_fill()
        ttl.pendown()
        ttl.left(162)
        ttl.forward(radius)
        ttl.right(162)
        for turns in range(5):
            ttl.forward(line)
            ttl.right(144)
        ttl.end_fill()    

    #Prompts user to enter the height of the flag in pixels
    flagHeight = int(input("Enter the height of the flag in pixels: "))
    flagWidth = 1.9 * flagHeight
    #Creates a turtle called ttl
    ttl = turtle.Turtle()
    #Speeds up turtle a bit
    ttl.speed(10)
    screen = turtle.Screen()
    screen.title("USFlag")
    #Allows for 100 pixels around the sides of the flag
    screen.setup(flagWidth + 200, flagHeight + 200, 0, 0)

    #Draws the outline of the flag
    ttl.penup()
    ttl.goto(-flagWidth/2,-flagHeight/2)
    ttl.pendown()
    ttl.forward(flagWidth)
    ttl.left(90)
    ttl.forward(flagHeight)
    ttl.left(90)
    ttl.forward(flagWidth)
    ttl.left(90)
    ttl.forward(flagHeight)
    ttl.left(90)

    #Uses a loop to draw the 7 red stripes    
    for i in range(0,13,2):
        starty = (-flagHeight/2) + flagHeight*(i/13)
        drawFilledRectangle(ttl,-flagWidth/2,starty,flagWidth,flagHeight/13,"red")

    #Draws the canton
    ttl.goto(-flagWidth/2,flagHeight/2)
    ttl.fillcolor("blue")
    ttl.begin_fill()
    ttl.forward(flagWidth*(2/5))
    ttl.right(90)
    ttl.forward(flagHeight*(7/13))
    ttl.right(90)
    ttl.forward(flagWidth*(2/5))
    ttl.right(90)
    ttl.forward(flagHeight*(7/13))
    ttl.end_fill()
    ttl.right(90)

    #Sets up varibables for the canvas height, width, and radius of the circle a star is inscribed in
    canvasHeight = flagHeight * (7/13)
    canvasWidth = flagWidth * (2/5)
    radius = flagHeight/13 * (4/5) / 2

    #Uses a loop to draw the stars in grid of the canton (I used the specifications off of the Wikipedia page)
    #If the row is odd, it draws the 6 stars; if the row is even, it draws 5 stars
    for i in range(1,10):
        if (i % 2 == 0):
            for l in range(2,11,2):
                startx = -flagWidth/2 + (l/12) * canvasWidth
                starty = flagHeight/2 - (i/10) * canvasHeight
                drawWhiteStar(ttl,radius,startx,starty)
        else:
            for j in range(1,12,2):
                startx = -flagWidth/2 + (j/12) * canvasWidth
                starty = flagHeight/2 - (i/10) * canvasHeight
                drawWhiteStar(ttl,radius,startx,starty)

    #Hides the cursor
    ttl.hideturtle()

main()
