class LivingThing:
    can_talk = "No"
    
class Plant(LivingThing):
    can_talk = "No"
    
class Animal(LivingThing):
    can_fly = "No"
    can_talk = "Yes"

class Dog(Animal):

    def __init__(self):
        self.name = "Fido"


class Cat(Animal):

    name = "Meredith"

    def changeAllNames(self, newName):
        Cat.name = newName

class Bird(Animal):

    can_fly = "Yes"

    def __init__(self, name):
        self.name = name
        self.legs = 2
        self.wings = 2

class Penguin(Bird):

    can_fly = "No"
    
    def __init__(self):
        self.name = ""

def main():

    dog1 = Dog()
    dog2 = Dog()
    dog2.name = "Spot"
    print(dog1.name, dog2.name)

    cat1 = Cat()
    cat2 = Cat()

    cat2.name = "Sylvester"

    cat3 = Cat()
    cat2.changeAllNames("Puddy Tat")
    print(cat1.name, cat2.name, cat3.name)
    
    bird1 = Bird("ass")
    bird2 = Bird("ass")
    bird2.name = "Robin the Boy Wonder"
    bird2.can_fly = "No"
    print(bird1.name, bird2.name, bird1.legs)

    penguin1 = Penguin()
    penguin1.name = "Opus"
    print(penguin1.name, penguin1.can_fly)

main()
