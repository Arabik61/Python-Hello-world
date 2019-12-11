class Bird:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "I am bird, my name is {0}".format(self.name)

    def getName(self):
        return self.name


class Aviary:
    def __init__(self, name, bird):
        self.name = name
        self.bird = bird

    def pushBird(self, bird):
        self.bird = bird

    def showBird(self):
        print(self.bird)


if __name__ == '__main__':
    b1 = Bird("Bird1")
    b2 = Bird("Bird2")
    aviary = Aviary("Aviary for bird", b1)
    aviary.showBird()
    aviary.pushBird(b2)
    aviary.showBird()
