# Even numbers
# Given a list with the following items: 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# Create a new list which contains only the even numbers.

item_list = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

new_list = [i for i in item_list if i % 2 == 0]

print(new_list)