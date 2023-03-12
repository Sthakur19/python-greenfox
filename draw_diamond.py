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

draw_diamond = int(input("Please enter the number to draw pyramid : "))

for i in range (0, draw_diamond//2+1):
    number_of_stras = i*2+1
    number_of_space= draw_diamond - number_of_stras
    line=""
    for j in range(0, int(number_of_space/2)):
        line = line + " "
    for k in range(0, number_of_stras):
        line = line + "*"
    print(line)
for l in range (0, draw_diamond//2+1):
    number_of_stras = (draw_diamond-l)-l
    number_of_space= draw_diamond - number_of_stras
    line=""
    for m in range(0, int(number_of_space/2)):
        line = line + " "
    for n in range(0, number_of_stras):
        line = line + "*"
    print(line)