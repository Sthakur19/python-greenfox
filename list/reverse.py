# - Create a variable named `numbers`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Reverse the order of the elements of `numbers` programmatically
# - Print the elements of the reversed `numbers`:
#   [7, 6, 5, 4, 3]

numbers = [3, 4, 5, 6, 7]

# reverse_arrey = numbers.reverse()

# print(numbers)

reverse_array = []

for val in numbers:
    print(val)
    reverse_array.insert(0,val)
print(reverse_array)