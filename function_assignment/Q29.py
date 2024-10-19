# 29. Lambda function to return a list of squares of a list of numbers:

square_numbers = lambda lst: list(map(lambda x: x ** 2, lst))
l=[2,3,4]
print(square_numbers(l))