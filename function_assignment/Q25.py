# 25. Recursive function to find the greatest common divisor of two numbers:

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)
print(gcd_recursive(10,20))
