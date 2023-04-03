# # Product database 2

# We are going to represent our products in a map where the keys are strings
# representing the product's name and the values are numbers representing the
# product's price.

# - Create a map with the following key-value pairs:

#   | Product name (key) | Price (value) |
#   | :----------------- | :------------ |
#   | Eggs               | 200           |
#   | Milk               | 200           |
#   | Fish               | 400           |
#   | Apples             | 150           |
#   | Bread              | 50            |
#   | Chicken            | 550           |

# - Create an application which prints out the answers to the following
#   questions:
#   - Which products cost less than 201? (just the name)
#   - Which products cost more than 150? (name + price)
  
# The full output of your `main` method should be the following:

# ```text
# Apples
# Eggs
# Milk
# Bread
# Fish 400
# Chicken 550
# Eggs 200
# Milk 200
# ```

product_database = {
    "Eggs"    : 200,
    "Milk"    : 200,
    "Fish"    : 400,
    "Apples"  : 150,
    "Bread"   : 50,
    "Chicken" : 550
}
print("```text")
for item, price in product_database.items():
    if price < 201:
        print(item)
    if price > 150:
        print(item, price)
print("```")