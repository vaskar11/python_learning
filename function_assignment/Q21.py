# 21. Recursive function to find the factorial of a number:

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

print(factorial_recursive(5))