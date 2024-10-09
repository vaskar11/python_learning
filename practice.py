# list_of_lists = [[1, 2], [3, 4], [5, 6]]
# flattened_list = []

# for sublist in list_of_lists:
#     for item in sublist:
#         flattened_list.append(item)

# print(flattened_list)

# def rotate_left(my_list, n):
#     return my_list[n:] + my_list[:n]

# # Example usage:
# my_list = [1, 2, 3, 4, 5]
# print(rotate_left(my_list, 2))  # Output: [3, 4, 5, 1, 2]


# def is_palindrome(my_list):
#     return my_list == my_list[::-1]

# # Example usage:
# my_list = [1, 2, 3, 2, 1]
# print(is_palindrome(my_list))  # Output: True

# def bubble_sort(my_list):
#     n = len(my_list)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if my_list[j] > my_list[j + 1]:
#                 my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
#     return my_list

# # Example usage:
# my_list = [64, 25, 12, 22, 11]
# print(bubble_sort(my_list))  # Output: [11, 12, 22, 25, 64]


# def find_pairs(my_list, target_sum):
#     pairs = []
#     seen = set()
#     for num in my_list:
#         complement = target_sum - num
#         if complement in seen:
#             pairs.append((complement, num))
#         seen.add(num)
#     return pairs

# # Example usage:
# my_list = [2, 4, 3, 5, 7]
# target_sum = 7
# print(find_pairs(my_list, target_sum))  # Output: [(4, 3), (5, 2)]

# def remove_duplicates(my_list):
#     seen = set()
#     return [x for x in my_list if not (x in seen or seen.add(x))]

# # Example usage:
# my_list = [1, 2, 2, 3, 4, 3, 5]
# print(remove_duplicates(my_list))  # Output: [1, 2, 3, 4, 5]

# def merge_and_sort(list1, list2):
#     merged_list = list1 + list2  # Concatenate the two lists
#     return sorted(merged_list)  # Sort the merged list

# # Example usage:
# list1 = [1, 3, 5, 7]
# list2 = [2, 4, 6, 8]
# print(merge_and_sort(list1, list2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# def find_majority_element(nums):
#     candidate = None
#     count = 0
    
#     # Step 1: Find a candidate for the majority element
#     for num in nums:
#         if count == 0:  # If counter is 0, pick a new candidate
#             candidate = num
#         if num == candidate:
#             count += 1  # Increment counter if the current element matches the candidate
#         else:
#             count -= 1  # Otherwise, decrement the counter

#     if nums.count(candidate) > len(nums) // 2:
#         return candidate
#     else:
#         return "No majority element"


# nums = [3, 3, 4, 2, 3, 3, 2, 3, 3]
# print(find_majority_element(nums))  # Output: 3

#modules

# a=555

# def add(a,b):
#     print('sum is ',a+b)
    
# def product(a,b):
#     print('the product is: ',a*b)
    
    
# class A:
#     pass


# print(__name__)

# def f():
#     if __name__ =='__main__':
#         print('this is direct execution')
#     else: print('this is indirect execution.')
    
# f()

def f1():
    print('1st function execution.')

def f2():
    print('2nd function execution.')

def f3():
    print('3rd function execution.')

if __name__=='__main__'  :
    f1()
    f2()
    f3()