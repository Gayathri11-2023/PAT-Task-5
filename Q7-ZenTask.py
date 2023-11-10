# write a function that takes a string and returns the most frequent character in it
def most_frequent_character(input_string):
    
    char_count = {}
    
    for char in input_string:
        if char.isalpha():  
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    
    most_frequent_char = max(char_count, key=char_count.get)
    
    return most_frequent_char


input_string = "programming language"
result = most_frequent_character(input_string)
print(f"The most frequent character in '{input_string}' is '{result}'")
