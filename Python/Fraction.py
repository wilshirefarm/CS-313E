class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + " / " + str(self.den)

    def __add__(self, otherFrac):
        newnum = (self.num * otherFrac.den) + (otherFrac.num * self.den)
        newden = self.den * otherFrac.den
        return Fraction(newnum, newden)

def addFrac(f1,f2):
    newNum = f1.den*f2.num + f2.den*f1.num
    newDen = f1.den * f2.den
    newFrac = Fraction(newNum,newDen)
    return(newFrac)

def main():

    threeFourths = Fraction(3, 4)
    oneThird = Fraction(1, 3)

    total = threeFourths + oneThird
    print("total= " + str(total))

    newFrac = addFrac(threeFourths, oneThird)
    print("total= " + str(newFrac))

main()
