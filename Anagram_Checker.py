#Task: Write a function that checks if two strings are anagrams of each other.

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

#example
print(are_anagrams("evil", "vile"))
# Output: True

print(are_anagrams("truck", "turck"))
# Output: False

