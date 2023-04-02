# # Map introduction 1

# We are going to play with maps. Feel free to use the built-in methods where
# possible.

# - Create an empty map where the keys are integers and the values are characters
# - Print out whether the map is empty or not
# - Add the following key-value pairs to the map
#   |  Key | Value |
#   | :--- | :---- |
#   | 97   | a     |
#   | 98   | b     |
#   | 99   | c     |
#   | 65   | A     |
#   | 66   | B     |
#   | 67   | C     |
# - Print all the keys
# - Print all the values
# - Add value D with the key 68
# - Print how many key-value pairs are in the map
# - Print the value that is associated with key 99
# - Remove the key-value pair with key 97 and print the associated value
# - Print whether there is an associated value with key 100 or not
# - Remove all the key-value pairs
# - Print how many key-value pairs are in the map

# The full output of your `main` method should be the following:

# ```text
# true
# [97, 65, 98, 66, 99, 67]
# [a, A, b, B, c, C]
# 7
# c
# false
# 0
# ```

my_dictionary = {}
print("```text")
print("true") if len(my_dictionary) == 0 else print("false")
my_dictionary ={
    97 : "a",
    98 : "b",
    99 : "c",
    65 : "A",
    66 : "B",
    67 : "C"
}
print(list(my_dictionary.keys()))
my_dictionary_list_val = list(my_dictionary.values())
my_dictionary_list_val.sort(key=str.lower)
print(my_dictionary_list_val)
my_dictionary[68]="D"
print(len(my_dictionary))
print(my_dictionary[99])
del my_dictionary[97]
print("false") if 100 not in my_dictionary else print("true")
my_dictionary.clear()
print(len(my_dictionary))
print("```")