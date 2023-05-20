# Average of odd numbers
# Given a list with the following items: 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# Calculate the average of the odd numbers.

item_list = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

odd_numer = [i for i in item_list if i % 2 == 0]

average = sum(odd_numer)/len(odd_numer)
print(average)