# Sum of numbers
# Given a list with the following items: 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# Calculate the sum of the even numbers which are below or equal to 10.

numbers = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

result = sum(num for num in numbers if num <= 10 and num % 2 == 0)

print(result)