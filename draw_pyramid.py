# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was

draw_pyramid = int(input("Please enter the number to draw pyramid"))

k = draw_pyramid - 1

for i in range (0, draw_pyramid):
    for j in range(0, k):
        print(end= " ")
    k = k - 1
    for j in range(0, i+1):
        print("* ", end="")
    print("\r")
