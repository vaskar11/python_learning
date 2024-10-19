# 15. Function to return the greatest common divisor of two numbers:

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(find_gcd(6,8))