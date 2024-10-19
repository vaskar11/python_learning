# 16. Function to return the sum of squares of the first n natural numbers:

def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))
print(sum_of_squares(6))