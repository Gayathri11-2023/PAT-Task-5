def is_anagram(str1, str2):
    str1_cleaned = ''.join(str1.split()).lower()
    str2_cleaned = ''.join(str2.split()).lower()

    return sorted(str1_cleaned) == sorted(str2_cleaned)

str1 = "a gentleman"
str2 = "elegant man"
result = is_anagram(str1, str2)
print(f'Are "{str1}" and "{str2}" anagrams? {result}')
