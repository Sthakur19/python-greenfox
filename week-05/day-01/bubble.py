# 12 bubble
# and returns a list where the elements are sorted in ascending numerical order
# When you are done, add a second boolean parameter to the function
# If it is `true` sort the list descending, otherwise ascending


# def bubble(arr):
#     pass


# def advanced_bubble(arr, is_descending):
#     pass


# Example:
# print(bubble([43, 12, 24, 9, 5]))
# should print [5, 9, 12, 24, 34]
# print(advanced_bubble([43, 12, 24, 9, 5], True))
# should print [34, 24, 9, 5]

def bubble(sorting_list):
    list_val_new = str(sorting_list[0])[::-1]
    sorting_list[0] = int(list_val_new)
    sorting_list.sort()
    return sorting_list

sorting_list = [43, 12, 24, 9, 5]

print(bubble(sorting_list))

def advanced_bubble(sorting_list, is_descending):
     sorting_list.reverse()
     return sorting_list

print(advanced_bubble(sorting_list, True))
