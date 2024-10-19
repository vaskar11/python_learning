# 9. Function to check if a number is prime:

def is_prime(n):
    c=0
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            c=c+1
    if c==0:
        return True
    return False

print(is_prime(6))