class Animal:
    def __init__(self):
        self.hunger = 50
        self.thirst = 50

    def eat(self):
        self.hunger -= 1

    def drink(self):
        self.drink -= 1

    def play(self):
        self.hunger -= 1
        self.drink -= 1 