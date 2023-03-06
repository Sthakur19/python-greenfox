# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

triangle_number = int(input("Please Enter the number for Triangle: "))

for i in range(0, triangle_number):
    for j in range (0, i+1): 
        print( "*", end = " ")  
    print("\r")
     
