# Squared above 20
# Given a list with the following items: 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14

# Create a new list which contains the numbers if their squared value is above 20.

given_list = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

new_list = [i for i in given_list if i ** 2 > 20]

print(new_list)