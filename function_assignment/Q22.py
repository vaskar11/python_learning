# 22. Recursive function to return the n-th Fibonacci number:

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
print(fibonacci_recursive(6))