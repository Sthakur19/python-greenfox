class Product:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount
    
    def GetDiscount(self):
        oldPrice = self.price
        newPrice = self.price * (100 - self.discount) / 100
        return(self.name, oldPrice, newPrice)


product1 = Product("Mobile", 1000, 20)

print(product1.GetDiscount())