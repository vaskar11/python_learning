# 7. Function to return the first n numbers in the Fibonacci sequence:
def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq

print(fibonacci(5))