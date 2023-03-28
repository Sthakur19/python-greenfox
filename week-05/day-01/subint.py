# 7 subint
# Create a function that takes a number and a list of numbers as a parameter
# and returns the indeces of the numbers of the list which contain the given number
# or returns an empty list (if the number is not part of any of the numbers in the list)

my_list_1 = []
def subint(my_num, my_list):
    for ix, i in enumerate(my_list):
        if my_num == my_list[ix]:
            my_list_1.append(ix)
        else:
            my_list_1
    return my_list_1

print(subint(5, [6, 7, 8, 5, 6,7,5,6,8,3]))




