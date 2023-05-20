# All positive
# Given a list with the following items: 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# Determine whether every number is positive or not using all().

item_list = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

new_list = all(i > 0 for i in item_list)
print(new_list)


        
