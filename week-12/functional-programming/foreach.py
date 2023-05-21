# Foreach
# Create a function called foreach which can take an iterable and an other function. 
# Apply the function for all the elements in the iterable.

def custome_foreach(iterable, function):
    for item in iterable:
        function(item)

def print_squre(num):
    print(num ** 2)

numbers = [1,2,3,4,5,6,7]

custome_foreach(numbers, print_squre)