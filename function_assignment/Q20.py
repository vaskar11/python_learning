# 20. Function to check if two strings are anagrams:


def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram('race','care'))