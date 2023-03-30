# # List introduction 1

# We are going to play with lists. Feel free to use the built-in methods where
# possible.

# - Create an empty list which will contain names (strings)
# - Print out the number of elements in the list
# - Add "William" to the list
# - Print out whether the list is empty or not
# - Add "John" to the list
# - Add "Amanda" to the list
# - Print out the number of elements in the list
# - Print out the 3rd element
# - Iterate through the list and print out each name
#   ```text
#   William
#   John
#   Amanda
#   ```
# - Iterate through the list and print
#   ```text
#   1. William
#   2. John
#   3. Amanda
#   ```
# - Remove the 2nd element
# - Iterate through the list in a reversed order and print out each name
#   ```text
#   Amanda
#   William
#   ```
# - Remove all elements
# - Print out the number of elements in the list

# The full output of your `main` method should be the following:

# ```text
# 0
# false
# 3
# Amanda
# William
# John
# Amanda
# 1. William
# 2. John
# 3. Amanda
# Amanda
# William
# 0
# ```

print("```text")
my_list = []
print(len(my_list))
my_list.append("William")
if len(my_list) == 0:
    print(True)
else:
    print(False)
def multiple_extend(my_list, *addtion_element):
    return my_list.extend(addtion_element)
multiple_extend(my_list, "John", "Amanda")  
print(len(my_list))
print(my_list[2])

for val in my_list:
    print(val)

for ix, val in enumerate(my_list):
    i = ix+1
    print(f"{i}. {val}")

del my_list[1]

for val in reversed(my_list):
    print(val)

my_list.clear()
print(len(my_list))
print("```")