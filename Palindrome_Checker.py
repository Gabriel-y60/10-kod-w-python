#Task: Check whether a given string is a palindrome (reads the same forward and backward).

def is_palindrome(s):
    return s == s[::-1]

#example
print(is_palindrome("kajak"))
# Output: True
print(is_palindrome("wheel"))
# Output: False
