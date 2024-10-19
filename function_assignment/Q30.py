# 30. Lambda function to sort a list of tuples based on the second element:

sort_by_second = lambda lst: sorted(lst, key=lambda x: x[1])
print("Sorting list of tuples by second element:", sort_by_second([(1, 3), (4, 2), (5, 6), (2, 1)]))