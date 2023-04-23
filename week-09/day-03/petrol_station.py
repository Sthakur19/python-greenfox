class Station:
    def __init(self, gas_amount):
        self.gas_amount = gas_amount

    def refill(self, car):
        self.gas_amount = car.capacity - car.gas_amount
        car.gas_amount = car.capacity


class Car:    
    def __init__(self):
        self.gas_amount = 0
        self.capacity = 100


station = Station(50)
car = Car()

print(f"Initial gas amount of the car: {car.gas_amount}")

station.refill(car)

print(f"Final gas amount of the car: {car.gas_amount}")
print(f"Gas amount of the station: {station.gas_amount}")