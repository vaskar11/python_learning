# 38. Function to concatenate an arbitrary number of strings (using *args)

def concatenate_strings(*args):
    return ''.join(args)

print("Concatenated string:", concatenate_strings("Hello", " ", "World"))