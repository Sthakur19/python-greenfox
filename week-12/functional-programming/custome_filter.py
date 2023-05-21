# Filter
# Create your own filter function. It should take an iterable and an other function.


def custome_filter(iterable, function):
    filtered_list = []
    for item in iterable:
        if function(item):
            filtered_list.append(item)
    return filtered_list

def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_number = custome_filter(numbers, is_even)
print(filtered_number)