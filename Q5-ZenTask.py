#Write a funtion to get string and returns true if it is palindrome, false otherwise
def palindrome(in_string):
    palindrome_string = in_string.replace(" ", "").lower()
    return palindrome_string == palindrome_string[:: -1]

    
in_string = "madam"
out_string = palindrome(in_string)
print(f'Is "{in_string}" a palindrome? {out_string}')