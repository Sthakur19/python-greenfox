class Counter:
    def __init__(self, counter=0):
        self.counter = counter
        self.initial_value = counter

    def add(self, number=1):
        self.counter += number 
        print("Check", self.counter)

    def get(self):
        return self.counter

    def reset(self):
        self.counter = self.initial_value

counter1 = Counter()
counter2 = Counter(10)

counter1.add()
counter2.add(5)

print(counter1.get())
print(counter2.get())

counter1.reset()
counter2.reset()
print(counter1.get()) 
print(counter2.get())  