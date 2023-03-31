# - Create a list ('`List A`') which contains the following values
#   ```text
#   Apple, Avocado, Blueberries, Durian, Lychee
#   ```
# - Create a new list ('`List B`') with the values of `List A`
# - Print out whether `List A` contains "Durian" or not
# - Remove "Durian" from `List B`
# - Add "Kiwifruit" to `List A` after the 4th element
# - Compare the size of `List A` and `List B`
# - Get the index of "Avocado" from `List A`
# - Get the index of "Durian" from `List B`
# - Add "Passion Fruit" and "Pomelo" to `List B` in a single statement
# - Print out the 3rd element from `List A`
# - Print all elements of `List A`
# - Print all elements of `List B`

# The full output of your `main` method should be the following:

# ```text
# true
# false
# 1
# -1
# Blueberries
# [Apple, Avocado, Blueberries, Durian, Kiwifruit, Lychee]
# [Apple, Avocado, Blueberries, Lychee, Passion Fruit, Pomelo]
# ```

list_A = ["Apple", "Avocado", "Blueberries", "Durian", "Lychee"]
list_B = list_A.copy()

if "Durian" in list_A:
    print("true")
else:
    print("false")

list_B.remove("Durian")

list_A.insert(4,"Kiwifruit")

if len(list_A) == len(list_B):
    print("true")
else:
    print("false")

index_avacodo_list_A = list_A.index("Avocado")
# index_durian_list_B = list_B.index("Durian")

print(index_avacodo_list_A)
# print(index_durian_list_B)

list_B.extend(["Passion Fruit" ,"Pomelo"])
print(list_A[2])
print(list_A)
print(list_B)