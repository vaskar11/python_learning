# 31. Lambda function to filter even numbers from a list
filter_even = lambda lst: list(filter(lambda x: x % 2 == 0, lst))

print("Even numbers:", filter_even([1, 2, 3, 4, 5, 6]))