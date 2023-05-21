# Map
# Create your own map function. It should take an iterable and an other function.

def custome_map(iterable, function):
    for item in iterable:
        function(item)

def print_squre(num):
    print(num ** 2)

numbers = [1,2,3,4,5,6,7]

print(custome_map(numbers, print_squre))