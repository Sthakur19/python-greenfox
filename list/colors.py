# - Create a two dimensional list (of strings)
#   which can contain the different shades of specified colors
# - In `colors[0]` store the shades of green:
#   `"lime", "forest green", "olive", "pale green", "spring green"`
# - In `colors[1]` store the shades of red:
#   `"orange red", "red", "tomato"`
# - In `colors[2]` store the shades of pink:
#   `"orchid", "violet", "pink", "hot pink"`
# - Print the array in the following format:
#
#   lime, forest green, oline, pale green, spring green
#   orange red, red, tomato
#   orchid, violet, pink, hot pink

colors = [
    ["lime", "forest green", "olive", "pale green", "spring green"],
    ["orange red", "red", "tomato"],
    ["orchid", "violet", "pink", "hot pink"]
]

for i in range(0 , 1):
    for j in range(0, len(colors)):
        print(*colors[j] , sep=", ")