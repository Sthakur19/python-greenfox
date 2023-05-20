class Sharpie:
    def __init__(self, color, width):
        self.color = color
        self.width = width
        self.ink_amount = 100

    def use(self):
        self.ink_amount -= 10

    def print_my_color(self):
        print(f"Print my color {self.color} and its width {self.width} and its ink amount {self.ink_amount}")

red_sharpie = Sharpie("red", 5) 
red_sharpie.use() 
red_sharpie.print_my_color()
