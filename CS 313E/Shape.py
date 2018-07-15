class Shape:

    description = "Quadrilateral for now"
    author = "Wilshire"

    def __init__(self, length, width):
        self.x = length
        self.y = width
        print(self.x, self.y)

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * (self.x + self.y)

class Square(Shape):

    def __init__(self,side):
        self.x = side
        self.y = side
    
def main():

    print("Create myRectangle")
    myRectangle = Shape(100, 50)
    print("Area is:", myRectangle.area())
    print("Perimeter is:", myRectangle.perimeter())

    print("Create myRectangle")
    myRectangle2 = Shape(25, 85)
    print("Area is:", myRectangle2.area())
    print("Perimeter is:", myRectangle2.perimeter())

    print(myRectangle.description)
    Shape.description = "Easy rectangles"
    print(myRectangle.description)
    print(myRectangle2.description)

    mySquare = Square(10)
    mySquare.description = "I'm a square"
    print(mySquare.area())
    print(mySquare.perimeter())
    print(mySquare.description)

    mySquare2 = Square(15)
    print(mySquare2.description)

main()
