# write a function that takes two input string and returns the longest common substring between them
def longest_common_substring(str1, str2):
    # Create a table to store the length of the common substring at each position
    m, n = len(str1), len(str2)
    table = [[0] * (n + 1) for _ in range(m + 1)]
    
    max_length = 0  # Length of the longest common substring
    end_position = 0  # Ending position of the longest common substring in str1
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > max_length:
                    max_length = table[i][j]
                    end_position = i
                    
    # Extract the longest common substring from str1
    longest_common_substring = str1[end_position - max_length:end_position]
    
    return longest_common_substring

# Test the function
str1 = "reindeer"
str2 = "raindeer"
result = longest_common_substring(str1, str2)
print(f"The longest common substring between '{str1}' and '{str2}' is: '{result}'")






