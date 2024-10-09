# my_tuple = (1, 2, 3)
# if 2 in my_tuple:
#     print("it exixts")

# list_of_tuples = [(1, 3), (2, 1), (4, 2)]
# sorted_list = sorted(list_of_tuples, key=lambda x: x[1])
# print(sorted_list)

# set

# if 3 in my_set:
#     print("3 is in the set")
# 
# A2={1,2,3,4,5,6,7}
# is_subset = my_set.issubset(A2)
# print(is_subset)
# my_set= {1,2,3,4}
# for element in my_set:
#     print(element)

# set1 = {1, 2}
# set2 = {'a', 'b'}
# cartesian_product = {(x, y) for x in set1 for y in set2}
# print(cartesian_product)

# my_set = {1, 2, 3, 4, 5}
# elements_to_remove = {2, 4}

# for element in elements_to_remove:
#     my_set.discard(element)

# print(my_set)  # Output: {1, 3, 5}

def find_subsets(s):
    s = list(s)  # Convert the set to a list to index its elements
    subsets = []
    for i in range(1 << len(s)):  # Loop over all possible subsets (2^n possibilities)
        subset = {s[j] for j in range(len(s)) if i & (1 << j)}  # Include element if corresponding bit is 1
        subsets.append(subset)
    return subsets

# Example
my_set = {1, 2, 3}
unique_subsets = find_subsets(my_set)
for subset in unique_subsets:
    print(subset)
