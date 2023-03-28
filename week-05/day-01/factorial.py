
#4  5 factorial
# - Create a function called `calculateFactorial()`
#   that returns the factorial of its input

factorial_number = int(input("Please enter the number here :"))
def factorial(factorial_number):
    
    if factorial_number == 0:
        return 1
    else:
        total = 1
        for i in range(1, factorial_number + 1):
            total *= i
    return total

print(f"Factorial number of {factorial_number} is: {factorial(factorial_number) }" )
