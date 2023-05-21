# Contains even numbers
# Given a list with the following items: 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# Determine whether it contains even numbers or not using any().

item_list = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

new_item = any(i % 2 == 0 for i in item_list)

print(new_item)