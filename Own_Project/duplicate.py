duplicate_letter = []

def most_common_letter(word):
    word_with_test_cases = word.lower().replace(" ", "")
    for letter in word_with_test_cases:
        if word_with_test_cases.count(letter) > 1:
            if letter not in duplicate_letter:
                duplicate_letter.append(letter)
    print(*duplicate_letter[1])

# most_common_letter('ApPle')
most_common_letter('This is not soooo hard')