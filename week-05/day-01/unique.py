# # 8 unique
# Create a function that takes a list of numbers as a parameter
# and returns a list of numbers where every number is unique (occurs only once)

# def unique(arr):
#     pass

# #  Example
# print(find_unique_items([1, 11, 34, 11, 52, 61, 1, 34]))
# should print: `[1, 11, 34, 52, 61]`



def find_unique(nums_list):
    result = []
    for i in nums_list:
        if i not in result:
            result.append(i)
    return result

print(find_unique([1, 11, 34, 11, 52, 61, 1, 34]))