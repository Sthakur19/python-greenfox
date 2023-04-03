# Shopping list

# We are going to represent a shopping list by a list containing strings.

# - Create a list with the following items:
#   - `eggs`, `milk`, `fish`, `apples`, `bread` and `chicken`
# - Create an application which prints out the answers to the following
#   questions:
#   - Do we have `milk` in the shopping list? (yes/no)
#   - Do we have `bananas` in the shopping list? (yes/no)

# The full output of your `main` method should be the following:

# ```text
# yes
# no
# ```

shopping_list = ["eggs", "milk", "fish", "apple", "bread", "chicken"]
print("```text")
if "milk" in shopping_list:
    print("yes") 
if "bananas" not in shopping_list:
    print("no")
print("```")