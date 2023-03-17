# - Create an array variable named `animals`
#   with the following content:
#   `["koal", "pand", "zebr", "anacond", "bo", "chinchill", "cobr",
#     "gorill", "hyen", "hydr", "iguan", "impal", "pum", "tarantul", "piranh"]`
#
# - Add an `"a"` at the end of all elements (use a loop!)
# - Print the 'fixed' array to the console:
#   [koala, panda, zebra, anaconda, boa, ..., puma, tarantula, piranha]


animals = ["koal", "pand", "zebr", "anacond", "bo", "chinchill", "cobr",
  "gorill", "hyen", "hydr", "iguan", "impal", "pum", "tarantul", "piranh"]

for ix, val in enumerate(animals):
    animals[ix] = animals[ix] + 'a'
print(animals)