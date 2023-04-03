# # Shopping list 2

# - Represent the following products with their prices:

#   | Product         | Price  |
#   | :-------------- | :----- |
#   | Milk            | 1.07   |
#   | Rice            | 1.59   |
#   | Eggs            | 3.14   |
#   | Cheese          | 12.60  |
#   | Chicken Breasts | 9.40   |
#   | Apples          | 2.31   |
#   | Tomato          | 2.58   |
#   | Potato          | 1.75   |
#   | Onion           | 1.10   |

# - Represent Bob's shopping list:

#   | Product         | Amount |
#   | --------------- | ------ |
#   | Milk            | 3      |
#   | Rice            | 2      |
#   | Eggs            | 2      |
#   | Cheese          | 1      |
#   | Chicken Breasts | 4      |
#   | Apples          | 1      |
#   | Tomato          | 2      |
#   | Potato          | 1      |

# - Represent Alice's shopping list:

#   | Product         | Amount |
#   | --------------- | ------ |
#   | Rice            | 1      |
#   | Eggs            | 5      |
#   | Chicken Breasts | 2      |
#   | Apples          | 1      |
#   | Tomato          | 10     |

# - Create an application which prints out the answers to the following
#   questions:
#   - How much does Bob pay?
#   - How much does Alice pay?
#   - Who buys more Rice?
#   - Who buys more Potato?
#   - Who buys more Ham?
#   - Who buys more Apples?
#   - Who buys more of different products?
#   - Who buys more items? (more pieces)

# The full output of your `main` method should be the following:

# ```text
# 72.09
# 64.2
# Bob
# Bob
# no one
# no one
# Bob
# Alice
# ```

product_dictionary = {
    "Milk"            : 1.07,
    "Rice"            : 1.59, 
    "Eggs"            : 3.14,  
    "Cheese"          : 12.60,  
    "Chicken Breasts" : 9.40,  
    "Apples"          : 2.31,   
    "Tomato"          : 2.58, 
    "Potato"          : 1.75,  
    "Onion"           : 1.10 
}

bob_shopping_list = {
    "Milk"            :    3,
    "Rice"            :    2,
    "Eggs"            :    2,
    "Cheese"          :    1,
    "Chicken Breasts" :    4,
    "Apples"          :    1,
    "Tomato"          :    2,
    "Potato"          :    1
}

alice_shopping_list = {
    "Rice"            :    1,
    "Eggs"            :    5,
    "Chicken Breasts" :    2,
    "Apples"          :    1,
    "Tomato"          :    10,
}
total_pay_by_bob = []
total_pay_by_alice = []
total_qty_by_bob = []
total_qty_by_alice = []

for item, qty in bob_shopping_list.items():
    total_qty_by_bob.append(qty)
    total_pay_by_bob.append(qty*product_dictionary[item])
for item, qty in alice_shopping_list.items():
    total_qty_by_alice.append(qty)
    total_pay_by_alice.append(qty*product_dictionary[item])
print(sum(total_pay_by_bob))  
print(sum(total_pay_by_alice))     

print("Bob") if bob_shopping_list["Rice"] > alice_shopping_list["Rice"] else ("Alice")
print("Bob") if bob_shopping_list.get("Potato", 0) > alice_shopping_list.get("Potato", 0) else ("Alice")  

if bob_shopping_list.get("Ham", 0) > alice_shopping_list.get("Ham", 0):
    print("Bob")  
elif bob_shopping_list.get("Ham", 0) < alice_shopping_list.get("Ham", 0):   
    print("Alice")
else:
    print("no one")

if bob_shopping_list.get("Apples", 0) > alice_shopping_list.get("Apples", 0):
    print("Bob")  
elif bob_shopping_list.get("Apples", 0) < alice_shopping_list.get("Apples", 0):   
    print("Alice")
else:
    print("no one")

print("Bob") if len(bob_shopping_list) > len(alice_shopping_list) else print("Bob")
print("Alice") if sum(total_qty_by_alice) > sum(total_qty_by_bob) else print("Bob")