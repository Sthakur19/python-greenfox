# - Create an array variable named `orders`
#   with the following content: `["first", "second", "third"]`
# - Swap the first and the third element of `orders` programmatically
# - Print the swapped array into the console:
#   [third, second, first]

orders = ["first", "second", "third"]

temp = orders[0]

orders[0] = orders[2]
orders[2] = temp

print(orders)
