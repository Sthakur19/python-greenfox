

# Write a program that asks for an integer n,
# then it creates a two-dimensional array (of integers) of the specified
# size (nxn) with the value of 1 on the main diagonal and the value of 0
# everywhere else. Print the 2d array into the output
#
# Example:
#
# Please enter the array (matrix) size: 4
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

m = int(input("please enter the row :"))
n = int(input("please enter the cols :"))

for i in range(1, m+1):
    for j in range(1, n+1):
        if i==j:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print("\r")


