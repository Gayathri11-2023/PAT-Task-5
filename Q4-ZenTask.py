# write a function that takes a string and returns a number of unique characters in it.
def unique(in_string) :
    unique_chars = set(in_string) # set function is to build an unordered collection of unique elements
    return len(unique_chars)
in_string = "Welcome to Guvi Geek Pvt Limited!"
count_of_char = unique(in_string)
print("Number of unique characters: ", count_of_char)
