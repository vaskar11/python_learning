# 17. Function to return the longest word from a list of words:

def longest_word(words):
    return max(words, key=len)

w=['My', 'name' ,'is', 'Bhaskar', 'Subedi']
print(longest_word(w))