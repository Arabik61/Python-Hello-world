# Принцип S - виношу функцію поміщення у вольєр з класу BIrd
# Принцип О - в класах Duck, Parrot i Penguin реалізована функція voice,
#           які унаслідуються від класів FlyingBird i NonflyingBird
# Принцип L - розділяю клас Bird на два: FlyingBird i NonflyingBird,
#           щоб у класі Bird не знаходилася функція fly(), яка не буде в класі Penguin,
#           що порушує логіку
# Принцип I - кожен клас працює з тими функціями, які їм потрібні,
#           тобто в NonflyingBird нема функції fly()
# Принцип D - в клас вольєр будуть передавати об'єкти класів Duck, Penguin i Parrot
#           хоча сам клас вольєр приймає обєкт типу Bird


class FlyingBird:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def voice(self):
        pass

    def fly(self):
        pass


class NonflyingBird:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def voice(self):
        pass


class Duck(NonflyingBird):
    def voice(self):
        print("I am duck")


class Parrot(FlyingBird):
    def voice(self):
        print("I am parrot")


class Penguin(NonflyingBird):
    def voice(self):
        print("I am penguin")


class Aviary:
    def __init__(self):
        self.birds = []

    def pushBird(self, bird):
        self.birds.append(bird)

    def popBird(self, bird):
        self.birds.remove(bird)


if __name__ == '__main__':
    parrot = Parrot("parrot1")
    duck = Duck("duck2")
    penguin = Penguin("penguin3")
    aviary = Aviary()
    arr = [penguin, duck, parrot]
    for x in arr:
        x.voice()

    for x in arr:
        aviary.pushBird(x)
