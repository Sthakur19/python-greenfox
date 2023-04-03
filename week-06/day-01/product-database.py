# # Product database

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
#   - [How much is the fish?](https://www.youtube.com/watch?v=cbB3iGRHtqA)
#   - What is the most expensive product?
#   - What is the average price?
#   - How many products' price is below 300?
#   - Is there anything we can buy for exactly 125?
#   - What is the cheapest product?

# The full output of your `main` method should be the following:

# ```text
# 400
# Chicken
# 258.33334
# 4
# no
# Bread
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
print(product_database["Fish"])
# print(max(product_database.values()))
print(max(product_database, key = product_database.get))
average_price = sum(product_database.values())/ len(product_database)
print(round(average_price, 4))

no_item_price = []
for item, price in product_database.items():
    if price <= 300:
        no_item_price.append(price)
print(len(no_item_price))

print("yes") if product_database.values() == 125 else print("no")
print(min(product_database, key = product_database.get))
print("```")