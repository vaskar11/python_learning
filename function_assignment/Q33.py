# 33. Lambda function to check if a given string is a palindrome
is_palindrome = lambda s: s == s[::-1]
print("Is 'radar' a palindrome?", is_palindrome('radar'))