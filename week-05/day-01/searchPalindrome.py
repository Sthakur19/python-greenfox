# # 11 palindrome searcher
# Create a function named searchPalindrome() following your current language's style guide. It should take a string, search for palindromes that is at least 3 characters long and return a list with the found palindromes.

# Examples
# input	output
# "dog goat dad duck doodle never"	["og go", "g g", " dad ", "dad", "d d", "dood", "eve"]
# "apple"	[]
# "racecar"	["racecar", "aceca", "cec"]
# ""	[]

def searchPalindrome(palindrome_word):
    palindrome_word_list = []
    len_of_palindrome_word = len(palindrome_word)
    for i in range(len_of_palindrome_word):
        for j in range(i+1, len_of_palindrome_word +1):
            word = palindrome_word[i:j]
            print(word)
            if word == word[::-1] and len(word) > 2:
                palindrome_word_list.append(word)
    return palindrome_word_list

print(searchPalindrome('racecar'))