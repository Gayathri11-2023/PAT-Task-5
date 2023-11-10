def count_words(input_string):

    words = input_string.split()
    return len(words)

# Test the function
input_string = " Inroduction to Pyhton programming language"
word_count = count_words(input_string)
print(f'The number of words in the input string is: {word_count}')
