
# 10 palindrome builder
# A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward, such as madam or racecar. [for more detail check palindrome on Wikipedia].

# Create a function named createPalindrome() following your current language's style guide. It should take a string, create a palindrome from it and then return it.

# Examples
# input	output
# ""	""
# "greenfox"	"greenfoxxofneerg"
# "123"	"123321"

def createPalindrome(your_data):
    store_new_valu = your_data + your_data[::-1]
    return store_new_valu

palindrome = createPalindrome("greenfox")
print(palindrome)