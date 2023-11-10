# Calculate the total number of vowels in given string
given_string = "Guvi Geeks Network Private Limited"
vowels ="AEIOUaeiou"
vowel_count = 0
for char in  given_string :
    if char in  vowels:
        vowel_count += 1
print("-----------------------------------------------")
print("The total number of vowels in given string is : ", vowel_count )
print("-----------------------------------------------")

# To count of each individual vowel in given string 
count_of_a = count_of_e = count_of_i = count_of_o = count_of_u = 0
for char in given_string :
    if char == "a" :
        count_of_a += 1
    elif char == "e" :
        count_of_e += 1
    elif char == "i" :
        count_of_i += 1
    elif char == "o":
        count_of_o += 1
    elif char == "u":
        count_of_u += 1
print("***********************************************")
print("Count of each individual vowel in given string: ")
print("***********************************************")
print(" count of a :", count_of_a)
print(" count of e :", count_of_e)
print(" count of i :", count_of_i)
print(" count of o :", count_of_o)
print(" count of u :", count_of_u)






