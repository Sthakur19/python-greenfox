
#4 sum
#Write a function called `sum()` that returns the sum of numbers from zero to the given parameter

enter_sum_number = int(input("Please Enter Number :"))

def sum(enter_sum_number):
    total = 0
    for i in range (0, enter_sum_number+1):
        total = total + i
    return total 

print(sum(enter_sum_number)) 