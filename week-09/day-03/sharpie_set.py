from sharpie import Sharpie

class SharpieSet:
    def __init__(self):
        self.listOfSharpies = []

    def addShrapie(self, sharpie):
        self.listOfSharpies.append(sharpie)

    def count_usable(self):
        count = 0
        for sharpie in self.listOfSharpies:
            if sharpie.ink_amount > 0:
                count += 1
        return count 

    def remove_trash(self):
        self.listOfSharpies = [sharpie for sharpie in self.listOfSharpies if sharpie.ink_amount > 0]

sharpieset= SharpieSet()

sharpieset.addShrapie(Sharpie("red", 7, 10))
sharpieset.addShrapie(Sharpie("blue", 4, 5))
sharpieset.addShrapie(Sharpie("green", 3, 7))
print(f"Number of usable Sharpies: {sharpieset.count_usable()}")

sharpieset.remove_trash()

print(f"Number of usable Sharpies after removing trash: {sharpieset.count_usable()}")


        
