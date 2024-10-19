# 43. Recursive function to flatten any number of nested lists passed as arguments

def flatten_recursive(*args):
    flat_list = []
    for arg in args:
        if isinstance(arg, (list, tuple)):
            flat_list.extend(flatten_recursive(*arg))
        else:
            flat_list.append(arg)
    return flat_list

print("Flattened list:", flatten_recursive(1, [2, 3], [4, [5, 6], 7]))