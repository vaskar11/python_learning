# 36. Function to multiply all numbers passed as arguments (using *args)

def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

print("Product of 2, 3, 4:", multiply_all(2, 3, 4))