# 6. Function to check if a string is a palindrome:

def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Make case insensitive and ignore spaces
    return s == s[::-1]

print(is_palindrome('hih'))