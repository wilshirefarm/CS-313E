class Person:

    population = 0

    def __init__(self, name):
        self.name = name
        print("(Initializing " + self.name + ")")
        Person.population += 1
        pop = 0

    def greet(self):
        print("Hi, my name is " + self.name)

    def howMany(self):
        if Person.population == 0:
            print("I am the only person here. ")
        else:
            print("We have " + str(Person.population) + " people here.")

    def leave(self):
        Person.population -= 1
        if Person.population == 0:
            print("I was the last one.")
        else:
            print("There are still " + str(Person.population) + " people here.")


def main():
    
    barack = Person("Barack")    
    barack.greet()
    barack.howMany()

    michelle = Person("Michelle")
    michelle.greet()
    michelle.howMany()

    michelle.leave()
    barack.leave()
    barack.leave()

main()
