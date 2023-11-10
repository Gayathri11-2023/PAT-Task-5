# write a function that takes a string and returns a new string with all the vowels removed.
def  delete_vowels(a) :
    vowels ="AEIOUaeiou"
    result_string = ''.join([ch for ch in a if ch not in vowels ])
    return result_string
new_string = delete_vowels("intelligent")
print(new_string)

   
        

       


