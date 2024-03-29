# # Map introduction 2

# - Create a map where the keys are strings and the values are strings with the
#   following initial values
#   | Key               | Value                   |
#   | :---------------- | :---------------------- |
#   | 978-1-60309-452-8 | A Letter to Jo          |
#   | 978-1-60309-459-7 | Lupus                   |
#   | 978-1-60309-444-3 | Red Panda and Moon Bear |
#   | 978-1-60309-461-0 | The Lab                 |

# - Print all the key-value pairs in the following format
#   ```text
#   A Letter to Jo (ISBN: 978-1-60309-452-8)
#   Lupus (ISBN: 978-1-60309-459-7)
#   Red Panda and Moon Bear (ISBN: 978-1-60309-444-3)
#   The Lab (ISBN: 978-1-60309-461-0)
#   ```
# - Remove the key-value pair with key 978-1-60309-444-3
# - Remove the key-value pair with value The Lab
# - Add the following key-value pairs to the map
#   | Key               | Value                 |
#   | :---------------- | :-------------------- |
#   | 978-1-60309-450-4 | They Called Us Enemy  |
#   | 978-1-60309-453-5 | Why Did We Trust Him? |

# - Print whether there is an associated value with key 478-0-61159-424-8 or not
# - Print the value associated with key 978-1-60309-453-5

# The full output of your `main` method should be the following:

# ```text
# A Letter to Jo (ISBN: 978-1-60309-452-8)
# Red Panda and Moon Bear (ISBN: 978-1-60309-444-3)
# Lupus (ISBN: 978-1-60309-459-7)
# The Lab (ISBN: 978-1-60309-461-0)
# false
# Why Did We Trust Him?
# ```

my_dictionary = {
    "978-1-60309-452-8" : "A Letter to Jo",          
    "978-1-60309-459-7" : "Lupus",                
    "978-1-60309-444-3" : "Red Panda and Moon Bear",
    "978-1-60309-461-0" : "The Lab"   
}
print("```text")

for key in my_dictionary:
    print(f"{my_dictionary[key]} (ISBN: {key})")

del my_dictionary["978-1-60309-444-3"]
del my_dictionary["978-1-60309-461-0"]

my_dictionary["978-1-60309-450-4"] = "They Called Us Enemy"
my_dictionary["978-1-60309-453-5"] = "Why Did We Trust Him?"

print("false") if "478-0-61159-424-8" not in my_dictionary else print("true")
print(my_dictionary["978-1-60309-453-5"])

print("```")