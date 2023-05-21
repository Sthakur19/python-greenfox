# Fizz Buzz generator
# Create a generator which will always yield the next item from the fizz buzz sequence.

def fizz_buzz_generator():
    num = 1
    while True:
        if num % 3 == 0 and num % 5 == 0:
            yield "FizzBuzz"
        elif num % 3 == 0:
            yield "Fizz"
        elif num % 5 == 0:
            yield "buzz"
        else:
            yield num
        num += 1

fizz_buzz_gen = fizz_buzz_generator()

print(next(fizz_buzz_gen))
print(next(fizz_buzz_gen))
print(next(fizz_buzz_gen))
print(next(fizz_buzz_gen))
print(next(fizz_buzz_gen))
print(next(fizz_buzz_gen))
print(next(fizz_buzz_gen))
print(next(fizz_buzz_gen))
print(next(fizz_buzz_gen))
print(next(fizz_buzz_gen))
print(next(fizz_buzz_gen))
print(next(fizz_buzz_gen))
print(next(fizz_buzz_gen))
print(next(fizz_buzz_gen))
print(next(fizz_buzz_gen))