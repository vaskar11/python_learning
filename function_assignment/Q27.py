# 27. Recursive function to flatten a nested list:

def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

lst=['Bhaskar','Biplov','Dipesh']
print(flatten(lst))