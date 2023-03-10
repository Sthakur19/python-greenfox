# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was

draw_diamond = int(input("Please enter the number to draw pyramid"))

k = 2*draw_diamond - 2

for i in range (0, draw_diamond):
    for j in range(0, k):
        print(end= " ")
    k = k - 1
    for j in range(0, i+1):
        print("* ", end="")
    print("\r")

k = draw_diamond - 2

for i in range ( draw_diamond , -1, -1):
    for j in range(k , 0 , -1):
        print(end= " ")
    k = k + 1
    for j in range(0, i+1):
        print("* ", end="")
    print("\r")