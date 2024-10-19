# 12. Function to remove duplicate elements from a list:

def remove_duplicates(lst):
    return list(set(lst))
l=[1,2,3,4,5,6,3,5]
print(remove_duplicates(l))